"""
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру (например, словарь).
"""

from abc import ABC, abstractmethod
class OfficeEquipment(ABC):
    model: str
    price: int

    @abstractmethod
    def build(self, count):
        pass


class Printer(OfficeEquipment):
    model = 'printer001'
    price = 5000
    printing_technology = 'laser'
    def build(self):
        printers = []
        count = 1
        for x in range(count):
            printers.append([Printer.model, Printer.price])
        return printers


class Scanner(OfficeEquipment):
    model = 'scanner012'
    price = 3000
    scanner_type = 'flatbed type'
    def build(self):
        count = 1
        scanners = []
        for x in range(count):
            scanners.append([Scanner.model, Scanner.price])
        return scanners


class Copier(OfficeEquipment):
    model = 'copier006'
    price = 4000
    copier_type = 'digital-type'
    def build(self):
        count = 1
        copiers = []
        for x in range(count):
            copiers.append([Copier.model, Copier.price])
        return copiers


class Stock(Copier, Scanner, Printer):
    max_count: int
    printers: list
    scanners: list
    copiers: list
    def __init__(self, count = 10):
        self.max_count = count
        self.printers = []
        self.scanners = []
        self.copiers = []

    @classmethod
    def store(self, printers: Printer, scanners: Scanner, copiers: Copier):
        printers.extend(printers)
        scanners.extend(scanners)
        copiers.extend(copiers)
        return f'{printers}, {scanners}, {copiers}'


class Office(Stock):
    money: int
    office_equipment: list

    def buy_p(self, printers: Printer, scanners: Scanner, copiers: Copier):
        super().store(printers, scanners, copiers)
        printers.extend(printers)
        scanners.extend(scanners)
        copiers.extend(copiers)
        return f'{printers}, {scanners}, {copiers}'


printer = Printer()
scanner = Scanner()
copier = Copier()
stock = Stock(10)
printer_list = printer.build()
scanner_list = scanner.build()
copier_list = copier.build()

print(Stock.store(printer_list, scanner_list, copier_list))
office = Office(15000)
print(Office.buy_p(printer_list, scanner_list, copier_list))