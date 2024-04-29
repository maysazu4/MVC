from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse

router = APIRouter()
templates = Jinja2Templates(directory="frontend/templates")

@router.get("/login", response_class=HTMLResponse)
def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
async def post_login(request: Request,login_data: dict):
    # Authentication logic
    # For simplicity, let's assume authentication is successful
    return JSONResponse(content={"success": True})


@router.get("/logout", response_class=HTMLResponse)
def logout(request: Request):
    # Logout logic
    return templates.TemplateResponse("logout.html", {"request": request})
