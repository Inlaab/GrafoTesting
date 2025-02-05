import sys
import os

# Agregar la ruta del directorio principal del proyecto
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grafo import Grafo
from agente_ia import AgenteIA

def main():
    grafo = Grafo()
    grafo.mostrar_grafo()
    agente = AgenteIA(grafo)

if __name__ == "__main__":
    main()