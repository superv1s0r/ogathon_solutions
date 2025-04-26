
from typing import List

class ReciclajeSeparador:
    def __init__(self):
        pass

    def execute(self, matrix: List[List[int]]) -> int:
        n = len(matrix)  # Número de contenedores (filas)

        tipos = [0, 1, 2]  # Vidrio, Cartón, Plástico

        from itertools import permutations

        min_movimientos = float('inf')

        # Probar todas las permutaciones posibles de asignación tipo -> contenedor
        for asignacion in permutations(range(n), 3):
            movimientos = 0

            for tipo_residuo, contenedor_destino in enumerate(asignacion):
                for contenedor_idx in range(n):
                    if contenedor_idx == contenedor_destino:
                        continue
                    movimientos += matrix[contenedor_idx][tipo_residuo]

            min_movimientos = min(min_movimientos, movimientos)

        return int(min_movimientos)
