import os
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QMessageBox
from PyQt5.QtCore import Qt


class VentanaAbrirAlgoritmo(QMainWindow):
    def __init__(self, menu_principal):
        super().__init__()
        self.setWindowTitle("Archivos de Algoritmos")
        self.setGeometry(150, 150, 400, 200)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.menu_principal = menu_principal

        # Layout principal
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Encabezado
        encabezado = QLabel("Documentos de Algoritmos")
        encabezado.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(encabezado)

        # Botón para abrir el archivo Word
        boton_abrir = QPushButton("Abrir Documento")
        boton_abrir.clicked.connect(self.abrir_archivo_word)
        layout.addWidget(boton_abrir)

        # Botón para regresar al menú principal
        boton_regresar = QPushButton("Regresar")
        boton_regresar.clicked.connect(self.cerrar_ventana)
        layout.addWidget(boton_regresar)

        self.setCentralWidget(central_widget)

    def abrir_archivo_word(self):
        """Abre un archivo Word al hacer clic en el botón."""
        ruta_archivo = "Algoritmizacion_y_Esrtuctura_de_Datos-Documento.docx"  # Cambia a la ruta de tu archivo
        if os.path.exists(ruta_archivo):
            os.startfile(ruta_archivo)  # Abre el archivo con el programa predeterminado
            QMessageBox.information(self, "Archivo Abierto", f"Se ha abierto el archivo:\n{ruta_archivo}")
        else:
            QMessageBox.warning(self, "Error", f"No se encontró el archivo:\n{ruta_archivo}")

    def cerrar_ventana(self):
        """Cierra la ventana y regresa al menú principal."""
        self.close()
