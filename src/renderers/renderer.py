class Renderer:
    """Класс для отрисовки графики на холсте Tkinter."""

    def __init__(self, canvas):
        """
        Инициализация рендерера
        """
        self.canvas = canvas
        self.scale_factor = 10
        self.offset_x = 400
        self.offset_y = 550

    def draw_grid(self):
        """Отрисовка клетчатого поля на фоне."""
        for i in range(0, 800, 50):
            self.canvas.create_line(i, 0, i, 600, fill="#333333")
        for i in range(0, 600, 50):
            self.canvas.create_line(0, i, 800, i, fill="#333333")

    def clear(self):
        """Полная очистка холста."""
        self.canvas.delete("all")

    def draw_segment(self, x1: float, z1: float, x2: float, z2: float):
        """
        Отрисовка одного сегмента линии аттрактора.

        :param x1: Начальная координата X.
        :param z1: Начальная координата Z.
        :param x2: Конечная координата X.
        :param z2: Конечная координата Z.
        """
        x_pixel1 = self.offset_x + x1 * self.scale_factor
        y_pixel1 = self.offset_y - z1 * self.scale_factor
        x_pixel2 = self.offset_x + x2 * self.scale_factor
        y_pixel2 = self.offset_y - z2 * self.scale_factor

        self.canvas.create_line(
            x_pixel1, y_pixel1, x_pixel2, y_pixel2,
            fill="cyan", width=2
        )
