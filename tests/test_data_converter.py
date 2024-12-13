"""
Бенчмарк-тесты, провеющие производительность методов класса DataConverter.

Тесты сериализации имеют единую структуру:

Args:
----
benchmark : Callable
    Фикстура pytest-benchmark для измерения производительности.
size_in_bytes : int
    Размер генерируемой строки в байтах.

Описание
- Генерирует случайную строку заданного размера.
- Измеряет время сериализации строки в данный формат с помощью benchmark.
- Проверяет корректность сериализации путем сравнения с результатом.



Тесты десериализации имеют единую структуру:

Параметры:
----------
benchmark : Callable
    Фикстура pytest-benchmark для измерения производительности.
size_in_bytes : int
    Размер генерируемой строки в байтах.

Описание:
- Генерирует случайную строку заданного размера.
- Сериализует строку в данный формат без измерения производительности.
- Измеряет время десериализации строки из данного формата с помощью benchmark.
- Проверяет корректность десериализации путем сравнения с исходной строкой.



Не получилось объединить тесты для сериализации и десериализации в один,
так как в одном тесте может вызваться фикстура benchmark только 1 раз.
Также, возможно, я слишком раздул код, так как в тестах много повторений.
Может быть нужно было создать 1 функцию, которая принимала бы в качестве параметра метод сериализации данных
Но с другой стороны мой код более читаемый, модульный и расширяемый. Поэтому решил оставить его

"""

import json
import pickle
import random
import string
import sys
from collections.abc import Callable

import msgpack
import pytest

from src.data_converter import DataConverter


def generate_random_string(size_in_bytes: int) -> str:
    """
    Генерирует случайную строку заданного размера в байтах.

    Args:
    ----
    size_in_bytes : int
        Размер требуемой строки в байтах. Должен быть больше или равен минимальному размеру строки.

    Returns:
    -------
    str
        Случайная строка, состоящая из букв и цифр, заданного размера.

    Raises:
    ------
    ValueError
        Если size_in_bytes меньше минимального разрешённого размера min_string_size

    """
    if size_in_bytes < min_string_size:
        msg = f"Минимальный вес строки = {min_string_size}"
        raise ValueError(msg)

    return "".join(
        random.choices(
            string.ascii_letters + string.digits, k=size_in_bytes - min_string_size
        )
    )


min_string_size = sys.getsizeof("")
samples = [1024, 1024 * 1024, 10 * 1024 * 1024]
samples_ids = ["1KB", "1MB", "10MB"]


# Тесты для JSON
@pytest.mark.parametrize("size_in_bytes", samples, ids=samples_ids)
def test_json_serialization(benchmark: Callable, size_in_bytes: int):
    """Тестирует производительность и корректность сериализации строки в формат JSON."""
    input_string = generate_random_string(size_in_bytes)
    assert benchmark(DataConverter().serialize_to_json, input_string) == json.dumps(
        input_string, ensure_ascii=False
    )


@pytest.mark.parametrize("size_in_bytes", samples, ids=samples_ids)
def test_json_deserialization(benchmark: Callable, size_in_bytes: int):
    """Тестирует производительность и корректность десериализации строки из формата JSON."""
    input_string = generate_random_string(size_in_bytes)
    serialized_data = DataConverter().serialize_to_json(input_string)
    assert (
        benchmark(DataConverter().deserialize_from_json, serialized_data)
        == input_string
    )


# Тесты для Pickle
@pytest.mark.parametrize("size_in_bytes", samples, ids=samples_ids)
def test_pickle_serialization(benchmark: Callable, size_in_bytes: int):
    """Тестирует производительность и корректность сериализации строки в формат Pickle."""
    input_string = generate_random_string(size_in_bytes)
    assert benchmark(DataConverter().serialize_to_pickle, input_string) == pickle.dumps(
        input_string
    )


@pytest.mark.parametrize("size_in_bytes", samples, ids=samples_ids)
def test_pickle_deserialization(benchmark: Callable, size_in_bytes: int):
    """Тестирует производительность и корректность десериализации строки в формат Pickle."""
    input_string = generate_random_string(size_in_bytes)
    serialized_data = DataConverter().serialize_to_pickle(input_string)
    assert (
        benchmark(DataConverter().deserialize_from_pickle, serialized_data)
        == input_string
    )


# Тесты для Msgpack
@pytest.mark.parametrize("size_in_bytes", samples, ids=samples_ids)
def test_msgpack_serialization(benchmark: Callable, size_in_bytes: int):
    """Тестирует производительность и корректность сериализации строки в формат Msgpack."""
    input_string = generate_random_string(size_in_bytes)
    assert benchmark(
        DataConverter().serialize_to_msgpack, input_string
    ) == msgpack.packb(input_string, use_bin_type=1)


@pytest.mark.parametrize("size_in_bytes", samples, ids=samples_ids)
def test_msgpack_deserialization(benchmark: Callable, size_in_bytes: int):
    """Тестирует производительность и корректность десериализации строки в формат Msgpack."""
    input_string = generate_random_string(size_in_bytes)
    serialized_data = DataConverter().serialize_to_msgpack(input_string)
    assert (
        benchmark(DataConverter().deserialize_from_msgpack, serialized_data)
        == input_string
    )
