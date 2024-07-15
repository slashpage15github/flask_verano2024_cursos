import model.package_model.Database as Database
from flask import jsonify
class Aspirante:
    def __init__(self, rfc='', nombre='', paterno='', materno='',id_empresa=0, telefono=0, email='', fecha_registro=''):
        self.__rfc=rfc
        self.__nombre=nombre
        self.__paterno=paterno
        self.__materno=materno
        self.__id_empresa=id_empresa
        self.__telefono=telefono
        self.__email=email
        self.__fecha_registro=fecha_registro
    
    @staticmethod    
    def existe_aspirante(rfc):
        conexion = conexion = Database.Database()
        aspirante = None
        with conexion.cursor as cursor:
            cursor.execute(
                "SELECT count(*) as ex FROM aspirantes WHERE RFC = %s", rfc)
            aspirante = cursor.fetchone()
        conexion.conn.close()
        #return jsonify(aspirante[0])    
        return aspirante[0]    
    
    def insertar_aspirante(self, obj_asp):
        #return obj_asp.__rfc
        #return obj_asp
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                query="INSERT INTO aspirantes(RFC,NOMBRE,PATERNO,MATERNO,ID_EMPRESA,TELEFONO,EMAIL,FECHA_REGISTRO) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                vals=(obj_asp.__rfc, obj_asp.__nombre, obj_asp.__paterno,obj_asp.__materno,obj_asp.__id_empresa,obj_asp.__telefono,obj_asp.__email,obj_asp.__fecha_registro)
                #print(query,vals)
                #return (query % vals) ver sentencia
                affected=cursor.execute(query,vals)
                conexion.conn.commit()
                return str(cursor.rowcount)
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
            finally:
                conexion.conn.close() 
    
    def eliminar_aspirante(self,rfc):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            affected=cursor.execute("DELETE FROM aspirantes WHERE RFC = %s", (rfc))
        conexion.conn.commit()
        conexion.conn.close()
        return affected
    
    def actualizar_aspirante(self, obj_asp ):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            affected=cursor.execute("UPDATE aspirantes SET ID_EMPRESA = %s, NOMBRE = %s, PATERNO = %s, MATERNO = %s, TELEFONO = %s, EMAIL = %s, FECHA_REGISTRO=%s WHERE RFC = %s",
                       obj_asp.__id_empresa, obj_asp.__nombre, obj_asp.__paterno,obj_asp.__materno,obj_asp.__telefono,obj_asp.__email,obj_asp.__fecha_registro)
        conexion.conn.commit()
        conexion.conn.close()
        return affected

    def obtener_aspirantes(self):
        conexion = Database.Database()
        students = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT * FROM aspirantes")
            students = cursor.fetchall()
        conexion.conn.close()
        return students
    
    def obtener_aspirante_por_rfc(rfc):
        conexion = conexion = Database.Database()
        student = None
        with conexion.cursor as cursor:
            cursor.execute(
                "SELECT * FROM aspirantes WHERE RFC = %s", (rfc))
            student = cursor.fetchone()
        conexion.conn.close()
        return student                