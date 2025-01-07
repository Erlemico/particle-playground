import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Dimensi layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Playground")

# Warna
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Perspektif Kamera
FOCAL_LENGTH = 500

# Partikel 3D
class Particle3D:
    def __init__(self, x, y, z, radius, vx, vy, vz, color):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.color = color

    def move(self):
        # Update posisi
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

        # Pantulan di batas "ruang"
        if self.x - self.radius <= -WIDTH or self.x + self.radius >= WIDTH:
            self.vx *= -1
        if self.y - self.radius <= -HEIGHT or self.y + self.radius >= HEIGHT:
            self.vy *= -1
        if self.z - self.radius <= -WIDTH or self.z + self.radius >= WIDTH:
            self.vz *= -1

    def project(self):
        # Proyeksi 3D ke 2D berdasarkan z (perspektif)
        factor = FOCAL_LENGTH / (FOCAL_LENGTH + self.z)
        x2d = self.x * factor + WIDTH // 2
        y2d = self.y * factor + HEIGHT // 2
        size = max(1, int(self.radius * factor))
        return int(x2d), int(y2d), size

    def draw(self, screen):
        x2d, y2d, size = self.project()
        pygame.draw.circle(screen, self.color, (x2d, y2d), size)

# Membuat partikel awal
particles = []
for _ in range(200):
    x = random.randint(-WIDTH, WIDTH)
    y = random.randint(-HEIGHT, HEIGHT)
    z = random.randint(-WIDTH, WIDTH)
    radius = random.randint(2, 6)
    vx = random.uniform(-2, 2)
    vy = random.uniform(-2, 2)
    vz = random.uniform(-2, 2)
    color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    particles.append(Particle3D(x, y, z, radius, vx, vy, vz, color))

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)  # Bersihkan layar

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Tambahkan partikel baru saat mouse diklik
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            x = mx - WIDTH // 2
            y = my - HEIGHT // 2
            z = random.randint(-WIDTH, WIDTH)
            radius = random.randint(2, 6)
            vx = random.uniform(-2, 2)
            vy = random.uniform(-2, 2)
            vz = random.uniform(-2, 2)
            color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            particles.append(Particle3D(x, y, z, radius, vx, vy, vz, color))

    # Update dan gambar partikel
    for particle in particles:
        particle.move()
        particle.draw(screen)

    pygame.display.flip()  # Update layar
    clock.tick(60)  # Batasi ke 60 FPS

pygame.quit()