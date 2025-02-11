import json

class Grafo:
    def __init__(self):
        self.nodos = {}
        self.aristas = {}
        self.cargar_todos_los_datos()

    def cargar_datos(self, filepath, key):
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
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

    def consultar(self, categoria, query_params):
        """
        Consulta genérica que acepta un diccionario de parámetros
        """
        try:
            if categoria not in self.nodos:
                return "Categoría no encontrada"
                
            datos = self.nodos[categoria]
            resultado = datos
            
            for key in query_params:
                if isinstance(resultado, dict):
                    resultado = resultado.get(key, None)
                else:
                    return "Ruta de consulta inválida"
                    
            return resultado if resultado is not None else "No se encontraron datos"
                
        except Exception as e:
            return f"Error en consulta: {str(e)}"

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
        config_archivos = {
            'Servicios': 'kb/servicios_activos.json',
            'Consultores': 'kb/consultores_activos.json',
            'Ubicaciones': 'kb/ubicaciones_geo.json',
            'Franjas_Horarias': 'kb/franjas_horarias.json',
            'Distancias': 'kb/matriz_distancias.json',
            'Tarifas': 'kb/tarifas_servicios.json',
            'Capacidad': 'kb/capacidad_operativa.json'
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
    print(estructura)

    # Obtener contexto de una categoría
    contexto_servicios = grafo.obtener_contexto('Servicios')
    print(contexto_servicios)

    contexto_ubicaciones = grafo.obtener_contexto('Ubicaciones')
    print(contexto_ubicaciones)