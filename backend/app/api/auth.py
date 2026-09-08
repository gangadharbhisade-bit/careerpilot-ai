import re
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import get_password_hash, verify_password, create_access_token, decode_token
from app.models.entities import User, UserProfile
from app.schemas.schemas import UserCreate, UserLogin, Token, UserResponse, ProfileSchema
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(prefix="/auth", tags=["Authentication"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login", auto_error=False)

EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication token required. Please sign in.",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    payload = decode_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token. Please log in again.",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    user_id = payload.get("sub")
    user = db.query(User).filter(User.id == int(user_id)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User account not found.")
    return user

@router.post("/register", response_model=Token)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    # 1. Validate email format
    if not re.match(EMAIL_REGEX, user_in.email.strip()):
        raise HTTPException(status_code=400, detail="Please enter a valid email address.")

    # 2. Validate password length
    if len(user_in.password) < 8:
        raise HTTPException(status_code=400, detail="Password must contain at least 8 characters.")

    # 3. Check duplicate email
    existing = db.query(User).filter(User.email == user_in.email.strip().lower()).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="An account with this email already exists.")
        
    # 4. Create user
    user = User(
        email=user_in.email.strip().lower(),
        hashed_password=get_password_hash(user_in.password),
        full_name=user_in.full_name.strip() if user_in.full_name else "Career Navigator"
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    # Initial profile for new account
    profile = UserProfile(
        user_id=user.id,
        skills=[],
        programming_languages=[],
        target_career=None,
        experience_level="Beginner"
    )
    db.add(profile)
    db.commit()

    access_token = create_access_token(user.id)
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {"id": user.id, "email": user.email, "full_name": user.full_name}
    }

@router.post("/login", response_model=Token)
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    if not credentials.email or not credentials.password:
        raise HTTPException(status_code=400, detail="Please provide both email and password.")

    user = db.query(User).filter(User.email == credentials.email.strip().lower()).first()
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password.")
        
    access_token = create_access_token(user.id)
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {"id": user.id, "email": user.email, "full_name": user.full_name}
    }

@router.post("/guest", response_model=Token)
def guest_login(db: Session = Depends(get_db)):
    # Guest Demo Account
    user = db.query(User).filter(User.email == "demo@careerpilot.ai").first()
    if not user:
        user = User(
            email="demo@careerpilot.ai",
            hashed_password=get_password_hash("DemoPass123!"),
            full_name="Alex Navigator (Demo Guest)"
        )
        db.add(user)
        db.commit()
        db.refresh(user)

        profile = UserProfile(
            user_id=user.id,
            education="B.Tech",
            degree="Computer Science",
            branch="CSE",
            current_role="Student",
            experience_level="Beginner",
            skills=["Python", "HTML", "CSS", "SQL"],
            target_career="Software Developer"
        )
        db.add(profile)
        db.commit()

    access_token = create_access_token(user.id)
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {"id": user.id, "email": user.email, "full_name": user.full_name}
    }

@router.post("/logout")
def logout():
    return {"message": "Logged out successfully."}

@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user
