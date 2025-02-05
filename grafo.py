import json

class Grafo:
    def __init__(self):
        self.nodos = {}
        self.aristas = []

    def cargar_datos(self, archivo, tipo):
        with open(archivo, 'r') as f:
            datos = json.load(f)
            self.nodos[tipo] = datos

    def agregar_arista(self, desde, hacia, tipo, peso, funciones):
        self.aristas.append({
            'desde': desde,
            'hasta': hacia,
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

    def consultar_tarifa(self, departamento, municipio):
        tarifas = self.nodos.get('Tarifas', {}).get('tarifas', [])
        for tarifa in tarifas:
            if tarifa['departamento'] == departamento and tarifa['municipio'] == municipio:
                return tarifa['tarifa']
        return None

# Ejemplo de uso
if __name__ == "__main__":
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