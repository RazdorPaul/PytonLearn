import math

class Figure:
    sides_count = 0

    def __init__(self, colors, sides):
        self.filled = True
        self.__sides = sides
        if self.__isValidColor(colors):
            self.__color = colors
        else:
            self.__color = (255, 255, 255)
            self.filled = False

    def getColor(self):
        return self.__color

    def __isValidColor(self, colors):
        flag = True
        if len(colors) != 3:
            flag = False
        else:
            r = colors[0]
            g = colors[1]
            b = colors[2]
            if (r < 0 or r > 255) or (g < 0 or g > 255) or (b < 0 or b > 255):
                flag = False
        return flag

    def setColor(self, *colors):
        if self.__isValidColor(colors):
            self.__color = colors
            self.filled = True

    def getSides(self):
        return self.__sides

    def getCount(self):
        return self.sides_count

    def setSides(self, *sides):
        if self.__isValidSides(sides):
            self.__sides = list(sides)

    def __isValidSides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        else:
            return True

    def __len__(self):
        perimetr = 0
        for i in self.__sides:
            perimetr += i
        return perimetr

class Circle(Figure):
    sides_count = 1

    def __init__(self, colors, *sides):
        if len(sides) != self.getCount():
            side = [1]
        else:
            side =list(sides)
        super().__init__(colors, side)
        self.__radius = side[0] / (2 * math.pi)

    def getSquare(self):
        return math.pi * self.__radius * self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, colors, *sides):
        if len(sides) != self.getCount():
            self.__sides = [1, 1, 1]
        else:
            self.__sides = [sides[0], sides[1], sides[2]]
        super().__init__(colors, self.__sides)
        self.__height = [2 * self.getSquare() / self.__sides[0],
                         2 * self.getSquare() / self.__sides[1],
                         2 * self.getSquare() / self.__sides[2]]

    def getSquare(self):
        p = self.__sides[0] + self.__sides[1] + self.__sides[2]
        p /= 2
        square = p
        for i in self.__sides:
            square *= (p - i)
        return math.sqrt(square)

    def getHeight(self):
        return self.__height


class Cube(Figure):
    sides_count = 12

    def __init__(self, colors, *sides):
        if  (len(sides) != 1 and len(sides) != self.getCount()) or all(i == sides[0] for i in sides) != True:
            sides = [1] * 12
        else:
            sides = [sides[0]] * 12
        super().__init__(colors, sides)

    def getVolume(self):
        return self.getSides()[0] ** 3

cub = Cube((10, 10, 10), 10,10,10,10,10,10,10,10,10,10,10,10)
print(cub.getCount(), cub.__len__(), cub.getColor(), cub.filled)
print("Объем куба равен ", cub.getVolume())
trian = Triangle((254, 255, 10), 3, 4, 5)
print(trian.getCount(), trian.__len__(), trian.getColor(), trian.filled)
print("Площадь треугольника равна ", trian.getSquare())
print("Список высот треугольника ", trian.getHeight())
circl =Circle((15, 10, 100), 9)
print(circl.getCount(), circl.__len__(), circl.getColor(), circl.filled)
print("площадь круга равна ", circl.getSquare(), "\n\n")

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.setColor(55, 66, 77) # Изменится
cube1.setColor(300, 70, 15) # Не изменится
print(circle1.getColor())
print(cube1.getColor())

# Проверка на изменение сторон:
cube1.setSides(5, 3, 12, 4, 5) # Не изменится
circle1.setSides(15) # Изменится
print(cube1.getSides())
print(circle1.getSides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.getVolume())
