from typing import List, Dict, Any
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.fetch_openapi import fetch_openapi_schemas


router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
	apis: List[Dict[str, Any]] = await fetch_openapi_schemas()
	context = {
		"request": request,
		"portal_name": "FinFlow API Portal",
		"apis": apis,
	}
	return templates.TemplateResponse("index.html", context)

