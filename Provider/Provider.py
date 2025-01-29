import Item.Item
import Store.Store


class Provider: # поставщик
    __items_list = list()
    def __init__(self, items_list):
        self.__items_list = items_list

    def send_order(self, order_item_list : list, store):
        needed_items = []
        print(f'Поставщик принял запрос на отправку товаров \n\t с ID поставщика: {[str(item._Item__id_provider) for item in order_item_list]} на склад №{store._Store__id}')
        for item in order_item_list:
            if(item in self.__items_list):
                print(f'Товар ID:{item._Item__id_provider} - {item._Item__name} - есть в наличии у поставщика')
                needed_items.append(item)
                self.__items_list.remove(item)
        print("Поставщик отправил выбранные товары на склад")
        store.get_items(needed_items)
        pass

    # send_order - принять и отправить заказ складу