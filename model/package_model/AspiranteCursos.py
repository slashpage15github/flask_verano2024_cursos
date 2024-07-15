import model.package_model.Database as Database
from flask import jsonify
class AspiranteCursos:
    def __init__(self, id_curso='',rfc='',fecha_registro=''):
        self.__id_curso=id_curso
        self.__rfc=rfc
        self.__fecha_registro=fecha_registro

    @staticmethod    
    def existe_curso(id_curso):
        conexion = conexion = Database.Database()
        aspirantecurso = None
        with conexion.cursor as cursor:
            cursor.execute(
                "SELECT count(*) as ex FROM aspirantes_cursos WHERE ID_CURSO = %s",(id_curso))
            aspirantecurso = cursor.fetchone()
        conexion.conn.close()
        #return jsonify(aspirante[0])    
        return aspirantecurso[0]
    
    @staticmethod    
    def existe_aspirantecursos(id_curso,rfc):
        conexion = conexion = Database.Database()
        aspirantecurso = None
        with conexion.cursor as cursor:
            cursor.execute(
                "SELECT count(*) as ex FROM aspirantes_cursos WHERE ID_CURSO=%s and RFC = %s", (id_curso,rfc))
            aspirantecurso = cursor.fetchone()
        conexion.conn.close()
        return aspirantecurso[0]    
    
    def insertar_aspirantecurso(self, obj_asp):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                query="INSERT INTO aspirantes_cursos(ID_CURSO,RFC,FECHA_REGISTRO) VALUES (%s, %s, %s)"
                vals=(obj_asp.__id_curso, obj_asp.__rfc,obj_asp.__fecha_registro)
                print(query,vals)
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
    
    def eliminar_aspirantecurso(self,id_curso,rfc):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            affected=cursor.execute("DELETE FROM aspirantes_cursos WHERE ID_CURSO=%s and RFC = %s", (id_curso,rfc))
        conexion.conn.commit()
        conexion.conn.close()
        return affected
    
    def actualizar_aspirante(self, id_curso,rfc,id_curso_new ):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            affected=cursor.execute("UPDATE aspirantes_cursos SET ID_CURSO = %s WHERE ID_CURSO=%s AND RFC =%s",(id_curso_new,id_curso,rfc))
        conexion.conn.commit()
        conexion.conn.close()
        return affected

    def obtener_aspirantescursos(self):
        conexion = Database.Database()
        apspiran_crusos = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT * FROM aspirantes_cursos")
            apspiran_crusos = cursor.fetchall()
        conexion.conn.close()
        return apspiran_crusos
    
    def obtener_aspirantecursos_por_rfc(self,rfc):
        conexion = conexion = Database.Database()
        aspiran_cursos = None
        with conexion.cursor as cursor:
            cursor.execute(
                "SELECT * FROM aspirantes_cursos WHERE RFC = %s", (rfc))
            aspiran_cursos = cursor.fetchone()
        conexion.conn.close()
        return aspiran_cursos                