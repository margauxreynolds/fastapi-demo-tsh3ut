#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os

DBHOST = "ds2022.cqee4iwdcaph.us-east-1.rds.amazonaws.com"
DBUSER = "ds2022"
DBPASS = os.getenv('DBPASS')
DB = "tsh3ut"
db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
cur=db.cursor()


app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/genres')
def get_genres():
    query = "SELECT * FROM genres ORDER BY genreid;"
    try:    
        cur.execute(query)
        headers=[x[0] for x in cur.description]
        results = cur.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(headers,result)))
        return(json_data)
    except Error as e:
        return {"Error": "MySQL Error: " + str(e)}
    
@app.get('/songs')
def get_songs():
    query = """
    SELECT 
        songs.title, 
        songs.album, 
        songs.artist, 
        songs.year, 
        songs.file AS mp3_file,
        genres.genre AS genre
    FROM songs
    JOIN genres ON songs.genre = genres.genreid;
    """
    try:
        cur.execute(query) 
        headers = [x[0] for x in cur.description] 
        results = cur.fetchall()  
        json_data = []
        for result in results:
            json_data.append(dict(zip(headers, result)))  
        return json_data
    except Error as e:
        return {"Error": "MySQL Error: " + str(e)}

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

@app.get("/cube/{a}") # another new endpoint added to cube number
def cube(a: int):
    return {"result": a ** 3}