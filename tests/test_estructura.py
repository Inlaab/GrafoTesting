import unittest
import sys
import os
from pathlib import Path

# Agregar el directorio raíz al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grafo import Grafo

class TestEstructuraGrafo(unittest.TestCase):
    def setUp(self):
        self.grafo = Grafo()

    def test_existencia_archivos(self):
        """Verifica que existan todos los archivos JSON necesarios"""
        archivos_requeridos = [
            'kb/servicios_activos.json',
            'kb/consultores_activos.json',
            'kb/ubicaciones_geo.json',
            'kb/franjas_horarias.json',
            'kb/matriz_distancias.json',
            'kb/tarifas_servicios.json',
            'kb/capacidad_operativa.json'
        ]
        
        for archivo in archivos_requeridos:
            self.assertTrue(Path(archivo).exists(), f"Archivo {archivo} no encontrado")

    def test_estructura_grafo(self):
        """Verifica que el grafo tenga la estructura básica correcta"""
        self.assertIsNotNone(self.grafo.nodos)
        self.assertIsNotNone(self.grafo.aristas)
        self.assertTrue(len(self.grafo.nodos) > 0)
        self.assertTrue(len(self.grafo.aristas) > 0)

    def test_tipos_nodos(self):
        """Verifica que existan todos los tipos de nodos requeridos"""
        tipos_requeridos = [
            'Servicios',
            'Consultores',
            'Ubicaciones',
            'Franjas_Horarias',
            'Distancias',
            'Tarifas',
            'Capacidad'
        ]
        
        for tipo in tipos_requeridos:
            self.assertIn(tipo, self.grafo.nodos)

if __name__ == '__main__':
    unittest.main()