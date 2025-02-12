import math

class AgenteIA:
    def __init__(self, grafo):
        """
        Inicializar el Agente IA con un grafo.
        
        :param grafo: Instancia de la clase Grafo.
        """
        self.grafo = grafo
        self.contexto = {}

    # [... resto de métodos sin cambios hasta validar_horarios_permitidos ...]

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

    # [... resto de métodos sin cambios hasta extraer_id ...]

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

    def interactuar(self, consulta):
        """
        Método principal para interactuar con el usuario.
        
        :param consulta: String con la consulta del usuario.
        :return: Respuesta en lenguaje natural.
        """
        if not consulta:
            return "Por favor, ingresa una consulta válida."
            
        consulta = consulta.lower()
        
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

    # [... resto de la clase sin cambios ...]
