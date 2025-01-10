from django.shortcuts import render
from expression.models import CalcHistory
import random


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def expression_page(request):
    operations_choice_list = [add, subtract]
    operation = [random.choice(operations_choice_list), random.choice(operations_choice_list),
                 random.choice(operations_choice_list)]
    numbers = [random.randint(10, 99), random.randint(10, 99), random.randint(10, 99), random.randint(10, 99)]
    result = numbers[0]
    for i in range(len(operation)):
        result = operation[i](result, numbers[i + 1])

    operation_char = []
    for i in range(len(operation)):
        operation_char.append('+' if operation[i] == add else '-')

    calc_history = CalcHistory(first_number=numbers[0], second_number=numbers[1], third_number=numbers[2],
                               four_number=numbers[3],
                               first_operation=operation_char[0],
                               second_operation=operation_char[1],
                               third_operation=operation_char[2],
                               result=result
                               )
    calc_history.save()
    context = {
        "numbers_f": numbers[0],
        "numbers_s": numbers[1],
        "numbers_t": numbers[2],
        "numbers_four": numbers[3],
        "operation_f": operation_char[0],
        "operation_s": operation_char[1],
        "operation_t": operation_char[2],
        "result": result
    }
    print(numbers, operation_char, result)
    return render(request, 'expression.html', context)
