from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QInputDialog, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

class VentanaListas(QMainWindow):
    def __init__(self, menu_principal):
        super().__init__()
        self.setWindowTitle("Operaciones con Listas")
        self.setGeometry(150, 150, 400, 400)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.menu_principal = menu_principal
        self.lista = menu_principal.lista  # Compartir la lista con el menú principal

        # Layout principal
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Encabezado
        encabezado = QLabel("Operaciones con Listas")
        encabezado.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(encabezado)

        # Tabla para mostrar la lista
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(2)  # Índice y Valor
        self.tabla.setHorizontalHeaderLabels(["Índice", "Valor"])
        self.tabla.setEditTriggers(QTableWidget.NoEditTriggers)  # Tabla de solo lectura
        layout.addWidget(self.tabla)

        # Actualizar la tabla con datos iniciales
        self.actualizar_tabla()

        # Botones
        botones = ["Agregar", "Editar", "Eliminar", "Regresar"]
        for boton_texto in botones:
            boton = QPushButton(boton_texto)
            boton.clicked.connect(lambda checked, opt=boton_texto: self.boton_click(opt))
            layout.addWidget(boton)

        self.setCentralWidget(central_widget)

    def actualizar_tabla(self):
        """Actualiza la tabla con los elementos de la lista."""
        self.tabla.setRowCount(len(self.lista))
        for i, valor in enumerate(self.lista):
            self.tabla.setItem(i, 0, QTableWidgetItem(str(i)))  # Índice
            self.tabla.setItem(i, 1, QTableWidgetItem(str(valor)))  # Valor

    def boton_click(self, opcion):
        if opcion == "Agregar":
            self.agregar_elemento()
        elif opcion == "Editar":
            self.editar_elemento()
        elif opcion == "Eliminar":
            self.eliminar_elemento()
        elif opcion == "Regresar":
            self.close()

    def agregar_elemento(self):
        """Agrega un nuevo elemento a la lista."""
        elemento, ok = QInputDialog.getText(self, "Agregar Elemento", "Ingrese un elemento:")
        if ok and elemento:
            self.lista.append(elemento)
            self.actualizar_tabla()
            QMessageBox.information(self, "Elemento Agregado", f"Elemento '{elemento}' agregado.")

    def editar_elemento(self):
        """Edita un elemento existente en la lista."""
        if not self.lista:
            QMessageBox.warning(self, "Error", "La lista está vacía.")
            return
        item, ok = QInputDialog.getItem(self, "Editar Elemento", "Seleccione un elemento:", self.lista, 0, False)
        if ok and item:
            nuevo_elemento, ok = QInputDialog.getText(self, "Editar Elemento", f"Modificar '{item}' a:")
            if ok and nuevo_elemento:
                index = self.lista.index(item)
                self.lista[index] = nuevo_elemento
                self.actualizar_tabla()
                QMessageBox.information(self, "Elemento Editado", f"Elemento '{item}' cambiado a '{nuevo_elemento}'.")

    def eliminar_elemento(self):
        """Elimina un elemento por índice de la lista."""
        if not self.lista:
            QMessageBox.warning(self, "Error", "La lista está vacía.")
            return

        # Mostrar un cuadro de diálogo para que el usuario seleccione el índice
        indices = [str(i) for i in range(len(self.lista))]
        indice_seleccionado, ok = QInputDialog.getItem(self, "Eliminar Elemento", "Seleccione el índice del elemento a eliminar:", indices, 0, False)
        if ok and indice_seleccionado is not None:
            indice = int(indice_seleccionado)
            elemento_eliminado = self.lista.pop(indice)  # Elimina por índice
            self.actualizar_tabla()
            QMessageBox.information(self, "Elemento Eliminado", f"Elemento '{elemento_eliminado}' en el índice {indice} ha sido eliminado.")
