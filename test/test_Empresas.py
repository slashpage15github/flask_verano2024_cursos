import model.package_model.Empresa as Empresa
db = Empresa.Empresa()
lista=db.obtener_empresa()
print(lista)

print("************************************")

lista_id = db.obtener_empresas_por_id(4)
print(lista_id)