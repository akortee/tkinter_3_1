import tkinter as tk


class ControlsFrame(tk.Frame):
    """Класс панели управления параметрами модели."""

    def __init__(self, parent, reset_callback, **kwargs):
        """
        Инициализация панели управления.

        :param parent: родительский виджет Tkinter.
        :param reset_callback: функция обратного вызова для кнопки сброса.
        """
        super().__init__(parent, **kwargs)
        self.configure(bg="#2b2b2b")

        # Ползунок Sigma
        tk.Label(
            self, text="Параметр Sigma (σ)",
            bg="#2b2b2b", fg="white"
        ).pack(pady=(20, 0))
        self.scale_sigma = tk.Scale(
            self, from_=1, to=30, resolution=0.1,
            orient=tk.HORIZONTAL, bg="#444", fg="white",
            length=150
        )
        self.scale_sigma.set(10.0)
        self.scale_sigma.pack()

        # Ползунок r
        tk.Label(
            self, text="Параметр r (r)",
            bg="#2b2b2b", fg="white"
        ).pack(pady=(20, 0))
        self.scale_r = tk.Scale(
            self, from_=1, to=50, resolution=0.1,
            orient=tk.HORIZONTAL, bg="#444", fg="white",
            length=150
        )
        self.scale_r.set(28.0)
        self.scale_r.pack()

        # Ползунок b
        tk.Label(
            self, text="Параметр b (b)",
            bg="#2b2b2b", fg="white"
        ).pack(pady=(20, 0))
        self.scale_b = tk.Scale(
            self, from_=0.1, to=10, resolution=0.1,
            orient=tk.HORIZONTAL, bg="#444", fg="white",
            length=150
        )
        self.scale_b.set(2.666)
        self.scale_b.pack()

        # Кнопка сброса (без bg/fg для корректной работы на macOS)
        self.btn_reset = tk.Button(
            self, text="Сбросить / Начать заново",
            command=reset_callback
        )
        self.btn_reset.pack(pady=40)

    def get_parameters(self) -> tuple:
        """
        Получение текущих значений ползунков.
        :return: кортеж параметров (sigma, r, b).
        """
        return self.scale_sigma.get(), self.scale_r.get(), self.scale_b.get()
