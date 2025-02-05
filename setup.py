import os

def crear_estructura(base_path):
    estructura = {
        "kb": {
            "servicios_activos.json": "",
            "consultores_activos.json": "",
            "ubicaciones_geo.json": "",
            "franjas_horarias.json": "",
            "matriz_distancias.json": "",
            "tarifas_servicios.json": "",
            "capacidad_operativa.json": ""
        },
        "src": {
            "grafo.py": "",
            "main.py": ""
        },
        "README.md": ""
    }

    for nombre, contenido in estructura.items():
        path = os.path.join(base_path, nombre)
        if isinstance(contenido, dict):
            os.makedirs(path, exist_ok=True)
            for archivo, contenido_archivo in contenido.items():
                with open(os.path.join(path, archivo), 'w') as f:
                    f.write(str(contenido_archivo))
        else:
            with open(path, 'w') as f:
                f.write(str(contenido))

# Ejemplo de uso
crear_estructura(r"E:\GitHub\GrafoTesting")