from funciones import *

app = Flask(__name__)

# Definimos las variables del entorno. Desde la shell lo haremos con "export variable = valor".
port=os.environ["PORT"]
nombrebd=os.environ["BDNAME"]
maquina=os.environ["HOST"]

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template("login.html")

    
@app.route('/inicio',methods=["GET","POST"])
def inicio():
    if request.method == 'POST' and 'usuario' in request.form and 'contraseña' in request.form:
        usuario=request.form.get("usuario")
        contraseña=request.form.get("contraseña")
        nombrebd="2asir"
        maquina="localhost"
        db=Conectar_BD(maquina,usuario,contraseña,nombrebd)
        if db is not None:
            registros=Mostrar_profesores_y_asignaturas(db)
            return render_template('inicio.html',registros=registros)
        else:
            error="Error, credenciales incorrectas."
            return render_template("login.html",respuesta=error)
    else:
        return render_template("login.html")

app.run('0.0.0.0',int(port),debug=False)