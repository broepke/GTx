# Copy your Burrito class from the last exercise. Below,
# We've given you three additional classes named "Meat",
# "Rice" and "Beans." We've gone ahead and built getters
# and setters in these classes to check if the incoming
# values are valid, so you'll be able to remove those
# from your original code.
#
# First, edit the constructor of your Burrito class.
# Instead of calling setters to set the values of the
# attributes self.meat, self.rice, and self.beans, it
# should instead create new instances of Meat, Rice, and
# Beans. The arguments to these new instances should be
# the same as the arguments you were sending to the
# setters previously (e.g. self.rice = Rice("brown")
# instead of set_rice("brown")).
#
# Second, modify your getters and setters from your
# original code so that they still return the same value
# as before. get_rice(), for example, should still
# return "brown" for brown rice, False for no rice, etc.
# instead of returning the instance of Rice.
#
# Third, make sure that your get_cost function still
# works when you're done changing your code.
#
# Hint: When you're done, creating a new instance of
# Burrito with Burrito("pork", True, "brown", "pinto")
# should still work to create a new Burrito. The only
# thing changing is the internal reasoning of the
# Burrito class.
#
# Hint 2: Notice that the classes Meat, Beans, and Rice
# already contain the code to validate whether input is
# valid. So, your setters in the Burrito class no
# longer need to worry about that -- they can just pass
# their input to the set_value() methods for those
# classes.
#
# Hint 3: This exercise requires very little actual
# coding: you'll only write nine lines of new code, and
# those nine lines all replace existing lines of code
# in the constructor, getters, and setters of Burrito.
#
# You should not need to modify the code below.

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


# Add and modify your code here!


# Below are some lines of code that will test your class.
# You can change the value of the variable(s) to test your
# class with different inputs. Remember though, the results
# of this code should be the same as the previous problem:
# what should be different is how it works behind the scenes.
#
# If your function works correctly, this will originally
# print: 7.75
a_burrito = Burrito("pork", False, "white", "black", extra_meat=True, guacamole=True)
print(a_burrito.get_cost())
