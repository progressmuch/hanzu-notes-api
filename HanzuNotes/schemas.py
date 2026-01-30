from pydantic import BaseModel


class NoteData(BaseModel):
    note: str

class NoteRespond(BaseModel):
    note: str 
    noteId: int
    class Config:
        from_attributes = True