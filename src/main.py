from grafo import Grafo

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

if __name__ == "__main__":
    main()