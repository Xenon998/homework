# Part 1
immutable_var = (123, True, "string")
print(immutable_var)

# Part 2
immutable_var[0] = 5
print(immutable_var)
# Суть кортежа состоит в том, что он неизменяем и чаще всего
# используется для тех списков, что мы не хотим затронуть.
# Но несмотря на его неизменность, мы также можем хранить в кортеже и изменяемые объекты.

# Part 3
mutable_list = ["A", "B", "C"]
print(mutable_list)
mutable_list[0] = "new"
print("Измененный список:", mutable_list)