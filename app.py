from flask import Flask, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Configurazione database
db_config = {
    'user': 'avnadmin',         # Sostituisci con il tuo username
    'password': 'AVNS_balPQpZCbrzbAw3-iGY',     # Sostituisci con la tua password
    'host': 'mysql-8c1d16d-iisgalvanimi-a23f.g.aivencloud.com',  # Sostituisci con l'host fornito da Aiven
    'port': 14529,                  # Porta di default per Aiven MySQL
    'database': 'DB_seminario'       # Nome del database
}

@app.route('/')
def homepage():
    return render_template('homepage.html')
@app.route('/visualizza/<string:table_name>', methods=['GET'])
def visualizza_tabella(table_name):
    try:
        # Connessione al database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)  # Usa dictionary=True per ottenere risultati come dict

        # Query dinamica per la tabella specificata
        query = f"SELECT * FROM {table_name};"
        cursor.execute(query)
        result = cursor.fetchall()
        
        # Chiude il cursore e la connessione
        cursor.close()
        conn.close()
        
        return jsonify(result)
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    except Exception as e:
        return jsonify({'error': 'Errore generico', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)