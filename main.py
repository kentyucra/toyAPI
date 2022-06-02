import json
from fastapi import FastAPI
import requests
from info import headers
from datetime import datetime

app = FastAPI()


@app.get("/")
def index():
  return {
    "message": "Our first microservice",
    "date": datetime.now()
  }

@app.get("/version")
def version():
  return {
    "version-number": "0.0.1"
  }

@app.get("/lyrics/{artist_name}/{song_name}")
def lirycs(artist_name: str, song_name: str):
  url = f"http://api.lyrics.ovh/v1/{artist_name}/{song_name}"
  res = requests.get(url)
  json_res = res.json()
  return {
    "date": datetime.now(),
    "artist_name": artist_name,
    "song_name": song_name,
    "lyrics": json_res["lyrics"]
  }

@app.get("/artist/top_songs/{artist_name}")
def top_songs(artist_name: str):

  url = "https://shazam.p.rapidapi.com/search"

  querystring = {"term":artist_name,"offset":"0","limit":"10"}

  response = requests.request("GET", url, headers=headers, params=querystring)
  json_res = response.json()

  avatar = json_res["artists"]["hits"][0]["artist"]["avatar"]
  hits = json_res["tracks"]["hits"]
  hits_names = []

  for hit in hits:
    hits_names.append({
      "name": hit["track"]["title"]
    })

  return {
    "artist_name": artist_name,
    "avatar": avatar,
    "hits": hits_names
  }