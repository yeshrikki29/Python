#how to create class in python
#class is a template for a type of object

class Point():
    def __init__(self, inputX, inputY):
        self.x = inputX
        self.y = inputY
        
p = Point(2,9)
print(p.x, p.y)