import pygame
import random

# cores
preto = (0,0,0)
branco = (255,255,255)
azul = (0,0,255)
vermelho = (255,0,0)

#  imagem favicon
logo = pygame.image.load('imagens/pac-man-seeklogo.png')
pygame.display.set_icon(logo)


#  musica de fundo
pygame.mixer.init()
pygame.mixer.music.load('pacman_beginning.wav')
pygame.mixer.music.play(-1, 0.0)

class Parede(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura, cor):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([largura, altura])
        self.image.fill(cor)

        self.react = self.image.get_rect()
        self.react.top = y
        self.react.left = x

    # criar paredes do mapa
    def iniciarFazeum(listar_sprites):
        listar_parede=pygame.sprite.RenderPlain()

        #  [x, y, largura, altura]
        paredes = [ [0,0,6,600],
                  [0,0,600,6],
                  [0,600,606,6],
                  [600,0,6,606],
                  ]
        
        for item in paredes:
            parede=Parede(item[0],item,[1],item[2],item[3],azul)
            listar_parede.add(parede)
            listar_sprites.add(parede)

        return listar_parede
    
    def iniciarPortao(listar_sprites):
        portao= pygame.sprite.RenderPlain()
        listar_sprites.add(portao)
        return portao
    
    class Bola(pygame.sprite.Sprite):
        def __init__(self, cor, largura, altura):
             # chama o construtor da classe pai (Sprite)
             pygame.sprite.Sprite.__init__(self)

             self.image = pygame.Surface([largura, altura])
             self.image.fill(branco)
             self.image.set_colorkey(branco)
             pygame.draw.ellipse(self.image, cor,[0,0,largura,altura])

             self.react = self.image.get_rect()

    class Jogador(pygame.sprite.Sprite):
        mudar_x=0
        mudar_y=0

    def __init__(self,x,y, filename):
        pygame.sprite.Sprite.__init__(self)
   
        self.image = pygame.image.load(filename).convert()

        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.anterior_x = x
        self.anterior_y = y

    def mudarvelocidade(self,x,y):
        self.mudar_x+=x
        self.mudar_y+=y

    def rotate(self, angulo):
      self.image = pygame.transform.rotate(self.image, 90)

    def atualizar(self,paredes,portao):
        antigo_x=self.rect.left
        novo_x=antigo_x+self.mudar_x
        anterior_x=antigo_x+self.anterior_x
        self.rect.left = novo_x
        
        antigo_y=self.rect.top
        novo_y=antigo_y+self.mudar_y
        anterior_y=antigo_y+self.anterior_y

        x_colisao = pygame.sprite.spritecollide(self, paredes, False)
        if x_colisao:
            self.rect.left=antigo_x
        else:
            self.rect.top = novo_y

            y_colisao = pygame.sprite.spritecollide(self, paredes, False)
            if y_colisao:
                self.rect.top=antigo_y

        if portao != False:
          gate_hit = pygame.sprite.spritecollide(self, portao, False)
          if gate_hit:
            self.rect.left=antigo_x
            self.rect.top=antigo_y

    class Fantasma(Jogador):
        def mudarvelocidade(self, list, fantasma, virar, passos, l):
            try:
                z = list[virar][2]
                if passos < z:
                    self.mudar_x = list[virar][0]
                    self.mudar_y = list[virar][1]
                    passos += 1
                else:
                    if virar < l:
                        virar += 1
                    elif fantasma == "fantasminha":
                        virar = 2
                    else:
                        virar = 0
                    self.mudar_x = list[virar][0]
                    self.mudar_y = list[virar][1]
                    passos = 0
                return [virar, passos]
            except IndexError:
                return [0, 0]

    #definir movimentos dos fantasmas
    direcoes = [
      [-30,0,2],
      [0,-15,4],
      [15,0,5],
      [0,15,7],
      [-15,0,11],
      [0,-15,7],
      [-15,0,3],
      [0,15,7],
      [-15,0,7],
      [0,15,15],
      [15,0,15],
      [0,-15,3],
      [-15,0,11],
      [0,-15,7],
      [15,0,3],
      [0,-15,11],
      [15,0,9],
    ]

    pygame.init()

    #configuracoes da tela
    tela = pygame.display.set_mode([606, 606])

    pygame.display.set_caption('Pacman')

    background = pygame.Surface(tela.get_size())

    background = background.convert()
  
    background.fill(preto)

    relogio = pygame.time.Clock()

    pygame.font.init()
    font = pygame.font.Font("freesansbold.ttf", 24)

    def iniciarJogo():

        listar_sprites = pygame.sprite.RenderPlain()

        listar_bola = pygame.sprite.RenderPlain()

        listar_fantasmas = pygame.sprite.RenderPlain()

        colisao_pacman = pygame.sprite.RenderPlain()

        listar_parede = iniciarFazeum(listar_sprites)

        portao = iniciarPortao(listar_sprites)

        # localizacao dos bixo e pacman
        altura_pacman = 301
        largura_pacman = 242


        largura_fantasma = 400
        altura_fantasma = 100

        # add personagens
        pacman = Jogador(largura_pacman, altura_pacman, "persons/pacman-png-25189.png")
        listar_sprites.add(pacman)
        colisao_pacman.add(pacman)