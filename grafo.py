import json

class Grafo:
    def __init__(self):
        self.nodos = {}
        self.aristas = []

    def cargar_datos(self, archivo, tipo):
        with open(archivo, 'r') as f:
            datos = json.load(f)
            self.nodos[tipo] = datos

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

    def consultar_tarifa(self, departamento, municipio):
        tarifas = self.nodos.get('Tarifas', {}).get('tarifas', [])
        for tarifa in tarifas:
            if tarifa['departamento'] == departamento and tarifa['municipio'] == municipio:
                return tarifa['tarifa']
        return None