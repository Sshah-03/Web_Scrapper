from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.controllers.scraper_controller import ScraperController


app = FastAPI()

controller = ScraperController()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/scrape")
async def scrape(source: str = Form(...)):

    data = await controller.scrape(source)

    return {"results": data}
