import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer, QSize
from PyQt5.QtGui import QFont

import pyautogui

class CursorControl(QWidget):
    def __init__(self):
        super().__init__()
        self.speed = 5  # Velocidad de movimiento inicial
        self.max_speed = 165  # Velocidad máxima permitida
        self.dark_mode = True  # Modo oscuro por defecto
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Automatic Cursor')
        self.setGeometry(100, 100, 500, 200)

        # Aplicar estilo de fondo oscuro por defecto
        self.setStyleSheet("background-color: #222; color: #fff;")

        # Etiqueta para mostrar estado de modo de cursor y coordenadas del cursor
        self.status_label = QLabel(self)
        self.status_label.setText('Modo Cursor Automático: Inactivo\nCoordenadas del cursor: (0, 0)')
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setGeometry(10, 10, 480, 50)
        self.status_label.setFont(QFont('Arial', 10))

        # Etiqueta para mostrar velocidad del cursor
        self.speed_label = QLabel(self)
        self.speed_label.setText('Velocidad del cursor: {}'.format(self.speed))
        self.speed_label.setAlignment(Qt.AlignCenter)
        self.speed_label.setGeometry(10, 70, 480, 50)
        self.speed_label.setFont(QFont('Arial', 10))

        self.cursorModeActive = False
        self.direction = (1, 1)  # Inicializar la dirección del movimiento

        pyautogui.FAILSAFE = False  # Desactivar la función fail-safe

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_M and event.modifiers() == Qt.ControlModifier:
            self.toggleCursorMode()
        elif event.key() == Qt.Key_Up:
            self.speed = min(self.speed + 1, self.max_speed)  # Aumentar velocidad con límite superior de max_speed
            self.updateSpeedLabel()
        elif event.key() == Qt.Key_Down:
            self.speed = max(1, self.speed - 1)  # Disminuir velocidad con límite inferior de 1
            self.updateSpeedLabel()
        elif event.key() == Qt.Key_T and event.modifiers() == Qt.ControlModifier:
            self.toggleTheme()  # Cambiar entre modo oscuro y claro al presionar Ctrl + T

    def toggleCursorMode(self):
        if not self.cursorModeActive:
            self.cursorModeActive = True
            self.cursorInterval = pyautogui.PAUSE  # Guardar el intervalo original
            pyautogui.PAUSE = 0.01  # Establecer un intervalo pequeño para mover el cursor más rápido
            self.timer = QTimer()
            self.timer.timeout.connect(self.moveCursor)
            self.timer.start(10)  # Cada 10 milisegundos
            self.status_label.setText('Modo Cursor Automático: Activo\nCoordenadas del cursor: (0, 0)')
        else:
            self.cursorModeActive = False
            pyautogui.PAUSE = self.cursorInterval  # Restaurar el intervalo original
            self.timer.stop()
            self.status_label.setText('Modo Cursor Automático: Inactivo\nCoordenadas del cursor: (0, 0)')

    def moveCursor(self):
        width, height = pyautogui.size()
        x, y = pyautogui.position()

        # Cambiar la dirección si se llega a los límites de la pantalla
        if x <= 10 or x >= width - 10:
            self.direction = (-self.direction[0], self.direction[1])
        if y <= 10 or y >= height - 10:
            self.direction = (self.direction[0], -self.direction[1])

        # Mover el cursor en la dirección actual con la velocidad actual
        pyautogui.moveRel(self.direction[0] * self.speed, self.direction[1] * self.speed)

        # Actualizar etiqueta de coordenadas del cursor
        self.status_label.setText('Modo Cursor Automático: Activo\nCoordenadas del cursor: ({}, {})'.format(x, y))

    def updateSpeedLabel(self):
        self.speed_label.setText('Velocidad del cursor: {}'.format(self.speed))

    def toggleTheme(self):
        # Cambiar entre modo oscuro y claro
        if self.dark_mode:
            self.setStyleSheet("background-color: #fff; color: #000;")
            self.dark_mode = False
        else:
            self.setStyleSheet("background-color: #222; color: #fff;")
            self.dark_mode = True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CursorControl()
    ex.show()
    sys.exit(app.exec_())
