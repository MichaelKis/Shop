"""
Создание класса Товары
"""


class Goods:
    id = 0
    def __init__(self, name: str = 'Some Goods', price: float = 0.01, rating: int = 1):
        if not isinstance(name, str):
            raise TypeError('Не верный тип данных для name')
        self.name = name
        if not isinstance(price, float):
            raise TypeError('Не верный тип данных для price')
        self.price = price
        if not isinstance(rating, int):
            raise TypeError('Не верный тип данных для raiting')
        self.rating = rating
        self.id += 1

    def display_product(self):
        print('Id: {} Название продукта:{}. Цена:{}. Рейтинг:{} '.format(self.id, self.name, self.price, self.rating))


if __name__ == '__main__':

    print(50*'*')
    goods = Goods('Milk', 2999.01, 1)
    Goods.display_product(goods)
    goods1 = Goods('Sugar', 3666.02, 2)
    Goods.display_product(goods1)
    goods2 = Goods('Solt', 16.02, 3)
    Goods.display_product(goods2)

