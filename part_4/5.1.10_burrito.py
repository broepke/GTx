# Copy your Burrito class from the last exercise. Now, add
# a method called "get_cost" to the Burrito class. It should
# accept zero arguments (except for "self", of course) and
# it will return a float. Here's how the cost should be
# computed:
#
# - The base cost of a burrito is $5.00
# - If the burrito's meat is "chicken", "pork" or "tofu",
#   add $1.00 to the cost
# - If the burrito's meat is "steak", add $1.50 to the cost
# - If extra_meat is True and meat is not set to False, add
#   $1.00 to the cost
# - If guacamole is True, add $0.75 to the cost
#
# Make sure to return the result as a float even if the total
# is a round number (e.g. for burrito with no meat or
# guacamole, return 5.0 instead of 5).


# Write your code here!
class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False,
                 corn=False):
        self.set_meat(meat)
        self.set_to_go(to_go)
        self.set_rice(rice)
        self.set_beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)

    def set_meat(self, value):
        valid_options = ["chicken", "pork", "steak", "tofu", False]
        if value in valid_options:
            self.meat = value
        else:
            self.meat = False

    def set_to_go(self, value):
        valid_options = [True, False]
        if value in valid_options:
            self.to_go = value
        else:
            self.to_go = False

    def set_rice(self, value):
        valid_options = ["brown", "white", False]
        if value in valid_options:
            self.rice = value
        else:
            self.rice = False

    def set_beans(self, value):
        valid_options = ["black", "pinto", False]
        if value in valid_options:
            self.beans = value
        else:
            self.beans = False

    def set_extra_meat(self, value):
        valid_options = [True, False]
        if value in valid_options:
            self.extra_meat = value
        else:
            self.extra_meat = False

    def set_guacamole(self, value):
        valid_options = [True, False]
        if value in valid_options:
            self.guacamole = value
        else:
            self.guacamole = False

    def set_cheese(self, value):
        valid_options = [True, False]
        if value in valid_options:
            self.cheese = value
        else:
            self.cheese = False

    def set_pico(self, value):
        valid_options = [True, False]
        if value in valid_options:
            self.pico = value
        else:
            self.pico = False

    def set_corn(self, value):
        valid_options = [True, False]
        if value in valid_options:
            self.corn = value
        else:
            self.corn = False

    def get_meat(self):
        return self.meat

    def get_to_go(self):
        return self.to_go

    def get_rice(self):
        return self.rice

    def get_beans(self):
        return self.beans

    def get_extra_meat(self):
        return self.extra_meat

    def get_guacamole(self):
        return self.guacamole

    def get_cheese(self):
        return self.cheese

    def get_pico(self):
        return self.pico

    def get_corn(self):
        return self.corn

    def get_cost(self):

        cost = 5.00
        costly_meat = ["chicken", "pork", "tofu"]

        if self.meat in costly_meat:
            cost += 1.0

        if self.meat == "steak":
            cost += 1.5

        if self.extra_meat and self.meat:
            cost += 1.0

        if self.guacamole:
            cost += 0.75

        return cost


# - The base cost of a burrito is $5.00
# - If the burrito's meat is "chicken", "pork" or "tofu",
#   add $1.00 to the cost
# - If the burrito's meat is "steak", add $1.50 to the cost
# - If extra_meat is True and meat is not set to False, add
#   $1.00 to the cost
# - If guacamole is True, add $0.75 to the cost
#
# Make sure to return the result as a float even if the total
# is a round number (e.g. for burrito with no meat or
# guacamole, return 5.0 instead of 5).


# Below are some lines of code that will test your class.
# You can change the value of the variable(s) to test your
# class with different inputs.
#
# If your function works correctly, this will originally
# print: 7.75
a_burrito = Burrito("pork", False, "white", "black", extra_meat=True, guacamole=True)
print(a_burrito.get_cost())
