class Stationery:
    """
    Реализовать класс Stationery (канцелярская принадлежность).
●определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
●создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
    """
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки ручкой' + ' ' + self.title)


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки карандашом' + ' ' + self.title)


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки маркером' + ' ' + self.title)


my_pen = Pen('a')
my_pen.draw()
my_pencil = Pencil('b')
my_pencil.draw()
my_handle = Handle('c')
my_handle.draw()