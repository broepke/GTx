# Here's a long one -- you can do it!
#
# Rewrite the following class so that it uses getters and
# setters for all three variables (title, description,
# completed). The getters should be called: getTitle,
# getDescription,  getCompleted. The setters should be
# called: setTitle, setDescription, setCompleted.
#
# In addition, the setter should check to make sure that
# the new value is the correct type: title and description
# should always be of type str, and completed should always
# be of type bool. If the value is not the right type, set
# the value of the corresponding attribute to None (the
# keyword, not the string "None").
#
# To summarize (and give a to-do list):
# - Create getters and setters for each variable.
# - Check the type of the new value inside the setters,
#   and print an error if it's the wrong type.
#
# Hint: You can check to see if a variable is a string by
# checking the logical expression type(var) == str, where
# var is the variable you're checking. For integers, use
# int instead of str. For floats, use float. For booleans,
# use bool.
#
# Hint 2: Remember to put self before any instance variables
# or methods you're trying to access. For example, to access
# the variable title from within a method, you would need to
# write self.title.


class TodoItem:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def setTitle(self, new_title):
        if type(new_title) == str:
            self.title = new_title
            return
        else:
            self.title = None

    def setDescription(self, new_description):
        if type(new_description) == str:
            self.description = new_description
            return
        else:
            self.description = None
        return

    def setCompleted(self, new_completed):
        if type(new_completed) == bool:
            self.completed = new_completed
            return
        else:
            self.completed = None
        return

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def getCompleted(self):
        return self.completed

    # Below are some lines of code that will test your class.


# You can change this code to test how your class behaves
# with different variables and method calls.
#
# If your class works correctly, this will originally print:
# Mow
# Mow the lawn
# False
# True
# None
item = TodoItem("Mow", "Mow the lawn")
print(item.getTitle())
print(item.getDescription())
print(item.getCompleted())
item.setCompleted(True)
print(item.getCompleted())
item.setTitle(False)
print(item.getTitle())
