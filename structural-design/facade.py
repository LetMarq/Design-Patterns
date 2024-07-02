'''
    O padrão de projeto Facade é um padrão estrutural que fornece uma interface simplificada para um 
    conjunto de interfaces em um subsistema. Facade define uma interface de alto nível que torna o subsistema 
    mais fácil de usar, organizando e unificando chamadas complexas em operações simples e diretas para o usuário.
'''

class Amplifier:
    def on(self):
        print("Amplifier on")

    def off(self):
        print("Amplifier off")

class Tuner:
    def on(self):
        print("Tuner on")

    def off(self):
        print("Tuner off")

class DvdPlayer:
    def on(self):
        print("DVD Player on")
    
    def play(self, movie):
        print(f"Playing '{movie}'")

    def off(self):
        print("DVD Player off")

class Projector:
    def on(self):
        print("Projector on")
    
    def off(self):
        print("Projector off")

class HomeTheaterFacade:
    def __init__(self):
        self.amp = Amplifier()
        self.tuner = Tuner()
        self.dvd = DvdPlayer()
        self.projector = Projector()

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.amp.on()
        self.tuner.on()
        self.dvd.on()
        self.dvd.play(movie)
        self.projector.on()

    def end_movie(self):
        print("Shutting down movie theater...")
        self.projector.off()
        self.dvd.off()
        self.tuner.off()
        self.amp.off()

# Client
home_theater = HomeTheaterFacade()
home_theater.watch_movie("Inception")
home_theater.end_movie()
