"""
Начать работу над проектом «Склад оргтехники».
Создать класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
 общие для приведённых типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за приём оргтехники на склад
и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
 а также других данных, можно использовать любую подходящую структуру (например, словарь).
Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

"""
class Storage:
    def __init__(self, printer, scanner, xerox):
        self.printer = printer
        self.scanner = scanner
        self.xerox = xerox
        self.stor_dict = {}

    def validation(self):
        # чтобы не повторять код сделала функцию, так как цикл for не получилось сделать
        def val_for_item(item):
            if isinstance(item.quantity, int):
                return 'quantity is ok'
            else:
                return 'wrong quantity'

        return val_for_item(self.printer), val_for_item(self.scanner), val_for_item(self.xerox)

    def loading(self):
        # пыталась сделать в цикле for, но не получилось
        # в словарь добавляю, сколько каждой техники штук и полную информацию о ней
        def load_for_item(item):
            self.stor_dict.setdefault(f'{item.__class__.__name__} quantity',item.quantity)
            self.stor_dict.setdefault(f'{item.__class__.__name__} info',
                                      item.__dict__)
        load_for_item(self.printer)
        load_for_item(self.scanner)
        load_for_item(self.xerox)
        return self.stor_dict

class OfficeMachines:
    def __init__(self, model, price, weight, color, quantity):
        self.model = model
        self.price = price
        self.weight = weight
        self.color = color
        self.quantity = quantity

class Printer(OfficeMachines):
    def __init__(self, model, price, weight, color, quantity, cartrige_type):
        super().__init__(model, price, weight, color, quantity)
        self.cartrige_type = cartrige_type

class Scanner(OfficeMachines):
    def __init__(self, model, price, weight, color, quantity, scanner_type):
        super().__init__(model, price, weight, color, quantity)
        self.scanner_type = scanner_type

class Xerox(OfficeMachines):
    def __init__(self, model, price, weight, color, quantity,  xerox_type):
        super().__init__(model, price, weight, color, quantity)
        self.xerox_type = xerox_type

pr_1 = Printer('vdbbs1200', 5000, 3.5, 'black', 2, 'color')
sc_1 = Scanner('bsdfgsdrg', 4000, 2, 'white', 4, 'dgadgv')
xe_1 = Xerox('fadfgda', 5500, 5, 'grey', 3, 'gfdg')
storage_1 = Storage(pr_1, sc_1, xe_1)
print(storage_1.loading())
print(storage_1.validation())



