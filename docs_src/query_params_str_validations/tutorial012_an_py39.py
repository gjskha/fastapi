from typing import Optional, Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Optional[Annotated[list[str], Query()]] = None):
    q = ["foo", "bar"] if q is None else q
    query_items = {"q": q}
    return query_items
