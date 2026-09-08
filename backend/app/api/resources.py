from fastapi import APIRouter

router = APIRouter(prefix="/resources", tags=["Learning Resources"])

@router.get("")
def get_curated_resources():
    return {
        "official_docs": [
            {"title": "Python Docs", "url": "https://docs.python.org/3/", "category": "DOCUMENTATION", "badge": "FREE"},
            {"title": "MDN Web Docs", "url": "https://developer.mozilla.org/", "category": "DOCUMENTATION", "badge": "FREE"},
            {"title": "PyTorch Tutorials", "url": "https://pytorch.org/tutorials/", "category": "DOCUMENTATION", "badge": "FREE"},
            {"title": "FastAPI Docs", "url": "https://fastapi.tiangolo.com/", "category": "DOCUMENTATION", "badge": "FREE"}
        ],
        "interactive_platforms": [
            {"title": "freeCodeCamp", "url": "https://www.freecodecamp.org/", "category": "PRACTICE", "badge": "FREE"},
            {"title": "Kaggle Learn", "url": "https://www.kaggle.com/learn", "category": "PRACTICE", "badge": "FREE"},
            {"title": "LeetCode", "url": "https://leetcode.com/", "category": "PRACTICE", "badge": "FREE"}
        ],
        "top_video_courses": [
            {"title": "3Blue1Brown Mathematics", "url": "https://www.youtube.com/@3blue1brown", "category": "YOUTUBE", "badge": "FREE"},
            {"title": "Fast.ai Practical Deep Learning", "url": "https://course.fast.ai/", "category": "COURSE", "badge": "FREE"},
            {"title": "Coursera ML Specialization", "url": "https://www.coursera.org/", "category": "COURSE", "badge": "CERTIFICATION"}
        ]
    }
