import Item.Item
import Provider.Provider
import Workers
import time
import Order.Order

class Store:
    __id:int = 0
    __coords : int = 0
    __workers_list = list()
    __items_list = list()
    __begin_work : int = 0
    __end_work : int = 0
    def __init__(self, id, coords):
        if(isinstance(coords, int) and isinstance(id, int)):
            self.__coords = coords
            self.__id = id
            self.__workers_list = []
            self.__items_list = []
        else:
            print("Ошибка инициализации склада")


    #Получение товров от провайдера
    def get_items(self, items: list()):
        print("Склад получил товары")
        for item in items:
            self.__items_list.append(item)

    def set_working_time(self, begin_work, end_work):
        if(begin_work < 24 and begin_work >= 0 and end_work < 24 and end_work >=0):
            self.__begin_work = begin_work
            self.__end_work = end_work
        else:
            print("Ошибка назначения времени работы склада")

    def is_working(self):
        cur_t = time.localtime(time.time())
        if(cur_t.tm_hour >= self.__begin_work and cur_t.tm_hour < self.__end_work or self.__end_work == 0 and self.__begin_work == 0):
            if (len(self.__workers_list) > 1):
                there_is_courier = False
                there_is_storekeeper = False
                for worker in self.__workers_list:
                    if worker.is_ready():
                        if (isinstance(worker, Workers.Courier.Courier)):
                            there_is_courier = True
                        if (isinstance(worker, Workers.Storekeeper.Storekeeper)):
                            there_is_storekeeper = True
                return there_is_courier and there_is_storekeeper
            else:
                return False
        else:
            return False

    def min_time_to_get_ready(self):
        courier_waiting = 10000
        storekeeper_waiting = 10000
        for worker in self.__workers_list:
            if worker.is_ready():
                if (isinstance(worker, Workers.Courier.Courier)):
                    if(courier_waiting > worker.time_to_get_ready()):
                        courier_waiting = worker.time_to_get_ready()
                if (isinstance(worker, Workers.Storekeeper.Storekeeper)):
                    if (storekeeper_waiting > worker.time_to_get_ready()):
                        storekeeper_waiting = worker.time_to_get_ready()
        return max(courier_waiting, storekeeper_waiting)

    def take_order(self, order, provider):
        print("Склад №", self.__id, " принял заказ на товары с ID склада: \n\t", f'{[str(item._Item__id_store) for item in order._Order__order_item_list]}', sep="")
        self.send_request(order, provider)
        for item in order._Order__order_item_list:
            if(item in self.__items_list):
                print("Товар: ", item, " найден на складе", sep="")
        print("Ищем самого быстрого сборщика и курьера")
        courier_waiting = 10000
        storekeeper_waiting = 10000
        for worker in self.__workers_list:
            if worker.is_ready():
                if (isinstance(worker, Workers.Courier.Courier)):
                    if (courier_waiting > worker.time_to_get_ready()):
                        courier_waiting = worker.time_to_get_ready()
                        best_courier = worker
                if (isinstance(worker, Workers.Storekeeper.Storekeeper)):
                    if (storekeeper_waiting > worker.time_to_get_ready()):
                        storekeeper_waiting = worker.time_to_get_ready()
                        best_storekeeper = worker
        #print("Ваш заказ будет собирать лучший сборщик:", best_storekeeper.name)
        self.set_storekeeper(order, best_storekeeper)
        self.set_courier(order, best_courier)
        pass

    # принять заказ и начать его обрабатывать

    def send_request(self, order: Order.Order.Order, provider: Provider.Provider.Provider):
        print("Склад отправил запрос на выбранные товары поставщику")
        provider.send_order(order._Order__order_item_list, self)
        pass

    # send_request - отправить заказ для провайдера (что привезти)

    def set_courier(self, order: Order.Order.Order, courier):
        print("Курьер", courier._Worker__name, "назначен на заказ")
        if courier.is_busy():
            print("Освободится через:", courier.time_to_get_ready(), "сек и начнёт работу")
        else:
            print("Курьер начнёт работу после сборки заказа")
        courier.get_order(order)
        pass

    # дать заказу курьера

    def set_storekeeper(self, order: Order.Order.Order, storekeeper):
        print("Сборщик", storekeeper._Worker__name, "назначен на заказ")
        if storekeeper.is_busy():
            print("Освободится через:", storekeeper.time_to_get_ready(), "сек и начнёт работу")
        else:
            print("Сборщик начал работу")
        storekeeper.get_order(order)
        pass

    # дать заказу кладовщика

    def get_worker(self, worker):
        if (isinstance(worker, Workers.Worker.Worker)):
            if (isinstance(worker, Workers.Courier.Courier)):
                self.__workers_list.append(worker)
                print("Склад ", self.__id, ": Курьер ", worker._Worker__name, " принят на работу", sep="")
            if (isinstance(worker, Workers.Storekeeper.Storekeeper)):
                self.__workers_list.append(worker)
                print("Склад ", self.__id, ": Сборщик ", worker._Worker__name, " принят на работу", sep="")
        else:
            print("Ошибка назначения на работу")
        pass

    # взять работника к себе и дать ему смену

    def remove_worker(self, worker):
        if (isinstance(worker, Workers.Worker.Worker)):
            if (worker in self.__workers_list):
                if (isinstance(worker, Workers.Courier.Courier)):
                    self.__workers_list.remove(worker)
                    print("Склад ", self.__id, ": Курьер ", worker._Worker__name, " уволен", sep="")
                if (isinstance(worker, Workers.Storekeeper.Storekeeper)):
                    self.__workers_list.remove(worker)
                    print("Склад ", self.__id, ": Сборщик ", worker._Worker__name, " уволен", sep="")
            else:
                print("Такого работника нет на складе")
        else:
            print("Ошибка увольнения")
        pass