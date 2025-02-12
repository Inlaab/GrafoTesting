import json
import os

class Grafo:
    def __init__(self):
        self.nodos = {}
        self.aristas = {}
        self.cargar_todos_los_datos()

    # [... resto de métodos sin cambios hasta cargar_todos_los_datos ...]

    def cargar_todos_los_datos(self):
        """
        Carga datos usando un diccionario de configuración
        """
        base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kb')
        config_archivos = {
            'Servicios': os.path.join(base_path, 'servicios_activos.json'),
            'Consultores': os.path.join(base_path, 'consultores_activos.json'),
            'Ubicaciones': os.path.join(base_path, 'ubicaciones_geo.json'),
            'Franjas_Horarias': os.path.join(base_path, 'franjas_horarias.json'),
            'Distancias': os.path.join(base_path, 'matriz_distancias.json'),
            'Tarifas': os.path.join(base_path, 'tarifas_servicios.json'),
            'Capacidad': os.path.join(base_path, 'capacidad_operativa.json')
        }
        
        for key, filepath in config_archivos.items():
            self.cargar_datos(filepath, key)

        # Definir las aristas del grafo con caracteres correctamente codificados
        aristas = [
            {'desde': 'Servicios', 'hasta': 'Consultores', 'tipo': 'asignacion', 'peso': 1.0, 'funciones': ['Procesamiento']},
            {'desde': 'Consultores', 'hasta': 'Ubicaciones', 'tipo': 'localizacion', 'peso': 1.0, 'funciones': ['Consulta']},
            {'desde': 'Ubicaciones', 'hasta': 'Distancias', 'tipo': 'calculo', 'peso': 1.0, 'funciones': ['Cálculo']},
            {'desde': 'Franjas_Horarias', 'hasta': 'Consultores', 'tipo': 'disponibilidad', 'peso': 1.0, 'funciones': ['Validación']},
            {'desde': 'Distancias', 'hasta': 'Tarifas', 'tipo': 'factor', 'peso': 1.0, 'funciones': ['Cálculo']},
            {'desde': 'Capacidad', 'hasta': 'Consultores', 'tipo': 'limite', 'peso': 1.0, 'funciones': ['Validación']}
        ]
        for arista in aristas:
            self.agregar_arista(arista['desde'], arista['hasta'], arista['tipo'], arista['peso'], arista['funciones'])

    # [... resto de la clase sin cambios ...]
