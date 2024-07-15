#para metodos estaticos
#sfrom model.package_model.Aspirante import Aspirante
# cuantos = Aspirante.existe_aspirante('PETD7407148Z1')
# print(cuantos)

#para metodos de objetos
#import model.package_model.Aspirante as Aspirante
from datetime import datetime,date,time
#obj_aspirante= Aspirante.Aspirante()
rfc='PETD740714899'
nom='david'
pat='Perez'
mat='tinoco'
id_emp=2
tel=1234567890
ema='slaspage@hotmail.com'
f_reg=datetime.now()

if (len(rfc)==13):
    from model.package_model.Aspirante import Aspirante
    cuantos = Aspirante.existe_aspirante(rfc)
    if cuantos==0:
        import model.package_model.Aspirante as Aspirante
        obj_aspirante= Aspirante.Aspirante()
        aspirante = Aspirante.Aspirante(rfc,nom,pat,mat,id_emp,tel,ema,f_reg)
        result_ins=obj_aspirante.insertar_aspirante(aspirante)
        #print(result_ins)
        if result_ins=='1':
            print("Registro insertado correctamente")
        else:
            print("Regitro no insertado correctamente")
    else:
        print("El RFC ya existe")
else:
    print("El RFC debe tener 13 caracteres")