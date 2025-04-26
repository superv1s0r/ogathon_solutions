class Propagacion:
    def __init__(self):
        pass
    
    def execute(self, distancia):
  
        # Condiciones iniciales
        if distancia == 0:
            return 1
        elif distancia == 1:
            return 1
        
        # Inicializamos los dos primeros valores
        P_0 = 1  # P(0)
        P_1 = 1  # P(1)
        
        # Calculamos P(D) para D = 2 hasta distancia
        for D in range(2, distancia + 1):
            P_D = P_0 + P_1  # Usamos la relación recursiva
            P_0, P_1 = P_1, P_D  # Desplazamos los valores para el siguiente paso
        
        return P_1  # P(distancia) es el último valor calculado



