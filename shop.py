"""
Оформление заказа
"""

from goods import Goods
from basket import Basket


class Shop:

    def __init__(self):

        self.shops = [] # Хранить все товары
        self.basket = []  # Магазин товаров в корзине товаров
        self.load() # Загрузить товар


def load(self):
    """
    Загрузить товар
    """


    self.add(Goods('Apple Watch', 3299, 100))
    self.add(Goods('AirPods', 1288, 100))
    self.add(Goods('Home Pod', 1299, 100))
    self.add(Goods('iPhone X', 6288, 100))


def add(self, good):
    """
             Установите идентификатор нового продукта и добавьте его в список
             : param good: Новый продукт
    :return: None
    """
    good.id = len(self.shops) + 1
    self.shops.append(good)


def print_line(self):
    print('-' * 50)


def print_double_line(self):
    print('=' * 50)


def list(self):
    "" "Список всех товаров" ""
    печать(«Пожалуйста, выберите
    продукт:»)
    self.print_double_line()
    # Пройти список товаров
    for g in self.shops:
        print('%s       %s        %s' % (g.id, g.name, g.price))
        self.print_line()

    def list_cart(self):
        "" "Показать корзину товаров, рассчитать общую стоимость" ""

    self.print_line()
    total = 0.0
    for item in self.cart:
        print('%s     =￥%s' % (item, item.amout()))
        total += item.amout()
    self.print_line()
    печать(«Общая
    сумма: ￥ % .2
    f» % всего)

    def add_to_cart(self):
        "" "Добавить товар в корзину" ""

    print('\n')
    g_id = input(
        'Пожалуйста, введите идентификатор продукта (введите, чтобы оформить заказ, 0, чтобы очистить корзину):')

    if len(g_id) == 0:
        # Счет, пожалуйста
        total = 0.0
        for item in self.cart:
            total += item.amout()
        self.print_line()
        печать(«Пожалуйста, заплатите:.% .2
        f» % всего)

        # Пустая корзина
        self.cart.clear()
        печать(«Успешный
        платеж!»)

        elif g_id == '0':
        self.cart.clear()
        печать(«Корзина
        была
        опустошена!»)
        else:
        # Рассчитать индекс продукта
        idx = int(g_id) - 1
        # Вывезти товар
        goods = self.shops[idx]
        self.print_line()
        print(goods)

        count = int(input('Пожалуйста, введите количество покупки:'))
        # Определить, больше ли количество, чем инвентарь
    while count > goods.stock:
        count = int(input('Там не так много товаров, пожалуйста, введите заново:'))

    # Если товар уже есть в корзине, измените количество товаров
    # Переменная указывает, есть ли этот продукт в корзине
    is_exsts = False
    for item in self.cart:
        if item.goods == goods:
            # Объясните, что товар находится в корзине
            is_exsts = True
            item.count += count
            # уменьшить запас
            goods.stock -= count

            # Если это выполнено, значение is_exsts по-прежнему равно False, что указывает на то, что товара нет в корзине
    if is_exsts == False:
        # Добавить товар в корзину
        goods.stock -= count
        self.cart.append(CartItem(goods, count))

        # Показать корзину товаров и рассчитать общую стоимость
    self.list_cart()

    def run(self):
        "" "Запустить приложение" ""
        print(«Магазин
        электронных
        товаров
        Zhiyou»)
        print('v1.0')
        print('\n')

        self.list()

        while True:
            self.add_to_cart()

        shop = Shop()
        shop.run()



if __name__ == '__main__':

    shop()