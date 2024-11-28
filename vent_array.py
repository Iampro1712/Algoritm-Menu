from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QInputDialog, QMessageBox
from PyQt5.QtCore import Qt


class VentanaArreglos(QMainWindow):
    def __init__(self, menu_principal):
        super().__init__()
        self.setWindowTitle("Operaciones con Arreglos")
        self.setGeometry(150, 150, 400, 300)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.menu_principal = menu_principal
        self.arreglo = menu_principal.arreglo

        # Layout principal
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignCenter)

        # Encabezado
        encabezado = QLabel("Operaciones con Arreglos")
        encabezado.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(encabezado)

        # Botones
        opciones = [
            "Agregar",
            "Eliminar",
            "Leer el arreglo",
            "Eliminar el arreglo",
            "Regresar al menú principal"
        ]
        for opcion in opciones:
            boton = QPushButton(opcion)
            boton.setFixedSize(200, 40)
            boton.clicked.connect(lambda checked, opt=opcion: self.boton_click(opt))
            layout.addWidget(boton)

        self.setCentralWidget(central_widget)

    def boton_click(self, opcion):
        if opcion == "Agregar":
            self.agregar_elemento()
        elif opcion == "Eliminar":
            self.eliminar_elemento()
        elif opcion == "Leer el arreglo":
            self.leer_arreglo()
        elif opcion == "Eliminar el arreglo":
            self.eliminar_arreglo()
        elif opcion == "Regresar al menú principal":
            self.close()

    def agregar_elemento(self):
        elemento, ok = QInputDialog.getText(self, "Agregar Elemento", "Ingrese un elemento:")
        if ok and elemento:
            self.arreglo.append(elemento)
            QMessageBox.information(self, "Elemento Agregado", f"Elemento '{elemento}' agregado.")
            print(f"Elemento '{elemento}' agregado. Arreglo actual: {self.arreglo}")

    def eliminar_elemento(self):
        if not self.arreglo:
            QMessageBox.warning(self, "Error", "El arreglo está vacío. No hay nada que eliminar.")
            return
        elemento, ok = QInputDialog.getText(self, "Eliminar Elemento", "Ingrese el elemento a eliminar:")
        if ok and elemento:
            if elemento in self.arreglo:
                self.arreglo.remove(elemento)
                QMessageBox.information(self, "Elemento Eliminado", f"Elemento '{elemento}' eliminado.")
                print(f"Elemento '{elemento}' eliminado. Arreglo actual: {self.arreglo}")
            else:
                QMessageBox.warning(self, "Error", f"El elemento '{elemento}' no se encuentra en el arreglo.")

    def leer_arreglo(self):
        if not self.arreglo:
            QMessageBox.information(self, "Arreglo Vacío", "El arreglo está vacío.")
        else:
            QMessageBox.information(self, "Contenido del Arreglo", f"Arreglo actual: {', '.join(self.arreglo)}")
        print(f"Arreglo actual: {self.arreglo}")

    def eliminar_arreglo(self):
        self.arreglo.clear()
        QMessageBox.information(self, "Arreglo Eliminado", "El arreglo ha sido eliminado. Ahora está vacío.")
        print("El arreglo ha sido eliminado. Ahora está vacío.")
