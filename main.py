from fastapi import FastAPI
import http3

client = http3.AsyncClient()
app = FastAPI()


@app.get("/")
def index():
  return {
    "message": "Our first microservice"
  }

@app.get("/lyrics/{artist_name}/{song_name}")
async def lirycs(artist_name: str, song_name: str):
  url = f"http://api.lyrics.ovh/v1/{artist_name}/{song_name}"
  print("url = ", url)
  response = await client.get(url=url)
  json_response = response.json()
  return {
    "artist": artist_name,
    "song_name": song_name,
    "lyrics": json_response["lyrics"]
  }