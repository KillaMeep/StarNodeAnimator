import pygame
import sys
import random
import math
import os
import shutil
import subprocess

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Seamless Looping Animation")

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
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.size)

# Create random stars
stars = []
for _ in range(1600):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    size = random.randint(1, 3)
    speed_x = random.uniform(-.75, .75)
    speed_y = random.uniform(-.75, .75)
    creates_node = random.random() < 0.3  # 30% chance to create node
    stars.append(Star(x, y, size, speed_x, speed_y, creates_node))

# Create output directory if it doesn't exist
output_dir = "frames"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Main loop
clock = pygame.time.Clock()
frame_count = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move stars
    for star in stars:
        star.move()

    # Draw background
    screen.fill(BLACK)

    # Draw stars
    for star in stars:
        star.draw()

    # Draw connections between stars
    for i in range(len(stars)):
        for j in range(i + 1, len(stars)):
            if stars[i].creates_node and stars[j].creates_node:
                dx = stars[i].x - stars[j].x
                dy = stars[i].y - stars[j].y
                distance = math.sqrt(dx * dx + dy * dy)
                if distance < 100:
                    pygame.draw.line(screen, WHITE, (stars[i].x, stars[i].y), (stars[j].x, stars[j].y), 1)

    # Update display
    pygame.display.flip()

    # Capture and save frame
    frame_path = os.path.join(output_dir, f"frame_{frame_count:04d}.png")
    pygame.image.save(screen, frame_path)

    # Print progress
    print(f"Progress: {frame_count / 8640 * 100:.2f}%")

    # Cap the frame rate
    clock.tick(144)

    # Break the loop after 8640 frames (1 minute at 144 fps)
    frame_count += 1
    if frame_count >= 8640:
        break

pygame.quit()

# Convert frames to MP4 video using ffmpeg
video_output = "animation.mp4"
subprocess.run(["ffmpeg", "-framerate", "144", "-i", f"{output_dir}/frame_%04d.png", "-c:v", "libx264", "-pix_fmt", "yuv420p", video_output])

# Clean up temporary frames directory
shutil.rmtree(output_dir)
