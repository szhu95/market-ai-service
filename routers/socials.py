from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
import schemas
import crud
from database import SessionLocal

router = APIRouter(
    prefix="/socials"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", status_code=status.HTTP_201_CREATED)
def create_social(socials: schemas.SocialsRequest, db: Session = Depends(get_db)):
    social = crud.create_social(db, socials)
    return social

@router.get("", response_model=List[schemas.SocialsResponse])
def get_socials(db: Session = Depends(get_db)):
    socials = crud.read_socials(db)
    return socials

@router.get("/{id}")
def get_social_by_id(id: int, db: Session = Depends(get_db)):
    social = crud.read_social(db, id)
    if social is None:
        raise HTTPException(status_code=404, detail="social not found")
    return social

@router.put("/{id}")
def update_social(id: int, socials: schemas.SocialsRequest, db: Session = Depends(get_db)):
    social = crud.update_social(db, id, socials)
    if social is None:
        raise HTTPException(status_code=404, detail="social not found")
    return social

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_social(id: int, db: Session = Depends(get_db)):
    res = crud.delete_social(db, id)
    if res is None:
        raise HTTPException(status_code=404, detail="social not found")