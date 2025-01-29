from concurrent.futures._base import _yield_finished_futures
from dataclasses import dataclass
import time

@dataclass
class Order:
    __delivery_state: str
    __order_item_list: list
    __creating_time: int
    __storekeeper: str = ""
    __courier: str = ""
    __start_time: int = 0
    __start_storekeeper: int = 0
    __finish_storekeeper: int = 0
    __finish_time: int = 0
    __distance: int = 0
    __cancel: bool = False
    __taking: bool = False


    def get_delivery_state(self):
        cur_t = time.time()
        if not self.__cancel:
            if self.__start_storekeeper != 0:
                if not self.__taking:
                    if cur_t >= self.__finish_time:
                        self.__delivery_state = "Доставлен и готов к получению"
                    elif cur_t >= self.__start_storekeeper and cur_t < self.__finish_storekeeper:
                        self.__delivery_state = "Собирается"
                    elif cur_t >= self.__finish_storekeeper and cur_t < self.__finish_time:
                        self.__delivery_state = "Передан доставщику"
                    else:
                        self.__delivery_state = "Создан"
                else:
                    self.__delivery_state = "Получен"
            else:
                self.__delivery_state = "Ошибка заказа"
        else:
            self.__delivery_state = "Отменён"
        return self.__delivery_state

    def get_order_item_list(self):
        return self.order_item_list

    def set_storekeeper(self, storekeeper):
        self.storekeeper = storekeeper

    def set_courier(self, courier):
        self.courier = courier

    def isStarted(self):
        self.start_time = time.time()

    def get_start_time(self):
        return self.start_time

    def set_finish_time(self, time):
        self.finish_time = time


# Что находится в заказе? Статус доставки, список товаров, время создания-время доставки, кто собирал-доставлял