from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtCore import Qt
import webbrowser


class VentanaGitHub(QMainWindow):
    def __init__(self, menu_principal):
        super().__init__()
        self.setWindowTitle("Repositorio de GitHub")
        self.setGeometry(150, 150, 500, 300)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.menu_principal = menu_principal

        # Layout principal
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Encabezado
        encabezado = QLabel("Redirección al Repositorio de GitHub")
        encabezado.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #2c3e50;
            text-align: center;
            margin-bottom: 20px;
        """)
        encabezado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(encabezado)

        # Descripción
        descripcion = QLabel("Haz clic en el botón para visitar el repositorio del proyecto en GitHub.")
        descripcion.setStyleSheet("""
            font-size: 16px;
            color: #34495e;
            text-align: center;
            margin-bottom: 20px;
            padding: 0 10px;
        """)
        descripcion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(descripcion)

        # Botón para redirigir al repositorio de GitHub
        boton_github = QPushButton("Abrir Repositorio en GitHub")
        boton_github.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
            color: white;
            background-color: #1abc9c;
            border-radius: 10px;
            padding: 10px 20px;
            margin: 10px 0;
        """)
        boton_github.setCursor(Qt.CursorShape.PointingHandCursor)
        boton_github.clicked.connect(self.abrir_github)
        layout.addWidget(boton_github)

        # Botón para regresar al menú principal
        boton_regresar = QPushButton("Regresar")
        boton_regresar.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
            color: white;
            background-color: #95a5a6;
            border-radius: 10px;
            padding: 10px 20px;
            margin: 10px 0;
        """)
        boton_regresar.setCursor(Qt.CursorShape.PointingHandCursor)
        boton_regresar.clicked.connect(self.cerrar_ventana)
        layout.addWidget(boton_regresar)

        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Alinear elementos al inicio del layout
        self.setCentralWidget(central_widget)

    def abrir_github(self):
        """Redirige al navegador con el enlace del repositorio de GitHub."""
        url = "https://github.com/Iampro1712/Algoritm-Menu"  # Cambia esta URL a la de tu repo
        webbrowser.open(url)

    def cerrar_ventana(self):
        """Cierra la ventana y regresa al menú principal."""
        self.close()
