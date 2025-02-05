class AgenteIA:
    def __init__(self, grafo):
        self.grafo = grafo

    def procesar_input(self, input_usuario):
        if "tarifa" in input_usuario and "municipio" in input_usuario:
            return self.consultar_tarifa(input_usuario)
        elif "ruta" in input_usuario:
            return self.asignar_ruta(input_usuario)
        else:
            return "Lo siento, no entiendo la consulta."

    def consultar_tarifa(self, input_usuario):
        partes = input_usuario.split(" ")
        municipio = partes[-3]
        departamento = partes[-1]
        tarifa = self.grafo.consultar_tarifa(departamento, municipio)
        if tarifa:
            tarifa_formateada = f"${tarifa:,.0f}".replace(",", ".")
            return f"La tarifa para el municipio de {municipio} en {departamento} es de {tarifa_formateada} pesos."
        else:
            return f"No se encontró la tarifa para el municipio de {municipio} en {departamento}."

    def asignar_ruta(self, input_usuario):
        # Implementar lógica de asignación de ruta según el protocolo operativo Pathfinder 4.0
        return "Asignación de ruta en proceso..."
