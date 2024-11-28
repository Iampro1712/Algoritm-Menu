

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None  # Referencia al siguiente nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Inicio de la lista

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar_por_indice(self, indice):
        if not self.cabeza:
            return False  # Lista vacía
        if indice == 0:  # Eliminar el primer nodo
            self.cabeza = self.cabeza.siguiente
            return True
        actual = self.cabeza
        posicion = 0
        while actual.siguiente and posicion < indice - 1:
            actual = actual.siguiente
            posicion += 1
        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente
            return True
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

#  ---------- UI ------------
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QInputDialog, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

class VentanaListasEnlazadas(QMainWindow):
    def __init__(self, menu_principal):
        super().__init__()
        self.setWindowTitle("Operaciones con Listas Enlazadas")
        self.setGeometry(150, 150, 400, 400)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.menu_principal = menu_principal
        self.lista_enlazada = ListaEnlazada()  # Inicializar lista enlazada

        # Layout principal
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Encabezado
        encabezado = QLabel("Operaciones con Listas Enlazadas")
        encabezado.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(encabezado)

        # Tabla para mostrar la lista enlazada
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(2)
        self.tabla.setHorizontalHeaderLabels(["Índice", "Valor"])
        layout.addWidget(self.tabla)

        # Actualizar la tabla con datos iniciales
        self.actualizar_tabla()

        # Botones
        botones = ["Agregar", "Eliminar", "Editar", "Regresar"]
        for boton_texto in botones:
            boton = QPushButton(boton_texto)
            boton.clicked.connect(lambda checked, opt=boton_texto: self.boton_click(opt))
            layout.addWidget(boton)

        self.setCentralWidget(central_widget)

    def actualizar_tabla(self):
        """Actualiza la tabla con los elementos de la lista enlazada."""
        elementos = self.lista_enlazada.obtener_lista()
        self.tabla.setRowCount(len(elementos))
        for i, valor in enumerate(elementos):
            self.tabla.setItem(i, 0, QTableWidgetItem(str(i)))
            self.tabla.setItem(i, 1, QTableWidgetItem(str(valor)))

    def boton_click(self, opcion):
        if opcion == "Agregar":
            self.agregar_elemento()
        elif opcion == "Eliminar":
            self.eliminar_elemento()
        elif opcion == "Editar":
            self.editar_elemento()
        elif opcion == "Regresar":
            self.close()

    def agregar_elemento(self):
        elemento, ok = QInputDialog.getText(self, "Agregar Nodo", "Ingrese un valor para el nodo:")
        if ok and elemento:
            self.lista_enlazada.agregar(elemento)
            self.actualizar_tabla()
            QMessageBox.information(self, "Nodo Agregado", f"Nodo con valor '{elemento}' agregado.")

    def editar_elemento(self):
        """Editar un nodo de la lista enlazada por índice."""
        elementos = self.lista_enlazada.obtener_lista()
        if not elementos:
            QMessageBox.warning(self, "Error", "La lista enlazada está vacía.")
            return

        # Mostrar un cuadro de diálogo con los índices disponibles
        indices = [str(i) for i in range(len(elementos))]
        indice_seleccionado, ok = QInputDialog.getItem(self, "Editar Nodo", "Seleccione el índice del nodo a editar:", indices, 0, False)
        if ok and indice_seleccionado is not None:
            indice = int(indice_seleccionado)

            # Pedir el nuevo valor para el nodo seleccionado
            nuevo_valor, ok = QInputDialog.getText(self, "Editar Nodo", f"Ingrese el nuevo valor para el nodo en el índice {indice}:")
            if ok and nuevo_valor:
                editado = self.lista_enlazada.editar_por_indice(indice, nuevo_valor)
                if editado:
                    self.actualizar_tabla()
                    QMessageBox.information(self, "Nodo Editado", f"Nodo en el índice {indice} actualizado a '{nuevo_valor}'.")
                else:
                    QMessageBox.warning(self, "Error", f"No se pudo editar el nodo en el índice {indice}.")


    def eliminar_elemento(self):
        elementos = self.lista_enlazada.obtener_lista()
        if not elementos:
            QMessageBox.warning(self, "Error", "La lista enlazada está vacía.")
            return

        # Mostrar un cuadro de diálogo con los índices disponibles
        indices = [str(i) for i in range(len(elementos))]
        indice_seleccionado, ok = QInputDialog.getItem(self, "Eliminar Nodo", "Seleccione el índice del nodo a eliminar:", indices, 0, False)
        if ok and indice_seleccionado is not None:
            indice = int(indice_seleccionado)
            self.lista_enlazada.eliminar_por_indice(indice)
            self.actualizar_tabla()
            QMessageBox.information(self, "Nodo Eliminado", f"Nodo en el índice {indice} eliminado.")

