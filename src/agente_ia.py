import math

class AgenteIA:
    def __init__(self, grafo):
        """
        Inicializar el Agente IA con un grafo.
        
        :param grafo: Instancia de la clase Grafo.
        """
        self.grafo = grafo
        self.contexto = {}

    def validar_horario(self, franja, fecha, hora):
        """
        Validar si una fecha y hora están dentro de una franja horaria.
        
        :param franja: Franja horaria a validar
        :param fecha: Fecha a validar
        :param hora: Hora a validar
        :return: True si está dentro de la franja, False en caso contrario
        """
        try:
            dia_semana = fecha.weekday()  # 0-6 (Lunes-Domingo)
            hora_num = int(hora.split(':')[0])
            
            # Validar días laborables (Lunes-Viernes)
            if dia_semana < 5:  # Lunes a Viernes
                return 7 <= hora_num <= 17  # 7:00 AM - 5:00 PM
            # Validar sábados
            elif dia_semana == 5:  # Sábado
                return 7 <= hora_num <= 12  # 7:00 AM - 12:00 PM
            # Domingos no hay atención
            else:
                return False
        except Exception:
            return False

    def extraer_id(self, consulta):
        """
        Extrae el ID de un servicio o consultor de la consulta.
        
        :param consulta: String con la consulta del usuario.
        :return: ID extraído o None si no se encuentra.
        """
        try:
            import re
            numeros = re.findall(r'\d+', consulta)
            return numeros[0] if numeros else None
        except Exception:
            return None

    def procesar_consulta(self, tipo_consulta):
        """
        Procesa una consulta específica y retorna la información solicitada.
        
        :param tipo_consulta: Tipo de consulta a procesar
        :return: Respuesta procesada
        """
        if tipo_consulta == "servicios activos":
            servicios = self.grafo.obtener_nodo("Servicios")
            if servicios and len(servicios) > 0:
                return f"Hay {len(servicios)} servicios activos actualmente."
        return "No hay información disponible."

    def asignar_servicio_a_consultor(self, servicio_id):
        """
        Asigna un servicio al consultor más apropiado.
        
        :param servicio_id: ID del servicio a asignar
        :return: ID del consultor asignado o None si no hay disponibles
        """
        consultores = self.grafo.obtener_nodo("Consultores")
        if consultores:
            # Aquí iría la lógica de asignación
            # Por ahora retornamos el primer consultor disponible
            return list(consultores.keys())[0] if consultores else None
        return None

    def interactuar(self, consulta):
        """
        Método principal para interactuar con el usuario.
        
        :param consulta: String con la consulta del usuario
        :return: Respuesta en lenguaje natural
        """
        if not consulta:
            return "Por favor, ingresa una consulta válida."
            
        consulta = consulta.lower()
        
        if "optimiza ruta" in consulta or "optimizar ruta" in consulta:
            return ("Para optimizar la ruta necesito:\n"
                   "- Ciudad donde se realizará el servicio\n"
                   "- Fecha y hora deseada del servicio\n"
                   "- Puntos adicionales a visitar (opcional)\n\n"
                   "Con esta información podré:\n"
                   "- Asignar el consultor más cercano disponible\n"
                   "- Calcular la ruta más eficiente\n"
                   "- Proporcionar los tiempos estimados")
        
        if "servicio" in consulta:
            if "asignar" in consulta:
                servicio_id = self.extraer_id(consulta)
                if servicio_id:
                    consultor_id = self.asignar_servicio_a_consultor(servicio_id)
                    if consultor_id:
                        return f"¡Listo! El servicio {servicio_id} ha sido asignado al consultor {consultor_id}."
                    else:
                        return "Lo siento, no hay consultores disponibles en este momento."
                else:
                    return "No pude identificar el ID del servicio. ¿Podrías verificarlo?"
            elif "consultar" in consulta:
                return self.procesar_consulta("servicios activos")
        
        return "Lo siento, no entendí tu consulta. ¿Podrías reformularla?"

    def calcular_distancia(self, origen, destino):
        """
        Calcula la distancia entre dos puntos.
        
        :param origen: Punto de origen
        :param destino: Punto de destino
        :return: Distancia calculada
        """
        # Aquí iría el cálculo real de distancia
        return 0

    def validar_capacidad(self, consultor_id):
        """
        Valida la capacidad operativa de un consultor.
        
        :param consultor_id: ID del consultor a validar
        :return: True si tiene capacidad, False en caso contrario
        """
        capacidad = self.grafo.obtener_nodo("Capacidad")
        if capacidad and consultor_id in capacidad:
            return capacidad[consultor_id] > 0
        return False
