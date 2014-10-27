import pygame
import gate
import sys
import traceback
import math
import time

module = sys.modules[__name__]
poll   = gate.new(module)

screen = pygame.display.set_mode((320, 240), pygame.DOUBLEBUF)

def process_event(ev):
    if ev.type == pygame.KEYDOWN:
        if ev.key == pygame.K_DOWN:
            print 'down'
        if ev.key == pygame.K_LEFT:
            print 'left'
        if ev.key == pygame.K_RIGHT:
            print 'right'
        if ev.key == pygame.K_UP:
            print 'up'

def paint(t):
    screen.fill((10, 10, 10))

live = True
crash = False
while live:
    try:
        poll(crash)
        for ev in pygame.event.get():
            process_event(ev)
            if ev.type == pygame.QUIT:
                live = False
        paint(time.time())
        pygame.display.flip()
        crash = False
    except Exception as exc:
        traceback.print_exc()
        crash = True
