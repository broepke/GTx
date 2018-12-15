# Write a class called "Burrito". A Burrito should have the
# following attributes (instance variables):
#
# - meat
# - to_go
# - rice
# - beans
# - extra_meat (default: False)
# - guacamole (default: False)
# - cheese (default: False)
# - pico (default: False)
# - corn (default: False)
#
# The constructor should let any of these attributes be
# changed when the object is instantiated. The attributes
# with a default value should be optional. Both positional
# and keyword attributes should be in the order shown above
# (for the autograder to work).


# Write your code here!
class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False,
                 corn=False):
        self.meat = meat
        self.to_go = to_go
        self.rice = rice
        self.beans = beans
        self.extra_meat = extra_meat
        self.guacamole = guacamole
        self.cheese = cheese
        self.pico = pico
        self.corn = corn


# The code below will test your class. If it is written
# correctly, this will print True, then False. Note,
# though, that we'll test your code against more complex
# test cases when you submit.
newBurrito = Burrito("Tofu", True, True, True)
print(newBurrito.to_go)
print(newBurrito.guacamole)
