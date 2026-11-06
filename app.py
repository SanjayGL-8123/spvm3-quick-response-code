import os
import jinja2
import mysql.connector
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

load_dotenv()
app = Flask(__name__)

# Search for templates in both 'templates/' and project root folder
base_dir = os.path.dirname(os.path.abspath(__file__))
app.jinja_loader = jinja2.ChoiceLoader([
    jinja2.FileSystemLoader(os.path.join(base_dir, "templates")),
    jinja2.FileSystemLoader(base_dir),
])

def db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"), user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""), database=os.getenv("DB_NAME", "qr_studio"))

def query(sql, args=(), fetch=False):
    con = db(); cur = con.cursor(dictionary=True)
    cur.execute(sql, args)
    rows = cur.fetchall() if fetch else None
    con.commit(); last = cur.lastrowid; cur.close(); con.close()
    return rows if fetch else last

@app.route("/")
def index():
    return render_template("index.html")

@app.post("/api/save")
def save():
    d = request.get_json(force=True)
    if not d.get("content"):
        return jsonify(error="Content is empty"), 400
    try:
        new_id = query(
            "INSERT INTO qr_codes (name,qr_type,content,module_shape,eye_style,fg_color,bg_color,png_data,frame_style,occasion,frame_text) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (d.get("name") or "Untitled", d["type"], d["content"], int(d["shape"]), int(d["eye"]),
             d["fg"], d["bg"], d.get("png"), int(d.get("frame", 0)), int(d.get("occ", 0)),
             (d.get("ftext") or "")[:120]))
        return jsonify(id=new_id)
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.get("/api/history")
def history():
    try:
        rows = query("SELECT id,name,qr_type,content,module_shape,eye_style,fg_color,bg_color,png_data,"
                     "created_at FROM qr_codes ORDER BY id DESC LIMIT 50", fetch=True)
        for r in rows:
            r["created_at"] = str(r["created_at"])
        return jsonify(rows or [])
    except Exception as e:
        return jsonify([])

@app.delete("/api/history/<int:qid>")
def delete(qid):
    try:
        query("DELETE FROM qr_codes WHERE id=%s", (qid,))
        return jsonify(ok=True)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(debug=True)
