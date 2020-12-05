import telepot
import pygame
import time


def handle(msg):
    chat_id = msg['chat']['id']
    message = msg['text'].lower()

    if message == 'detect':
        pygame.mixer.init()
        pygame.mixer.music.load("end.mp3")
        pygame.mixer.music.play()



bot = telepot.Bot('1419698093:AAHZJjuVqY9lzZ07sz9CVZnTZm-m4wgZSII')

bot.message_loop(handle)            

while 1:
    time.sleep(10)