class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        
class Cake:
    #can you fill out the rest of this for me? im dumb
    #the cake needs to have the cake flavor and cake frosting stored
    def __init__(self, flavor, frosting):
        self.flavor = flavor
        self.frosting = frosting

class Cat:
    def __init__(self, name, age, fur_length):
        self.name = name
        self.age = age
        self.fur_length = fur_length
        
        
    def breedGuess(self):
        if self.fur_length == "long":
            return("Domestic Longhair")
        else:
            return("Domestic Shorthair")
            
class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        
    #create your own function! what do you want it to do?
    def colorCheck(self):
        if self.color == "White":
            print("Basic but cool")
        elif self.color == "Black":
            print("Still pretty basic but looks nice")
        else:
            ("A unique color")
   
def main():
    #fill this one out with a dog's name and age.. can be your dog, friend's dog, etc
    newDog = Dog("Luna", 4)
    print(newDog.name, newDog.age)
    
    #and what about a new employee
    newEmployee = Employee("Alex", 9387261, "Finance")
    #how would we print out each of the variables from newEmployee?
    print(newEmployee.name, newEmployee.idNumber, newEmployee.department)

    #now create and print out a cake you make
    newCake = Cake("Ice Cream", "Chocolate")
    print(newCake.flavor, newCake.frosting)
    
    #and now create another cake and print it out
    newCake = Cake("Red Velvet", "Vanilla")
    print(newCake.flavor, newCake.frosting)
    
    #create a cat!
    cat1 = Cat("Midnight", 7, "Short")

    #create another cat!
    cat2 = Cat("Socks", 9, "Long")

    #What would we put here to print out the result of breedGuess for cat1?
    print(cat1.breedGuess())
    
    #create a car!
    newCar = Car("Chevy Trax", 2024, "Black")
    print(newCar.model, newCar.year, newCar.color)

    #Now print out the function you made for car :)
    print(newCar.colorCheck())

main()