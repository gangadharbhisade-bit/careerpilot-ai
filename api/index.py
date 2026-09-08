import sys
import os
from pathlib import Path

# Add backend directory to Python path
current_dir = Path(__file__).resolve().parent
backend_dir = current_dir.parent / "backend"

if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

# Ensure Vercel /tmp directory is used for SQLite if no external DB provided
if "VERCEL" in os.environ and not os.environ.get("DATABASE_URL"):
    os.environ["DATABASE_URL"] = "sqlite:////tmp/careerpilot.db"

from app.main import app

# Vercel entrypoint
handler = app
