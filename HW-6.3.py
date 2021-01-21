#Реализовать базовый класс Worker (работник).
#● определить атрибуты: name, surname, position (должность), income (доход);
#● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
#элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
#● создать класс Position (должность) на базе класса Worker;
#● в классе Position реализовать методы получения полного имени сотрудника
#(get_full_name) и дохода с учётом премии (get_total_income);
#● проверить работу примера на реальных данных: создать экземпляры класса Position,
#передать данные, проверить значения атрибутов, вызвать методы экземпляров.


class Worker:
    
    def __init__(self, name, surname, position, income = {"wage": 36000, "bonus": 3800}):
        self.n = name
        self.s = surname
        self.p = position
        self.__i = income 
        
    
class Position(Worker):
    
    def get_full_name(self):
        print(f'Имя: {self.n} \nФамилия: {self.s}')


    def get_total_income(self):
        
        inc = float(inf_2._Worker__i.get('wage')) + float(inf_2._Worker__i.get('bonus'))
        print(inc)

        
inf_2 = Position('Ivan', 'Ivanov', 'Employe')
inf_2.get_full_name()
inf_2.get_total_income()

