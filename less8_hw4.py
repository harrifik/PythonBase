# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.


class Warehouse:
    def __init__(self):
        pass


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
