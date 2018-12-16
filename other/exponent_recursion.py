# We initially provided most of this code; only the line
# inside the else block needed to be completed:
def exponent_calc(base, expo):
    if expo == 0:
        return 1
    else:

        # How does this work recursively? Well, imagine
        # if base and expo were originally 5 and 3.
        # We want to calculate 5 ^ 3. 5 ^ 3 is the same
        # as 5 * 5 ^ 2, though: we separate out the base,
        # subtract 1 from the exponent, and calculate the
        # exponent again. So, that's our recursive call:
        return base * exponent_calc(base, expo - 1)

        # Notice how this is going to unpack when we run
        # it:
        #
        # exponent_calc(5, 3) ->
        # 5 * exponent_calc(5, 2) ->
        # 5 * 5 * exponent_calc(5, 1) ->
        # 5 * 5 * 5 * exponent_calc(5, 0) ->
        # 5 * 5 * 5 * 1 ->
        # 5 * 5 * 5 ->
        # 5 * 25 ->
        # 125
        #
        # Notice the base case is the last time we call
        # the function: when expo is 0, we return 1
        # instead of calling the function again. From
        # there, we work our way back "up the ladder".


print(exponent_calc(5,3))