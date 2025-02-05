import sys
import os

# Agregar la ruta del directorio principal del proyecto
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grafo import Grafo
from agente_ia import AgenteIA

def main():
    grafo = Grafo()
    grafo.cargar_datos('kb/servicios_activos.json', 'Servicios')
    grafo.cargar_datos('kb/consultores_activos.json', 'Consultores')
    grafo.cargar_datos('kb/ubicaciones_geo.json', 'Ubicaciones')
    grafo.cargar_datos('kb/franjas_horarias.json', 'Franjas_Horarias')
    grafo.cargar_datos('kb/matriz_distancias.json', 'Distancias')
    grafo.cargar_datos('kb/tarifas_servicios.json', 'Tarifas')
    grafo.cargar_datos('kb/capacidad_operativa.json', 'Capacidad')

    grafo.agregar_arista('Servicios', 'Consultores', 'asignacion', 1.0, ['Procesamiento'])
    grafo.agregar_arista('Consultores', 'Ubicaciones', 'localizacion', 1.0, ['Consulta'])
    grafo.agregar_arista('Ubicaciones', 'Distancias', 'calculo', 1.0, ['Cálculo'])
    grafo.agregar_arista('Franjas_Horarias', 'Consultores', 'disponibilidad', 1.0, ['Validación'])
    grafo.agregar_arista('Distancias', 'Tarifas', 'factor', 1.0, ['Cálculo'])
    grafo.agregar_arista('Capacidad', 'Consultores', 'limite', 1.0, ['Validación'])

    grafo.mostrar_grafo()

    agente = AgenteIA(grafo)

    # Prueba de interacción
    input_usuario = "¿Cuál es la tarifa para el municipio de Chía en Cundinamarca?"
    respuesta = agente.procesar_input(input_usuario)
    print(respuesta)

if __name__ == "__main__":
    main()