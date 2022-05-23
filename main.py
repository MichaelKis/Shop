from users import user_authorization
from goods import Goods

# Регистрация пользователя

print('Добро пожаловать в интернет-магазин продуктов питания!')
print('Просим Вас авторизоваться')
login=input('Введите Ваш Логин:')
password=input('Введите Ваш Пароль:')

user_authorization(login,password)

# Создание товаров




