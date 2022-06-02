from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
def index():
  return {
    "message": "Our first microservice"
  }

@app.get("/lyrics/{artist_name}/{song_name}")
def lirycs(artist_name: str, song_name: str):
  url = f"http://api.lyrics.ovh/v1/{artist_name}/{song_name}"
  print("url = ", url)
  # response = await client.get(url=url)
  # json_response = response.json()
  res = requests.get(url)
  return res.json()
  