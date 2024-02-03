from datetime import date
from fastapi import FastAPI
from typing import Optional, Union

app = FastAPI()

@app.get('/hotels')
def get_hotels(
    location:str,
    date_from: str,
    date_to: str,
    has_spa: bool|None = None,
    stars: int|None = None,
) -> None:
  return date_from, date_to


@app.get("/greet")
def say_hi(name:  str | None = None):
    return {"message": f"Hey {name}!"}