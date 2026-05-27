from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time

def Circle(xc, yc, x, y):
    """Draw 8 symmetric points of the circle"""
    glVertex2f(xc + x, yc + y)
    glVertex2f(xc - x, yc + y)
    glVertex2f(xc + x, yc - y)
    glVertex2f(xc - x, yc - y)
    glVertex2f(xc + y, yc + x)
    glVertex2f(xc - y, yc + x)
    glVertex2f(xc + y, yc - x)
    glVertex2f(xc - y, yc - x)

def bresenhamCircle(xc, yc, R):
    """Draw circle outline using Bresenham algorithm"""
    x = 0
    y = R
    p = 3 - 2 * R
    
    Circle(xc, yc, x, y)
    
    while x <= y: 
        if p < 0:
            p = p + 4 * x + 6
            x = x + 1
        else:
            p = p + 4 * (x - y) + 10
            x = x + 1
            y = y - 1
        
        Circle(xc, yc, x, y)

def horlin(x1, x2, y):
    """Draw horizontal line from x1 to x2 at y"""
    for x in range(int(x1), int(x2) + 1):
        glVertex2f(x, y)

def filcircle(xc, yc, r):
    """Draw filled circle using horizontal lines"""
    x = 0
    y = r
    p = 3 - 2 * r
    
    horlin(xc - y, xc + y, yc)
    
    while x <= y:
        if p < 0:
            p = p + 4 * x + 6
            x = x + 1
        else:
            p = p + 4 * (x - y) + 10
            x = x + 1
            y = y - 1
        
        horlin(xc - x, xc + x, yc + y)
        horlin(xc - x, xc + x, yc - y) 
        horlin(xc - y, xc + y, yc + x)
        horlin(xc - y, xc + y, yc - x)

def fill_rect(x, y, w, h):
    """Draw filled rectangle using horizontal lines"""
    for j in range(int(y), int(y + h) + 1):
        for i in range(int(x), int(x + w) + 1):
            glVertex2f(i, j)

def draw_rect(x, y, w, h):
    """Draw rectangle outline"""
    # Bottom edge
    for i in range(int(x), int(x + w) + 1):
        glVertex2f(i, y)
    # Top edge
    for i in range(int(x), int(x + w) + 1):
        glVertex2f(i, y + h)
    # Left edge
    for i in range(int(y), int(y + h) + 1):
        glVertex2f(x, i)
    # Right edge
    for i in range(int(y), int(y + h) + 1):
        glVertex2f(x + w, i)

