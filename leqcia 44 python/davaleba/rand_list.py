import random
def f_rand_list(size):
    my_list = []
    for i in range(size):
        x = random.randint(0,11)
        my_list.append(x)
    return my_list