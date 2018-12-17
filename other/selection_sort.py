def sort_with_select(a_list):
    for i in range(len(a_list)):

        minIndex = i

        for j in range(i + 1, len(a_list)):

            # The loops above already take care of the overall
            # control flow of selection sort: all we need to do
            # here is see if the current item is lower than the
            # lowest-found item on the current iteration. So,
            # we check the current item against the lowest-found
            # item so far:
            if a_list[j] < a_list[minIndex]:
                # And if it's lower, we note that this is the new
                # lowest-found item:
                minIndex = j

        minValue = a_list[minIndex]

        del a_list[minIndex]

        a_list.insert(i, minValue)

        print(a_list)

    return a_list


print(sort_with_select([3, 2, 5, 6, 4, 1]))

# 3 2 5 6 4 1