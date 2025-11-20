#class Person
#method greet __init__
#property age name
#object person1 person2


# class Myclass:
#     property1= 5

# print(Myclass.property1)

# without __init_method

# class Person:
#     pass

# student1 = Person()
# student1.name = 'George'
# student1.age = 20

# student2 = Person()
# student2.name = "Anna"
# student2.age = 30

# print(student1.name)
# print(student1.age)
# print(student2.name)
# print(student2.age)


#with __init_method

class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name:{self.name} Age:{self.age}"
        
    def greet(self):
        print(f"Hello " + self.name)

    
# # person1 = Person("Alice", 30)
# # del person1.name
# person2 = Person("George", 30)
# print(person2)

# # # print(f"Age: {person1.name}")
# print(f"Name: {person2.name}, Age: {person2.age}")
# # student2.greet()


class Student(Person):
    pass
student = Student("Martin", 40)

student.greet()