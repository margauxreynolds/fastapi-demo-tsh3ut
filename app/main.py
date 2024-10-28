#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os

app = FastAPI()

@app.get("/")  # zone apex (default url)
def zone_apex():
    return {"Hello": "Hello API"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@app.get("/multiply/{c}/{d}") #use different variables, dont use a and b again from previous one
def multiply(c: int, d: int):
    return {"product": c*d}

@app.get("/square/{a}") # new endpoint added to square a number
def square(a: int):
    return {"result": a ** 2}