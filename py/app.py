from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Configuración CORS para desarrollo (ajusta los orígenes en producción)
CORS(app, resources={
    r"/sumar-matrices": {
        "origins": ["http://localhost:*", "http://127.0.0.1:*"],
        "methods": ["POST", "OPTIONS"],
        "allow_headers": ["Content-Type"],
        "supports_credentials": False
    }
})

@app.route('/sumar-matrices', methods=['POST'])
def sumar_matrices():
    try:
        # Obtener datos JSON de la solicitud
        datos = request.get_json()
        
        # Validar que se recibieron ambas matrices
        if 'matriz1' not in datos or 'matriz2' not in datos:
            return jsonify({"error": "Debe proporcionar matriz1 y matriz2"}), 400
        
        matriz1 = datos['matriz1']
        matriz2 = datos['matriz2']
        
        # Validar que son matrices válidas
        if not all(isinstance(fila, list) for fila in matriz1) or not all(isinstance(fila, list) for fila in matriz2):
            return jsonify({"error": "Las matrices deben ser arrays bidimensionales"}), 400
        
        # Validar dimensiones compatibles
        if len(matriz1) != len(matriz2) or any(len(fila1) != len(fila2) for fila1, fila2 in zip(matriz1, matriz2)):
            return jsonify({"error": "Las matrices deben tener las mismas dimensiones"}), 400
        
        # Realizar la suma
        resultado = [
            [elem1 + elem2 for elem1, elem2 in zip(fila1, fila2)]
            for fila1, fila2 in zip(matriz1, matriz2)
        ]
        
        # Devolver respuesta exitosa
        return jsonify({
            "success": True,
            "resultado": resultado,
            "dimensiones": {
                "filas": len(resultado),
                "columnas": len(resultado[0]) if resultado else 0
            }
        })
    
    except Exception as e:
        # Manejo de errores inesperados
        return jsonify({
            "success": False,
            "error": f"Error al procesar las matrices: {str(e)}"
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4500, debug=True)