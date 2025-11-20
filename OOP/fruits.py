fruit1 = "Mango"
color1 = "Orange"

print(f"{fruit1, color1}")

fruit2 = "Stawbery"
color2 = "red"

print(f"{fruit2}, {color2}")

fruit3 = "Banana"
color3 = "yellow"

print(f"{fruit3}, {color3}")


class Fruit:
    def __init__(self, fruit,color):
        self.fruit = fruit
        self.color = color
    def __str__(self):
        return f"{self.fruit},{self.color}"
    
fruit1 = Fruit('Mango', "Orange")
