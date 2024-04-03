from pydantic import BaseModel
from datetime import datetime

class Cita(BaseModel):
    id: int
    fecha_cita: datetime
    usuario: str
    tipo_servicio: str


