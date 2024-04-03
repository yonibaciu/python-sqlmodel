from fastapi import FastAPI, Depends, HTTPException
from contextlib import asynccontextmanager
from db import init_db, get_session
from models import Song, SongCreate
from sqlmodel import Field, Session, select

@asynccontextmanager
async def lifespan(app: FastAPI):
  init_db()
  yield

app = FastAPI(lifespan=lifespan)

@app.get("/ping")
def ping():
  return {"ping": "pong!"}

@app.get("/songs", response_model=list[Song])
def get_songs(session: Session = Depends(get_session)):
  result = session.execute(select(Song))
  songs = result.scalars().all()
  return [Song(name=song.name, artist=song.artist, id=song.id) for song in songs]

@app.post("/songs", response_model=Song)
def add_song(song: SongCreate, session: Session = Depends(get_session)):
  song = Song(name=song.name, artist=song.artist)
  session.add(song)
  session.commit()
  session.refresh(song)
  return song

@app.get("/songs/{id}", response_model=Song)
def get_song(id: int, session: Session = Depends(get_session)):
  song = session.get(Song, id)
  if not song:
    raise HTTPException(status_code=404, detail="Song not found")
  return Song(name=song.name, artist=song.artist, id=song.id)
