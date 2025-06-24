from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import folium

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>🗺️ Willkommen bei deiner Routenplanungs-API</h1>
    <p><a href="/map">Zur Karte →</a></p>
    """

@app.get("/map", response_class=HTMLResponse)
def get_map():
    m = folium.Map(location=[49.4521, 11.0767], zoom_start=13)
    return m._repr_html_()
