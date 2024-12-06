from django.shortcuts import render


def calc_page(request):
    first_num = request.GET.get('first', 0)
    second_num = request.GET.get('second', 0)
    try:
        first_num = int(first_num)
    except ValueError:
        print(f"{first_num} is not int")
        first_num = 0

    try:
        second_num = int(second_num)
    except ValueError:
        print(f"{second_num} is not int")
        second_num = 0

    summa = first_num + second_num
    context = {
        "first_num": first_num,
        "second_num": second_num,
        "summa": summa
    }
    return render(request, 'templates/calc.html', context)
