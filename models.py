from sqlmodel import SQLModel, Field

class SongBase(SQLModel):
  name: str
  artist: str


class Song(SongBase, table=True):
  id: int = Field(default=None, nullable=False, primary_key=True)


class SongCreate(SongBase):
  pass

class Hero(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  name: str = Field(index=True)
  secret_name: str
  age: int | None = Field(default=None, index=True)
