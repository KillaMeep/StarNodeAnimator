import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import sys
import random
import math
import os
import shutil
import subprocess

# Initialize Pygame
pygame.init()
pygame.display.set_mode((1920, 1080), DOUBLEBUF | OPENGL)

# Set screen dimensions
screen_width = 1920
screen_height = 1080
glViewport(0, 0, screen_width, screen_height)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, screen_width, screen_height, 0, -1, 1)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define Star class
class Star:
    def __init__(self, x, y, size, speed_x, speed_y, creates_node):
        self.x = x
        self.y = y
        self.size = size
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.start_x = x
        self.start_y = y
        self.creates_node = creates_node

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x > screen_width:
            self.x = 0
        if self.y > screen_height:
            self.y = 0
        if self.x < 0:
            self.x = screen_width
        if self.y < 0:
            self.y = screen_height

    def draw(self):
        glBegin(GL_POINTS)
        glVertex2f(self.x, self.y)
        glEnd()

# Create random stars
stars = []
for _ in range(400):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    size = random.randint(1, 5)  # Update to random size between 1 and 5
    speed_x = random.uniform(-1, 1)
    speed_y = random.uniform(-1, 1)
    creates_node = random.random() < 0.5  # 30% chance to create node
    stars.append(Star(x, y, size, speed_x, speed_y, creates_node))

# Create output directory if it doesn't exist
output_dir = "frames"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Main loop
clock = pygame.time.Clock()
frame_count = 0
running = True
desired_fps = 144
desired_duration_sec = 60
frames_to_skip = math.ceil(desired_fps / pygame.time.get_ticks())
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move stars
    for star in stars:
        star.move()

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw stars
    for star in stars:
        glColor3fv(WHITE)  # Set color to white for stars
        glPointSize(star.size)  # Set the size of the point
        star.draw()

    # Draw connections between stars
    for i in range(len(stars)):
        for j in range(i + 1, len(stars)):
            if stars[i].creates_node and stars[j].creates_node:
                dx = stars[i].x - stars[j].x
                dy = stars[i].y - stars[j].y
                distance = math.sqrt(dx * dx + dy * dy)
                if distance < 100:
                    glBegin(GL_LINES)
                    glVertex2f(stars[i].x, stars[i].y)
                    glVertex2f(stars[j].x, stars[j].y)
                    glEnd()

    # Update display
    pygame.display.flip()

    # Capture and save frame
    frame_path = os.path.join(output_dir, f"frame_{frame_count:04d}.png")
    pygame.image.save(pygame.display.get_surface(), frame_path)

    # Print progress
    print(f"Progress: {frame_count / (desired_fps * desired_duration_sec) * 100:.2f}%")

    # Cap the frame rate
    clock.tick(desired_fps)

    # Skip frames if needed
    for _ in range(frames_to_skip - 1):
        pygame.event.get()

    # Break the loop after reaching the desired duration
    frame_count += 1
    if frame_count >= desired_fps * desired_duration_sec:
        break

pygame.quit()

# Convert frames to MP4 video using ffmpeg
video_output = "animation.mp4"
subprocess.run(["ffmpeg", "-framerate", str(desired_fps), "-i", f"{output_dir}/frame_%04d.png", "-c:v", "libx264", "-pix_fmt", "yuv420p", video_output])

# Clean up temporary frames directory
shutil.rmtree(output_dir)
