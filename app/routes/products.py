from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.product import Product
from app.schemas.product import ProductCreate

router = APIRouter(prefix="/products")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    p = Product(**product.dict())
    db.add(p)
    db.commit()
    return p

@router.get("/")
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
