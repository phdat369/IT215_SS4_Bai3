from fastapi import FastAPI
from typing import Optional
products = [
    {"id": 1, "name": "Laptop", "price": 15000000},
    {"id": 2, "name": "Mouse", "price": 200000},
    {"id": 3, "name": "Keyboard", "price": 500000},
    {"id": 4, "name": "Monitor", "price": 3000000}
]
app = FastAPI()
@app.get("/products")
def search_product(keyword: Optional[str] = None, max_price: Optional[float] = None):
    if max_price is not None and max_price < 0:
        return {"detail":"max_price không được âm"}
    if keyword is None and max_price is None:
        return products
    list_products = [item for item in products
        if (keyword is None or keyword.lower() in item["name"].lower()) and (max_price is None or item["price"] <= max_price)]
    return list_products
    