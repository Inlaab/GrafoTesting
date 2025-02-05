import json

class Grafo:
    def __init__(self):
        self.nodos = {}
        self.aristas = []
        self.cargar_todos_los_datos()

    def cargar_datos(self, archivo, tipo):
        with open(archivo, 'r') as f:
            datos = json.load(f)
            if tipo in self.nodos:
                if isinstance(self.nodos[tipo], list) and isinstance(datos, list):
                    self.nodos[tipo].extend(datos)
                elif isinstance(self.nodos[tipo], dict) and isinstance(datos, dict):
                    self.nodos[tipo].update(datos)
                else:
                    raise ValueError("Los datos existentes y los nuevos datos deben ser del mismo tipo (lista o diccionario).")
            else:
                self.nodos[tipo] = datos

    def cargar_aristas(self, aristas):
        if isinstance(aristas, list):
            self.aristas.extend(aristas)
        else:
            raise ValueError("Las aristas deben ser una lista.")

    def agregar_arista(self, desde, hasta, tipo, peso, funciones):
        self.aristas.append({
            'desde': desde,
            'hasta': hasta,
            'tipo': tipo,
            'peso': peso,
            'funciones': funciones
        })

    def mostrar_grafo(self):
        print("Nodos:")
        for tipo, nodos in self.nodos.items():
            print(f"{tipo}: {nodos}")
        print("Aristas:")
        for arista in self.aristas:
            print(arista)

    def cargar_todos_los_datos(self):
        self.cargar_datos('kb/servicios_activos.json', 'Servicios')
        self.cargar_datos('kb/consultores_activos.json', 'Consultores')
        self.cargar_datos('kb/ubicaciones_geo.json', 'Ubicaciones')
        self.cargar_datos('kb/franjas_horarias.json', 'Franjas_Horarias')
        self.cargar_datos('kb/matriz_distancias.json', 'Distancias')
        self.cargar_datos('kb/tarifas_servicios.json', 'Tarifas')
        self.cargar_datos('kb/capacidad_operativa.json', 'Capacidad')

        aristas = [
            {'desde': 'Servicios', 'hasta': 'Consultores', 'tipo': 'asignacion', 'peso': 1.0, 'funciones': ['Procesamiento']},
            {'desde': 'Consultores', 'hasta': 'Ubicaciones', 'tipo': 'localizacion', 'peso': 1.0, 'funciones': ['Consulta']},
            {'desde': 'Ubicaciones', 'hasta': 'Distancias', 'tipo': 'calculo', 'peso': 1.0, 'funciones': ['Cálculo']},
            {'desde': 'Franjas_Horarias', 'hasta': 'Consultores', 'tipo': 'disponibilidad', 'peso': 1.0, 'funciones': ['Validación']},
            {'desde': 'Distancias', 'hasta': 'Tarifas', 'tipo': 'factor', 'peso': 1.0, 'funciones': ['Cálculo']},
            {'desde': 'Capacidad', 'hasta': 'Consultores', 'tipo': 'limite', 'peso': 1.0, 'funciones': ['Validación']}
        ]
        self.cargar_aristas(aristas)