#1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'stroka', c = True):
    print("a:", a)
    print("b:", b)
    print("c:", c)

print_params()
print_params(b = 'new_stroka')
print_params(2, "another_stroka", False)

#2.Распаковка параметров:
def print_params(a, b, c):
    print("a:", a)
    print("b:", b)
    print("c:", c)

values_list = [3, "string", True]
values_dict = {
    "a": 1,
    "b": "text",
    "c": False
}
try:
    print_params(*values_list, **values_dict)
except Exception as e:
    print(e)

#3.Распаковка + отдельные параметры:
values_list_2 = [100, 'blablabla' ]
print_params(*values_list_2, 52)
