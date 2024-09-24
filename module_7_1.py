class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        try:
            is_file_exest = open(self.__file_name, 'r')
        except:
            is_file_exest = open(self.__file_name, 'w')
        is_file_exest.close()

    def add(self, *product):
        res_str = self.get_products()
        file = open(self.__file_name, 'a')
        for i in range(len(product)):
            if str(product[i]) in res_str:
                print(f'Продукт {product[i]} уже есть в магазине')
            else:
                file.write(f'{product[i]}\n')
        file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        res_str = file.read()
        file.close()
        return res_str


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
