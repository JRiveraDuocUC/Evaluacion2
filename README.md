# Evaluacion2

Mejora de un prototipo de geolocalización para la Biblioteca Nacional.
El script `graphhopper_es.py` usa la API de GraphHopper (geocodificación y rutas)
y muestra la ruta paso a paso en español.

## Qué hace
- Pide una ubicación de partida y un destino y los convierte en coordenadas.
- Calcula la ruta e imprime distancia, duración e indicaciones en español.
- Todos los valores numéricos se muestran con máximo 2 decimales.
- Se termina escribiendo `s` o `salir`.

## Requisitos
- Python 3 y la librería `requests`.
- Una API key de GraphHopper (https://www.graphhopper.com/).

## Ejecución
    git clone https://github.com/JRiveraDuocUC/Evaluacion2.git
    cd Evaluacion2
    # Reemplace TU_API_KEY en la línea 7 de graphhopper_es.py por su API key
    python3 graphhopper_es.py

## Ejemplo
    Ubicación de partida (s/salir para terminar): Santiago, Chile
    Destino (s/salir para terminar): Biblioteca Nacional, Santiago
