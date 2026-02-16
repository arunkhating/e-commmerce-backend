from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth, products

Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-Commerce Backend")

app.include_router(auth.router)
app.include_router(products.router)

@app.get("/")
def health():
    return {"status": "Backend running"}


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)