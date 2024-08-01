import sys

# Проверяем наличие аргументов командной строки
if len(sys.argv) > 1:
    # Выводим все аргументы, кроме первого (имени исполняемого файла)
    for arg in sys.argv[1:]:
        print(arg)
else:
    print("Нет аргументов командной строки.")
