import model.package_model.Database as Database

class Empresa:
    def __init__(self, id_empresa='', nombre_empresa=''):
        self.__id_empresa = id_empresa
        self.__nombre_empresa= nombre_empresa
        
    def obtener_empresa(self):
        conexion = Database.Database()
        empresas=[]
        with conexion.cursor as cursor:
            sql = "SELECT ID_EMPRESA,NOMBRE_EMPRESA FROM empresa"
            cursor.execute(sql)
            empresas = cursor.fetchall()
        conexion.close()
        return empresas
    
    def obtener_empresas_por_id(self,id):
        conexion = Database.Database()
        empresa=[]
        with conexion.cursor as cursor:
            sql = "SELECT ID_EMPRESA,NOMBRE_EMPRESA FROM empresa WHERE ID_EMPRESA=%s"
            cursor.execute(sql,(id))
            empresa = cursor.fetchone()
        conexion.close()
        return empresa
    
    