import numpy as np


class ListCreator:
    """Класс ListCreator предоставляет методы для создания списка целых чисел от 0 до указанной длины."""

    def create_with_list_comprehensions(self, lenght: int) -> list[int]:
        """Создает список с элементами от 0 до числа lenght - 1 с помощью списковых включений."""
        return [
            i for i in range(lenght)
        ]

    def create_with_for_cycle(self, lenght: int) -> list[int]:
        """Создает список с элементами от 0 до числа lenght - 1 в цикле for, добавляя элементы в конец."""
        result_list = []
        for elem in range(lenght):
            result_list.append(elem)
        return result_list

    def create_with_numpy(self, lenght: int) -> list[int]:
        """Создает список с элементами от 0 до числа lenght - 1 с помощью библиотеки numpy."""
        return np.arange(lenght).tolist()
