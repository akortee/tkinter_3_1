import tkinter as tk
from src.models.animation_model import LorenzModel
from src.renderers.renderer import Renderer
from src.widgets.controls import ControlsFrame


class App:
    """Основной класс приложения для управления окном и циклом анимации."""

    def __init__(self):
        """Инициализация главного окна и всех компонентов."""
        self.root = tk.Tk()
        self.root.title("Аттрактор Лоренца (Моя первая программа!)")
        self.root.geometry("1000x650")
        self.root.configure(bg="#2b2b2b")

        # Инициализация логики (Модель)
        self.model = LorenzModel()

        # Настройка интерфейса (Рендерер и Виджеты)
        self.canvas = tk.Canvas(
            self.root,
            width=800, height=600,
            bg="black", highlightthickness=0
        )
        self.canvas.pack(side=tk.LEFT, padx=10, pady=10)
        self.renderer = Renderer(self.canvas)

        self.controls = ControlsFrame(
            self.root, reset_callback=self.reset_animation
        )
        self.controls.pack(
            side=tk.RIGHT, fill=tk.BOTH,
            expand=True, padx=10, pady=10
        )

        # Начальное состояние
        self.renderer.draw_grid()
        self.is_running = True

    def reset_animation(self):
        """Обработчик сброса анимации в начальное состояние."""
        self.model.reset()
        self.renderer.clear()
        self.renderer.draw_grid()

    def update(self):
        """Главный цикл обновления и отрисовки кадра."""
        if not self.is_running:
            return

        try:
            # Получаем параметры из интерфейса
            sigma, r, b = self.controls.get_parameters()
        except tk.TclError:
            # Если окно закрыто крестиком
            self.is_running = False
            return

        # Делаем математический шаг
        old_x, old_z, next_x, next_z = self.model.step(sigma, r, b)

        # Отрисовываем шаг
        self.renderer.draw_segment(old_x, old_z, next_x, next_z)

        # Планируем следующий кадр
        self.root.after(10, self.update)

    def run(self):
        """Запуск основного цикла окна приложения."""
        self.update()
        self.root.mainloop()
