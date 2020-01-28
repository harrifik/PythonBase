# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    def __init__(self):
        self.warehouse = {}

    def set_equipment(self, type_of_eq, num_of_eq):
        try:
            if not num_of_eq.isdigit():
                raise MyError("Ошибка с количеством оргтехники!")
        except MyError as err:
            print(err)
        else:
            self.warehouse[type_of_eq] = int(num_of_eq)
            print(self.warehouse)

    def get_equipment(self, type_of_eq, num_of_eq):
        try:
            if not num_of_eq.isdigit():
                raise MyError("Ошибка с количеством оргтехники!")
        except MyError as err:
            print(err)
        else:
            self.warehouse[type_of_eq] -= int(num_of_eq)
            print(self.warehouse)


class OfficeEquipment:
    def __init__(self, color):
        self.color = color


class Printer(OfficeEquipment):
    def __init__(self, color, print_type):
        super().__init__(color)
        self.print_type = print_type


class Scanner(OfficeEquipment):
    def __init__(self, color, scanner_type):
        super().__init__(color)
        self.scanner_type = scanner_type


class Copier(OfficeEquipment):
    def __init__(self, color, copier_type):
        super().__init__(color)
        self.copier_type = copier_type


my_warehouse = Warehouse()

printer_1 = Printer('black', 'c laser')
printer_2 = Printer('black', 'bw laser')

my_warehouse.set_equipment(printer_1, '3')
my_warehouse.set_equipment(printer_2, 'a')
my_warehouse.get_equipment(printer_1, '1')
