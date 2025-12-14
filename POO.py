# Programa para calcular el promedio semanal del clima

# Programación Orientada a Objetos (POO)

class Clima:
    """
    Clase que representa la información del clima semanal.
    Aplica encapsulamiento al manejar las temperaturas
    como un atributo privado.
    """

    def __init__(self):
        self.__temperaturas = []  # Encapsulamiento

    def ingresar_temperaturas(self):
        """
        Método para ingresar las temperaturas
        de los 7 días de la semana.
        """
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.__temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Método que calcula el promedio semanal.
        """
        return sum(self.__temperaturas) / len(self.__temperaturas)


def main():
    """
    Función principal que utiliza la clase Clima.
    """
    print("Cálculo del promedio semanal del clima (POO)")
    clima_semanal = Clima()
    clima_semanal.ingresar_temperaturas()
    promedio = clima_semanal.calcular_promedio()
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")

main()
