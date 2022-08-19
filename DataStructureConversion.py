# I created this file to be better equipped to answer coding questions.

my_set = set()


def list_to_set(random_list):
    for i in random_list:
        my_set.add(i)

    return my_set


a_list = [1, 0, 0, 1, 9, 8, 5, 5]
another_list = ["my", 99, 99, 0, 0, 2.5, True]
a_set = (1, 5, 7, "wth!")
print(a_set[1])
list_to_set(a_list)
print("list to set conversion(1): " + str(my_set))

new_set = set(another_list)
print("Casting a list to a set: " + str(new_set))

new_list = list(a_set)
print("Casting a set to a list: " + str(new_list))

# Casting a datastructure to another is more simple than I though.
