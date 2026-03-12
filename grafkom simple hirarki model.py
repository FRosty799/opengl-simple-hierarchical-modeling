#terminal
#python 3.14 or later
#pip install pygame-ce PyOpenGL numpy Pillow tmx 

import os
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

os.environ['SDL_VIDEO_CENTERED'] = '1'
windowSize = (1280, 800)
pygame.display.set_mode(windowSize, pygame.DOUBLEBUF | pygame.OPENGL)
pygame.display.set_caption("OpenGL Matrix Stack - Furniture Scene")

def draw_rect(r, g, b):
    """Draws a standard 1x1 centered square."""
    glColor3f(r, g, b)
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()

def draw_table():
    glPushMatrix()
    # Table Top
    glPushMatrix()
    glScalef(0.8, 0.1, 1.0)
    draw_rect(0.5, 0.35, 0.05) # Brown
    glPopMatrix()
    
    # Legs
    for x_pos in [-0.35, 0.35]:
        glPushMatrix()
        glTranslatef(x_pos, -0.25, 0)
        glScalef(0.05, 0.4, 1.0)
        draw_rect(0.4, 0.25, 0.05)
        glPopMatrix()
    glPopMatrix()

def draw_chair():
    glPushMatrix()
    # Seat
    glPushMatrix()
    glScalef(0.4, 0.05, 1.0)
    draw_rect(0.6, 0.4, 0.1)
    glPopMatrix()
    # Backrest
    glPushMatrix()
    glTranslatef(-0.15, 0.25, 0)
    glScalef(0.05, 0.5, 1.0)
    draw_rect(0.6, 0.4, 0.1)
    glPopMatrix()
    # Legs
    for x_pos in [-0.15, 0.15]:
        glPushMatrix()
        glTranslatef(x_pos, -0.2, 0)
        glScalef(0.04, 0.35, 1.0)
        draw_rect(0.5, 0.3, 0.05)
        glPopMatrix()
    glPopMatrix()

def draw_fruit_basket():
    glPushMatrix()
    # Basket
    glPushMatrix()
    glScalef(0.3, 0.15, 1.0)
    draw_rect(0.7, 0.5, 0.3)
    glPopMatrix()
    # Apple (Fruit 1)
    glPushMatrix()
    glTranslatef(-0.05, 0.1, 0)
    glScalef(0.08, 0.08, 1.0)
    draw_rect(1.0, 0.0, 0.0)
    glPopMatrix()
    # Orange (Fruit 2)
    glPushMatrix()
    glTranslatef(0.06, 0.1, 0)
    glScalef(0.08, 0.08, 1.0)
    draw_rect(1.0, 0.6, 0.0)
    glPopMatrix()
    glPopMatrix()

def draw_ground():
    glPushMatrix()
    draw_rect(0.8, 0.8, 0.8)
    glPopMatrix()


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    glClearColor(1.0, 1.0, 1.0, 1.0) # White background
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity() 

    # 1. GROUND
    glPushMatrix()
    glTranslatef(0.0, -0.8, 0) # Position at bottom
    glScalef(2.0, 0.4, 1.0)    # Make it a wide floor
    draw_ground()
    glPopMatrix()

    # 2. TABLE & BASKET (The Hierarchy)
    glPushMatrix() 
    glTranslatef(0.1, -0.3, 0) # Move the whole set together
    draw_table()

    # The basket is "pushed" while the table's matrix is still active
    glPushMatrix()
    glTranslatef(0.0, 0.09, 0) # Position relative to table top
    glScalef(0.6, 0.6, 1.0)
    draw_fruit_basket()
    glPopMatrix() 

    glPopMatrix() # Now we close the table group

    # 3. CHAIR
    glPushMatrix()
    glTranslatef(-0.6, -0.4, 0)
    draw_chair()
    glPopMatrix()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()