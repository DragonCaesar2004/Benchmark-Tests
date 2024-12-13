import json
import pickle

import msgpack


class DataConverter:
    """Класс для сериализации и десериализации данных с использованием различных форматов: JSON, pickle, msgpack."""

    def serialize_to_json(self, input_data: object) -> str:
        """
        Сериализует объект в строку JSON.

        Args:
        ----
            input_data (object): Объект, который необходимо сериализовать в JSON.

        Returns:
        -------
            str: Сериализованный объект в формате JSON.

        Raises:
        ------
            ValueError: Если возникает ошибка при сериализации объекта в JSON.

        """
        try:
            return json.dumps(input_data, ensure_ascii=False)
        except (TypeError, ValueError) as e:
            msg = f"Ошибка сериализации объекта в JSON: {e}"
            raise ValueError(msg) from e

    def deserialize_from_json(self, input_json: str) -> object:
        """
        Десериализует строку JSON обратно в объект.

        Args:
        ----
            input_json (str): Строка JSON для десериализации.

        Returns:
        -------
            object: Десериализованный объект.

        Raises:
        ------
            ValueError: Если возникает ошибка при десериализации строки JSON.

        """
        try:
            return json.loads(input_json)
        except (json.JSONDecodeError, TypeError, ValueError) as e:
            msg = f"Ошибка десериализации JSON в объект: {e}"
            raise ValueError(msg) from e

    def serialize_to_pickle(self, input_data: object) -> bytes:
        """
        Сериализует объект в формат pickle.

        Args:
        ----
            input_data (object): Объект, который необходимо сериализовать с помощью pickle.

        Returns:
        -------
            bytes: Сериализованный объект в формате pickle.

        Raises:
        ------
            ValueError: Если возникает ошибка при сериализации объекта с помощью pickle.

        """
        try:
            return pickle.dumps(input_data)
        except (pickle.PicklingError, TypeError, ValueError) as e:
            msg = f"Ошибка сериализации объекта при помощи pickle: {e}"
            raise ValueError(msg) from e

    def deserialize_from_pickle(self, input_pickle: bytes) -> object:
        """
        Десериализует данные в формате pickle обратно в объект.

        Args:
        ----
            input_pickle (bytes): Данные в формате pickle для десериализации.

        Returns:
        -------
            object: Десериализованный объект.

        Raises:
        ------
            ValueError: Если возникает ошибка при десериализации данных pickle.

        """
        try:
            return pickle.loads(input_pickle)
        except (pickle.UnpicklingError, TypeError, ValueError) as e:
            msg = f"Ошибка десериализации pickle в объект: {e}"
            raise ValueError(msg) from e

    def serialize_to_msgpack(self, input_data: object) -> bytes:
        """
        Сериализует объект в формат MessagePack.

        Args:
        ----
            input_data (object): Объект, который необходимо сериализовать с помощью MessagePack.

        Returns:
        -------
            bytes: Сериализованный объект в формате MessagePack.

        Raises:
        ------
            ValueError: Если возникает ошибка при сериализации объекта с помощью MessagePack.

        """
        try:
            return msgpack.packb(input_data, use_bin_type=True)
        except (TypeError, ValueError) as e:
            msg = f"Ошибка сериализации объекта при помощи msgpack: {e}"
            raise ValueError(msg) from e

    def deserialize_from_msgpack(self, input_msgpack: bytes) -> object:
        """
        Десериализует данные в формате MessagePack обратно в объект.

        Args:
        ----
            input_msgpack (bytes): Данные в формате MessagePack для десериализации.

        Returns:
        -------
            object: Десериализованный объект.

        Raises:
        ------
            ValueError: Если возникает ошибка при десериализации данных MessagePack.

        """
        try:
            return msgpack.unpackb(input_msgpack, raw=False)
        except (msgpack.ExtraData, msgpack.FormatError, msgpack.StackError, TypeError, ValueError) as e:
            msg = f"Ошибка десериализации msgpack в объект: {e}"
            raise ValueError(msg) from e
