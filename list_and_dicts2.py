def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Facundo", "last": "García"}

    super_list = [
        {"firstname": "Facundo", "lastname": "Calderón"},
        {"firstname": "Maria", "lastname": "Zeledón"},
        {"firstname": "Federico", "lastname": "García"},
        {"firstname": "Fernando", "lastname": "Loría"},
        {"firstname": "Marcial", "lastname": "Méndez"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for i in super_list:
        for key, values in i.items():
            print(key, ": ",values)


if __name__ == '__main__':
    run()