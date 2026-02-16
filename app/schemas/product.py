from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    image: str

class ProductResponse(ProductCreate):
    id: int