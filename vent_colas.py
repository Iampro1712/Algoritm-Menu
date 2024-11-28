class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, valor):
        """Agrega un elemento al final de la cola."""
        self.elementos.append(valor)

    def desencolar(self):
        """Elimina y devuelve el elemento al frente de la cola."""
        if not self.esta_vacia():
            return self.elementos.pop(0)
        return None  # La cola está vacía

    def frente(self):
        """Devuelve el elemento al frente sin eliminarlo."""
        if not self.esta_vacia():
            return self.elementos[0]
        return None  # La cola está vacía

    def esta_vacia(self):
        """Devuelve True si la cola está vacía."""
        return len(self.elementos) == 0

    def obtener_cola(self):
        """Devuelve una lista con los elementos de la cola."""
        return self.elementos

#  ---------- UI ------------

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QInputDialog, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt


class VentanaColas(QMainWindow):
    def __init__(self, menu_principal):
        super().__init__()
        self.setWindowTitle("Operaciones con Colas")
        self.setGeometry(150, 150, 400, 400)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.menu_principal = menu_principal
        self.cola = Cola()  # Inicializar la cola

        # Layout principal
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Encabezado
        encabezado = QLabel("Operaciones con Colas")
        encabezado.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(encabezado)

        # Tabla para mostrar la cola
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(1)  # Solo una columna para los valores
        self.tabla.setHorizontalHeaderLabels(["Valor"])
        self.tabla.setEditTriggers(QTableWidget.NoEditTriggers)  # Tabla de solo lectura
        layout.addWidget(self.tabla)

        # Actualizar la tabla con datos iniciales
        self.actualizar_tabla()

        # Botones
        botones = ["Encolar", "Desencolar", "Ver Frente", "Regresar"]
        for boton_texto in botones:
            boton = QPushButton(boton_texto)
            boton.clicked.connect(lambda checked, opt=boton_texto: self.boton_click(opt))
            layout.addWidget(boton)

        self.setCentralWidget(central_widget)

    def actualizar_tabla(self):
        """Actualiza la tabla con los elementos de la cola."""
        elementos = self.cola.obtener_cola()
        self.tabla.setRowCount(len(elementos))  # Configurar filas según la cola
        for i, valor in enumerate(elementos):  # Mostrar desde el frente hasta el final
            self.tabla.setItem(i, 0, QTableWidgetItem(str(valor)))

    def boton_click(self, opcion):
        if opcion == "Encolar":
            self.encolar_elemento()
        elif opcion == "Desencolar":
            self.desencolar_elemento()
        elif opcion == "Ver Frente":
            self.ver_frente()
        elif opcion == "Regresar":
            self.close()

    def encolar_elemento(self):
        """Agrega un nuevo elemento a la cola."""
        elemento, ok = QInputDialog.getText(self, "Encolar Elemento", "Ingrese un valor para encolar:")
        if ok and elemento:
            self.cola.encolar(elemento)
            self.actualizar_tabla()
            QMessageBox.information(self, "Elemento Encolado", f"Elemento '{elemento}' encolado.")

    def desencolar_elemento(self):
        """Elimina el elemento al frente de la cola."""
        elemento = self.cola.desencolar()
        if elemento is not None:
            self.actualizar_tabla()
            QMessageBox.information(self, "Elemento Desencolado", f"Elemento '{elemento}' desencolado.")
        else:
            QMessageBox.warning(self, "Error", "La cola está vacía.")

    def ver_frente(self):
        """Muestra el elemento al frente de la cola."""
        elemento = self.cola.frente()
        if elemento is not None:
            QMessageBox.information(self, "Frente de la Cola", f"El elemento al frente es '{elemento}'.")
        else:
            QMessageBox.warning(self, "Error", "La cola está vacía.")
