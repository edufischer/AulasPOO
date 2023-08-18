class Musica:
    def __init__(self, titulo, artista, genero, ano, duracao):
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.ano = ano
        self.duracao = duracao

    def tocarMusica(self):
        print(f'Música {self.titulo} começando a tocar...')
        print(f'Música {self.titulo} ainda está tocando...')

    def encerrarMusica(self):
        print(f'Música {self.titulo} terminou sua reprodução sonora.')