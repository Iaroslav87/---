"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.
"""
class OfficeEquipment:
    model: str
    price: int
    def __init__(self, model, price):
        self.model = model
        self.price = price


class Printer(OfficeEquipment):
    model = 'printer001'
    common_price = 5000
    printing_technology = 'laser'



class Scanner(OfficeEquipment):
    model = 'scanner001'
    common_price = 3000
    scanner_type = 'flatbed type'


class Copier(OfficeEquipment):
    model = 'copier006'
    common_price = 4000
    copier_type = 'digital-type'

class Stock:
    max_count: int
    printers: list
    scanner: list
    copier: list
