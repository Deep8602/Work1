# def spisok(l, numb):
#     res = l[numb]
#     print(res)
#
#
# # lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lis = list(range(0, 10))
# print(lis)
#
# print(lis)
#
# spisok(lis, 0)
# print(len(lis))
# print("______________________")
# x = len(lis)
# print(x)
# not_bin = sorted([abr1 for abr1 in lis if abr1 % 2 != 0])
# print(not_bin)
# print("_________________________")
#
#
# def adder(*nums):
#     sum = 0
#
#     for n in range(0, 10):
#         sum += n
#
#     print("Sum: ", sum)
#
#
# adder(4, 4, 4, 4)
print("____________________________________")


class MySinglton():
    _instance = None

    def __new__(self):
        if not self._instance:
            self._instance = super(MySinglton, self).__new__(self)
            self.y = 10
            return self._instance


x = MySinglton()
print(x)
print(MySinglton.y)
x.y = 30
z = MySinglton()
print(x.y)
print("==============================")

import pytest

#
# class Date(object):
#
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('-'))
#         date1 = cls(day, month, year)
#         return date1
#
#
# date2 = Date.from_string('02-08-1986')
#
# print(date2)

import pytest
import random


@pytest.fixture
def suma_five():
    return random.random()


def test_suma(suma_five):
    print(suma_five)


squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::-1])

cubes = [i ** 2 for i in range(5)]
print(cubes)

print("spam, eggs, ham".split("s"))


def apply_twice(func, arg):
    return func(func(arg))


def add_five(x):
    return x + 5


print(apply_twice(add_five, 10))

print((lambda x: x ** 2 + 5 * x + 4)(-4))
print(1 ** 2)

nums = [11, 22, 33, 44, 55]
result = list(map(lambda x: x + 5, nums))
print(result)


def countdown():
    h = 5
    while h > 0:
        yield h
        h -= 1


for h in countdown():
    print(h)


def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


print(list(numbers(11)))


def decor(func):
    def wrap():
        print("============")
        func()
        print("============")

    return wrap


def print_text():
    print("Hello world!")


print_text = decor(print_text)
print_text()


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)


square = Rectangle.new_square(5)
print(square.calculate_area())

print('___________________________________')


list('one', 'two', 'three', 'four', 'five')
print(list)

# for i in len(list):
#     if i == 2:
#         print(list[i])
