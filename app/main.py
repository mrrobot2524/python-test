from fastapi import FastAPI
from typing import Optional, Union

app = FastAPI()

@app.get('/hotels')
def get_hotels(
    location,
    date_from,
    date_to,
    has_spa: Union[None, bool] = None,
    stars: Optional[int] = None,
) -> None:
  return date_from, date_to