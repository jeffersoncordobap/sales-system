import sqlite3
import os

class ConexionDB:
    def __init__(self):
        self.db_path = os.path.join("database", "store.db")
        self.schema_path = os.path.join("database", "schema.sql")

    def conectar(self):
        """Crea la conexión y activa las llaves foráneas."""
        try:
            conn = sqlite3.connect(self.db_path)
            conn.execute("PRAGMA foreign_keys = ON;")
            return conn
        except sqlite3.Error as e:
            print(f"Error al conectar: {e}")
            return None

    def inicializar_db(self):
        """Ejecuta el schema.sql si el archivo no existe o está vacío."""
        if not os.path.exists(self.db_path) or os.path.getsize(self.db_path) == 0:
            print("Inicializando base de datos desde el esquema...")
            conn = self.conectar()
            if conn:
                try:
                    with open(self.schema_path, "r", encoding="utf-8") as f:
                        script_sql = f.read()
                    conn.executescript(script_sql)
                    conn.commit()
                    print("¡Base de datos creada exitosamente!")
                except Exception as e:
                    print(f"Error cargando el esquema: {e}")
                finally:
                    conn.close()
        else:
            print("Base de datos ya existente.")
