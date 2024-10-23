# Faça um programa que abra e reproduza o áudio de um arquivo MP3.
import pygame

pygame.init()
pygame.mixer.music.load('/home/damaris/Área de trabalho/Curso Python/Exercises/exe021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()