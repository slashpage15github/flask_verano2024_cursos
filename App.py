from flask import Flask,render_template,url_for,request,flash,redirect
import model.package_model.Empresa as Empresa
import model.package_model.Curso as Curso
import model.package_model.Aspirante as Aspirante_obj
import model.package_model.AspiranteCursos as AspiranteCursos_o
from datetime import datetime,date,time

#import metodos static
from model.package_model.Aspirante import Aspirante
from model.package_model.AspiranteCursos import AspiranteCursos

app = Flask(__name__)
app.config['SECRET_KEY'] = 'j\x86\x14\xcc:\x99\xb3\x91\xf8/Bv\r\xaa"\xf1\x8a\xfa(A\xa1\xe2\x85\xd6'

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


if __name__ == "__main__":
    app.run(debug=True)

