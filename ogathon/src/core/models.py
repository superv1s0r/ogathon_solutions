from pydantic import BaseModel
from typing import List

# -- I can't use Request for GET methods as they're not accepted

#--- Virus Propagation, second subproblem ---
class VirusResponse(BaseModel):
    patternNumber: int

#--- Cipher, second subproblem ---

class CipherResponse(BaseModel):
    maximum: int


#--- Effective Recycling, second subproblem ---
class RecyclingRequest(BaseModel):
    matrix: List[List[int]]


class RecyclingResponse(BaseModel):
    moves: int



  
