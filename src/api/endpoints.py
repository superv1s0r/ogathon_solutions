from fastapi import APIRouter
from typing import List

from src.core.models import (
    VirusResponse,
    CipherResponse,
    RecyclingRequest, RecyclingResponse
)

from src.services.EncryptViaSequence import SecuenciaCifrado
from src.services.PredVirusPropagation import Propagacion
from src.services.EffectiveRecycle import ReciclajeSeparador

router = APIRouter()

# Instanciación de servicios
propagacion = Propagacion()
cipher = SecuenciaCifrado()
recycle = ReciclajeSeparador()

# Virus propagation endpoint
@router.get("/solution-1", response_model=VirusResponse)
def virus_simulate(n: int):
    result = propagacion.execute(n)
    return VirusResponse(patternNumber=result)

# Sequence encryption endpoint
@router.get("/solution-2", response_model=CipherResponse)
def sequence_cipher(n: int):
    result = cipher.execute(n)
    return CipherResponse(maximum=result)

# Recycling separation endpoint
@router.post("/solution-3", response_model=RecyclingResponse)
def recycling_moves(matrix: RecyclingRequest):
    result = recycle.execute(matrix.matrix)
    return RecyclingResponse(moves=result)
