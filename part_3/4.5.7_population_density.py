# Write a function called population_density. The function
# should take one parameter, which will be a list of
# dictionaries. Each dictionary in the list will have three
# key-value pairs:
#
# - name: the name of the country
# - population: the population of that country
# - area: the area of that country (in km^2)
#
# Your function should return the population density of all
# the countries put together. You can calculate this by
# summing all the populations, summing all the areas, and
# dividing the total population by the total area.
#
# Note that the input to this function will look quite long;
# don't let that scare you. That's just because dictionaries
# take a lot of text to define.


# Add your function here!
def population_density(countries):
    total_pop = 0
    total_area = 0

    for places in countries:
        total_pop += places["population"]
        total_area += places["area"]

    return total_pop / total_area


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 133.886 (or something around there)
countries = [{"name": "China", "population": 1390700000, "area": 9640821},
             {"name": "India", "population": 1348003000, "area": 3287240},
             {"name": "United States", "population": 325300000, "area": 9826675},
             {"name": "Indonesia", "population": 237556363, "area": 1904569}]
print(population_density(countries))