def draw_town():
    """Draw the entire town"""
    
    # ===== FIRST: Draw Sky and Ground (Background) =====
    
    # Sky (top half)
    glColor3f(0.5, 0.8, 1.0)  # Sky blue
    for i in range(0, 800):
        for j in range(300, 600):
            glVertex2f(i, j)
    
    # Ground (bottom half)
    glColor3f(0.2, 0.6, 0.2)  # Grass green
    for i in range(0, 800):
        for j in range(0, 300):
            glVertex2f(i, j)
    
    # ===== SECOND: Draw Roads (so they appear under buildings but above ground) =====
    
    # Horizontal road
    glColor3f(0.5, 0.5, 0.5)  # Gray road
    for i in range(0, 800):
        for j in range(135, 155):
            glVertex2f(i, j)
    
    # Road center line (yellow dashed)
    glColor3f(1.0, 1.0, 0.0)  # Yellow
    for i in range(0, 800, 20):  # Dashed line
        for j in range(144, 146):
            for k in range(10):
                if i + k < 800:
                    glVertex2f(i + k, j)
    
    # Vertical road
    glColor3f(0.5, 0.5, 0.5)
    for i in range(380, 400):
        for j in range(0, 300):
            glVertex2f(i, j)
    
    # Vertical road center line
    glColor3f(1.0, 1.0, 0.0)
    for i in range(389, 391):
        for j in range(0, 300, 20):
            for k in range(10):
                if j + k < 300:
                    glVertex2f(i, j + k)
    
    # ===== THIRD: Draw Buildings =====
    
    # Building 1 (left)
    glColor3f(0.8, 0.6, 0.4)  # Light brown fill
    fill_rect(50, 155, 80, 180)
    glColor3f(0.5, 0.3, 0.1)  # Dark brown outline
    draw_rect(50, 155, 80, 180)
    
    # Windows
    glColor3f(0.3, 0.6, 0.9)  # Blue
    fill_rect(65, 250, 15, 20)
    fill_rect(95, 250, 15, 20)
    fill_rect(65, 200, 15, 20)
    fill_rect(95, 200, 15, 20)
    
    # Door
    glColor3f(0.4, 0.2, 0.0)
    fill_rect(75, 155, 25, 40)
    
    # Building 2 (center-left)
    glColor3f(0.7, 0.7, 0.7)  # Gray fill
    fill_rect(170, 155, 90, 220)
    glColor3f(0.3, 0.3, 0.3)  # Dark gray outline
    draw_rect(170, 155, 90, 220)
    
    glColor3f(0.3, 0.5, 0.9)
    fill_rect(185, 280, 18, 22)
    fill_rect(225, 280, 18, 22)
    fill_rect(185, 220, 18, 22)
    fill_rect(225, 220, 18, 22)
    
    glColor3f(0.4, 0.2, 0.0)
    fill_rect(200, 155, 25, 45)
    
    # Building 3 (center tower)
    glColor3f(0.9, 0.3, 0.3)  # Red fill
    fill_rect(310, 155, 70, 290)
    glColor3f(0.6, 0.1, 0.1)  # Dark red outline
    draw_rect(310, 155, 70, 290)
    
    glColor3f(1.0, 1.0, 0.8)
    fill_rect(325, 340, 14, 20)
    fill_rect(350, 340, 14, 20)
    fill_rect(325, 280, 14, 20)
    fill_rect(350, 280, 14, 20)
    fill_rect(325, 220, 14, 20)
    fill_rect(350, 220, 14, 20)
    
    glColor3f(0.3, 0.2, 0.1)
    fill_rect(333, 155, 25, 50)
    
    # Clock on tower
    glColor3f(1.0, 1.0, 1.0)
    filcircle(345, 400, 20)
    glColor3f(0.0, 0.0, 0.0)
    filcircle(345, 400, 15)
    glColor3f(1.0, 1.0, 1.0)
    filcircle(345, 400, 2)
    glColor3f(0.0, 0.0, 0.0)
    bresenhamCircle(345, 400, 20)
    
    # Clock hands
    glColor3f(0.0, 0.0, 0.0)
    # Hour hand
    for i in range(345, 346):
        for j in range(388, 401):
            glVertex2f(i, j)
    # Minute hand
    for i in range(345, 356):
        for j in range(400, 401):
            glVertex2f(i, j)
    
    # Building 4 (right)
    glColor3f(0.4, 0.7, 0.5)  # Green fill
    fill_rect(480, 155, 80, 190)
    glColor3f(0.2, 0.5, 0.3)  # Dark green outline
    draw_rect(480, 155, 80, 190)
    
    glColor3f(0.8, 0.9, 1.0)
    fill_rect(495, 250, 16, 22)
    fill_rect(525, 250, 16, 22)
    fill_rect(495, 200, 16, 22)
    fill_rect(525, 200, 16, 22)
    
    glColor3f(0.4, 0.2, 0.0)
    fill_rect(507, 155, 25, 45)
    
    # Building 5 (small rightmost)
    glColor3f(0.9, 0.7, 0.3)  # Orange fill
    fill_rect(610, 155, 60, 150)
    glColor3f(0.6, 0.4, 0.1)
    draw_rect(610, 155, 60, 150)
    
    glColor3f(0.3, 0.6, 0.9)
    fill_rect(622, 230, 12, 18)
    fill_rect(645, 230, 12, 18)
    fill_rect(622, 190, 12, 18)
    fill_rect(645, 190, 12, 18)
    
    # ===== FOURTH: Draw Trees =====
    
    # Tree 1
    glColor3f(0.5, 0.3, 0.1)  # Trunk
    fill_rect(20, 155, 12, 50)
    glColor3f(0.0, 0.6, 0.0)  # Leaves
    filcircle(26, 205, 25)
    glColor3f(0.0, 0.4, 0.0)
    bresenhamCircle(26, 205, 25)
    
    # Tree 2
    glColor3f(0.5, 0.3, 0.1)
    fill_rect(700, 155, 12, 60)
    glColor3f(0.0, 0.7, 0.0)
    filcircle(706, 215, 28)
    glColor3f(0.0, 0.5, 0.0)
    bresenhamCircle(706, 215, 28)
    
    # Tree 3
    glColor3f(0.5, 0.3, 0.1)
    fill_rect(750, 155, 12, 45)
    glColor3f(0.0, 0.5, 0.0)
    filcircle(756, 200, 22)
    glColor3f(0.0, 0.3, 0.0)
    bresenhamCircle(756, 200, 22)
    
    # ===== FIFTH: Sun and Clouds (Top layer) =====
    
    # Sun
    glColor3f(1.0, 1.0, 0.0)  # Yellow fill
    filcircle(720, 520, 40)
    glColor3f(0.9, 0.6, 0.0)  # Orange outline
    bresenhamCircle(720, 520, 40)
    
    # Sun rays
    glColor3f(1.0, 0.8, 0.0)
    for angle in range(0, 360, 30):
        import math
        rad = math.radians(angle)
        x1 = 720 + 45 * math.cos(rad)
        y1 = 520 + 45 * math.sin(rad)
        x2 = 720 + 65 * math.cos(rad)
        y2 = 520 + 65 * math.sin(rad)
        # Draw ray as line of points
        for t in range(0, 21):
            xt = x1 + (x2 - x1) * t / 20
            yt = y1 + (y2 - y1) * t / 20
            glVertex2f(xt, yt)
    
    # Clouds
    glColor3f(1.0, 1.0, 1.0)
    filcircle(100, 530, 30)
    filcircle(135, 545, 35)
    filcircle(170, 530, 30)
    filcircle(135, 515, 28)
    
    filcircle(500, 560, 25)
    filcircle(530, 570, 30)
    filcircle(560, 555, 25)
    
    # Cloud outlines
    glColor3f(0.8, 0.8, 0.8)
    bresenhamCircle(100, 530, 30)
    bresenhamCircle(135, 545, 35)
    bresenhamCircle(170, 530, 30)
    bresenhamCircle(135, 515, 28)
    bresenhamCircle(500, 560, 25)
    bresenhamCircle(530, 570, 30)
    bresenhamCircle(560, 555, 25)
    
    # ===== SIXTH: Flowers =====
    glColor3f(1.0, 0.3, 0.6)  # Pink
    filcircle(140, 80, 5)
    filcircle(155, 75, 5)
    filcircle(440, 70, 5)
    filcircle(460, 65, 5)
    filcircle(670, 85, 5)
    
    glColor3f(1.0, 1.0, 0.0)  # Yellow center
    filcircle(140, 80, 2)
    filcircle(155, 75, 2)
    filcircle(440, 70, 2)
    filcircle(460, 65, 2)
    filcircle(670, 85, 2)

def showScreen():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 800, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  
    glOrtho(0, 800, 0, 600, 0, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Single glBegin/glEnd block
    glBegin(GL_POINTS)
    draw_town()
    glEnd()
    
    glFlush()

# Initialize and run
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 600) 
glutInitWindowPosition(100, 100)
glutCreateWindow(b'2d Town view')
glutDisplayFunc(showScreen)
glutMainLoop()