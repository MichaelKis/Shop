"""
Создание класса Корзина
"""

from goods import Goods


class Basket:
    def __init__(self, goods, count):
        self.goods = goods
        self.count = count

    def __str__(self):
        # % f является заполнителем для десятичного типа
        return '%s(￥%.2f)*%s' % (self.goods.name,
                                 self.goods.price, self.count)


    def amout(self): # Рассчитать подытог продукта
        return self.goods.price * self.count


if __name__ == '__main__':
    goods = Goods('Apple pods', 2999.01, 1)
    # Создайте объект продукта корзины покупок, вам нужно передать объект продукта
    item = Basket(goods, 1)
    money = item.amout()
    print(money)