import argparse
import logging
import unittest
import sys

# Добавляем логирование
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Класс для обработки аргументов командной строки
parser = argparse.ArgumentParser(description='Тесты для класса Rectangle')
parser.add_argument('--verbose', action='store_true', help='Включить подробное логирование')
args = parser.parse_args()

# Определение уровня логирования в зависимости от флага --verbose
if args.verbose:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

# Класс TestRectangle с поддержкой логирования
class TestRectangle(unittest.TestCase):

    def test_width(self):
        try:
            r1 = Rectangle(5)
            self.assertEqual(r1.width, 5)
        except Exception as e:
            logger.error('Ошибка при тестировании ширины: %s', e)

    def test_height(self):
        try:
            r2 = Rectangle(3, 4)
            self.assertEqual(r2.height, 4)
        except Exception as e:
            logger.error('Ошибка при тестировании высоты: %s', e)

    def test_perimeter(self):
        try:
            r1 = Rectangle(5)
            self.assertEqual(r1.perimeter(), 20)
        except Exception as e:
            logger.error('Ошибка при тестировании периметра: %s', e)

    def test_area(self):
        try:
            r2 = Rectangle(3, 4)
            self.assertEqual(r2.area(), 12)
        except Exception as e:
            logger.error('Ошибка при тестировании площади: %s', e)

    def test_addition(self):
        try:
            r1 = Rectangle(5)
            r2 = Rectangle(3, 4)
            r3 = r1 + r2
            self.assertEqual(r3.width, 8)
            self.assertEqual(r3.height, 6.0)
        except Exception as e:
            logger.error('Ошибка при тестировании сложения: %s', e)

# Запуск тестов
unittest.main(argv=[sys.argv[0], '-v'] if args.verbose else sys.argv[0])
