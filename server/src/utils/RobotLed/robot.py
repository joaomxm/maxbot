import time
import random

from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
from luma.core.virtual import viewport
from luma.core.render import canvas

if __name__ == 'robot': from Faces import *  
else: from .Faces.faces import * 

class Robot:
    def __init__(self):
        self.serial = spi(port=0, device=0, gpio=noop())
        self.device = max7219(self.serial, cascaded=1, block_orientation=180, rotate=0, contrast=50)
        self.virtual = viewport(self.device, width=200, height=100)
        
    
    def draw_robot( self, face:list ):
        """ 
        Draw face robot in display led 

        Args:
            face (list): Coordenadas (y,x) para formar o rosto

        Returns:
            None
        """
        self.device.clear()
        while True:
            with canvas(self.virtual) as draw:
                draw.point(face,fill='red')
    

    def draw_robot_multiple(self, faces:list,tempo:float=0.3, shuffle=False):
        """ 
        Draw faces robot in display led 
        
        Args:
            face (list): Coordenadas (y,x) para formar o rosto
            tempo (float): Tempo para cada face ser exibida
            shuffle (boolean): Embaralhar a ordem das faces a ser exibida

        Returns:
            None

        """
        while True:
            if shuffle: random.shuffle(faces) 
            for face in faces:
                with canvas(self.virtual) as draw:
                    draw.point(face,fill='red')
                time.sleep(tempo)

    def piscar_olho(self, direcao:str, after:list):
        """ 
        Pisca um olho do robo 

        Args:
            direcao (str): Olho que será fechado 
                0 -> Esquerda
                1 -> Direita
            after (list): Coordenadas (y,x) para formar a face após a piscada

        Returns:
            None

        """
        if direcao == '0': faces = desenho_piscada_esquerda_movimento
        elif direcao == '1': faces = desenho_piscada_direita_movimento
        
        while True:
            for face in faces:
                with canvas(self.virtual) as draw:
                    draw.point(face,fill='red')
                time.sleep(1)
            break
        
        self.draw_robot(desenho_normal)
    
    def get_draw(self,name:str) -> list:
        """
        Get coordinates of face

        Args:
            name (str): name of face
        
        Returns:
            List with coordinates
        """
        return faces_dict[name]



    def clean(self):
        """ 
        CLean display process 
        """
        self.device.cleanup()
        self.serial.cleanup()

