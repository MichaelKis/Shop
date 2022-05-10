"""
Создание класса Товары
"""


class Goods:

    def __init__(self, id: int, name: str, price: float, unit: str, volume: int, rating: int):
        if not isinstance(id, int):
            raise TypeError('Не верный тип данных для Кода товара')
        self.id = id
        if not isinstance(name, str):
            raise TypeError('Не верный тип данных для Названия товара')
        self.name = name
        if not isinstance(price, float):
            raise TypeError('Не верный тип данных для Цены')
        self.price = price
        if not isinstance(volume, int):
            raise TypeError('Не верный тип данных для Объема')
        self.volume = volume
        if not isinstance(unit, str):
            raise TypeError('Не верный тип данных для Ед.измерения')
        self.unit = unit
        if not isinstance(rating, int):
            raise TypeError('Не верный тип данных для Рейтинга')
        self.rating = rating


    def display_product(self):
        print('Код товара: {}, Название продукта: {}, Цена: {}, Объем: {}, Ед. измерения: {}, Рейтинг: {}, '.format(self.id, self.name,                                              self.price,
                                                                                                     self.volume,self.unit,
                                                                                                     self.rating))


if __name__ == '__main__':
    # Создаем 5 товаров
        print(50 * '*')
        goods = Goods(1,'Молоко',145.50,'гр.',950,1)
        Goods.display_product(goods)
        goods1 = Goods(2, 'Масло сливочное', 169.89, 'гр.',250, 2)
        Goods.display_product(goods1)
        goods2 = Goods(3, 'Икра лососовая', 319.99, 'гр.',95, 3)
        Goods.display_product(goods2)
        goods3 = Goods(4, 'Колбаса вареная', 159.99, 'гр.',1000, 4)
        Goods.display_product(goods3)
        goods4 = Goods(5, 'Картофель', 49.89, 'кг.',1, 5)
        Goods.display_product(goods4)

