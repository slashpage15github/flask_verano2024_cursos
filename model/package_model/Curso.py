import model.package_model.Database as Database
class Curso:
    def __init__(self, id_curso=0, nombre_curso='',fecha_alta=''):
        self.__id_curso=id_curso
        self.__nombre_curso=nombre_curso
        self.__fecha_alta=fecha_alta
        
    def obtener_cursos(self):
        conexion = Database.Database()
        cursos = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT ID_CURSO,NOMBRE_CURSO,FECHA_ALTA FROM catalogo_curso")
            cursos = cursor.fetchall()
        conexion.conn.close()
        return cursos
    
    def obtener_curso_por_id(self,id):
        conexion = conexion = Database.Database()
        curso = None
        with conexion.cursor as cursor:
            cursor.execute("SELECT ID_CURSO,NOMBRE_CURSO,FECHA_ALTA FROM catalogo_curso WHERE ID_CURSO = %s", (id))
            curso = cursor.fetchone()
        conexion.conn.close()
        return curso
    
    def agregar_curso(self, obj_cur):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                sql="INSERT INTO catalogo_curso(NOMBRE_CURSO,FECHA_ALTA) VALUES(%s,%s)"
                vals=(obj_cur.__nombre_curso, obj_cur.__fecha_alta)
                affected=cursor.execute(sql,vals)
                conexion.conn.commit()
                return affected
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: {0}".format(except_detail))
            finally:
                conexion.conn.close()
                
    def eliminar_curso(self, id):
        conexion = Database.Database()
        affected = 0
        with conexion.cursor as cursor:
            try:
                sql="DELETE FROM catalogo_curso WHERE ID_CURSO = %s"
                vals=(id)
                affected=cursor.execute(sql,vals)
                conexion.conn.commit()
                return affected
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: {0}".format(except_detail))
            finally:
                conexion.conn.close()
                
    def modificar_curso(self, obj_cur):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                sql="UPDATE catalogo_curso SET NOMBRE_CURSO = %s, FECHA_ALTA = %s WHERE ID_CURSO = %s"
                vals=(obj_cur.__nombre_curso, obj_cur.__fecha_alta, obj_cur.__id_curso)
                affected=cursor.execute(sql,vals)
                conexion.conn.commit()
                return affected
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: {0}".format(except_detail))
            finally:
                conexion.conn.close()
                
    @staticmethod
    def existe_curso(nom):
        conexion = Database.Database()
        curso = None
        with conexion.cursor as cursor:
            sql="SELECT count(*) as ex FROM catalogo_curso WHERE NOMBRE_CURSO = %s"
            vals=(nom)
            cursor.execute(sql, vals)
            curso = cursor.fetchone()
        conexion.conn.close()
        return curso[0]              
                