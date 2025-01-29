import time
import Order.Order
import Store.Store
import Provider.Provider

class User:
    __phone_number : str
    __coords : int = 0
    cart = list()

    def __init__(self, coords, phone_number):
        self.__coords = coords
        self.__phone_number = phone_number

    def make_order(self, stores_list, provider : Provider.Provider.Provider):
        if(len(stores_list) > 0):
            cur_time = time.localtime(time.time())
            order = Order.Order.Order("Создан", self.cart, time.time())
            #order.isStarted()
            print("Создан новый заказ:", "\n \t Статус заказа:", order._Order__delivery_state,
                  "\n \t Товары: \n", " \t \t", ["Наименование: \"" + item._Item__name + "\" - Стоимость: " + str(item._Item__price) for item in self.cart],
                  "\n \t Время создания: ", str(cur_time.tm_hour) + "ч " + str(cur_time.tm_min) + "мин " + str(cur_time.tm_sec) + "сек")
            no_one_store_work = True
            for store in stores_list:
                if store.is_working():
                    waiting_time = store.min_time_to_get_ready() + abs(store._Store__coords - self.__coords) * 30
                    order._Order__distance = abs(store._Store__coords - self.__coords)
                    best_store = store
                    no_one_store_work = False
            if (not no_one_store_work):
                for store in stores_list:
                    if store.is_working():
                        if waiting_time > store.min_time_to_get_ready() + abs(store._Store__coords - self.__coords) * 30:
                            waiting_time = store.min_time_to_get_ready() + abs(store._Store__coords - self.__coords) * 30
                            order._Order__distance = abs(store._Store__coords - self.__coords)
                            best_store = store
                        pass
                print("Выбран склад №", best_store._Store__id , " с наилучшим временем ожидания сборки и доставки товара: ", waiting_time + 30, "сек", sep="")
                print("Желаете продолжить?y/n")
                if (str(input()) == "y"):
                    best_store.take_order(order, provider)
                else:
                    order._Order__cancel = True
            else:
                print("Невозможно создать заказ: ни один склад сейчас не работает!")
            #print("Ожидаемое время доставки:", waiting_time + abs(self.coords - best_store.coords)*30, "сек")
            return order

        pass

    # сделать заказ

    def take_order(self, order : Order.Order.Order):
        if order.get_delivery_state() == "Доставлен и готов к получению":
            print("Пользователь получил заказ")
            order._Order__taking = True
        else:
            print("Товар ещё не доставлен")
        pass
    # забрать заказ

    def add_to_cart(self, item):
        self.cart.append(item)
        print("Добавлено в корзину: ", item)
    # добавить в корзину