
def bilangan(my_list):
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    return max

my_list = [10, 20, 5, 30, 15]
print(bilangan(my_list)) 



