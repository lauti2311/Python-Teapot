from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

damaged_system = None

@app.route('/status', methods=['GET'])
def status():
    global damaged_system
    systems = ["navigation", "communications", "life_support", "engines", "deflector_shield"]
    damaged_system = systems[0]  # Puedes usar random.choice(systems) para seleccionar uno al azar
    return jsonify({"damaged_system": damaged_system})

@app.route('/repair-bay', methods=['GET'])
def repair_bay():
    global damaged_system
    system_codes = {
        "navigation": "NAV-01",
        "communications": "COM-02",
        "life_support": "LIFE-03",
        "engines": "ENG-04",
        "deflector_shield": "SHLD-05"
    }
    code = system_codes.get(damaged_system, "UNKNOWN")
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Repair</title>
    </head>
    <body>
    <div class="anchor-point">{code}</div>
    </body>
    </html>
    """
    return html

# Tercera Llamada: POST /teapot
@app.route('/teapot', methods=['POST'])
def teapot():
    return '', 418

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)