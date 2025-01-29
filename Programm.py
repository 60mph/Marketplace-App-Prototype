from dataclasses import dataclass
import Workers.Worker
import Workers.Courier
import Workers.Storekeeper
import User.User
import Order.Order
import Store.Store
import time
import Item.Item
import Provider.Provider

item1 = Item.Item.Item('STORE1','PROV1',"Hennesy XO", 9000)
item2 = Item.Item.Item('STORE2','PROV2',"Jack Daniels", 5000)
item3 = Item.Item.Item('STORE3','PROV3',"Сухарики Кириешки", 70)
item4 = Item.Item.Item('STORE4','PROV4',"Чипсы Лейс с крабом", 100)

items_list = [item1, item2, item3, item4]

provider = Provider.Provider.Provider(items_list)

print("Регистрация пользователя:" + '\n' + "Введите ваш адрес:")
coords = int(input());
print("Номер телефона:")
phone = str(input());

us = User.User.User(coords, phone)

store1 = Store.Store.Store(1, 10)
store2 = Store.Store.Store(2,20)

stores_list = [store1, store2]

oguzok = Workers.Courier.Courier("Огузок")
miha = Workers.Storekeeper.Storekeeper("Михаил Джекович")
sheif = Workers.Courier.Courier("Шеф")
rodya = Workers.Storekeeper.Storekeeper("Родион Сергеевич")

store1.get_worker(oguzok)
store1.get_worker(miha)

store2.get_worker(sheif)
store2.get_worker(rodya)

oguzok.ready_to_work()
miha.ready_to_work()

sheif.ready_to_work()
rodya.ready_to_work()

us.add_to_cart(item1)
us.add_to_cart(item3)

order = us.make_order(stores_list, provider)

#print(order._Order__start_storekeeper, order._Order__finish_storekeeper, time.time())
#print(order._Order__distance)
print("Отслеживание состояния заказа:")
#state = order.get_delivery_state()
#print(time.localtime(time.time()).tm_hour, ":" ,time.localtime(time.time()).tm_min, ":", time.localtime(time.time()).tm_sec , " - ", order.get_delivery_state(), sep="")
while (order.get_delivery_state() != "Доставлен и готов к получению" and order.get_delivery_state() != "Отменён"):
    if(order.get_delivery_state() != "Ошибка заказа"):
        print(time.localtime(time.time()).tm_hour, ":", time.localtime(time.time()).tm_min, ":",
              time.localtime(time.time()).tm_sec, " - ", order.get_delivery_state(), sep="")
        time.sleep(1)
    else:
        break

print(time.localtime(time.time()).tm_hour, ":", time.localtime(time.time()).tm_min, ":",
          time.localtime(time.time()).tm_sec, " - ", order.get_delivery_state(), sep="")

time.sleep(2)
if(order.get_delivery_state() == "Доставлен и готов к получению"):
    us.take_order(order)
    print(time.localtime(time.time()).tm_hour, ":" ,time.localtime(time.time()).tm_min, ":", time.localtime(time.time()).tm_sec , " - ", order.get_delivery_state(), sep="")

oguzok.dont_ready_to_work()
rodya.dont_ready_to_work()
sheif.dont_ready_to_work()
miha.dont_ready_to_work()
#print(id(store2), id(store1))
#print(store2.workers_list)
