from django.shortcuts import render

from expression.models import CalcHistory


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b



def new_page(request):
    numbers = request.GET
    numbers_int_list = []
    operation = []
    operation_dict = {
        "a": add,
        "s": subtract,
    }
    status = ""
    if len(numbers) != 7:
        status = "должно быть 7 аргументов"
        return render(request, 'new.html', context={"status": status})
    for i in numbers:
        try:
            numbers_int_list.append(int(numbers[i]))
        except ValueError:
            if operation_dict.get(numbers[i][0]):
                operation.append(operation_dict[numbers[i][0]])
            else:
                status = f"недопустимый аргумент: {i} - '{numbers[i]}'не служебное слово(a,s), и не число(int)"
                return render(request, 'new.html', context={"status": status})

    result = numbers_int_list[0]
    print(numbers_int_list, result, operation)
    for i in range(len(operation)):
        result = operation[i](result, numbers_int_list[i + 1])

    operation_char = []
    for i in range(len(operation)):
        operation_char.append('+' if operation[i] == add else '-')

    calc_history = CalcHistory(first_number=numbers_int_list[0], second_number=numbers_int_list[1],
                               third_number=numbers_int_list[2],
                               four_number=numbers_int_list[3],
                               first_operation=operation_char[0],
                               second_operation=operation_char[1],
                               third_operation=operation_char[2],
                               result=result
                               )
    calc_history.save()

    status = "пример добавлен"
    return render(request, 'new.html', context={"status": status})
