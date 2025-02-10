import os
from grafo import Grafo

def test_estructura_basica():
    # 1. Verificar existencia de archivos
    archivos_requeridos = [
        'servicios_activos.json',
        'consultores_activos.json',
        'ubicaciones_geo.json',
        'franjas_horarias.json',
        'matriz_distancias.json',
        'tarifas_servicios.json',
        'capacidad_operativa.json'
    ]
    
    for archivo in archivos_requeridos:
        ruta = os.path.join('kb', archivo)
        if not os.path.exists(ruta):
            print(f"Error: No se encuentra {ruta}")
            return False

    # 2. Intentar crear el grafo
    try:
        grafo = Grafo()
        print("✓ Grafo creado exitosamente")
        
        # 3. Verificar estructura básica
        if not grafo.nodos:
            print("Error: No hay nodos cargados")
            return False
            
        if not grafo.aristas:
            print("Error: No hay aristas definidas")
            return False
            
        # 4. Mostrar estructura
        print("\nEstructura del grafo:")
        grafo.mostrar_grafo()
        
        return True
        
    except Exception as e:
        print(f"Error al crear/verificar el grafo: {str(e)}")
        return False

if __name__ == "__main__":
    resultado = test_estructura_basica()
    print(f"\nResultado final: {'✓ OK' if resultado else '✗ Error'}")