from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()


@router.get("/file", response_class = FileResponse)
def root_html():
    return "Files/Stalin.jpg"