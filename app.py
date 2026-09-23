from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def home():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "postgres"),
        port=5432,
        database=os.getenv("DB_NAME", "pythonapp"),
        user=os.getenv("DB_USER", "admin"),
        password=os.getenv("DB_PASSWORD")
    )

    cur = conn.cursor()
    cur.execute("SELECT id, name FROM users ORDER BY id;")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    users = [{"id": row[0], "name": row[1]} for row in rows]

    return jsonify(
        message="Python App connected to PostgreSQL",
        users=users
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
