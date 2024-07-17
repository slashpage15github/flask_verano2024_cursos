from flask import Flask,render_template,url_for,request,flash,redirect,jsonify,session
import model.package_model.Empresa as Empresa
import model.package_model.Curso as Curso
import model.package_model.Aspirante as Aspirante_obj
import model.package_model.AspiranteCursos as AspiranteCursos_o
import model.package_model.Usuarios as Usuarios_o
from datetime import datetime,date,time
import jsonpickle
import json

#import metodos static
from model.package_model.Aspirante import Aspirante
from model.package_model.AspiranteCursos import AspiranteCursos
from model.package_model.Usuarios import Usuarios

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SECRET_KEY'] = 'j\x86\x14\xcc:\x99\xb3\x91\xf8/Bv\r\xaa"\xf1\x8a\xfa(A\xa1\xe2\x85\xd6'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/db_cursos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class EmpresaORM(db.Model):
    __tablename__ = "empresa"
    ID_EMPRESA = db.Column(db.Integer, primary_key=True, autoincrement=True)
    NOMBRE_EMPRESA = db.Column(db.String(30))
    
    
    def __init__(self, nombre_empresa):
        self.NOMBRE_EMPRESA = nombre_empresa
         
with app.app_context():
    db.create_all()
    
class EmpresaORMSchema(ma.Schema):
    class Meta:
         fields = ('ID_EMPRESA','NOMBRE_EMPRESA')
    
empresa_schema = EmpresaORMSchema()
empresas_schema = EmpresaORMSchema(many=True)
        
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aspirante')
def add_aspirante():
    obj_emp= Empresa.Empresa()
    obj_cur= Curso.Curso()
    lista_empresas=obj_emp.obtener_empresa()
    lista_cursos=obj_cur.obtener_cursos()
    return render_template('aspirante.html', lista_empresas=lista_empresas, lista_cursos=lista_cursos)

@app.route('/registra', methods=['POST'])
def registra_aspirante():
    _rfc=request.form['f_rfc'].upper()
    _nom=request.form['f_nombre'].upper()
    _pat=request.form['f_paterno'].upper()
    _mat=request.form['f_materno'].upper()
    _tel=request.form['f_telefono']
    _id_emp=request.form['f_empresa']
    _ema=request.form['f_email']
    _fec=datetime.now()
    _id_curso=request.form['f_curso']
    
    cuantos_aspiran=Aspirante.existe_aspirante(_rfc)
    if cuantos_aspiran ==1:
        #1= validar que el curso a insertar no exista con ese rfc
        #2=si ya existe el curso y rfc , no insertar y avisar de lo contrario insertamos solo en aspirantecursos
        cuantos = AspiranteCursos.existe_aspirantecursos(_id_curso,_rfc)
        if cuantos==0:
            obj_asp_cur=AspiranteCursos_o.AspiranteCursos(_id_curso,_rfc,_fec)
            res=obj_asp_cur.insertar_aspirantecurso(obj_asp_cur)
            #return render_template('auxilia.html',res=res,res_cur='',msj='Como el rfc ya existe solo se inserta curso')
            flash(f"Curso agregado correctamente","success")
            return redirect(url_for('add_aspirante'))
        else:
            #return render_template('auxilia.html',res='',res_cur='',msj="El RFC y Curso  ya existen")
            flash(f"Aspirante y curso ya registrado","Error")
            return redirect(url_for('add_aspirante'))
    else:
        obj_asp= Aspirante_obj.Aspirante(_rfc,_nom,_pat,_mat,_id_emp,_tel,_ema,_fec)
        res=obj_asp.insertar_aspirante(obj_asp)
        obj_asp_cur=AspiranteCursos_o.AspiranteCursos(_id_curso,_rfc,_fec)
        res_cur=obj_asp_cur.insertar_aspirantecurso(obj_asp_cur)
        #return render_template('auxilia.html',res=res,res_cur=res_cur,msj='inserte en ambas tablas que es por prinmera vez del registro')
        flash(f"Aspirante y curso registrado correctamente","success")
        return redirect(url_for('add_aspirante'))

@app.route("/lista_cursos",methods=["POST","GET"])
def lista_cursos():
    obj_cur= Curso.Curso()
    lista_cursos = obj_cur.obtener_cursos()
    return render_template('lista_cursos.html',lista_cursos=lista_cursos)

@app.route("/add_curso",methods=['POST'])
def add_curso():
    _f_id=request.form['f_id']
    _f_nombre=request.form['f_nombre'].upper()
    _fec=datetime.now()
    if _f_id=='':
        obj_cur= Curso.Curso(_f_id,_f_nombre,_fec)
        res_cur=obj_cur.agregar_curso(obj_cur)
        return str(res_cur)
    else:
        obj_cur= Curso.Curso(_f_id,_f_nombre,_fec)
        res_cur=obj_cur.modificar_curso(obj_cur)
        return str(res_cur)
    
@app.route("/ver_detalle_curso_data",methods=['POST'])
def ver_detalle_curso_data():
    _curso_id=request.form['curso_id']
    obj_cur= Curso.Curso()
    datos_curso=obj_cur.obtener_curso_por_id(_curso_id)
    data = { 
            "id" : datos_curso[0], 
            "nombre" : datos_curso[1],
            "fecha" : datos_curso[2], 
        } 
    return jsonify(data)
    #return str(datos_curso)
    
@app.route("/ver_detalle_curso",methods=['POST'])
def ver_detalle_curso():
    _curso_id=request.form['curso_id']
    obj_cur= Curso.Curso()
    datos_curso=obj_cur.obtener_curso_por_id(_curso_id)
    return render_template('ver_detalle_curso.html',datos_curso=datos_curso)
    #return str(res_cur)
    
@app.route("/delete_curso",methods=['POST'])
def delete_curso():
    _curso_id=request.form['id']
    cuantos_cursos=AspiranteCursos.existe_curso(_curso_id)
    if cuantos_cursos == 0:
        obj_cur= Curso.Curso()
        datos_curso=obj_cur.eliminar_curso(_curso_id)
        return str(datos_curso)
    else:
        return "-1"
    
@app.route("/valida_usuario",methods=['GET','POST'])
def valida_usuario():
    if request.method=='POST':
        username=request.form['js_us']
        password=request.form['js_pw']
        existe=Usuarios.verifica_usuario(username,password)
        return str(existe)
    
@app.route("/sesion_usuario",methods=['GET','POST'])
def sesion_usuario():
    if request.method=='POST':
        username=request.form['js_us']
        password=request.form['js_pw']
        obj_user= Usuarios()
        user_datos=obj_user.verifica_usuario_datos(username,password)
        session['user_id']=user_datos[0]
        session['user_name']=user_datos[1]
        
        data = { 
            "id" : user_datos[0], 
            "nombre" : user_datos[1],
        } 
        return jsonify(data)
    
@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('user_id', None)
   session.pop('user_name', None)
   return redirect(url_for('index'))


@app.route('/add_empresa')
def add_empresa():
    return render_template('add_empresa.html')

@app.route("/registra_empresa",methods=['POST'])
def registra_empresa():
    _f_nombre=request.form['f_nombre'].upper()
    #print("hola:",_f_nombre)
    new_empre= EmpresaORM(_f_nombre)
    #print("hello:",new_empre)
    db.session.add(new_empre)
    db.session.commit()
    flash(f"Empresa registrada Correctamente","Success")
    return redirect(url_for('add_empresa'))

if __name__ == "__main__":
    app.run(debug=True)

