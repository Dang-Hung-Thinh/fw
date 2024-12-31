import turtle
import random
import time
import math


screen = turtle.Screen()
screen.bgcolor("black")
screen.title("🎆 Ultra Realistic Fireworks - HAPPY NEW YEAR 2025 🎆")
screen.setup(width=1000, height=700)


launcher = turtle.Turtle()
explosion = turtle.Turtle()
fader = turtle.Turtle()
text_turtle = turtle.Turtle()


for t in (launcher, explosion, fader, text_turtle):
    t.hideturtle()
    t.speed(0)
    t.penup()

# Bay lên với đuôi lửa lấp lánh
def launch_firework(x, y, color):
    launcher.goto(x, -330)
    launcher.color(color)
    launcher.pendown()
    for i in range(y + 330):
        launcher.goto(x, -330 + i)
        if i % 2 == 0:  # Đuôi lửa dày hơn
            launcher.dot(random.randint(3, 7), random.choice(["yellow", "orange", "red", "white"]))
        time.sleep(0.001)
    launcher.penup()
    launcher.clear()

# Nổ pháo hoa với nhiều tầng tia sáng
def explode_firework(x, y, color, size):
    explosion.goto(x, y)
    explosion.color(color)
    particles = random.randint(80, 150)  # Tăng số lượng hạt sáng

    # Vẽ nhiều lớp tia nổ
    for layer in range(3):  # Tạo 3 lớp pháo hoa
        for i in range(particles):
            angle = random.uniform(0, 2 * math.pi)
            distance = random.uniform(size * 0.3, size)
            px = x + math.cos(angle) * distance * (1 - layer * 0.3)
            py = y + math.sin(angle) * distance * (1 - layer * 0.3)
            explosion.goto(px, py)
            explosion.dot(random.randint(2, 5), random.choice([color, "yellow", "white", "orange"]))
        time.sleep(0.1)  # Tạo hiệu ứng giật nổ từng lớp

    # Fading – Ánh sáng tắt dần
    for fade in range(4, 0, -1):
        fader.color(color)
        for i in range(particles // 2):
            angle = random.uniform(0, 2 * math.pi)
            distance = random.uniform(size * 0.2, size * (fade / 4))
            px = x + math.cos(angle) * distance
            py = y + math.sin(angle) * distance
            fader.goto(px, py)
            fader.dot(random.randint(1, 3), random.choice(["yellow", "orange", "white"]))
        time.sleep(0.1)
    explosion.clear()
    fader.clear()

# Hiển thị dòng chữ lung linh HAPPY NEW YEAR 2025
def show_text():
    text_turtle.goto(0, -50)
    text_turtle.color("yellow")
    text_turtle.hideturtle()
    text_turtle.penup()
    for i in range(5):  # Hiệu ứng nhấp nháy
        text_turtle.write("🎆 HAPPY NEW YEAR 2025 🎆", align="center", font=("Arial", 36, "bold"))
        time.sleep(0.5)
        text_turtle.clear()
        time.sleep(0.2)
    text_turtle.write("🎆 HAPPY NEW YEAR 2025 🎆", align="center", font=("Arial", 36, "bold"))

# Chương trình chính
def firework_show():
    colors = ["red", "yellow", "blue", "green", "purple", "orange", "white", "pink"]
    firework_count = 12  # Số pháo hoa
    for i in range(firework_count):
        x = random.randint(-400, 400)
        y = random.randint(100, 300)
        color = random.choice(colors)
        
        # Bay lên
        launch_firework(x, y, color)
        time.sleep(0.1)
        
        # Nổ tung
        explode_firework(x, y, color, random.randint(100, 200))
    
    # Hiện chữ chúc mừng năm mới
    show_text()

# Chạy chương trình
firework_show()
screen.mainloop()
