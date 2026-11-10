import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QWidget, QLabel, QSlider
)

# Константы диапазона слайдера
VOLUME_MIN = 0
VOLUME_MAX = 100
VOLUME_DEFAULT = 50


class MainWindow(QMainWindow):
    """Главное окно приложения."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Настройки")
        self.setGeometry(100, 100, 400, 200)
        self.setMinimumSize(300, 150)

        self.init_ui()

    def init_ui(self):
        """Инициализация пользовательского интерфейса."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()

        self.title_label = QLabel("Громкость")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setMinimum(VOLUME_MIN)
        self.volume_slider.setMaximum(VOLUME_MAX)
        self.volume_slider.setValue(VOLUME_DEFAULT)
        self.volume_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.volume_slider.setTickInterval(10)

        self.min_label = QLabel(str(VOLUME_MIN))
        self.max_label = QLabel(str(VOLUME_MAX))

        slider_layout = QHBoxLayout()
        slider_layout.addWidget(self.min_label)
        slider_layout.addWidget(self.volume_slider)
        slider_layout.addWidget(self.max_label)

        self.value_label = QLabel(f"Текущее значение: {VOLUME_DEFAULT}")
        self.value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_layout.addWidget(self.title_label)
        main_layout.addLayout(slider_layout)
        main_layout.addWidget(self.value_label)

        central_widget.setLayout(main_layout)

        # Сигнал valueChanged -> слот on_slider_change
        self.volume_slider.valueChanged.connect(self.on_slider_change)

        self.statusBar().showMessage("Готово", 3000)

    def on_slider_change(self, value):
        """Слот: вызывается при каждом изменении положения слайдера.

        :param value: новое значение слайдера (int)
        """
        try:
            if not (VOLUME_MIN <= value <= VOLUME_MAX):
                raise ValueError(f"Значение {value} вне диапазона "
                                 f"{VOLUME_MIN}-{VOLUME_MAX}")

            self.value_label.setText(f"Текущее значение: {value}")
            self.statusBar().showMessage(f"Громкость: {value}%")
        except (ValueError, TypeError) as error:
            self.value_label.setText("Ошибка значения")
            self.statusBar().showMessage(str(error), 5000)
            print(f"[ERROR] {error}", file=sys.stderr)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
