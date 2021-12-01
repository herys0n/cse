Sandwich Class

The Sandwich class' primary function is in modeling a sandwich with varying types of bread, toppings,
age, and then a name. It can be modified in ways such as cutting, toasting, renaming, and aging it.
One of the main aspects of this class is the importance of the order of ingredients on the sandwich
and its easy modifiability in that regard.

Variables
cut - whether the sandwich has been cut in half or not; boolean
bread - the type of bread; string
toppings - all of the toppings on the sandwich; list
age - age of the sandwich, in days; integer
name - name of the sandwich - string

Methods
toast() - takes in self and a topping or bread, then returns it as a string with "toasted" in front of it
get_bread() - takes in self, returns bread
remove_topping() - takes self and a topping, then removes that topping from the list of toppings
set_topping() - takes self and a topping, then appends that topping onto the list of toppings
get_topping_placement() - takes self and a topping, indexes it in the list of topping, then returns that index
get_topping_order() - takes self, returns the list of toppings
set_age() - takes self and an integer, changes the age variable to the integer
get_age() - takes self, returns the age variable
check_food_poisoning() - takes self, compares the age variable to the number 7, then returns a string depending on if the age is greater, equal to, or less than 7
set_name() - takes self and a string, then changes the name variable to the string
get_name() - takes self, returns the name variable
cut_sandwich() - takes self, changes the cut variable to True
check_cut() - takes self, returns True if cut is True and False if cut is False

Demo Program
The demo program prompts the user to input bread, toppings, age, and a sandwich name, then creates an object with it.
There is a while loop that offers various commands to be input that can call each available method, including calling
a list of commands and exiting the loop.

To run the program, simply input the correct numbers and strings when prompted, then each command as the user sees fit.
When done, exit the loop with "exit".