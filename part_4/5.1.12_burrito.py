# In this exercise, you won't edit any of your code from the
# Burrito class. Instead, you're just going to write a
# function to use instances of the Burrito class. You don't
# actually have to copy/paste your previous code here if you
# don't want to, although you'll need to if you want to write
# some test code at the bottom.
#
# Write a function called total_cost. total_cost should take
# as input a list of instances of Burrito, and return the
# total cost of all those burritos together as a float.
#
# Hint: Don't reinvent the wheel. Use the work that you've
# already done. The function can be written in only five
# lines, including the function declaration.
#
# Hint 2: The exercise here is to write a function, not a
# method. That means this function should *not* be part of
# the Burrito class.


# If you'd like to use the test code, paste your previous
# code here.
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
        self.meat = Meat(value)

    def set_rice(self, value):
        self.rice = Rice(value)

    def set_beans(self, value):
        self.beans = Beans(value)

    def set_to_go(self, value):
        valid_options = [True, False]
        if value in valid_options:
            self.to_go = value
        else:
            self.to_go = False

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

        if self.meat.value in costly_meat:
            cost += 1.0

        if self.meat.value == "steak":
            cost += 1.5

        if self.extra_meat and self.meat:
            cost += 1.0

        if self.guacamole:
            cost += 0.75

        return cost


class Meat:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["chicken", "pork", "steak", "tofu"]:
            self.value = value
        else:
            self.value = False


class Rice:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["brown", "white"]:
            self.value = value
        else:
            self.value = False


class Beans:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["black", "pinto"]:
            self.value = value
        else:
            self.value = False


# Write your new function here.
def total_cost(burrito_list):

    total = 0.0

    for burrito in burrito_list:
        total += burrito.get_cost()

    return total

# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs. Note that these lines
# will ONLY work if you copy/paste your Burrito, Meat,
# Beans, and Rice classes in.
#
# If your function works correctly, this will originally
# print: 27.0
burrito_1 = Burrito("tofu", True, "white", "black")
burrito_2 = Burrito("steak", True, "white", "pinto", extra_meat = True)
burrito_3 = Burrito("pork", True, "brown", "black", guacamole = True)
burrito_4 = Burrito("chicken", True, "brown", "pinto", extra_meat = True, guacamole = True)
burrito_list = [burrito_1, burrito_2, burrito_3, burrito_4]
print(total_cost(burrito_list))
