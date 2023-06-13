import pygame


from game.components.spaceship import SpaceShip # Importa la nave
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE # Importa las características de la ventana

# Game tiene un "Spaceship" - Por lo general esto es iniciliazar un objeto Spaceship en el __init__

# Game tiene un "Spaceship" - Por lo general esto es iniciliazar un objeto Spaceship en el __init__
class Game:

    def __init__(self):

        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        # Variables inicio fondo
        self.x_pos_bg = 0
        self.y_pos_bg = 0

        self.playing = False # Variable para cambiar el ciclo
        self.game_speed = 10 # Variable de la velocidad del juego

        self.button_rect = pygame.Rect(20, 20, 200, 50) # Variable que tiene el tamaño de los botones

        self.controls = '' # Variable de cuales controles se van a usar

        self.game_mode = '' # Variable de cual es el tipo de juego
        self.game_mode_select = False # Variable define si ya se selecciono el modo

        self.spaceship = SpaceShip(self.controls) # Variable que contiene la nave aliada

    def run(self):
        # Game loop: events - update - draw
        self.playing = True

        # while self.playing == True
        while self.playing: # Mientras el atributo playing (self.playing) sea true "repito"
            self.handle_events()
            self.update()
            self.draw()
        else:
            print("Something ocurred to quit the game!!!")
        
        pygame.display.quit()
        pygame.quit()

    def change_controls(self, controls):

        self.game_mode_select = True # Se define como ya seleccionado el modo de juego
        self.controls = controls # Se asigna a los controles cuales van a ser
        self.spaceship = SpaceShip(self.controls) # Se crea la nave con nuevos controles

    def handle_events(self):

        # Para un "event" (es un elemento) en la lista (secuencia) que me retorna el metodo get()
        for event in pygame.event.get():

            # Si el "event" type es igual a pygame.QUIT entonces cambiamos playing a False
            if event.type == pygame.QUIT:
                self.playing = False

            # Si el 'event' es un clic de ratón
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Captura el lugar del mause en la pantalla
                mouse_pos = pygame.mouse.get_pos()

                # Verifica a cual botón le dio click
                if self.first_button_rect.collidepoint(mouse_pos):
                    self.change_controls('mouse') # Ejecuta la función para cambiar los controles y envia que tipo de control va a ser
                if self.second_button_rect.collidepoint(mouse_pos):
                    self.change_controls('keyboard') # Ejecuta la función para cambiar los controles y envia que tipo de control va a ser

    def update(self):

        # Se ejecuta la función update de la SpaceShip
        self.spaceship.update()

    def draw(self):

        self.clock.tick(FPS) # Velocidad de los fotogramas del juego
        self.screen.fill((255, 255, 255)) # Rellena la pantalla de color blanco
        self.draw_background() # Ejecuta la función para poner el fondo y que suba de forma suave

        if self.game_mode_select == False: # Verifica si ya se selecciono el modo de juego

            # Se usa un tamaño de letra de 24 pixeles para el texto de los botones 'none' indica que no especifico la tipografía
            font = pygame.font.SysFont(None, 24)

            first_button_text_rendered = font.render('infinite', True, (255, 255, 255)) # Renderiza el texto con bordes suaves y color blanco

            # Trae las dimenciones del rectangulo y la posición del texto, además establece todo en el centro de la pantalla
            button_text_rect = first_button_text_rendered.get_rect(center = self.screen.get_rect().center)
            button_text_rect.move_ip(-100, 0) # Se mueve el texto 100 px antes

            # Se asigna el ancho y alto del botón
            button_rect_width = self.button_rect.width
            button_rect_height = self.button_rect.height
            button_rect_top = (self.screen.get_height() - button_rect_height) / 2 # Se define el alto de los 2 botones

            button_rect_left = ((self.screen.get_width() - button_rect_width) / 2) - 100 # Se mueve 100 pixeles antes la caja

            self.first_button_rect = pygame.Rect(button_rect_left, button_rect_top, button_rect_width, button_rect_height) # Crea el objeto
            pygame.draw.rect(self.screen, (0, 0, 0), self.first_button_rect) # Dibuja un rectángulo solido con el color negro
            self.screen.blit(first_button_text_rendered, button_text_rect) # Dibujamos el objeto que creamos en pantalla

            second_button_text_rendered = font.render('levels', True, (0, 0, 0)) # Renderiza el texto con bordes suaves y color blanco
            
            # Trae las dimenciones del rectangulo y la posición del texto, además establece todo en el centro de la pantalla
            button_text_rect = second_button_text_rendered.get_rect(center = self.screen.get_rect().center)
            button_text_rect.move_ip(+100, 0) # Se mueve el texto 100 px después

            button_rect_left = ((self.screen.get_width() - button_rect_width) / 2) + 100 # Se mueve 100 pixeles después la caja

            self.second_button_rect = pygame.Rect(button_rect_left, button_rect_top, button_rect_width, button_rect_height) # Crea el objeto
            pygame.draw.rect(self.screen, (255, 255, 255), self.second_button_rect) # Dibuja un rectángulo solido con el color blanco
            self.screen.blit(second_button_text_rendered, button_text_rect) # Dibujamos el botón en pantalla

        else:
            self.screen.blit(self.spaceship.image, self.spaceship.image_rect) # dibujamos la nave en pantalla
            
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
