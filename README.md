# Automatic Cursor

Este es un script de Python que crea una ventana que permite activar/desactivar un modo de movimiento automático del cursor, inspirado en el protector de pantalla del logo de DVD.

## Descripción

El script crea una ventana con un botón que al ser presionado activa o desactiva el modo de movimiento automático del cursor. Cuando el modo está activado, el cursor se moverá automáticamente en diagonal por la pantalla. Además, el cursor cambiará de dirección cuando alcance los bordes de la pantalla, imitando el comportamiento del protector de pantalla del logo de DVD.

## Funcionalidades

- Activa/desactiva el modo de movimiento automático del cursor mediante un botón o la combinación de teclas Ctrl + M.
- El cursor se mueve en diagonal por la pantalla.
- El cursor rebota contra los bordes de la pantalla para evitar salirse de ella.

## Uso

1. Ejecuta el script `main.py`.
2. Haz clic en el botón "Activar/Desactivar Modo Cursor Automático" o presiona Ctrl + M para activar/desactivar el modo de movimiento automático del cursor.

## Requisitos

- Python 3.x
- PyQt5
- pyautogui

## Instalación

1. Clona el repositorio:

git clone https://github.com/tu_usuario/automatic-cursor.git

2. Instala las dependencias:

pip install PyQt5 pyautogui

## Ejecución

python main.py

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir al proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commits (`git commit -am 'Agrega nueva característica'`).
4. Sube tus cambios (`git push origin feature/nueva-caracteristica`).
5. Abre una solicitud de extracción en GitHub.

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).
