class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, valor):
        """Agrega un elemento a la pila."""
        self.elementos.append(valor)

    def desapilar(self):
        """Elimina y devuelve el elemento en la cima de la pila."""
        if not self.esta_vacia():
            return self.elementos.pop()
        return None  # La pila está vacía

    def cima(self):
        """Devuelve el elemento en la cima sin eliminarlo."""
        if not self.esta_vacia():
            return self.elementos[-1]
        return None  # La pila está vacía

    def esta_vacia(self):
        """Devuelve True si la pila está vacía."""
        return len(self.elementos) == 0

    def obtener_pila(self):
        """Devuelve una lista con los elementos de la pila (desde el fondo hasta la cima)."""
        return self.elementos

#  ---------- UI ------------

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QInputDialog, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt


class VentanaPilas(QMainWindow):
    def __init__(self, menu_principal):
        super().__init__()
        self.setWindowTitle("Operaciones con Pilas")
        self.setGeometry(150, 150, 400, 400)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.menu_principal = menu_principal
        self.pila = Pila()  # Inicializar la pila

        # Layout principal
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Encabezado
        encabezado = QLabel("Operaciones con Pilas")
        encabezado.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(encabezado)

        # Tabla para mostrar la pila
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(1)  # Solo una columna para los valores
        self.tabla.setHorizontalHeaderLabels(["Valor"])
        self.tabla.setEditTriggers(QTableWidget.NoEditTriggers)  # Tabla de solo lectura
        layout.addWidget(self.tabla)

        # Actualizar la tabla con datos iniciales
        self.actualizar_tabla()

        # Botones
        botones = ["Apilar", "Desapilar", "Ver Cima", "Regresar"]
        for boton_texto in botones:
            boton = QPushButton(boton_texto)
            boton.clicked.connect(lambda checked, opt=boton_texto: self.boton_click(opt))
            layout.addWidget(boton)

        self.setCentralWidget(central_widget)

    def actualizar_tabla(self):
        """Actualiza la tabla con los elementos de la pila."""
        elementos = self.pila.obtener_pila()
        self.tabla.setRowCount(len(elementos))  # Configurar filas según la pila
        for i, valor in enumerate(reversed(elementos)):  # Mostrar desde la cima hasta el fondo
            self.tabla.setItem(i, 0, QTableWidgetItem(str(valor)))

    def boton_click(self, opcion):
        if opcion == "Apilar":
            self.apilar_elemento()
        elif opcion == "Desapilar":
            self.desapilar_elemento()
        elif opcion == "Ver Cima":
            self.ver_cima()
        elif opcion == "Regresar":
            self.close()

    def apilar_elemento(self):
        """Agrega un nuevo elemento a la pila."""
        elemento, ok = QInputDialog.getText(self, "Apilar Elemento", "Ingrese un valor para apilar:")
        if ok and elemento:
            self.pila.apilar(elemento)
            self.actualizar_tabla()
            QMessageBox.information(self, "Elemento Apilado", f"Elemento '{elemento}' apilado.")

    def desapilar_elemento(self):
        """Elimina el elemento en la cima de la pila."""
        elemento = self.pila.desapilar()
        if elemento is not None:
            self.actualizar_tabla()
            QMessageBox.information(self, "Elemento Desapilado", f"Elemento '{elemento}' desapilado.")
        else:
            QMessageBox.warning(self, "Error", "La pila está vacía.")

    def ver_cima(self):
        """Muestra el elemento en la cima de la pila."""
        elemento = self.pila.cima()
        if elemento is not None:
            QMessageBox.information(self, "Cima de la Pila", f"El elemento en la cima es '{elemento}'.")
        else:
            QMessageBox.warning(self, "Error", "La pila está vacía.")
