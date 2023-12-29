from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
import schemas
import crud
from database import SessionLocal

router = APIRouter(
    prefix="/prompts"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", status_code=status.HTTP_201_CREATED)
def create_prompt(prompts: schemas.PromptsRequest, db: Session = Depends(get_db)):
    prompt = crud.create_prompt(db, prompts)
    return prompt

@router.get("", response_model=List[schemas.PromptsResponse])
def get_prompts(db: Session = Depends(get_db)):
    prompts = crud.read_prompts(db)
    return prompts

@router.get("/{id}")
def get_prompt_by_id(id: int, db: Session = Depends(get_db)):
    prompt = crud.read_prompt(db, id)
    if prompt is None:
        raise HTTPException(status_code=404, detail="prompt not found")
    return prompt

@router.put("/{id}")
def update_prompt(id: int, prompts: schemas.PromptsRequest, db: Session = Depends(get_db)):
    prompt = crud.update_prompt(db, id, prompts)
    if prompt is None:
        raise HTTPException(status_code=404, detail="prompt not found")
    return prompt

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_prompt(id: int, db: Session = Depends(get_db)):
    res = crud.delete_prompt(db, id)
    if res is None:
        raise HTTPException(status_code=404, detail="prompt not found")