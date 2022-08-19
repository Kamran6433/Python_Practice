# I created this file to be better equipped to answer coding questions.

my_set = set()


def list_to_set(random_list):
    for i in random_list:
        my_set.add(i)

    return my_set


a_list = [1, 0, 0, 1, 9, 8, 5, 5]
list_to_set(a_list)
print("list to set conversion(1): " + str(my_set))

