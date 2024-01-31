from typing import Optional
from fastapi import FastAPI
import logging


app = FastAPI()

logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    logger.error(f"request / endpoint!")
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    logger.critical(f"requested ITEM {item_id} to endpoint /items !")
    return {"item_id": item_id, "q": q}
    