import matplotlib.pyplot as plt

class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None  # Hijo izquierdo
        self.derecho = None   # Hijo derecho


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        """Agrega un valor al árbol."""
        nuevo_nodo = NodoArbol(valor)
        if not self.raiz:
            self.raiz = nuevo_nodo
        else:
            self._agregar_recursivo(self.raiz, nuevo_nodo)

    def _agregar_recursivo(self, nodo_actual, nuevo_nodo):
        """Función auxiliar para agregar nodos recursivamente."""
        if nuevo_nodo.valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = nuevo_nodo
            else:
                self._agregar_recursivo(nodo_actual.izquierdo, nuevo_nodo)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = nuevo_nodo
            else:
                self._agregar_recursivo(nodo_actual.derecho, nuevo_nodo)

    def en_orden(self):
        """Devuelve una lista con los valores del árbol en recorrido en orden."""
        resultado = []
        self._en_orden_recursivo(self.raiz, resultado)
        return resultado

    def _en_orden_recursivo(self, nodo_actual, resultado):
        """Función auxiliar para el recorrido en orden."""
        if nodo_actual:
            self._en_orden_recursivo(nodo_actual.izquierdo, resultado)
            resultado.append(nodo_actual.valor)
            self._en_orden_recursivo(nodo_actual.derecho, resultado)

    def graficar(self):
        """Genera una representación gráfica del árbol."""
        if not self.raiz:
            return

        def _posiciones(nodo, x=0, y=0, nivel=1, posiciones={}, conexiones=[]):
            if nodo:
                posiciones[nodo.valor] = (x, y)
                if nodo.izquierdo:
                    conexiones.append((nodo.valor, nodo.izquierdo.valor))
                    _posiciones(nodo.izquierdo, x - 1 / nivel, y - 1, nivel + 1, posiciones, conexiones)
                if nodo.derecho:
                    conexiones.append((nodo.valor, nodo.derecho.valor))
                    _posiciones(nodo.derecho, x + 1 / nivel, y - 1, nivel + 1, posiciones, conexiones)

        posiciones = {}
        conexiones = []
        _posiciones(self.raiz, nivel=1, posiciones=posiciones, conexiones=conexiones)

        # Graficar nodos y conexiones
        plt.figure(figsize=(8, 6))
        for padre, hijo in conexiones:
            x1, y1 = posiciones[padre]
            x2, y2 = posiciones[hijo]
            plt.plot([x1, x2], [y1, y2], 'k-')  # Línea negra

        for valor, (x, y) in posiciones.items():
            plt.scatter(x, y, s=500, c='skyblue', zorder=3)  # Nodos
            plt.text(x, y, str(valor), ha='center', va='center', fontsize=10, zorder=4)  # Etiquetas

        plt.axis('off')
        plt.title("Árbol Binario")
        plt.show()


#  ---------- UI ------------

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QInputDialog, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt


class VentanaArbol(QMainWindow):
    def __init__(self, menu_principal):
        super().__init__()
        self.setWindowTitle("Árbol Binario")
        self.setGeometry(150, 150, 600, 400)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.menu_principal = menu_principal
        self.arbol = ArbolBinario()  # Inicializar el árbol binario

        # Layout principal
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Encabezado
        encabezado = QLabel("Operaciones con Árbol Binario")
        encabezado.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(encabezado)

        # Tabla para representar el árbol
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(2)  # Dos columnas: Nodo y Valor
        self.tabla.setHorizontalHeaderLabels(["Nodo", "Valor"])
        self.tabla.setEditTriggers(QTableWidget.NoEditTriggers)  # Tabla de solo lectura
        layout.addWidget(self.tabla)

        # Botones
        botones = ["Agregar Nodo", "Eliminar Nodo", "Mostrar En Orden", "Regresar"]
        for boton_texto in botones:
            boton = QPushButton(boton_texto)
            boton.clicked.connect(lambda checked, opt=boton_texto: self.boton_click(opt))
            layout.addWidget(boton)

        self.setCentralWidget(central_widget)

    def actualizar_tabla(self, valores):
        """Actualiza la tabla con el recorrido en orden del árbol."""
        self.tabla.setRowCount(len(valores))  # Configurar filas según los valores
        for i, valor in enumerate(valores):
            self.tabla.setItem(i, 0, QTableWidgetItem(f"Nodo {i + 1}"))
            self.tabla.setItem(i, 1, QTableWidgetItem(str(valor)))
        self.tabla.resizeColumnsToContents()  # Ajustar el ancho de las columnas automáticamente

    def boton_click(self, opcion):
        if opcion == "Agregar Nodo":
            self.agregar_nodo()
        elif opcion == "Eliminar Nodo":
            self.eliminar_nodo()
        elif opcion == "Mostrar En Orden":
            self.mostrar_en_orden()
        elif opcion == "Regresar":
            self.close()

    def agregar_nodo(self):
        """Agrega un nuevo nodo al árbol."""
        valor, ok = QInputDialog.getInt(self, "Agregar Nodo", "Ingrese el valor del nodo:")
        if ok:
            self.arbol.agregar(valor)
            QMessageBox.information(self, "Nodo Agregado", f"El nodo con valor {valor} ha sido agregado.")

    def eliminar_nodo(self):
        """Elimina un nodo del árbol."""
        valor, ok = QInputDialog.getInt(self, "Eliminar Nodo", "Ingrese el valor del nodo a eliminar:")
        if ok:
            self.arbol.eliminar(valor)
            QMessageBox.information(self, "Nodo Eliminado", f"El nodo con valor {valor} ha sido eliminado.")

    def mostrar_en_orden(self):
        """Muestra los valores del árbol en recorrido en orden y lo grafica."""
        valores = self.arbol.en_orden()
        self.actualizar_tabla(valores)
        QMessageBox.information(self, "Recorrido En Orden", f"Valores en orden: {', '.join(map(str, valores))}")
        self.arbol.graficar()  # Graficar el árbol
