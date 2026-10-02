from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ProductCreate(BaseModel):
    name: str
    category: str


products = [
    {"id": 1, "name": "Coca-Cola", "category": "drinks"},
    {"id": 2, "name": "Lays", "category": "snacks"},
    {"id": 3, "name": "Milka", "category": "sweets"},
]


@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}


@app.get("/products")
def get_products(category: str | None = None):
    if category is None:
        return products

    return [product for product in products if product["category"] == category]


@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    return {"error": "Product not found"}


@app.post("/products")
def create_product(product: ProductCreate):
    new_product = {
        "id": len(products) + 1,
        "name": product.name,
        "category": product.category,
    }

    products.append(new_product)

    return new_product


@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return {"message": "Product deleted"}

    return {"error": "Product not found"}