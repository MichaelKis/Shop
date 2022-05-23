class Goods:
    counter = 0
    def __init__(self, id: int, name: str, price: int, category: int):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        Goods.counter +=1

    def __str__(self):
        return f'Код товара: {self.id},\t Название товара: {self.name}, \t Цена товара: {self.price}'

class Category:
    counter = 0
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.goods = []
        Category.counter +=1

    def __str__(self):
        return f'Код категории: {self.id},\t Название категории: {self.name}'

class Select_goods:
        counter = 0

        def __init__(self,id:int, name: str, price: int):

            self.id = id
            self.name = name
            self.price = price

        def __str__(self):
            return f'Код товара: {self.id},\t Название товара: {self.name}, \t Цена товара: {self.price}'


class Basket:
    counter = 0
    def __init__(self, goods =None, count=None):

        self.goods = goods
        self.count = count

        Basket.counter +=1


    def amount(self):
        return self.goods.price * self.count

    def __str__(self):
        return f'Название товара: {self.goods.name}, \t Цена товара: {self.goods.price}, \t Количество: {self.count}'







if __name__ == '__main__':

    goods_list = [[1, 'milk', 100.00, 1], [2, 'solt', 10.05, 4], [3, 'sugar', 15.35, 4], [4, 'kofee', 11.75, 3],
                  [5, 'tea', 5.15, 2]]  # список товаров в формате: id, name, price, category

    category_list = [[1, 'Milk', []], [2, 'Tea', []], [3, 'Kofee', []],
                     [4, 'Other', []]]  # список категорий товаров в формате: id, name, [goods]

    vars_good = []  # переменная для товаров

    vars_category = []  # переменная для категории товаров

    count_basket = 0  # кол-во товаров в корзине до покупки

    for i in range(len(goods_list)):  # генерируем товары
        vars_good.append(f'goods{i}')
        vars_good[i] = Goods(goods_list[i][0], goods_list[i][1], goods_list[i][2], goods_list[i][3])
        #print(vars_good[i].id,vars_good[i].name,vars_good[i].price, vars_good[i].category)

    for i in range(len(category_list)):  # генерируем категории товаров
        vars_category.append(f'category{i}')
        vars_category[i] = Category(category_list[i][0], category_list[i][1])
        # print(vars_category[i].id,vars_category[i].name,vars_category[i].goods)

    for i in range(len(goods_list)): # связываем товары и категории товаров
        for n in range(len(category_list)):

            if vars_good[i].category == vars_category[n].id:
                vars_category[n].goods.append(vars_good[i].id)

    # for n in range(len(category_list)):  # проверяем наполнение категорий товаров
    #     print(vars_category[n].id, vars_category[n].name, vars_category[n].goods)

    #basket = Basket()  # инициализируем корзину
    # print(basket.goods,basket.count)

    #basket = Basket(vars_good[2], 5)  # Добавляем в корзину товар

    #print(basket.goods.id, basket.goods.name, basket.goods.price, basket.count)

    #money = Basket.amount(basket)

    #print(money)

    # print(vars_category[0])
    # print(Goods.counter)
    # print(Basket.counter)

    #for i in range (Goods(vars_good))

    # while True:
    #     number_good = int(input('Введите код товара: '))
    #     count_good = int(input('Введите количество товара: '))
    #     basket_count += 1
    #     basket = Basket(vars_good[number_good-1], count_good)
    #     print(basket.goods.id, basket.goods.name, basket.goods.price, basket.count)
    #     print(basket_count)

    # Выведем список категории товаров

    # Начало работы

    print('-'*50)
    print('Список категорий товаров')
    print('-' * 50)
    for i in range (Category.counter):
        print(vars_category[i])
    print('-' * 50)
    category_number = int(input(f'Выберите категорию товаров от 1 до {i+1}: '))


    print(f'Список товаров для категории товаров {vars_category[category_number-1].name} :')
    print('-' * 80)

    count_good = 0
    select_goods = [[]]

    for i in range (Goods.counter):
        if vars_good[i].category == category_number:
            count_good += 1
            select_goods.append(f'select_goods{count_good}')
            select_goods[count_good] = Select_goods(count_good,vars_good[i].name,vars_good[i].price)
            print(select_goods[count_good])
    print('-' * 80)

    good_number = int(input(f'Выберите код товара от 1 до {count_good}: '))

    print('-'*80)

    print(f'Вы выбрали :{select_goods[good_number]}')

    print('-'*80)

    good_count = int(input('Введите кол-во выбранного товара: '))

    print()

    basket = Basket(select_goods[good_number],good_count)
    basket.total = select_goods[good_number].price * good_count

    print('В корзину добавлены:')
    print('-'*80)
    print(f'{basket}\t На сумму: {basket.total}')
    print('-' * 80)

    next = input('Перейти к оплате = Y или продолжить покупки любая клавиша: ')

    if str.upper(next) == 'Y':
        print('Переходим к оплате')
    else:
        print('Продолжить покупки')
