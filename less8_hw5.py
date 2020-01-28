# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.


class Warehouse:
    def __init__(self):
        self.warehouse = {}

    def set_equipment(self, type_of_eq, num_of_eq):
        self.warehouse[type_of_eq] = num_of_eq
        print(self.warehouse)

    def get_equipment(self, type_of_eq, num_of_eq):
        self.warehouse[type_of_eq] -= num_of_eq
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

my_warehouse.set_equipment(printer_1, 3)
my_warehouse.set_equipment(printer_2, 2)
my_warehouse.get_equipment(printer_1, 1)