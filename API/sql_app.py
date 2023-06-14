from flask import Flask,request, jsonify,render_template
import psycopg2
import psycopg2.extras

def select_all():
    conn= connexion()
    cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT * FROM data")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
def select_one_id(id):
    conn= connexion()
    cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cursor.execute(f"SELECT * FROM data WHERE id = {id}")
    result = cursor.fetchone()
    return result
def insert_one(tuple):
    conn= connexion()
    cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    try:
        cursor.execute(f"INSERT INTO data (id,name,value) VALUES {(tuple[0],tuple[1],tuple[2])}")
        result = {"State":"Sucess"}
    except Exception as e:
        print(e)
        result = {"State":"Echec"}
    cursor.close()
    conn.commit()
    conn.close()
    return result
def update_one(id,tuple):
    conn= connexion()
    cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    try:
        cursor.execute(f"UPDATE data SET id = {tuple[0]}, name = '{tuple[1]}', value = '{tuple[2]}' WHERE id = {id} ;")
        result = {"State":"Sucess"}
    except Exception as e:
        print("except")
        result = {"State":"Echec"}
    conn.commit()
    cursor.close()
    conn.close()
    return result
def delete_one(id):
    conn= connexion()
    cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    try:
        cursor.execute(f"DELETE FROM data WHERE id = {id};")
        result = {"State":"Sucess"}
    except Exception as e:
        print(e)
        result = {"State":"Echec"}
        
    cursor.close()
    conn.commit()
    conn.close()
    return result

def connexion():
    try:
        conn = psycopg2.connect(
            user = "jwxpkqbn",
            password = "i-WIDluzGYUI0t21LS7W4XUNN7aQssx0",
            host = "babar.db.elephantsql.com",
            port = "5432",
            database = "jwxpkqbn"
        )
        return conn
    except (Exception, psycopg2.Error) as error :
        print ("Erreur lors de la connexion à PostgreSQL", error)

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return render_template("login.html")


@app.route('/api/select-all', methods=['GET'])
def api_select_all():

    return jsonify(select_all())

@app.route('/api/insert-one', methods=['GET','POST'])
def api_insert_one():
    if request.method == "POST":
        return jsonify(insert_one((request.form["id"],request.form["name"],request.form["value"])))
    return render_template("login.html")

@app.route('/api/select-one', methods=['GET','POST'])
def api_select_one():
    if request.method == "POST":
        return jsonify(select_one_id(request.form["id"]))
    return render_template("login.html")

@app.route('/api/update-one/', methods=['GET','POST'])
def api_update_one():
    if request.method == "POST":
        return jsonify(update_one(request.form["replaceId"],(request.form["id"],request.form["name"],request.form["value"])))
    return render_template("login.html")

@app.route('/api/delete-one', methods=['GET','POST'])
def api_delete_one():
    if request.method == "POST":
        return jsonify(delete_one(request.form["id"]))
    return render_template("login.html")
# @app.route('/api/select-all', methods=['GET'])
# def api_select_all():

#     return jsonify(select_all())

# @app.route('/api/select-one/<int:id>', methods=['GET'])
# def api_select_one(id):

#     return jsonify(select_one_id(id))

# @app.route('/api/insert-one/<insert>', methods=['GET'])
# def api_insert_one(insert):
#     liste = insert[1:-1].split(",")
#     return jsonify(insert_one(liste))

# @app.route('/api/update-one/<int:id>/<update>', methods=['GET'])
# def api_update_one(id,update):
#     liste = update[1:-1].split(",")
#     return jsonify(update_one(id,liste))

# @app.route('/api/delete-one/<int:id>', methods=['GET'])
# def api_delete_one(id):
#     return jsonify(delete_one(id))

app.run()
