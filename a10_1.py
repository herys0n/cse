"""
Harrison Stamper
Assignment 10.1: Your Own Class
The purpose of this script is to create a class that models a sandwich.
"""

class Sandwich:
    # Set class variable.
    cut = False
    # Init function stores private data variables.
    def __init__(self,bread,toppings,age,name):
        self.__bread = bread
        self.__toppings = toppings
        self.__age = age
        self.__name = name
    def toast(self,ingredient):
        # Set counter.
        n = -1
        # If statement that will either change the name of the bread or enter a for loop to find the specified ingredient, then change it.
        if ingredient == self.__bread:
            self.__bread = f"toasted {self.__bread}"
        else:
            for t in self.__toppings:
                n += 1
                if t == ingredient:
                    self.__toppings.remove(t)
                    self.__toppings.insert(n,f"toasted {t}")
    def get_bread(self):
        # Return bread variable.
        return self.__bread
    def remove_topping(self,topping):
        # Remove topping from list.
        self.__toppings.remove(topping)
    def set_topping(self,topping):
        # Add topping to list via append.
        self.__toppings.append(topping)
    def get_topping_placement(self,topping):
        # Return index of specified topping.
        return self.__toppings.index(topping)
    def get_topping_order(self):
        # Returns list of toppings.
        return self.__toppings
    def set_age(self,age):
        # Change age variable.
        self.__age = age
    def get_age(self):
        # Return age variable.
        return f"{self.__age} days old"
    def check_food_poisoning(self):
        # If statement comparing age to number 7, If it is greater, print warning. If it is less, print other message.
        if self.__age >= 7:
            return "It's probably bad!"
        else:
            return "Hm... it's safe to eat. Maybe."
    def set_name(self,name):
        # Change name variable.
        self.__name = name
    def get_name(self):
        # Return name variable.
        return self.__name
    def cut_sandwich(self):
        # Set cut variable to True.
        self.cut = True
    def check_cut(self):
        # If statement to check if cut is True or False.
        if self.cut == True:
            return True
        else:
            return False

def main():
    # Initialize variable.
    l = []
    # Prompt usee to input class arguments.
    b = input("Choose your bread: ")
    while True:
        t = input("Enter a topping or 'done' to finish: ")
        if t == "done":
            break
        else:
            l.append(t)
    a = int(input("Enter sandwich age: "))
    n = input("Now, name your sandwich: ")
    s = Sandwich(b,l,a,n)
    # While loop cycling through command inputs until entry of "exit".
    print("Enter 'help' for commands.")
    while True:
        i = input("Enter command: ")
        if i == "help":
            print("'toast','get_bread','remove_topping','set_topping','get_topping_placement','get_topping_order','set_age','get_age','check_food_poisoning','set_name','get_name','cut_sandwich','check_cut','help','exit'")
        elif i == "toast":
            ing = input("Enter ingredient: ")
            s.toast(ing)
        elif i == "get_bread":
            print(s.get_bread())
        elif i == "remove_topping":
            t = input("Enter topping: ")
            s.remove_topping(t)
        elif i == "set_topping":
            t = input("Enter topping: ")
            s.set_topping(t)
        elif i == "get_topping_placement":
            t = input("Enter topping: ")
            print(s.get_topping_placement(t))
        elif i == "get_topping_order":
            print(s.get_topping_order())
        elif i == "set_age":
            age = int(input("Enter age: "))
            s.set_age(age)
        elif i == "get_age":
            print(s.get_age())
        elif i == "check_food_poisoning":
            print(s.check_food_poisoning())
        elif i == "set_name":
            name = input("Enter name: ")
            s.set_name(name)
        elif i == "get_name":
            print(s.get_name())
        elif i == "cut_sandwich":
            s.cut_sandwich()
        elif i == "check_cut":
            print(s.check_cut())
        elif i == "exit":
            print("Enjoy!")
            break
if __name__ == "__main__":
    main()