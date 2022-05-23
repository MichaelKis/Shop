




if __name__ == '__main__':


    goods = [[1, 'milk', 100.00, 1],[2, 'solt', 10.05,1], [3, 'sugar', 15.35,1]] # переменная со списком товаров

    basket= [1, 'milk', 100.00, 1],[2, 'solt', 100.00, 1] # переменная корзины

    stop = ''

    for i in range(len(goods)):
        print(f'Код товара: {goods[i][0]}, \t Название товара: {goods[i][1]}, \t Цена товара: {goods[i][2]}')

    while True:
        number_good = int(input('Введите код товара: '))
        count_good = int(input('Введите количество товара: '))
        # print(len(basket))
        print(basket)

        # for i in range(len(basket)):
        #     if basket[i][0] != number_good:
        #         print('+ добавим товар в корзину')
        #         basket.append(goods[number_good-1])
        #     else:
        #         print('товар уже есть')
        #
        #
        # print(basket)

        stop = input('Закончить выбор: Y ')

        if stop == 'Y': break
