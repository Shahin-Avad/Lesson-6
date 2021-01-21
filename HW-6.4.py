#Реализуйте базовый класс Car.
#● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
#также методы: go, stop, turn(direction), которые должны сообщать, что машина
#поехала, остановилась, повернула (куда);
#● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#● добавьте в базовый класс метод show_speed, который должен показывать текущую
#скорость автомобиля;
#● для классов TownCar и WorkCar переопределите метод show_speed. При значении
#скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
#превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
#выведите результат. Вызовите методы и покажите результат.


class Car:

    def __init__(self, speed, color, name, is_police = bool):
        self.s = speed
        self.c = color
        self.n = name
        self.p = is_police

    def go(self):
        if self.s > 0:
            print('Go')
        elif self.s < 0:
            print('Вероятно вы едете задним ходом...')        

    def show_speed(self):
        
        print('Speed: ' + (self.s))


    def stop(self):
        
        if self.s == 0:
            print('Stop')

    def turn(self, l):
        
        if l == 'Left':
            print('Left')
        else:
            print('Right')

    def poice(self):
        
        if self.p == True:
            print('The police car')
        else:
            print('Not the police car')
        


class TownCar(Car):

    def info(self):
    
        print(f'{self.n}\n{self.c}')

    def show_speed(self):
        
        if self.s > 60:
            print("High speed")
        else:
            print('Normal speed')
        
        print('Speed: ' + str(self.s))
        


class SportCar(Car):
    
    def info(self):
    
        print(f'{self.n}\n{self.c}')
    
    def show_speed(self):    
        
        print('Speed: ' + str(self.s))


class WorkCar(Car):
    
    def info(self):
    
        print(f'{self.n}\n{self.c}')
        
        if self.s > 40:
            print("High speed")
        else:
            print('Normal speed')
        
    def show_speed(self):    
        print('Speed: ' + str(self.s))
    

class PoliceCar(Car):
    
    def info(self):
    
        print(f'{self.n}\n{self.c}')
    
    def show_speed(self):
        if self.p == True and self.s > 60:
            print('Pursuit\nSpeed:' + str(self.s))
        elif self.p == True and self.s <= 60:
            print(f'Patrol\nSpeed: {str(self.s)}')
        elif self.p == False:
            print("Realy? Sorry but i don't know what to do with this problem")

        
    

car_1 = SportCar(60, 'Blue', 'Mazda', False)
car_1.info()
car_1.poice()
car_1.go()
car_1.show_speed()
car_1.stop()
car_1.turn('Left')
