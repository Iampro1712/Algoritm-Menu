import matplotlib.pyplot as plt
import networkx as nx

class Grafo:
    def __init__(self):
        self.grafo = {}  # Diccionario para almacenar nodos y sus conexiones

    def agregar_nodo(self, nodo):
        """Agrega un nodo al grafo."""
        if nodo not in self.grafo:
            self.grafo[nodo] = []

    def agregar_arista(self, nodo1, nodo2):
        """Agrega una arista (conexión) entre dos nodos."""
        if nodo1 in self.grafo and nodo2 in self.grafo:
            self.grafo[nodo1].append(nodo2)
            self.grafo[nodo2].append(nodo1)  # Grafo no dirigido

    def obtener_nodos(self):
        """Devuelve una lista de los nodos en el grafo."""
        return list(self.grafo.keys())

    def obtener_aristas(self):
        """Devuelve una lista de las aristas en el grafo."""
        aristas = []
        for nodo, conexiones in self.grafo.items():
            for conexion in conexiones:
                if (conexion, nodo) not in aristas:  # Evitar duplicados
                    aristas.append((nodo, conexion))
        return aristas

    def mostrar_grafo(self):
        """Muestra el grafo completo."""
        for nodo, conexiones in self.grafo.items():
            print(f"{nodo}: {', '.join(map(str, conexiones))}")


    def graficar(self):
        """Genera una representación gráfica del grafo."""
        G = nx.Graph()

        # Agregar nodos y aristas al grafo de NetworkX
        for nodo in self.obtener_nodos():
            G.add_node(nodo)
        for nodo1, nodo2 in self.obtener_aristas():
            G.add_edge(nodo1, nodo2)

        # Dibujar el grafo
        pos = nx.spring_layout(G)  # Algoritmo para distribuir nodos
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10, font_weight='bold')
        plt.title("Grafo")
        plt.show()

#  ---------- UI ------------

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QInputDialog, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

class VentanaGrafo(QMainWindow):
    def __init__(self, menu_principal):
        super().__init__()
        self.setWindowTitle("Operaciones con Grafos")
        self.setGeometry(150, 150, 600, 400)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.menu_principal = menu_principal
        self.grafo = Grafo()  # Inicializar el grafo

        # Layout principal
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Encabezado
        encabezado = QLabel("Operaciones con Grafos")
        encabezado.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(encabezado)

        # Tabla para mostrar nodos y conexiones
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(2)  # Columnas: Nodo y Conexiones
        self.tabla.setHorizontalHeaderLabels(["Nodo", "Conexiones"])
        self.tabla.setEditTriggers(QTableWidget.NoEditTriggers)  # Tabla de solo lectura
        layout.addWidget(self.tabla)

        # Botones
        botones = ["Agregar Nodo", "Agregar Arista", "Mostrar Grafo", "Regresar"]
        for boton_texto in botones:
            boton = QPushButton(boton_texto)
            boton.clicked.connect(lambda checked, opt=boton_texto: self.boton_click(opt))
            layout.addWidget(boton)

        self.setCentralWidget(central_widget)

    def actualizar_tabla(self):
        """Actualiza la tabla con los nodos y sus conexiones."""
        nodos = self.grafo.obtener_nodos()
        self.tabla.setRowCount(len(nodos))  # Configurar filas según los nodos
        for i, nodo in enumerate(nodos):
            conexiones = ', '.join(map(str, self.grafo.grafo[nodo]))
            self.tabla.setItem(i, 0, QTableWidgetItem(str(nodo)))  # Nodo
            self.tabla.setItem(i, 1, QTableWidgetItem(conexiones))  # Conexiones
        self.tabla.resizeColumnsToContents()  # Ajustar el ancho de las columnas automáticamente

    def boton_click(self, opcion):
        if opcion == "Agregar Nodo":
            self.agregar_nodo()
        elif opcion == "Agregar Arista":
            self.agregar_arista()
        elif opcion == "Mostrar Grafo":
            self.mostrar_grafo()
        elif opcion == "Regresar":
            self.close()

    def agregar_nodo(self):
        """Agrega un nuevo nodo al grafo."""
        nodo, ok = QInputDialog.getText(self, "Agregar Nodo", "Ingrese el nombre del nodo:")
        if ok and nodo:
            self.grafo.agregar_nodo(nodo)
            self.actualizar_tabla()
            QMessageBox.information(self, "Nodo Agregado", f"El nodo '{nodo}' ha sido agregado.")

    def agregar_arista(self):
        """Agrega una arista entre dos nodos."""
        nodo1, ok1 = QInputDialog.getText(self, "Agregar Arista", "Ingrese el primer nodo:")
        if ok1 and nodo1:
            nodo2, ok2 = QInputDialog.getText(self, "Agregar Arista", "Ingrese el segundo nodo:")
            if ok2 and nodo2:
                if nodo1 in self.grafo.grafo and nodo2 in self.grafo.grafo:
                    self.grafo.agregar_arista(nodo1, nodo2)
                    self.actualizar_tabla()
                    QMessageBox.information(self, "Arista Agregada", f"Se ha creado una conexión entre '{nodo1}' y '{nodo2}'.")
                else:
                    QMessageBox.warning(self, "Error", "Uno o ambos nodos no existen en el grafo.")

    def mostrar_grafo(self):
        """Muestra el grafo visualmente."""
        self.grafo.graficar()
