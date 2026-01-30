from fastapi import APIRouter,status, Depends, HTTPException
from .. import schemas,models
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List



router = APIRouter(
    prefix= "/notes"
)

@router.get('', status_code=status.HTTP_200_OK, response_model=List[schemas.NoteRespond])
def get_notes(db: Session = Depends(get_db)):
    notes = db.query(models.Notes).all()

    return notes

# CREATE END-POINT
@router.post('', status_code=status.HTTP_201_CREATED, response_model= schemas.NoteRespond)
def create_note(user_note: schemas.NoteData, db: Session = Depends(get_db)):
    notee = models.Notes(note = user_note.note)

    db.add(notee)
    db.commit()
    db.refresh(notee)
    return notee

# DELETE ENDPOINT
@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_note(id: int, db: Session = Depends(get_db)):
    dnote = db.query(models.Notes).filter(models.Notes.noteId == id)

    if not dnote.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Details not found')
    
    dnote.delete(synchronize_session=False)
    db.commit()
    return {}

#UPDATE ENDPOINT
@router.put('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.NoteRespond)
def update_note(id: int, user_note: schemas.NoteData, db: Session = Depends(get_db)):
    noteUpdate = db.query(models.Notes).filter(models.Notes.noteId == id)
    noteUpdate.first()

    if noteUpdate.first() == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'Note with id {id} does not exist')
    
    noteUpdate.update(user_note.dict(), synchronize_session=False)
    db.commit()
    return noteUpdate.first()