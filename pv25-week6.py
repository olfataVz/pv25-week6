import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QSlider, QLabel
from PyQt6 import uic
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Slider.ui", self)

        self.fontSizeSlider: QSlider = self.findChild(QSlider, "fontSizeSlider")
        self.bgColorSlider: QSlider = self.findChild(QSlider, "bgColorSlider")
        self.fontColorSlider: QSlider = self.findChild(QSlider, "fontColorSlider")
        self.label: QLabel = self.findChild(QLabel, "labelNIM")

        self.fontSizeSlider.setRange(20, 60)
        self.bgColorSlider.setRange(0, 255)
        self.fontColorSlider.setRange(0, 255)

        self.fontSizeSlider.valueChanged.connect(self.update_display)
        self.bgColorSlider.valueChanged.connect(self.update_display)
        self.fontColorSlider.valueChanged.connect(self.update_display)
        
        self.update_display()

    def update_display(self):
        font_size = self.fontSizeSlider.value()
        bg_value = self.bgColorSlider.value()
        font_value = self.fontColorSlider.value()

        bg_color = f'rgb({bg_value}, {bg_value}, {bg_value})'
        font_color = f'rgb({font_value}, {font_value}, {font_value})'

        style = f"""
            font-size: {font_size}pt;
            background-color: {bg_color};
            color: {font_color};
        """
        self.label.setStyleSheet(style)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("F1D022057 - Lalu Olfata Vedora Zurji")
    window.show()
    sys.exit(app.exec())
