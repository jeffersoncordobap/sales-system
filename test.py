from repositories.product_repository import RepositorioProducto
from models.product import Producto
from database.connection import ConexionDB


def test_listar_productos():
    db = ConexionDB()
    repo = RepositorioProducto(db.conectar())
    lista_productos = repo.listar_productos()
    print(lista_productos)
    
test_listar_productos()