import random
def f_rand_list(size,to):
    my_list = []
    for i in range(size):
        x = random.randint(0,to)
        my_list.append(x)
    return my_list