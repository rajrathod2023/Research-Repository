1. Import the Turtle module:
   ```python
   import turtle
   ```
   This line imports the Turtle graphics module in Python, which allows us to create a drawing canvas and draw various shapes using a turtle (a drawing pen).

2. Create a Turtle screen:
   ```python
   screen = turtle.Screen()
   screen.bgcolor("white")
   ```
   Here, we create a Turtle screen object and set its background color to white. This is where the drawing will take place.

3. Create a Turtle object for drawing the flower:
   ```python
   flower = turtle.Turtle()
   flower.shape("turtle")
   flower.color("red")
   flower.speed(1)
   ```
   We create a Turtle object named `flower` that will draw the flower. We set its shape to "turtle," color to red, and speed to 1 (which is a slow drawing speed).

4. Define a function to draw a petal:
   ```python
   def draw_petal():
       flower.circle(100, 60)
       flower.left(120)
       flower.circle(100, 60)
       flower.left(120)
   ```
   This function, `draw_petal`, draws a single petal of the flower. It uses the `circle()` method to draw a semicircle with a radius of 100 units and an angle of 60 degrees. Then, it rotates the turtle left by 120 degrees to prepare for drawing the next part of the petal.

5. Define a function to draw the flower:
   ```python
   def draw_flower():
       for _ in range(6):
           draw_petal()
           flower.left(60)
   ```
   The `draw_flower` function is responsible for drawing the entire flower. It calls the `draw_petal` function six times to create six petals. After drawing each petal, it rotates the turtle left by 60 degrees to position it for the next petal.

6. Move the turtle to the starting position:
   ```python
   flower.penup()
   flower.goto(0, -100)
   flower.pendown()
   ```
   We lift the pen (penup), move the turtle to the starting position at coordinates (0, -100), and then put the pen down (pendown) to begin drawing.

7. Draw the flower:
   ```python
   draw_flower()
   ```
   We call the `draw_flower` function to draw the flower.

8. Close the drawing window when clicked:
   ```python
   screen.exitonclick()
   ```
   This line ensures that the drawing window will remain open until you click on it, allowing you to view the drawn flower. Once you click, the window will close.

