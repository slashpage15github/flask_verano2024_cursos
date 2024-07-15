#import model.package_model.Curso as Curso
from model.package_model.Curso import Curso

from datetime import datetime,date,time
#obj_curso = Curso.Curso()
# lista_cursos = obj_curso.obtener_cursos()

# if lista_cursos!=None:
#          for x in lista_cursos:
#             print(x)
# else:
#      print("No se encontraron datos de cursos")
     
# print("\n=====================================\n")
# curso_id = obj_curso.obtener_curso_por_id(4)
# print(curso_id)

# print("\n======INSERTADO===========\n")
# id=0
# nom=''
# fecha=datetime.now()
# if len(nom)>2:
#     obj_curso_new=Curso.Curso(id,nom,fecha)
#     result_ins=obj_curso.agregar_curso(obj_curso_new)

#     if result_ins==1:
#         print("Registro insertado correctamente")
#     else:
#         print("Error al insertar el registro")
# else:
#     print("Un dato es incorrecto, no se puede insertar")
    
    
# print("\n======borrado===========\n")
# id=77
# result_del=obj_curso.eliminar_curso(id)
# if result_del==1:
#     print("Registro eliminado correctamente")
# else:
#     print("Error al eliminar el registro")
    

# print("\n======update===========\n")
# id=19
# nom='DESARROLLO MOVIL ANDROID'
# fecha=datetime.now()
# if len(nom)>2:
#      obj_curso_new=Curso.Curso(id,nom,fecha)
#      result_upd=obj_curso.modificar_curso(obj_curso_new)
#      if result_upd==1:
#          print("Registro actualizado correctamente")
#      else:
#          print("Error al actualizar el registro")
# else:
#      print("Un dato es incorrecto, no se puede actualizar")
     
cuantos = Curso.existe_curso('ANGULAR 14')
print(cuantos)