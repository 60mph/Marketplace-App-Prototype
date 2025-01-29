import time

import Store.Store


class Worker:
    __name:str = ""
    __start_time:int = 0
    __finish_time:int = 0
    __is_ready_to_work:bool = False
    __store: Store.Store.Store

    def __init__(self, name):
        if(isinstance(name, str)):
            self.__name = name

    # принять заказ, если возможно

    def get_shift():
        pass

    # получить смену, когда работает
    def time_to_get_ready():
        pass

    def is_ready():
        pass