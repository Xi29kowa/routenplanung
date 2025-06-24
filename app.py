from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from generate_nbg_waste_basket_map_with_citycenter_and_hotspots import generate_map_html

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <h1>Routenplanung API</h1>
    <p><a href="/map">Interaktive Karte öffnen →</a></p>
    """

@app.get("/map", response_class=HTMLResponse)
def show_map():
    return generate_map_html()
