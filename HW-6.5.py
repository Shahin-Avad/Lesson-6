#Реализовать класс Stationery (канцелярская принадлежность).
#● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
#сообщение «Запуск отрисовки»;
#● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
#● в каждом классе реализовать переопределение метода draw. Для каждого класса
#метод должен выводить уникальное сообщение;
#● создать экземпляры классов и проверить, что выведет описанный метод для каждого
#экземпляра.

class Stationery:

    def __init__(self, title):
        self.t = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    
    def draw(self):
        print("запуск отрисовки карандашом")


class Pencil(Stationery):

    def draw(self):
        print("Запуск отрисовки ручкой")


class Handle(Stationery):

    def draw(self):
        print("Запукой отрисовки маркером")


paint = Pen('рисунок карандашом')
paint.draw()

paint = Pencil('рисунок ручкой')
paint.draw()

paint = Handle('рисунок маркером')
paint.draw()