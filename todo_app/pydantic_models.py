import datetime
from pydantic import BaseModel
from typing import Optional


class Py_Todo(BaseModel):
    todo: str


