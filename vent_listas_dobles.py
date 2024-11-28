class NodoDoble:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None  # Puntero al siguiente nodo
        self.anterior = None  # Puntero al nodo anterior


class ListaDoble:
    def __init__(self):
        self.cabeza = None  # Inicio de la lista
        self.cola = None    # Final de la lista

    def agregar(self, valor):
        nuevo_nodo = NodoDoble(valor)
        if not self.cabeza:  # Si la lista está vacía
            self.cabeza = self.cola = nuevo_nodo
        else:  # Agregar al final
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

    def eliminar_por_indice(self, indice):
        if not self.cabeza:
            return False  # Lista vacía
        actual = self.cabeza
        posicion = 0
        while actual:
            if posicion == indice:
                if actual.anterior:  # Si no es el primer nodo
                    actual.anterior.siguiente = actual.siguiente
                else:  # Si es el primer nodo
                    self.cabeza = actual.siguiente
                if actual.siguiente:  # Si no es el último nodo
                    actual.siguiente.anterior = actual.anterior
                else:  # Si es el último nodo
                    self.cola = actual.anterior
                return True
            actual = actual.siguiente
            posicion += 1
        return False  # Índice fuera de rango

    def editar_por_indice(self, indice, nuevo_valor):
        actual = self.cabeza
        posicion = 0
        while actual:
            if posicion == indice:
                actual.valor = nuevo_valor  # Cambiar el valor del nodo
                return True
            actual = actual.siguiente
            posicion += 1
        return False  # Índice fuera de rango

    def obtener_lista(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        return elementos

    def obtener_lista_reversa(self):
        elementos = []
        actual = self.cola
        while actual:
            elementos.append(actual.valor)
            actual = actual.anterior
        return elementos
    
 # ------------ UI ------------

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QInputDialog, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

class VentanaListasDobles(QMainWindow):
    def __init__(self, menu_principal):
        super().__init__()
        self.setWindowTitle("Operaciones con Listas Dobles Enlazadas")
        self.setGeometry(150, 150, 600, 400)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.menu_principal = menu_principal
        self.lista_doble = ListaDoble()  # Inicializar lista doble enlazada

        # Layout principal
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Encabezado
        encabezado = QLabel("Operaciones con Listas Dobles Enlazadas")
        encabezado.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(encabezado)

        # Tabla para mostrar la lista doble enlazada
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)  # Índice, Valor, Anterior, Siguiente
        self.tabla.setHorizontalHeaderLabels(["Índice", "Valor", "Anterior", "Siguiente"])
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
        """Actualiza la tabla con los elementos de la lista doble enlazada."""
        self.tabla.setRowCount(0)  # Limpiar la tabla
        actual = self.lista_doble.cabeza
        indice = 0
        while actual:
            self.tabla.insertRow(indice)
            self.tabla.setItem(indice, 0, QTableWidgetItem(str(indice)))  # Índice
            self.tabla.setItem(indice, 1, QTableWidgetItem(str(actual.valor)))  # Valor
            self.tabla.setItem(indice, 2, QTableWidgetItem(str(actual.anterior.valor) if actual.anterior else "None"))  # Anterior
            self.tabla.setItem(indice, 3, QTableWidgetItem(str(actual.siguiente.valor) if actual.siguiente else "None"))  # Siguiente
            actual = actual.siguiente
            indice += 1

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
        """Agrega un nuevo nodo a la lista doble enlazada."""
        elemento, ok = QInputDialog.getText(self, "Agregar Nodo", "Ingrese un valor para el nodo:")
        if ok and elemento:
            self.lista_doble.agregar(elemento)
            self.actualizar_tabla()
            QMessageBox.information(self, "Nodo Agregado", f"Nodo con valor '{elemento}' agregado.")

    def editar_elemento(self):
        """Edita un nodo de la lista doble enlazada por índice."""
        elementos = self.lista_doble.obtener_lista()
        if not elementos:
            QMessageBox.warning(self, "Error", "La lista doble enlazada está vacía.")
            return

        indices = [str(i) for i in range(len(elementos))]
        indice_seleccionado, ok = QInputDialog.getItem(self, "Editar Nodo", "Seleccione el índice del nodo a editar:", indices, 0, False)
        if ok and indice_seleccionado is not None:
            indice = int(indice_seleccionado)
            nuevo_valor, ok = QInputDialog.getText(self, "Editar Nodo", f"Ingrese el nuevo valor para el nodo en el índice {indice}:")
            if ok and nuevo_valor:
                self.lista_doble.editar_por_indice(indice, nuevo_valor)
                self.actualizar_tabla()
                QMessageBox.information(self, "Nodo Editado", f"Nodo en el índice {indice} actualizado a '{nuevo_valor}'.")

    def eliminar_elemento(self):
        """Elimina un nodo de la lista doble enlazada por índice."""
        elementos = self.lista_doble.obtener_lista()
        if not elementos:
            QMessageBox.warning(self, "Error", "La lista doble enlazada está vacía.")
            return

        indices = [str(i) for i in range(len(elementos))]
        indice_seleccionado, ok = QInputDialog.getItem(self, "Eliminar Nodo", "Seleccione el índice del nodo a eliminar:", indices, 0, False)
        if ok and indice_seleccionado is not None:
            indice = int(indice_seleccionado)
            self.lista_doble.eliminar_por_indice(indice)
            self.actualizar_tabla()
            QMessageBox.information(self, "Nodo Eliminado", f"Nodo en el índice {indice} eliminado.")
