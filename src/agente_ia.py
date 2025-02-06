import math

class AgenteIA:
    def __init__(self, grafo):
        """
        Inicializar el Agente IA con un grafo.
        
        :param grafo: Instancia de la clase Grafo.
        """
        self.grafo = grafo

    # ANÁLISIS DE PROXIMIDAD REAL
    def calcular_distancia(self, origen, destino):
        """
        Calcular la distancia entre dos puntos usando coordenadas.
        
        :param origen: Coordenadas del punto de origen.
        :param destino: Coordenadas del punto de destino.
        :return: Distancia calculada.
        """
        distancia = math.sqrt((destino[0] - origen[0]) ** 2 + (destino[1] - origen[1]) ** 2)
        return distancia

    def evaluar_rutas_alternativas(self, origen, destino):
        """
        Evaluar rutas alternativas para reducir tiempo de viaje.
        
        :param origen: Coordenadas del punto de origen.
        :param destino: Coordenadas del punto de destino.
        :return: Ruta óptima.
        """
        # Implementar evaluación de rutas alternativas
        pass

    def asignar_servicio_a_consultor(self, servicio_id):
        """
        Asignar un servicio al consultor más cercano disponible.
        
        :param servicio_id: ID del servicio a asignar.
        :return: ID del consultor asignado o None si no hay consultores disponibles.
        """
        servicio = self.grafo.nodos['Servicios'][servicio_id]
        ubicacion_servicio = servicio['ubicacion']
        consultores_disponibles = []

        # Buscar consultores disponibles
        for consultor in self.grafo.nodos['Consultores']:
            if self.verificar_disponibilidad(consultor['id'], servicio['fecha'], servicio['hora']):
                distancia = self.calcular_distancia(consultor['ubicacion'], ubicacion_servicio)
                consultores_disponibles.append((consultor['id'], distancia))

        # Ordenar consultores por distancia
        consultores_disponibles.sort(key=lambda x: x[1])

        if consultores_disponibles:
            consultor_asignado = consultores_disponibles[0][0]
            print(f"Servicio {servicio_id} asignado al consultor {consultor_asignado}")
            return consultor_asignado
        else:
            print("No hay consultores disponibles.")
            return None

    def determinar_punto_inicio_optimo(self, puntos):
        """
        Determinar el punto de inicio óptimo para una ruta.
        
        :param puntos: Lista de puntos de la ruta.
        :return: Punto de inicio óptimo.
        """
        # Implementar lógica para determinar el punto de inicio óptimo
        pass

    # MATRIZ DE DECISIÓN ACTUALIZADA
    def proximidad_real_a_base(self, consultor_id, base_id):
        """
        Calcular la proximidad real de un consultor a una base.
        
        :param consultor_id: ID del consultor.
        :param base_id: ID de la base.
        :return: Distancia calculada.
        """
        consultor = self.grafo.nodos['Consultores'][consultor_id]
        base = self.grafo.nodos['Ubicaciones'][base_id]
        return self.calcular_distancia(consultor['ubicacion'], base['ubicacion'])

    def capacidad_cumplir_prioridades(self, consultor_id, servicio_id):
        """
        Evaluar la capacidad de un consultor para cumplir con las prioridades de un servicio.
        
        :param consultor_id: ID del consultor.
        :param servicio_id: ID del servicio.
        :return: True si puede cumplir, False en caso contrario.
        """
        # Implementar lógica para evaluar la capacidad de cumplir prioridades
        pass

    def zona_predeterminada(self, consultor_id):
        """
        Obtener la zona predeterminada de un consultor.
        
        :param consultor_id: ID del consultor.
        :return: Zona predeterminada.
        """
        consultor = self.grafo.nodos['Consultores'][consultor_id]
        return consultor['zona']

    # PROTOCOLO DE VERIFICACIÓN
    def validar_horarios_permitidos(self, consultor_id, fecha, hora):
        """
        Validar si un consultor está disponible en una fecha y hora específicas.
        
        :param consultor_id: ID del consultor.
        :param fecha: Fecha de la solicitud.
        :param hora: Hora de la solicitud.
        :return: True si está disponible, False en caso contrario.
        """
        # Verificar la disponibilidad del consultor
        for franja in self.grafo.nodos['Franjas_Horarias']:
            if franja['consultor_id'] == consultor_id and franja['disponible']:
                # Verificar día de la semana y hora
                if self.validar_horario(franja, fecha, hora):
                    return True
        return False

    def pre_validacion_dia_festivos_hora(self, fecha, hora):
        """
        Pre-validar si una fecha y hora son válidas considerando días festivos.
        
        :param fecha: Fecha de la solicitud.
        :param hora: Hora de la solicitud.
        :return: True si es válida, False en caso contrario.
        """
        # Implementar lógica de pre-validación de día, festivos y hora
        pass

    def verificar_proximidad_por_punto(self, consultor_id, punto):
        """
        Verificar la proximidad de un consultor a un punto específico.
        
        :param consultor_id: ID del consultor.
        :param punto: Coordenadas del punto.
        :return: Distancia calculada.
        """
        consultor = self.grafo.nodos['Consultores'][consultor_id]
        return self.calcular_distancia(consultor['ubicacion'], punto)

    def bloqueo_automatico_solicitudes_no_validas(self, servicio_id):
        """
        Bloquear automáticamente solicitudes no válidas.
        
        :param servicio_id: ID del servicio.
        :return: True si la solicitud es válida, False en caso contrario.
        """
        servicio = self.grafo.nodos['Servicios'][servicio_id]
        if not self.pre_validacion_dia_festivos_hora(servicio['fecha'], servicio['hora']):
            print(f"Servicio {servicio_id} bloqueado por no ser válido.")
            return False
        return True

    # CONTROL DE ASIGNACIONES
    def prevalencia_proximidad_real(self, consultor_id, zona):
        """
        Dar prevalencia a la proximidad real sobre la división zonal.
        
        :param consultor_id: ID del consultor.
        :param zona: Zona predeterminada.
        :return: True si la proximidad real prevalece, False en caso contrario.
        """
        # Implementar lógica para prevalencia de proximidad real
        pass

    def documentar_excepciones(self, excepcion):
        """
        Documentar excepciones en el proceso de asignación.
        
        :param excepcion: Descripción de la excepción.
        """
        # Implementar lógica para documentar excepciones
        pass

    def control_sobrecargas(self, consultor_id):
        """
        Controlar la sobrecarga de asignaciones a un consultor.
        
        :param consultor_id: ID del consultor.
        :return: True si no hay sobrecarga, False en caso contrario.
        """
        # Implementar lógica para controlar sobrecargas
        pass

    def gestion_restricciones_horarias(self, consultor_id, fecha, hora):
        """
        Gestionar las restricciones horarias de un consultor.
        
        :param consultor_id: ID del consultor.
        :param fecha: Fecha de la solicitud.
        :param hora: Hora de la solicitud.
        :return: True si cumple con las restricciones, False en caso contrario.
        """
        return self.validar_horarios_permitidos(consultor_id, fecha, hora)

    # PROTOCOLO DE EVALUACIÓN Y ASIGNACIÓN
    def division_rutas_criterios_obligatorios(self, puntos):
        """
        Dividir rutas según criterios obligatorios.
        
        :param puntos: Lista de puntos de la ruta.
        :return: Rutas divididas.
        """
        # Implementar lógica para dividir rutas según criterios obligatorios
        pass

    def optimizacion_rutas_unicas(self, puntos):
        """
        Optimizar una ruta única para minimizar la distancia y el tiempo de viaje.
        
        :param puntos: Lista de puntos de la ruta.
        :return: Ruta optimizada.
        """
        # Implementar optimización de ruta única
        pass

    def gestion_multiples_consultores(self, servicios):
        """
        Gestionar la asignación de múltiples consultores a servicios.
        
        :param servicios: Lista de servicios a asignar.
        :return: Asignaciones de consultores.
        """
        # Implementar lógica para gestionar múltiples consultores
        pass

    def control_tiempos_distancias(self, puntos):
        """
        Controlar los tiempos y distancias de una ruta.
        
        :param puntos: Lista de puntos de la ruta.
        :return: Tiempos y distancias controlados.
        """
        # Implementar control de tiempos y distancias
        pass

    # GENERACIÓN DE RUTAS
    def generar_enlace_google_maps(self, origen, destino):
        """
        Generar un enlace de Google Maps para una ruta específica.
        
        :param origen: Coordenadas del punto de origen.
        :param destino: Coordenadas del punto de destino.
        :return: Enlace de Google Maps.
        """
        enlace = f"https://www.google.com/maps/dir/?api=1&origin={origen[0]},{origen[1]}&destination={destino[0]},{destino[1]}"
        return enlace

    def desglose_por_tramos(self, puntos):
        """
        Desglosar una ruta en tramos.
        
        :param puntos: Lista de puntos de la ruta.
        :return: Tramos desglosados.
        """
        # Implementar lógica para desglosar por tramos
        pass

    def calcular_distancias_tiempos(self, puntos):
        """
        Calcular las distancias y tiempos de una ruta.
        
        :param puntos: Lista de puntos de la ruta.
        :return: Distancias y tiempos calculados.
        """
        # Implementar cálculo de distancias y tiempos
        pass

    def secuenciacion_optimizada(self, puntos):
        """
        Optimizar la secuenciación de una ruta.
        
        :param puntos: Lista de puntos de la ruta.
        :return: Ruta secuenciada de manera óptima.
        """
        # Implementar secuenciación optimizada
        pass

    # COTIZADOR DE SERVICIOS
    def identificar_referencias_similares(self, servicio_id):
        """
        Identificar referencias similares para un servicio.
        
        :param servicio_id: ID del servicio.
        :return: Referencias similares.
        """
        # Implementar lógica para identificar referencias similares
        pass

    def calcular_rangos_proyectados(self, servicio_id):
        """
        Calcular rangos proyectados para un servicio.
        
        :param servicio_id: ID del servicio.
        :return: Rangos proyectados.
        """
        # Implementar lógica para calcular rangos proyectados
        pass

    def validar_tarifas_base(self, servicio_id):
        """
        Validar un servicio contra las tarifas base.
        
        :param servicio_id: ID del servicio.
        :return: True si es válido, False en caso contrario.
        """
        # Implementar lógica para validar tarifas base
        pass

    def presentar_opciones_tarifarias(self, servicio_id):
        """
        Presentar opciones tarifarias para un servicio.
        
        :param servicio_id: ID del servicio.
        :return: Opciones tarifarias.
        """
        # Implementar lógica para presentar opciones tarifarias
        pass

    # CONTROL DE CALIDAD Y COSTOS
    def verificar_asignaciones_optimas(self):
        """
        Verificar que las asignaciones sean óptimas.
        
        :return: True si las asignaciones son óptimas, False en caso contrario.
        """
        # Implementar lógica para verificar asignaciones óptimas
        pass

    def documentar_desviaciones(self, desviacion):
        """
        Documentar desviaciones en el proceso de asignación.
        
        :param desviacion: Descripción de la desviación.
        """
        # Implementar lógica para documentar desviaciones
        pass

    def control_costos_operativos(self):
        """
        Controlar los costos operativos de las asignaciones.
        
        :return: True si los costos son aceptables, False en caso contrario.
        """
        # Implementar lógica para controlar costos operativos
        pass

    def diferenciacion_tipo_consultor(self, consultor_id):
        """
        Diferenciar asignaciones según el tipo de consultor.
        
        :param consultor_id: ID del consultor.
        :return: Tipo de consultor.
        """
        consultor = self.grafo.nodos['Consultores'][consultor_id]
        return consultor['tipo']

    # Instrucciones adicionales
    def no_citar_fuentes(self):
        """
        Instrucción para no citar fuentes en las respuestas.
        """
        pass

    def cambiar_mensaje_consulta(self, mensaje):
        """
        Cambiar "Voy a consultar" por "consultando información...".
        
        :param mensaje: Mensaje original.
        :return: Mensaje modificado.
        """
        return mensaje.replace("Voy a consultar", "consultando información...")