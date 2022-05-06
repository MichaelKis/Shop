"""
Генерация данных (категории, товары, пользователи)
"""
import dbf

db = dbf.Table('products.dbf')
db.open()
print(db)
# db = dbf.Dbf('products.dbf')

products_list = ['AAA', 'BBB', 'CCC', 'DDD']

SCHEMA = (
    ("ID", "N", 8),
    ("PRODUCT", "C", 200),
    ("PRIСE", "N", 8, 2),
    ("DATE", "D"),
)

db = dbf.Dbf("products.dbf", new=True)
db.addField(*SCHEMA)

id_ = 0
for product in products_list:
    rec_ = db.newRecord()
    rec_["ID"] = product.id_
    rec_["PRODUCT"] = product.product.encode("cp866")
    rec_["PRICE"] = product.price
    rec_["DATE"] = product.date
    id_ += 1
    rec_.store()
db.close()
