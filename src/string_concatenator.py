class StringConcatenator:
    """
    Класс для конкатенации строк.

    Этот класс предоставляет методы для соединения списков строк при помощи
    различных методов.
    """

    def concatenate_strings_with_join_method(self,string_list:list[str])->str:
        """Конкатенирует строки при помощи специального метода join()."""
        return "".join(string_list)

    def concatenate_strings_with_plus_operation(self,string_list:list[str])->str:
        """Конкатенирует строки при помощи специального метода перегруженного оператора +."""
        result = ""
        for string in string_list:
            result+=string
        return result
