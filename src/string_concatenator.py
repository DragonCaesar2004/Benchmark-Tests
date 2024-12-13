class StringConcatenator:
    """
    Класс для конкатенации строк.

    Этот класс предоставляет методы для соединения списков строк при помощи
    различных методов.
    """

    def concatenate_strings_with_join_method(self, string_list: list[str]) -> str:
        """
        Конкатенирует список строк с использованием метода join().

        Данный метод объединяет все элементы списка string_list в одну строку,
        используя пустую строку в качестве разделителя.

        Args:
        ----
            string_list (list[str]): Список строк, которые необходимо объединить.

        Returns:
        -------
            str: Одна объединенная строка, состоящая из всех элементов string_list.

        """
        return "".join(string_list)

    def concatenate_strings_with_plus_operation(self, string_list: list[str]) -> str:
        """
        Конкатенирует список строк с использованием оператора +.

        Этот метод проходит по каждому элементу в string_list и последовательно
        добавляет его к результирующей строке с помощью оператора +.

        Args:
        ----
            string_list (list[str]): Список строк, которые необходимо объединить.

        Returns:
        -------
            str: Одна объединенная строка, созданная путем последовательного
                добавления всех элементов string_list.

        """
        result = ""
        for string in string_list:
            result += string
        return result
