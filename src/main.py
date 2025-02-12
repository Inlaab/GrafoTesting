def main():
    grafo = Grafo()
    agente = AgenteIA(grafo)
    
    # Ejemplos de interacción
    consultas = [
        "Quiero agendar un servicio para el 15 de diciembre a las 2:30 pm en Calle 123 #45-67",
        "Necesito cotizar un servicio desde la Calle 100 hasta la Calle 170",
        "¿Qué servicios están disponibles?",
    ]
    
    for consulta in consultas:
        print(f"\nConsulta: {consulta}")
        respuesta = agente.interactuar(consulta)
        print(f"Respuesta: {respuesta}")

if __name__ == "__main__":
    main()
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