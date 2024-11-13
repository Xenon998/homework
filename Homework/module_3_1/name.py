calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):
    count_calls()

    string = string.lower()

    for item in list_to_search:
        if string == item.lower():
            return True

    return False


my_string = "bye, bye"
my_list = ["bye,", "bye"]
result_tuple = string_info(my_string)
print("Длина строки:", result_tuple[0])
print("Строка в верхнем регистре:", result_tuple[1])
print("Строка в нижнем регистре:", result_tuple[2])

if is_contains(my_string, my_list):
    print("Строка найдена в списке")
else:
    print("Строка не найдена в списке")

print("Количество вызовов функций:", calls)
