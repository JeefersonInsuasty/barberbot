from sqlalchemy.orm import Session
from models.cita import Cita
from database.database import SessionLocal

def get_citas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Cita).offset(skip).limit(limit).all()

def create_cita(db: Session, cita: Cita):
    db_cita = Cita(**cita.dict())
    db.add(db_cita)
    db.commit()
    db.refresh(db_cita)
    return db_cita

def update_cita(db: Session, cita_id: int, cita: Cita):
    db_cita = db.query(Cita).filter(Cita.id == cita_id).first()
    if db_cita:
        for var, value in vars(cita).items():
            setattr(db_cita, var, value)
        db.commit()
        db.refresh(db_cita)
    return db_cita

def delete_cita(db: Session, cita_id: int):
    db_cita = db.query(Cita).filter(Cita.id == cita_id).first()
    if db_cita:
        db.delete(db_cita)
        db.commit()
        return db_cita


