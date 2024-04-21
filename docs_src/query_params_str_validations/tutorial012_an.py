from typing import Optional, List

from fastapi import FastAPI, Query
from typing_extensions import Annotated

app = FastAPI()


@app.get("/items/")
async def read_items(q: Optional[Annotated[List[str], Query()]] = None):
    q = ["foo", "bar"] if q is None else q
    query_items = {"q": q}
    return query_items
