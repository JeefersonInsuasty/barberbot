from fastapi import APIRouter, HTTPException
from typing import List
from database import crud, database
from models.cita import Cita

router = APIRouter()

@router.get("/citas/", response_model=List[Cita])
async def read_citas(skip: int = 0, limit: int = 10):
    return crud.get_citas(skip=skip, limit=limit)

@router.post("/citas/", response_model=Cita)
async def create_cita(cita: Cita):
    return crud.create_cita(db=database.SessionLocal(), cita=cita)

@router.put("/citas/{cita_id}", response_model=Cita)
async def update_cita(cita_id: int, cita: Cita):
    return crud.update_cita(db=database.SessionLocal(), cita_id=cita_id, cita=cita)

@router.delete("/citas/{cita_id}", response_model=Cita)
async def delete_cita(cita_id: int):
    return crud.delete_cita(db=database.SessionLocal(), cita_id=cita_id)

