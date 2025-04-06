import random

class Juego:
    def __init__(self, numero_de_vidas):
        self.numeroDeVidas = numero_de_vidas
        self.record = 0
    
    def reiniciaPartida(self):
        self.numeroDeVidas = 3  # Reinicia el número de vidas (puedes cambiar el valor por defecto)
    
    def actualizaRecord(self):
        self.record += 1
    
    def quitaVida(self):
        self.numeroDeVidas -= 1
        return self.numeroDeVidas > 0

class JuegoAdivinaNumero(Juego):
    def __init__(self, numero_de_vidas):
        super().__init__(numero_de_vidas)
        self.numeroAAdivinar = 0
    
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("Adivina un número entre 0 y 10")
        
        while True:
            try:
                numero_usuario = int(input("Introduce un número: "))
                if numero_usuario == self.numeroAAdivinar:
                    print("¡Acertaste!")
                    self.actualizaRecord()
                    break
                else:
                    if self.quitaVida():
                        mensaje = "El número es mayor" if numero_usuario < self.numeroAAdivinar else "El número es menor"
                        print(f"Incorrecto. {mensaje}. Intenta de nuevo.")
                    else:
                        print("No te quedan más vidas. Fin del juego.")
                        break
            except ValueError:
                print("Por favor, ingresa un número válido.")

class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()

# Ejecutar el juego
if __name__ == "__main__":
    Aplicacion.main()