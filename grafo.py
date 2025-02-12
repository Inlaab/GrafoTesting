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

    def consultar(self, categoria, filtro=None):
        try:
            if categoria not in self.nodos:
                return "Categoría no encontrada"
            if filtro is None:
                return self.format_output(self.nodos[categoria])
            if categoria == "Servicios":
                if "tipo" en filtro:
                    servicio = self.nodos[categoria].get(filtro["tipo"])
                    if servicio:
                        return self.format_output(servicio)
                    return "Servicio no encontrado"
            return "Filtro no válido"
        except Exception as e:
            return f"Error en consulta: {str(e)}"

    def format_output(self, data):
        if isinstance(data, dict):
            return json.dumps(data, indent=2, ensure_ascii=False)
        return data
