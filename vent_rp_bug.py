from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtCore import Qt
import webbrowser


class VentanaReportarBug(QMainWindow):
    def __init__(self, menu_principal):
        super().__init__()
        self.setWindowTitle("Reportar Bug")
        self.setGeometry(150, 150, 500, 300)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.menu_principal = menu_principal

        # Layout principal
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Encabezado
        encabezado = QLabel("Reportar un Bug")
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
        descripcion = QLabel("¿Has encontrado un error? Ayúdanos a mejorarlo.\nHaz clic en el botón para reportar un bug.")
        descripcion.setStyleSheet("""
            font-size: 16px;
            color: #34495e;
            text-align: center;
            margin-bottom: 20px;
            padding: 0 10px;
        """)
        descripcion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(descripcion)

        # Botón para redirigir al correo o formulario
        boton_reportar = QPushButton("Reportar Bug")
        boton_reportar.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
            color: white;
            background-color: #e74c3c;
            border-radius: 10px;
            padding: 10px 20px;
            margin: 10px 0;
        """)
        boton_reportar.setCursor(Qt.CursorShape.PointingHandCursor)
        boton_reportar.clicked.connect(self.reportar_bug)
        layout.addWidget(boton_reportar)

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

        layout.setAlignment(Qt.AlignmentFlag.AlignTop)  # Alinear elementos al inicio del layout
        self.setCentralWidget(central_widget)

    def reportar_bug(self):
        """Redirige a un correo prellenado para reportar un bug."""
        email = "eduardpro17@gmail.com"
        asunto = "Reporte de Bug"
        cuerpo = "Por favor describe el bug aquí:\n\n"
        url = f"mailto:{email}?subject={asunto}&body={cuerpo}"
        webbrowser.open(url)

    def cerrar_ventana(self):
        """Cierra la ventana y regresa al menú principal."""
        self.close()
