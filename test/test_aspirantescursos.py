#para metodos estaticos
# from model.package_model.AspiranteCursos import AspiranteCursos
# cuantos = AspiranteCursos.existe_aspirantecursos(1,'AAAA740714832')
# print(cuantos)

#para metodos de objetos
import model.package_model.AspiranteCursos as AspiranteCursos_o
from datetime import datetime,date,time

id_curso=4
rfc='AAAA740714832'
f_reg=datetime.now()

from model.package_model.AspiranteCursos import AspiranteCursos
cuantos = AspiranteCursos.existe_aspirantecursos(id_curso,rfc)
if cuantos==0:
    obj_aspirantecurso= AspiranteCursos_o.AspiranteCursos()
    aspirantecurso = AspiranteCursos_o.AspiranteCursos(id_curso,rfc,f_reg)
    result_ins=obj_aspirantecurso.insertar_aspirantecurso(aspirantecurso)
    if result_ins=='1':
        print("Curso y RFC insertado correctamente")
    else:
        print("Curso y RFC NO insertado correctamente")
else:
    print("El aspirante ya esta registrado en el curso")