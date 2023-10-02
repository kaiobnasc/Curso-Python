import pygame   
pygame.init() #inicia a biblioteca pygame
pygame.mixer.music.load("021_audio.mp3") #carrega o arquivo contendo o áudio
pygame.mixer.music.play() #play na música
input() #necessita do input devido a atualização do python
pygame.event.wait() #espera tocar a música e encerra o programa

