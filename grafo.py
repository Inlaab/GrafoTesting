def validar_cobertura(self, direccion):
    """
    Valida si una dirección está dentro de la cobertura
    
    :param direccion: Dirección a validar
    :return: True si está en cobertura, False si no
    """
    try:
        ubicaciones = self.nodos['Ubicaciones']
        # Implementar lógica de validación de cobertura
        return True  # Por ahora siempre retorna True
    except:
        return False
import json
import os

class Grafo:
    def __init__(self):
        self.nodos = {}
        self.aristas = {}
        self.cargar_todos_los_datos()

    def cargar_datos(self, filepath, key):
        try:
            with open(filepath, 'r', encoding='utf-8-sig') as file:
                datos = json.load(file)
                # Diccionario de transformaciones por tipo
                transformaciones = {
                    'Servicios': lambda x: x['tipos_servicio'],
                    'Ubicaciones': lambda x: x['regiones'],
                    'default': lambda x: x
                }
                # Aplicar transformación según key o usar default
                self.nodos[key] = transformaciones.get(key, transformaciones['default'])(datos)
        except FileNotFoundError:
            raise Exception(f"Archivo no encontrado: {filepath}")
        except json.JSONDecodeError:
            raise Exception(f"Error al decodificar JSON: {filepath}")

    def agregar_arista(self, desde, hasta, tipo, peso=1.0, funciones=None):
        if funciones is None:
            funciones = []
        
        arista = {
            'desde': desde,
            'hasta': hasta,
            'tipo': tipo,
            'peso': peso,
            'funciones': funciones
        }
        
        if desde not in self.aristas:
            self.aristas[desde] = []
        self.aristas[desde].append(arista)

    def consultar(self, categoria, filtro=None):
        """
        Consulta datos de una categoría con filtro opcional
        """
        try:
            if categoria not in self.nodos:
                return "Categoría no encontrada"
                
            if filtro is None:
                return self.format_output(self.nodos[categoria])
                
            if categoria == "Servicios":
                if "tipo" in filtro:
                    servicio = self.nodos[categoria].get(filtro["tipo"])
                    if servicio:
                        return self.format_output(servicio)
                    return "Servicio no encontrado"
            
            return "Filtro no válido"
        except Exception as e:
            return f"Error en consulta: {str(e)}"

    def format_output(self, data):
        """Formatea la salida para mejor legibilidad"""
        if isinstance(data, dict):
            return json.dumps(data, indent=2, ensure_ascii=False)
        return data

    def obtener_estructura(self):
        """
        Retorna un diccionario con la estructura completa del grafo
        para que el LLM pueda procesarla
        """
        return {
            'nodos': self.nodos,
            'aristas': self.aristas
        }

    def obtener_contexto(self, categoria):
        """
        Retorna toda la información relacionada a una categoría,
        incluyendo sus aristas
        """
        return {
            'datos': self.nodos.get(categoria, {}),
            'conexiones': self.aristas.get(categoria, [])
        }

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

        # Definir las aristas del grafo
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

if __name__ == "__main__":
    grafo = Grafo()
    # Ejemplo de uso
    grafo.cargar_datos('E:\\GitHub\\GrafoTesting\\kb\\servicios_activos.json', 'Servicios')
    grafo.cargar_datos('E:\\GitHub\\GrafoTesting\\kb\\ubicaciones_geo.json', 'Ubicaciones')

    # Agregar aristas de ejemplo
    grafo.agregar_arista('Servicios', 'Consultores', 'asignacion', 1.0, ['Procesamiento'])
    grafo.agregar_arista('Bogotá', 'Soacha', 'ruta', 10)
    grafo.agregar_arista('Bogotá', 'Calle 13', 'ruta', 5)

    # Obtener estructura completa
    estructura = grafo.obtener_estructura()
    print(grafo.format_output(estructura))

    # Obtener contexto de una categoría
    contexto_servicios = grafo.obtener_contexto('Servicios')
    print(grafo.format_output(contexto_servicios))

    contexto_ubicaciones = grafo.obtener_contexto('Ubicaciones')
    print(grafo.format_output(contexto_ubicaciones))