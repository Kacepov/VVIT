import turtle

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_radius(self):
        return self.radius
    
    def set_radius(self, new_radius):
        self.radius = new_radius
    
    def draw(self, color="black", x=0, y=0):
        t = turtle.Turtle()
        t.speed(5)
        t.color(color)
        t.penup()
        
        t.goto(x, y - self.radius)
        t.pendown()
        
        t.circle(self.radius)
        
        t.penup()
        t.goto(x + self.radius + 10, y)
        t.write(f"Радиус: {self.radius}", align="left", font=("Arial", 12, "normal"))
        
        t.hideturtle()

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Демонстрация класса Circle")
    screen.setup(800, 600)
    screen.bgcolor("white")
    
    print("=== Демонстрация класса Circle с визуализацией ===")
    
    circle = Circle(40)
    print(f"Начальный радиус: {circle.get_radius()}")
    
    circle.draw(color="red", x=-200, y=0)
    
    circle.set_radius(70)
    print(f"Новый радиус: {circle.get_radius()}")
    
    circle.draw(color="blue", x=0, y=0)
    
    circle.set_radius(30)
    print(f"Окончательный радиус: {circle.get_radius()}")
    
    circle.draw(color="green", x=200, y=0)
    
    # Добавляем информационный текст
    info_turtle = turtle.Turtle()
    info_turtle.penup()
    info_turtle.hideturtle()
    info_turtle.goto(0, -200)
    info_turtle.write("Красный: начальный радиус 50\nСиний: измененный радиус 80\nЗеленый: окончательный радиус 30", 
                     align="center", font=("Arial", 14, "normal"))
    
    print("\nНа экране отображены три круга с разными радиусами:")
    print("- Красный: начальный радиус 40")
    print("- Синий: измененный радиус 70") 
    print("- Зеленый: окончательный радиус 30")
    
    screen.exitonclick()