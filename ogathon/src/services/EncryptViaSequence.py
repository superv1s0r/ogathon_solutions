class SecuenciaCifrado:
    def __init__(self):
        pass

    def suma_cuadrados_digitos(self, n: int) -> int:
        """
        Calcula la suma de los cuadrados de los dígitos de un número.
        """
        return sum(int(digit)**2 for digit in str(n))

    def genera_secuencia(self, n: int) -> bool:
        """
        Genera la secuencia de un número hasta llegar a un ciclo.
        Retorna True si la secuencia alcanza 89, False si alcanza 1.
        """
        while n != 1 and n != 89:
            n = self.suma_cuadrados_digitos(n)
        return n == 89

    def execute(self, maximo: int) -> int:
        """
        Cuenta cuántos números desde 1 hasta 'maximo' generan secuencias que terminan en 89.
        """
        contador = 0
        for i in range(1, maximo + 1):
            if self.genera_secuencia(i):
                contador += 1
        return contador
