import time
import random
import Order.Order
import Workers.Worker

class Storekeeper(Workers.Worker.Worker):

    def get_order(self, order):
        self._Worker__start_time = time.time()
        order._Order__start_storekeeper = time.time() + self.time_to_get_ready()
        order._Order__finish_storekeeper = time.time() + self.time_to_get_ready() + 30
        self._Worker__finish_time = time.time() + self.time_to_get_ready() + 30
        order._Order__storekeeper = self
        pass

    def is_busy(self):
        cur_t = time.time()
        if (self._Worker__start_time <= cur_t and self._Worker__finish_time >= cur_t):
            return True
        else:
            return False

    def time_to_get_ready(self):
        cur_t = time.time()
        if (self.is_busy()):
            return self._Worker__finish_time - cur_t
        else:
            return 0
        pass

    def ready_to_work(self):
        rand = random.randint(1, 10)
        if rand != 1:
            self._Worker__is_ready_to_work = True
            print(self._Worker__name, "начал смену")
        else:
            print(self._Worker__name, "заявил что выйдет на смену, но не явился. Штраф")

    def dont_ready_to_work(self):
        if self._Worker__is_ready_to_work != False:
            self._Worker__is_ready_to_work = False
            print(self._Worker__name, "закончил смену")

    def is_ready(self):
        return self._Worker__is_ready_to_work