import argparse
import logging
import time
from datetime import datetime
import unittest
import sys

# Добавляем логирование
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Класс MyStr с поддержкой логирования
class MyStr(str):

    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time.time()
        return instance

    def __str__(self):
        formatted_time = datetime.fromtimestamp(self.time).strftime('%Y-%m-%d %H:%M')
        return f"{super().__str__()} (Автор: {self.author}, Время создания: {formatted_time})"

    def __repr__(self):
        return f"MyStr('{super().__repr__()}', '{self.author}')"

# Класс для обработки аргументов командной строки
class CommandLineArguments:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Тесты для класса MyStr')
        self.parser.add_argument('--verbose', action='store_true', help='Включить подробное логирование')
        self.args = self.parser.parse_args()

    def process_arguments(self):
        if self.args.verbose:  # Используйте self.args, а не просто args
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)

class TestMyStr(unittest.TestCase):

    def test_my_str(self):
        my_str = MyStr('Привет, мир!', 'Автор')
        expected_output = 'Привет, мир! (Автор: Автор, Время создания: 2022-09-22 12:00)'
        self.assertEqual(str(my_str), expected_output)

# Создание экземпляра CommandLineArguments
args = CommandLineArguments()
args.process_arguments()  # Вызываем обработку аргументов перед запуском тестов

# Проверяем наличие аргументов командной строки
if len(sys.argv) > 1:
    # Выводим все аргументы, кроме первого (имени исполняемого файла)
    for arg in sys.argv[1:]:
        print(arg)
else:
    print("Нет аргументов командной строки.")

# Запуск тестов с использованием флага --verbose
unittest.main(argv=[sys.argv[0], '-v'] if args.verbose else sys.argv[0])

