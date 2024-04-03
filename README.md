# BarberBOT

BarberBOT es una aplicación para gestionar citas en una barbería. Permite a los clientes agendar citas para servicios de barbería de manera fácil y rápida.

## Instalación

1. Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/JeefersonInsuasty/barberbot.git

cd barberbot
pip install -r requirements.txt

uvicorn main:app --reload

http://localhost:8000

GET /citas/ - Obtiene la lista de citas
POST /citas/ - Crea una nueva cita
PUT /citas/{cita_id} - Actualiza una cita existente
DELETE /citas/{cita_id} - Elimina una cita existente
