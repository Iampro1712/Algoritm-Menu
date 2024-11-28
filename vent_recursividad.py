
class Recursividad:
    @staticmethod
    def fibonacci(n):
        """Cálculo recursivo de Fibonacci."""
        if n <= 1:  # Caso base
            return n
        return Recursividad.fibonacci(n - 1) + Recursividad.fibonacci(n - 2)

#  ---------- UI ------------

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QInputDialog, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

class VentanaFibonacci(QMainWindow):
    def __init__(self, menu_principal):
        super().__init__()
        self.setWindowTitle("Visualización de Fibonacci")
        self.setGeometry(150, 150, 400, 600)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.menu_principal = menu_principal

        # Layout principal
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Encabezado
        encabezado = QLabel("Recursividad: Fibonacci")
        encabezado.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(encabezado)

        # Tabla para mostrar los resultados
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(2)  # Dos columnas: Índice y Valor
        self.tabla.setHorizontalHeaderLabels(["n", "Fibonacci(n)"])
        self.tabla.setEditTriggers(QTableWidget.NoEditTriggers)  # Tabla de solo lectura
        layout.addWidget(self.tabla)

        # Botones
        botones = ["Calcular Fibonacci", "Regresar"]
        for boton_texto in botones:
            boton = QPushButton(boton_texto)
            boton.clicked.connect(lambda checked, opt=boton_texto: self.boton_click(opt))
            layout.addWidget(boton)

        self.setCentralWidget(central_widget)

    def actualizar_tabla(self, valores):
        """Actualiza la tabla con los valores de Fibonacci."""
        self.tabla.setRowCount(len(valores))  # Configurar filas según la cantidad de valores
        for i, valor in enumerate(valores):
            self.tabla.setItem(i, 0, QTableWidgetItem(str(i)))  # Índice
            self.tabla.setItem(i, 1, QTableWidgetItem(str(valor)))  # Valor de Fibonacci(n)
        self.tabla.resizeColumnsToContents()  # Ajustar el ancho de las columnas automáticamente

    def boton_click(self, opcion):
        if opcion == "Calcular Fibonacci":
            self.calcular_fibonacci()
        elif opcion == "Regresar":
            self.close()

    def calcular_fibonacci(self):
        """Calcula los valores de Fibonacci y los muestra en la tabla."""
        n, ok = QInputDialog.getInt(self, "Fibonacci", "Ingrese el valor de n (≥ 0):", 0, 0)
        if ok:
            valores = [Recursividad.fibonacci(i) for i in range(n + 1)]  # Calcular Fibonacci para todos los valores desde 0 hasta n
            self.actualizar_tabla(valores)  # Mostrar los valores en la tabla
            QMessageBox.information(self, "Resultado", f"Fibonacci({n}) = {valores[-1]}")
