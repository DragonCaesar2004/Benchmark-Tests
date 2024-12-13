"""
Бенчмарк-тесты, провеющие производительность методов класса StringConcatenator.

Тесты имеют единую структуру:

Параметры:

string_list (list[str]):
    Список строк для соединения.
benchmark: Callable
    Объект для бенчмаркинга, который позволяет измерять
    время выполнения необходимых функций.

Проверяет:

Проверяет, что результат методов класса StringConcatenator
соответствует ожидаемому результату.
"""

from collections.abc import Callable

import pytest

from src.string_concatenator import StringConcatenator

samples = [
    ["a" for _ in range(10)],
    ["a" for _ in range(10**2)],
    ["a" for _ in range(10**3)],
    ["a" for _ in range(10**4)],
    ["a" for _ in range(10**5)],
    ["a" for _ in range(10**6)],
    ["a" * 10, "b" * 10],
    ["a" * 10**2, "b" * 10**2],
    ["a" * 10**3, "b" * 10**3],
    ["a" * 10**4, "b" * 10**4],
    ["a" * 10**5, "b" * 10**5],
    ["a" * 10**6, "b" * 10**6],
]


@pytest.mark.parametrize("string_list", samples)
def test_concatenate_strings_with_join_method(
    benchmark: Callable, string_list: list[str]
):
    """Тестирует производительность метода соединения строк с помощью метода join."""
    assert benchmark(
        StringConcatenator().concatenate_strings_with_join_method, string_list
    ) == "".join(string_list)


@pytest.mark.parametrize("string_list", samples)
def test_concatenate_strings_with_plus_operation(
    benchmark: Callable, string_list: list[str]
):
    """Тестирует производительность метода соединения строк с помощью оператора +."""
    assert benchmark(
        StringConcatenator().concatenate_strings_with_plus_operation, string_list
    ) == "".join(string_list)
