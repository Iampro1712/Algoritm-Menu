class NodoCircular:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None  # Referencia al siguiente nodo


class ListaCircular:
    def __init__(self):
        self.cabeza = None  # Nodo inicial

    def agregar(self, valor):
        nuevo_nodo = NodoCircular(valor)
        if not self.cabeza:  # Si la lista está vacía
            self.cabeza = nuevo_nodo
            self.cabeza.siguiente = self.cabeza  # Enlace circular
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:  # Encontrar el último nodo
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza  # Enlace circular

    def eliminar_por_indice(self, indice):
        if not self.cabeza:  # Lista vacía
            return False
        if indice == 0:  # Eliminar la cabeza
            if self.cabeza.siguiente == self.cabeza:  # Solo un elemento
                self.cabeza = None
            else:
                actual = self.cabeza
                while actual.siguiente != self.cabeza:  # Encontrar el último nodo
                    actual = actual.siguiente
                actual.siguiente = self.cabeza.siguiente
                self.cabeza = self.cabeza.siguiente
            return True
        actual = self.cabeza
        posicion = 0
        while actual.siguiente != self.cabeza and posicion < indice - 1:
            actual = actual.siguiente
            posicion += 1
        if posicion == indice - 1 and actual.siguiente != self.cabeza:
            actual.siguiente = actual.siguiente.siguiente
            return True
        return False  # Índice fuera de rango

    def editar_por_indice(self, indice, nuevo_valor):
        actual = self.cabeza
        posicion = 0
        while actual:
            if posicion == indice:
                actual.valor = nuevo_valor
                return True
            actual = actual.siguiente
            posicion += 1
            if actual == self.cabeza:  # Evitar bucles infinitos
                break
        return False  # Índice fuera de rango

    def obtener_lista(self):
        elementos = []
        if not self.cabeza:
            return elementos
        actual = self.cabeza
        while True:
            elementos.append(actual.valor)
            actual = actual.siguiente
            if actual == self.cabeza:  # Regresó al inicio
                break
        return elementos
    
#  # ------------ UI ------------

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QInputDialog, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt


class VentanaListasCirculares(QMainWindow):
    def __init__(self, menu_principal):
        super().__init__()
        self.setWindowTitle("Operaciones con Listas Circulares")
        self.setGeometry(150, 150, 600, 400)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.menu_principal = menu_principal
        self.lista_circular = ListaCircular()  # Inicializar lista circular

        # Layout principal
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Encabezado
        encabezado = QLabel("Operaciones con Listas Circulares")
        encabezado.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(encabezado)

        # Tabla para mostrar la lista circular
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(2)  # Índice y Valor
        self.tabla.setHorizontalHeaderLabels(["Índice", "Valor"])
        self.tabla.setEditTriggers(QTableWidget.NoEditTriggers)  # Hacer la tabla de solo lectura
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
        """Actualiza la tabla con los elementos de la lista circular."""
        self.tabla.setRowCount(0)  # Limpiar la tabla
        elementos = self.lista_circular.obtener_lista()
        for i, valor in enumerate(elementos):
            self.tabla.insertRow(i)
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
        """Agrega un nuevo nodo a la lista circular."""
        elemento, ok = QInputDialog.getText(self, "Agregar Nodo", "Ingrese un valor para el nodo:")
        if ok and elemento:
            self.lista_circular.agregar(elemento)
            self.actualizar_tabla()
            QMessageBox.information(self, "Nodo Agregado", f"Nodo con valor '{elemento}' agregado.")

    def editar_elemento(self):
        """Edita un nodo de la lista circular por índice."""
        elementos = self.lista_circular.obtener_lista()
        if not elementos:
            QMessageBox.warning(self, "Error", "La lista circular está vacía.")
            return

        indices = [str(i) for i in range(len(elementos))]
        indice_seleccionado, ok = QInputDialog.getItem(self, "Editar Nodo", "Seleccione el índice del nodo a editar:", indices, 0, False)
        if ok and indice_seleccionado is not None:
            indice = int(indice_seleccionado)
            nuevo_valor, ok = QInputDialog.getText(self, "Editar Nodo", f"Ingrese el nuevo valor para el nodo en el índice {indice}:")
            if ok and nuevo_valor:
                self.lista_circular.editar_por_indice(indice, nuevo_valor)
                self.actualizar_tabla()
                QMessageBox.information(self, "Nodo Editado", f"Nodo en el índice {indice} actualizado a '{nuevo_valor}'.")

    def eliminar_elemento(self):
        """Elimina un nodo de la lista circular por índice."""
        elementos = self.lista_circular.obtener_lista()
        if not elementos:
            QMessageBox.warning(self, "Error", "La lista circular está vacía.")
            return

        indices = [str(i) for i in range(len(elementos))]
        indice_seleccionado, ok = QInputDialog.getItem(self, "Eliminar Nodo", "Seleccione el índice del nodo a eliminar:", indices, 0, False)
        if ok and indice_seleccionado is not None:
            indice = int(indice_seleccionado)
            self.lista_circular.eliminar_por_indice(indice)
            self.actualizar_tabla()
            QMessageBox.information(self, "Nodo Eliminado", f"Nodo en el índice {indice} eliminado.")

