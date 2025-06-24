from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from generate_nbg_waste_basket_map_with_citycenter_and_hotspots import generate_map_html

app = FastAPI()

# Generiere Karte beim Start – einmalig
print("🔄 Generiere Karte...")
cached_map_html = generate_map_html()
print("✅ Karte fertig.")

# Liefere Karte direkt bei /
@app.get("/", response_class=HTMLResponse)
def map():
    return cached_map_html
