from fastapi import FastAPI
from backend.views import clienteView, articuloView, ventaView

app = FastAPI()
app.include_router(clienteView.router)
app.include_router(articuloView.router)
app.include_router(ventaView.router)