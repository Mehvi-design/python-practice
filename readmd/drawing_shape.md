
# Drawing Shapes with Python

In this exercise, you're provided with a base `Shape` class, and a `Square` class that extends it. Your task is to modify and extend this class to create a new `Triangle` class that prints different types of triangles.

## Provided Code

The `Square` class has already been implemented and works as follows:

```python
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Square(Shape):
    def __init__(self, size):
        super().__init__(size, size)

    def print(self):
        for i in range(self.height):
            print('#' * self.width)

# Test Code
s = Square(5)
s.print()
```

Output:
```
#####
#####
#####
#####
#####
```

## Your Task

The task is to implement the `Triangle` class that should inherit from `Shape`. Your triangle should print either a **right-angle triangle** or an **equilateral-ish triangle** depending on the dimensions.

### Guidelines:

1. **Triangle Class**: The `Triangle` class should inherit from the `Shape` class, and you should modify the constructor to accept `width` and `height` for the triangle.
   
2. **Print Method**: Implement the `print` method to print the triangle's shape to the console.

3. **Right-Angle Triangle**:
    - A **right-angle triangle** could look like this for a height of 5:
      ```
      #
      ##
      ###
      ####
      #####
      ```

4. **Equilateral Triangle**:
    - An **equilateral-ish triangle** could look like this (though it may not be perfectly symmetric, it should appear reasonably close):
      ```
          #
         ###
        #####
       #######
      #########
      ```
5. **Adjustable Dimensions**: You may want to modify the height and width of your triangle to see how it changes.

## Test Code

After implementing the `Triangle` class, use the following test code to verify that your implementation works:

```python
# Test Code
t = Triangle(5, 5)
t.print()
```
## RESULT
![Factorial Challenge]()
