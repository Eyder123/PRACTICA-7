import random

class Juego:
    def __init__(self, numero_de_vidas):
        self.numeroDeVidas = numero_de_vidas
        self.record = 0
    
    def reiniciaPartida(self):
        self.numeroDeVidas = 3
    
    def actualizaRecord(self):
        self.record += 1
    
    def quitaVida(self):
        self.numeroDeVidas -= 1
        return self.numeroDeVidas > 0

class JuegoAdivinaNumero(Juego):
    def __init__(self, numero_de_vidas):
        super().__init__(numero_de_vidas)
        self.numeroAAdivinar = 0
    
    def validaNumero(self, numero):
        return 0 <= numero <= 10
    
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("Adivina un número entre 0 y 10")
        
        while True:
            try:
                numero_usuario = int(input("Introduce un número: "))
                if not self.validaNumero(numero_usuario):
                    print("Número fuera de rango. Intenta de nuevo.")
                    continue
                
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

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if 0 <= numero <= 10 and numero % 2 == 0:
            return True
        print("Error: Debes ingresar un número par entre 0 y 10.")
        return False

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if 0 <= numero <= 10 and numero % 2 != 0:
            return True
        print("Error: Debes ingresar un número impar entre 0 y 10.")
        return False

class Aplicacion:
    @staticmethod
    def main():
        juego1 = JuegoAdivinaNumero(3)
        juego2 = JuegoAdivinaPar(3)
        juego3 = JuegoAdivinaImpar(3)
        
        print("\nJuego Adivina Número Normal")
        juego1.juega()
        
        print("\nJuego Adivina Número Par")
        juego2.juega()
        
        print("\nJuego Adivina Número Impar")
        juego3.juega()

if __name__ == "__main__":
    Aplicacion.main()
