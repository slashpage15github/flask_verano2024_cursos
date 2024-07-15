import model.package_model.Database as Database
class Usuarios:
    def __init__(self, usuario='', password='',nombre=''):
        self.__usuario=usuario
        self.__password=password
        self.__nombre=nombre
        
    def obtener_usuarios(self):
        conexion = Database.Database()
        cursos = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT usuario,pwd,nombre FROM usuarios")
            cursos = cursor.fetchall()
        conexion.conn.close()
        return cursos
    
    @staticmethod
    def verifica_usuario(usuario,password):
        conexion = conexion = Database.Database()
        curso = None
        with conexion.cursor as cursor:
            cursor.execute("SELECT count(*) as cuantos FROM usuarios WHERE usuario = %s and pwd=%s", (usuario,password))
            curso = cursor.fetchone()
        conexion.conn.close()
        return curso[0]
    
    def verifica_usuario_datos(self,usuario,password):
        conexion = conexion = Database.Database()
        curso = None
        with conexion.cursor as cursor:
            cursor.execute("SELECT usuario,nombre FROM usuarios WHERE usuario = %s and pwd= %s ", (usuario,password))
            curso = cursor.fetchone()
        conexion.conn.close()
        return curso                    