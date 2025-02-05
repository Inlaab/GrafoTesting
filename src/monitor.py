import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import sys

# Agregar la ruta del directorio principal del proyecto
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grafo import Grafo

class Watcher:
    DIRECTORY_TO_WATCH = "kb"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        elif event.event_type == 'modified':
            # Aquí es donde actualizamos el grafo
            print(f"Archivo modificado: {event.src_path}")
            actualizar_grafo()

def actualizar_grafo():
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

if __name__ == '__main__':
    w = Watcher()
    w.run()