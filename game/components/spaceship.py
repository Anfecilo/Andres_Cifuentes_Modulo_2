import pygame
from pygame.sprite import Sprite


from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

# casi Todo en pygame es un objeto
# Un personaje en mi juego es un objeto (instancia de algo)
# La nave (spaceship) es un personaje => necesito una clase


# SpaceShip es una clase derivada (hija) de Sprite

# spaceship tiene una "imagen"
class SpaceShip(Sprite):

    def __init__(self, controls):

        self.controls = controls # Define que tipo de controles son con los que se va a usar la nave

        # Características de la imagen
        self.image_size = (40, 60)
        self.image = pygame.transform.scale(SPACESHIP, self.image_size)
        self.image_rect = self.image.get_rect()
        self.image_rect.x = SCREEN_WIDTH / 2
        self.image_rect.y = SCREEN_HEIGHT * .8

        self.speed = 10 # Velocidad de la nave

    def update(self):

        if self.controls == 'mouse':

            cursor_pos = pygame.mouse.get_pos() # Obtener la posición actual del cursor
            
            # Actualizar la posición de la nave de acuerdo a la posición del cursor
            self.image_rect.centerx = cursor_pos[0]
            self.image_rect.centery = cursor_pos[1]

        if self.controls == 'keyboard':

            keys = pygame.key.get_pressed() # Obtener la tecla que presiono
            
            if keys[pygame.K_LEFT]: # Si preciono la tecla flecha izquierda
                self.image_rect.x -= self.speed # Su posición en X va a ser menor
        
            if keys[pygame.K_RIGHT]: # Si preciono la tecla flecha derecha
                self.image_rect.x += self.speed # Su posición en X va a ser mayor

            if self.image_rect.left < 0: # Si la nave pasa el limite de la izquierda 
                self.image_rect.right = SCREEN_WIDTH # Aparece en la parte derecha

            if self.image_rect.right > SCREEN_WIDTH: # Si la nave pasa el limite de la izquierda
                self.image_rect.left = 0 # Aparece en la parte izquierda
