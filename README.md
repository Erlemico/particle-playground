# Particle Playground

**Particle Playground** is a particle simulation built with Pygame, where particles move within a 3D space and are projected onto a 2D screen using perspective. Users can add new particles by clicking the mouse.

## Key Features
1. **3D Particle Simulation**:
   - Particles have coordinates `(x, y, z)` within a 3D space.
   - Particle size changes based on perspective (distant particles appear smaller).

2. **Interactivity**:
   - Add new particles by clicking the mouse.
   - Particles bounce off the boundaries of the simulation space.

3. **Dynamic Visualization**:
   - Each frame visualizes particle motion in real-time with perspective projection effects.

## Prerequisites
- Python 3.10 or later.
- Pygame library.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd particle-playground
   ```

2. Install Pygame:
   ```bash
   pip install pygame
   ```

3. Run the program:
   ```bash
   python main.py
   ```

## Code Explanation

### Main Structure
- **Particle3D Class**:
  - Handles particle properties such as position `(x, y, z)`, velocity `(vx, vy, vz)`, and color.
  - Main methods:
    - `move`: Updates particle position and handles bouncing off boundaries.
    - `project`: Converts 3D coordinates to 2D screen coordinates based on perspective.
    - `draw`: Renders the particle on the screen.

- **Main Loop**:
  - Handles events such as mouse input.
  - Updates particle positions and redraws the screen each frame.

### Perspective Projection
- Uses the formula:
  ```
  factor = FOCAL_LENGTH / (FOCAL_LENGTH + self.z)
  x2d = self.x * factor + WIDTH // 2
  y2d = self.y * factor + HEIGHT // 2
  size = max(1, int(self.radius * factor))
  ```
- Distant particles appear smaller, creating a depth illusion.

### Interactivity
- Clicking the mouse adds new particles with random attributes (position, velocity, color).

## How It Works
1. **Particle Bouncing**:
   - Particles reverse their velocity upon reaching the virtual space boundaries, simulating a bounce.
2. **Adding New Particles**:
   - Mouse clicks generate new particles at the cursor position.
3. **Perspective Effect**:
   - Uses a focal length to simulate depth.

## Example
- The initial screen displays 200 randomly generated particles moving in 3D space.
- Click on the screen to add more particles.

## License
This project is licensed under the [MIT License](LICENSE).