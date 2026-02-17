from fastapi import FastAPI
from backend.views import clienteView, articuloView, ventaView
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
app.include_router(clienteView.router)
app.include_router(articuloView.router)
app.include_router(ventaView.router)

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("API_PORT",8000))
    uvicorn.run("backend.main:app", host="0.0.0.0", port=port, reload=True)