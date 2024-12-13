"""
Бенчмарк-тесты, провеющие производительность методов класса ListCreator.

Тесты имеют единую структуру:

Параметры:

benchmark: Callable
    Объект для бенчмаркинга, который позволяет измерять
    время выполнения необходимых функций.
lenght: int
    Длина списка, который будет создан с использованием
    генераторов списков. Тестируется для разных значений из списка samples

Проверяет:

Проверяет, что результат функции создания списка совпадает с
ожидаемым значением, а именно, что созданный список равен
списку, который создается с использованием множества значений
от 0 до lenght - 1
"""

from collections.abc import Callable

import pytest

from src.list_creating import ListCreator

samples = [
    1,
    10,
    10**2,
    10**3,
    10**4,
    10**5,
    10**6,
    10**7,
]
samples_ids = [
    "1",
    "10",
    "10**2",
    "10**3",
    "10**4",
    "10**5",
    "10**6",
    "10**7",
]


@pytest.mark.parametrize("lenght", samples, ids=samples_ids)
def test_create_with_list_comprehensions(benchmark: Callable, lenght: int):
    """Тестирует производительность метода создания списка при помощи списковых включений."""
    assert benchmark(ListCreator().create_with_list_comprehensions, lenght) == [
        i for i in range(lenght)
    ]


@pytest.mark.parametrize("lenght", samples, ids=samples_ids)
def test_create_with_for_cycle(benchmark: Callable, lenght: int):
    """Тестирует производительность метода создания списка при помощи цикла for."""
    assert benchmark(ListCreator().create_with_for_cycle, lenght) == [
        i for i in range(lenght)
    ]


@pytest.mark.parametrize("lenght", samples, ids=samples_ids)
def test_create_with_numpy(benchmark: Callable, lenght: int):
    """Тестирует производительность метода создания списка при помощи numpy."""
    assert benchmark(ListCreator().create_with_numpy, lenght) == [
        i for i in range(lenght)
    ]
