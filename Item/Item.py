from dataclasses import dataclass

@dataclass
class Item:
    __id_store: str
    __id_provider: str
    __name: str
    __price: int

    def __str__(self):
        return f'Наименование: {self.__name} - Стоимость: {self.__price}'

# Что должно быть? Id внутри системы складов, id внутри системы поставщика, название, себестоимость