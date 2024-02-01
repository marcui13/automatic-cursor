import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer
import pyautogui

class CursorControl(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Cursor Automático')
        self.setGeometry(100, 100, 300, 100)

        self.label = QLabel('Activar/Desactivar Modo Cursor Automático (Ctrl + M)', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(10, 10, 280, 30)

        self.cursorModeActive = False
        self.direction = (1, 1)  # Inicializar la dirección del movimiento

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_M and event.modifiers() == Qt.ControlModifier:
            self.toggleCursorMode()

    def toggleCursorMode(self):
        if not self.cursorModeActive:
            self.cursorModeActive = True
            self.cursorInterval = pyautogui.PAUSE  # Guardar el intervalo original
            pyautogui.PAUSE = 0.01  # Establecer un intervalo pequeño para mover el cursor más rápido
            self.timer = QTimer()
            self.timer.timeout.connect(self.moveCursor)
            self.timer.start(10)  # Cada 10 milisegundos
        else:
            self.cursorModeActive = False
            pyautogui.PAUSE = self.cursorInterval  # Restaurar el intervalo original
            self.timer.stop()

    def moveCursor(self):
        width, height = pyautogui.size()
        x, y = pyautogui.position()

        speed = 5  # Velocidad de movimiento

        # Cambiar la dirección si se llega a los límites de la pantalla
        if x <= 10 or x >= width - 10:
            self.direction = (-self.direction[0], self.direction[1])
        if y <= 10 or y >= height - 10:
            self.direction = (self.direction[0], -self.direction[1])

        # Mover el cursor en la dirección actual
        pyautogui.moveRel(self.direction[0] * speed, self.direction[1] * speed)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CursorControl()
    ex.show()
    sys.exit(app.exec_())
