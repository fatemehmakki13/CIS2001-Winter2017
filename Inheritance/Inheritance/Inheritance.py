class Polygon:
    def __init__(self, name):
        return

    def getArea(self):
        return 0

    def setSideLength(self, side_number, side_length ):
        return 

class Triangle(Polygon):
    number_of_sides = 3

    def __init__(self, name):
        self._name = name
        self._side_lengths = [0,0,0]

    def setSideLength(self, side_number, side_length ):
        if ( 0 <= side_number < self.number_of_sides ):
            self._side_lengths[side_number] = side_length

    def getArea(self):
        return .5 * self._side_lengths[0] * self._side_lengths[1]

class Rectangle(Polygon):
    number_of_sides = 4

    def __init__(self, name):
        self._side_lengths = [0,0,0,0]
        self._name = name
    
    def setSideLength(self, side_number, side_length ):
        if ( 0 <= side_number < self.number_of_sides ):
            if side_number % 2 == 0:
                self._side_lengths[0] = side_length
                self._side_lengths[2] = side_length
            else:
                self._side_lengths[1] = side_length
                self._side_lengths[3] = side_length

    def getArea(self):
        return self._side_lengths[0] * self._side_lengths[1]

    def __str__(self):
        return "Rectangle: " + self._name + " sides: " + str(self._side_lengths)

class Square(Rectangle):

    def __init__(self, name):
        super().__init__(name)

    def setSideLength(self, side_number, side_length):
        super().setSideLength(0, side_length)
        super().setSideLength(1, side_length)

    def __str__(self):
        return "Square: " + self._name + " sides: " + str(self._side_lengths) 

class Cube(Square):

    def __init__(self, name):
        super().__init__(name)
        self._height = 0
    
    def setSideLength(self, side_number, side_length):
        super().setSideLength(side_number, side_length)
        self._height = side_length

    def getVolume(self):
        return self.getArea() * self._height

    def getSurfaceArea(self):
        return self.getArea() * 6

    def __str__(self):
        return "Cube: " + self._name + " sides: " + str(self._side_lengths) + " Height: " + str(self._height)

first_shape = Rectangle("15x20")
first_shape.setSideLength(0, 5)
first_shape.setSideLength(1, 10)
first_shape.setSideLength(2, 15)
first_shape.setSideLength(3, 20)
print(first_shape.getArea() )
print(first_shape )

second_shape = Square("10x10")
second_shape.setSideLength(100,10)
print(second_shape.getArea() )
print(second_shape)

third_shape = Cube("10x10x10")
third_shape.setSideLength(10,10)
print("Area:", third_shape.getArea() )
print("Surface Area:",third_shape.getSurfaceArea() )
print("Volume:",third_shape.getVolume() )
print(third_shape)