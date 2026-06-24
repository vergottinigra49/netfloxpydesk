import psycopg2
from psycopg2 import Error

def conectar_db():
    """Establece la conexión con el servidor de PostgreSQL."""
    try:
        conexion = psycopg2.connect(
            host="localhost",
            database="netflox_db",  # Nombre de la base de datos
            user="postgres",       # Tu usuario de Postgres (suele ser postgres)
            password="grace77", # TU CONTRASEÑA REAL DE POSTGRES
            port="5432"            # Puerto por defecto de Postgres
        )
        return conexion
    except (Exception, Error) as error:
        print("Error al conectar a PostgreSQL:", error)
        return None

def crear_tabla():
    """Crea la tabla de películas si no existe en la base de datos."""
    conexion = conectar_db()
    if conexion is None:
        return
        
    try:
        cursor = conexion.cursor()
        # En Postgres usamos SERIAL en lugar de AUTOINCREMENT
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS peliculas (
                id SERIAL PRIMARY KEY,
                titulo VARCHAR(150) NOT NULL,
                genero VARCHAR(100) NOT NULL,
                anio INTEGER NOT NULL
            )
        """)
        conexion.commit()
        print("Tabla 'peliculas' verificada/creada con éxito en PostgreSQL.")
    except (Exception, Error) as error:
        print("Error al crear la tabla:", error)
    finally:
        if conexion:
            cursor.close()
            conexion.close()

# ==========================================
#                  C.R.U.D.
# ==========================================

def insertar_pelicula(titulo, genero, anio):
    """CREATE: Inserta una nueva película en PostgreSQL."""
    conexion = conectar_db()
    if conexion is None: return
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO peliculas (titulo, genero, anio) 
            VALUES (%s, %s, %s)
        """, (titulo, genero, anio))
        conexion.commit()
        print(f"Película '{titulo}' agregada correctamente.")
    except (Exception, Error) as error:
        print("Error al insertar:", error)
    finally:
        if conexion:
            cursor.close()
            conexion.close()

def listar_peliculas():
    """READ: Devuelve una lista con todas las películas."""
    conexion = conectar_db()
    peliculas = [] # Así estaba definido
    if conexion is None: return peliculas # <-- CORREGIDO AQUÍ
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT id, titulo, genero, anio FROM peliculas")
        peliculas = cursor.fetchall()
    except (Exception, Error) as error:
        print("Error al listar:", error)
    finally:
        if conexion:
            cursor.close()
            conexion.close()
    return peliculas #

def modificar_pelicula(id_pelicula, nuevo_titulo, nuevo_genero, nuevo_anio):
    """UPDATE: Modifica los datos de una película mediante su ID."""
    conexion = conectar_db()
    if conexion is None: return
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE peliculas 
            SET titulo = %s, genero = %s, anio = %s 
            WHERE id = %s
        """, (nuevo_titulo, nuevo_genero, nuevo_anio, id_pelicula))
        conexion.commit()
        print(f"Película ID {id_pelicula} actualizada correctamente.")
    except (Exception, Error) as error:
        print("Error al modificar:", error)
    finally:
        if conexion:
            cursor.close()
            conexion.close()

def borrar_pelicula(id_pelicula):
    """DELETE: Elimina una película usando su ID."""
    conexion = conectar_db()
    if conexion is None: return
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM peliculas WHERE id = %s", (id_pelicula,))
        conexion.commit()
        print(f"Película ID {id_pelicula} eliminada correctamente.")
    except (Exception, Error) as error:
        print("Error al borrar:", error)
    finally:
        if conexion:
            cursor.close()
            conexion.close()

# Prueba rápida del archivo
if __name__ == "__main__":
    crear_tabla()

    # 2. Insertamos películas de prueba
    print("\nCargando películas de prueba...")
    insertar_pelicula("El Secreto de sus Ojos", "Drama/Suspenso", 2009)
    insertar_pelicula("Inception", "Ciencia Ficción", 2010)
    insertar_pelicula("Relatos Salvajes", "Comedia Negra/Drama", 2014)
    
    # 3. Probamos listarlas en la consola para verificar
    print("\nLista de películas guardadas en Postgres:")
    lista = listar_peliculas()
    for peli in lista:
        print(f"ID: {peli[0]} | Título: {peli[1]} | Género: {peli[2]} | Año: {peli[3]}")