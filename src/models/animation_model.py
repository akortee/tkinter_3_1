class LorenzModel:
    """
    Класс для вычисления координат аттрактора Лоренца.
    """

    def __init__(self, dt: float = 0.01):
        """
        Инициализация параметров модели.
        """
        self.dt = dt
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.reset()

    def reset(self):
        """Сброс координат к начальным значениям."""
        self.x = 0.1
        self.y = 0.0
        self.z = 0.1

    def step(self, sigma: float, r: float, b: float) -> tuple:
        """
        :param sigma: Параметр Прандтля.
        :param r: Параметр Рэлея.
        :param b: Физический параметр (пропорции).
        :return: Кортеж (old_x, old_z, next_x, next_z) для отрисовки.
        """
        # Дифференциальные уравнения Лоренца
        dx = sigma * (self.y - self.x) * self.dt
        dy = (self.x * (r - self.z) - self.y) * self.dt
        dz = (self.x * self.y - b * self.z) * self.dt

        # Приближение Эйлера для вычисления следующих координат
        next_x = self.x + dx
        next_y = self.y + dy
        next_z = self.z + dz

        # Сохранение старых координат для отрисовки линии
        old_x, old_z = self.x, self.z

        # Обновление текущего состояния
        self.x, self.y, self.z = next_x, next_y, next_z

        return old_x, old_z, next_x, next_z
