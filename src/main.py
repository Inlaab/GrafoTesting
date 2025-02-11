import sys
import os

# Agregar la ruta del directorio principal del proyecto
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grafo import Grafo
from agente_ia import AgenteIA

def main():
    # Crear una instancia de la clase Grafo
    grafo = Grafo()
    
    # Mostrar la estructura del grafo (nodos y aristas)
    print("\n=== ESTRUCTURA COMPLETA DEL GRAFO ===")
    print(grafo.obtener_estructura())
    
    # Pruebas de consulta
    print("\n=== PRUEBAS DE CONSULTA ===")
    print("\nTodos los servicios:")
    print(grafo.consultar("Servicios"))
    
    print("\nConsulta específica - Servicio Avalúo:")
    print(grafo.consultar("Servicios", {"tipo": "Avalúo"}))
    
    # Crear una instancia del Agente IA y pasarle el grafo
    agente = AgenteIA(grafo)

if __name__ == "__main__":
    # Ejecutar la función principal si este archivo se ejecuta directamente
    main()