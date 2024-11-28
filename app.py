import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction
import os
from vent_algo import VentanaAbrirAlgoritmo
from vent_array import VentanaArreglos
from vent_listas import VentanaListas
from vent_listas_enlz import VentanaListasEnlazadas
from vent_listas_dobles import VentanaListasDobles
from vemt_listas_circ import VentanaListasCirculares
from vent_pilas import VentanaPilas
from vent_colas import VentanaColas
from vent_recursividad import VentanaFibonacci
from vent_arboles import VentanaArbol
from vent_grafos import VentanaGrafo
from creditos import VentanaIntegrantes
from vent_github import VentanaGitHub
from vent_rp_bug import VentanaReportarBug


class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Curso de AED")
        self.setGeometry(100, 100, 600, 600)  # Tamaño ampliado para mejor visualización
        self.arreglo = []  # Inicializar el arreglo vacío
        self.lista = []  # Inicializar la lista vacía

        # Configuración del layout principal
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)  # Alinear elementos al inicio

        # Encabezado
        self.encabezado = QLabel("Bienvenido al Curso de AED")
        self.estilo_encabezado_claro = """
            font-size: 28px;
            font-weight: bold;
            color: #2c3e50;
            text-align: center;
            margin-bottom: 20px;
        """
        self.estilo_encabezado_oscuro = """
            font-size: 28px;
            font-weight: bold;
            color: white;
            text-align: center;
            margin-bottom: 20px;
        """
        self.encabezado.setStyleSheet(self.estilo_encabezado_claro)
        self.encabezado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.encabezado)

        # Crear botones para el menú
        opciones = [
            "Algoritmos",
            "Arreglos",
            "Listas",
            "Listas Enlazadas",
            "Listas Dobles",
            "Listas Circulares",
            "Pilas",
            "Colas",
            "Recursividad",
            "Arboles",
            "Grafos",
            "Integrantes",
            "Repositorio de GitHub",
            "Reportar Bug",
            "Salir"
        ]

        for opcion in opciones:
            self.boton = QPushButton(opcion)
            self.boton.setFixedHeight(50)  # Altura fija para uniformidad
            self.boton.setStyleSheet("""
                font-size: 18px;
                font-weight: bold;
                color: white;
                background-color: #3498db;
                border-radius: 10px;
                margin: 5px;
                padding: 10px;
            """)
            self.boton.setCursor(Qt.CursorShape.PointingHandCursor)
            self.boton.clicked.connect(lambda checked, opt=opcion: self.boton_click(opt))
            layout.addWidget(self.boton)

        self.setCentralWidget(central_widget)

         # Barra de menú
        menu_bar = self.menuBar()

        # Menú de Tema
        tema_menu = menu_bar.addMenu("Tema")

        # Opción de Tema Claro
        tema_claro_action = QAction("Claro", self)
        tema_claro_action.triggered.connect(self.aplicar_tema_claro)
        tema_menu.addAction(tema_claro_action)

        # Opción de Tema Oscuro
        tema_oscuro_action = QAction("Oscuro", self)
        tema_oscuro_action.triggered.connect(self.aplicar_tema_oscuro)
        tema_menu.addAction(tema_oscuro_action)

    def aplicar_tema_claro(self):
        """Aplica el tema claro."""
        self.setStyleSheet("")  # Tema predeterminado
        self.encabezado.setStyleSheet(self.estilo_encabezado_claro)  # Restaurar estilo del QLabel

    def aplicar_tema_oscuro(self):
        """Aplica el tema oscuro."""
        self.setStyleSheet("""
            QMainWindow { background-color: #2c3e50; }
            QPushButton {
                background-color: #34495e;
                color: white;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #1abc9c;
            }
            QPushButton:pressed {
                background-color: #16a085;
            }
        """)
        self.encabezado.setStyleSheet(self.estilo_encabezado_oscuro)

    def boton_click(self, opcion):
        if opcion == "Salir":
            self.close()
        elif opcion == "Algoritmos":
            self.abrir_ventana_algoritmos()
        elif opcion == "Arreglos":
            self.abrir_ventana_arreglos()
        elif opcion == "Listas":
            self.abrir_ventana_listas()
        elif opcion == "Listas Enlazadas":
            self.abrir_ventana_listas_enlazadas()
        elif opcion == "Listas Dobles":
            self.abrir_ventana_listas_dobles()
        elif opcion == "Listas Circulares":
            self.abrir_ventana_listas_circulares()
        elif opcion == "Pilas":
            self.abrir_ventana_pilas()
        elif opcion == "Colas":
            self.abrir_ventana_colas()
        elif opcion == "Recursividad":
            self.abrir_ventana_recursividad()
        elif opcion == "Arboles":
            self.abrir_ventana_arboles()
        elif opcion == "Grafos":
            self.abrir_ventana_grafos()
        elif opcion == "Integrantes":
            self.abrir_ventana_integrantes()
        elif opcion == "Repositorio de GitHub":
            self.abrir_ventana_github()
        elif opcion == "Reportar Bug":
            self.abrir_ventana_reportar_bug()
        else:
            print(f"Has seleccionado: {opcion}")

    # Métodos de apertura para las ventanas
    def abrir_ventana_algoritmos(self):
        self.ventana_abrir_algoritmo = VentanaAbrirAlgoritmo(self)
        self.ventana_abrir_algoritmo.show()

    def abrir_ventana_arreglos(self):
        self.ventana_arreglos = VentanaArreglos(self)
        self.ventana_arreglos.show()

    def abrir_ventana_listas(self):
        self.ventana_listas = VentanaListas(self)
        self.ventana_listas.show()
    
    def abrir_ventana_listas_enlazadas(self):
        self.ventana_listas_enlazadas = VentanaListasEnlazadas(self)
        self.ventana_listas_enlazadas.show()

    def abrir_ventana_listas_dobles(self):
        self.ventana_listas_dobles = VentanaListasDobles(self)
        self.ventana_listas_dobles.show()

    def abrir_ventana_listas_circulares(self):
        self.ventana_listas_circulares = VentanaListasCirculares(self)
        self.ventana_listas_circulares.show()

    def abrir_ventana_pilas(self):
        self.ventana_pilas = VentanaPilas(self)
        self.ventana_pilas.show()

    def abrir_ventana_colas(self):
        self.ventana_colas = VentanaColas(self)
        self.ventana_colas.show()

    def abrir_ventana_recursividad(self):
        self.ventana_recursividad = VentanaFibonacci(self)
        self.ventana_recursividad.show()

    def abrir_ventana_arboles(self):
        self.ventana_arboles = VentanaArbol(self)
        self.ventana_arboles.show()

    def abrir_ventana_grafos(self):
        self.ventana_grafos = VentanaGrafo(self)
        self.ventana_grafos.show()

    def abrir_ventana_integrantes(self):
        self.ventana_integrantes = VentanaIntegrantes(self)
        self.ventana_integrantes.show()

    def abrir_ventana_github(self):
        self.ventana_github = VentanaGitHub(self)
        self.ventana_github.show()

    def abrir_ventana_reportar_bug(self):
        self.ventana_reportar_bug = VentanaReportarBug(self)
        self.ventana_reportar_bug.show()


# Configuración de la aplicación
if __name__ == "__main__":
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    app = QApplication(sys.argv)
    window = MenuWindow()
    window.show()
    sys.exit(app.exec_())
