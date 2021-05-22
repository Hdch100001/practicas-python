# Clase 19
#     Como trabajar con archivos


def read():
    numbers = []
    with open("./archivos/archivo.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Rocío", "María", "Miguel"]
    with open("./archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    write()


if __name__ == '__main__':
    run()