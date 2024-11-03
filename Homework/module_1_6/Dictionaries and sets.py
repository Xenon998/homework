my_dict = {'Ksenia': 2002, 'Max': 1900, 'Dava': 2000}
print(my_dict)
print(my_dict['Ksenia'])
print(my_dict.get('Anton'))
my_dict.update({'Masha': 2001, 'Sasha': 2003})
deleted_value = my_dict.pop("Max")
print(deleted_value)
print(my_dict)

my_set = {1, 1, 34, 34, 'apple', 'apple'}
print(my_set)
my_set.update({111, 112, 'pineapple'})
my_set.remove('apple')
print(my_set)
