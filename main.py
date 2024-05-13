class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

store1 = Store("Моя семья", "Вадковский переулок 1")
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)
store1.add_item("апельсины", 0.8)

# Создание магазина №2
store2 = Store("ВкусВилл", "Мичуринский проспект 18")
store2.add_item("молоко", 3.5)
store2.add_item("яйца", 5.0)
store2.add_item("масло", 7.5)

# Создание магазина №3
store3 = Store("Помпончик", "Каширское шоссе 145")
store3.add_item("хлеб зерновой", 1.2)
store3.add_item("пончик с карамелью", 2.5)
store3.add_item("ватрушка с творогом", 2.0)

price_of_bread = store3.get_price("хлеб")
print("Цена хлеба:", price_of_bread)

store2.update_price("яйца", 5.5)
print("Новая цена яиц:", store2.get_price("яйца"))

