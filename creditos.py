from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class VentanaIntegrantes(QMainWindow):
    def __init__(self, menu_principal):
        super().__init__()
        self.setWindowTitle("Integrantes del Proyecto")
        self.setGeometry(150, 150, 500, 500)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.menu_principal = menu_principal

        # Layout principal
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Encabezado
        encabezado = QLabel("Integrantes del Proyecto")
        encabezado.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #2c3e50;
            text-align: center;
            margin-bottom: 20px;
        """)
        encabezado.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget(encabezado)

        # Lista de integrantes
        integrantes = [
            {"nombre": "Gutiérrez Espinoza María Natasha", "carnet": "2023-0647I", "whatsapp": "+50557555104"},
            {"nombre": "Espinoza López María Esther", "carnet": "2023-0726I", "whatsapp": "+50582567090"},
            {"nombre": "Ruiz Sánchez Gabriela Vanessa", "carnet": "2023-0629I", "whatsapp": "+50581554349"},
            {"nombre": "Bejarano Carrión Eduard Antonio", "carnet": "2023-0626I", "whatsapp": "+50582338298"}
        ]

        for integrante in integrantes:
            # Layout horizontal para el integrante
            integrante_layout = QHBoxLayout()

            # Etiqueta con nombre y carnet
            etiqueta = QLabel(f"Nombre: {integrante['nombre']} | Carnet: {integrante['carnet']}")
            etiqueta.setStyleSheet("""
                font-size: 16px;
                color: #34495e;
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                padding: 10px;
                background-color: #ecf0f1;
                margin-right: 10px;
            """)
            etiqueta.setAlignment(Qt.AlignmentFlag.AlignTop)
            integrante_layout.addWidget(etiqueta)

            # Botón de WhatsApp
            boton_whatsapp = QPushButton()
            boton_whatsapp.setIcon(QIcon("whatsapp.jpg"))
            boton_whatsapp.setIconSize(QSize(40, 40))
            boton_whatsapp.setStyleSheet("border: none;")  # Sin borde
            boton_whatsapp.setCursor(Qt.CursorShape.PointingHandCursor)
            boton_whatsapp.clicked.connect(lambda _, numero=integrante['whatsapp']: self.abrir_whatsapp(numero))
            integrante_layout.addWidget(boton_whatsapp)

            layout.addLayout(integrante_layout)

        # Botón para regresar al menú principal
        boton_regresar = QPushButton("Regresar")
        boton_regresar.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
            color: white;
            background-color: #3498db;
            border-radius: 10px;
            padding: 10px 20px;
        """)
        boton_regresar.setCursor(Qt.CursorShape.PointingHandCursor)
        boton_regresar.clicked.connect(self.cerrar_ventana)
        layout.addWidget(boton_regresar)

        layout.setAlignment(Qt.AlignmentFlag.AlignTop)  # Alinear elementos al inicio del layout
        self.setCentralWidget(central_widget)

    def abrir_whatsapp(self, numero):
        """Abre el enlace de WhatsApp con el número especificado."""
        import webbrowser
        url = f"https://wa.me/{numero.replace('+', '')}"  # Crear enlace de WhatsApp
        webbrowser.open(url)

    def cerrar_ventana(self):
        """Cierra la ventana y regresa al menú principal."""
        self.close()
