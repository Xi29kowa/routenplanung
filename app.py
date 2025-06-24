from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import folium

app = FastAPI()

@app.get("/map", response_class=HTMLResponse)
def get_map():
    m = folium.Map(location=[49.4521, 11.0767], zoom_start=13)
    return m._repr_html_()
