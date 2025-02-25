import requests
from bs4 import BeautifulSoup
import pandas as pd
import psycopg2
from psycopg2 import sql

# URL de la página a scrapear
url = "https://www.house.gov/representatives"

# Paso 1: Extraer datos de la página web
def extract_data():
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")

    # Encontrar la tabla en la página
    table = soup.find("table", {"class": "table"})  
    if table is None:
        raise ValueError("Error encontrar tabla en la página.")

    # Extraer las filas de la tabla
    rows = table.find_all("tr") 
    
    data = []
    count = 0  

    for row in rows[1:]: 

        cols = row.find_all("td")
        if len(cols) >= 5:  # Verificar que la fila tenga al menos 5 columnas
            state = cols[0].text.strip()
            name = cols[1].text.strip()
            district = cols[2].text.strip()
            party = cols[3].text.strip()
            committees = cols[4].text.strip()

            # Verificación adicional para evitar registros erróneos
            if state and name and district and party:  
                data.append([state, name, district, party, committees])
                
                count += 1  # Incrementar el contador solo si agregamos datos válidos
    for row in rows[1:4]:  

        cols = row.find_all("td")
        if len(cols) >= 5:
            state = cols[0].text.strip()
            name = cols[1].text.strip()
            district = cols[2].text.strip()
            party = cols[3].text.strip()
            committees = cols[4].text.strip()

            # Verificación adicional para evitar registros erróneos
            if state and name and district and party:  
                data.append([state, name, district, party, committees])
                
                count += 1  # Incrementar el contador solo si agregamos datos válidos
        
    # Convertir los datos en un DataFrame de pandas
    df = pd.DataFrame(data, columns=["State", "Name", "District", "Party", "Committees"])
    return df

# Paso 2: Verificar datos (sin valores nulos y tipos de datos consistentes)
def verify_data(df):
    if df.isnull().values.any():
        print("Advertencia: Se encontraron valores nulos en los datos.")
        df = df.fillna("VACIO") 

    for col in df.columns:
        df[col] = df[col].astype(str)

    return df

# Paso 3: Crear la base de datos si no existe
def create_database_if_not_exists():
    try:
        # Conectar a la base de datos predeterminada 'postgres'
        conn = psycopg2.connect(
            database="postgres",  # Conéctate a la base de datos predeterminada
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        conn.autocommit = True  # Habilitar autocommit para crear la base de datos
        cursor = conn.cursor()

        # Verificar si la base de datos 'practica2' existe
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'practica2';")
        exists = cursor.fetchone()

        # Crear la base de datos si no existe
        if not exists:
            cursor.execute("CREATE DATABASE practica2;")
            print("Base de datos 'practica2' creada correctamente.")
        else:
            print("La base de datos 'practica2' ya existe.")

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error al crear la base de datos: {e}")

# Paso 4: Escribir datos en PostgreSQL
def write_to_postgres(df):
    try:
        # Conectar a la base de datos 'practica2'
        conn = psycopg2.connect(
            database="practica2",  # Conéctate a 'practica2'
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        # Crear la tabla si no existe
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS datos_practica2 (
            id SERIAL PRIMARY KEY,
            state TEXT,
            name TEXT,
            district TEXT,
            party TEXT,
            committees TEXT
        );
        """)
        conn.commit()

        # Insertar datos en la tabla
        for _, row in df.iterrows():
            cursor.execute("""
            INSERT INTO datos_practica2 (state, name, district, party, committees)
            VALUES (%s, %s, %s, %s, %s);
            """, tuple(row))

        conn.commit()
        print("Datos insertados correctamente en la tabla 'datos_practica2'.")
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error al insertar datos en la base de datos: {e}")

# Ejecutar todas las funciones
if __name__ == "__main__":
    # Crear la base de datos si no existe
    create_database_if_not_exists()

    # Extraer, verificar y escribir datos
    df = extract_data()
    df = verify_data(df)
    write_to_postgres(df)
    print(df)
    
    # Guardar los datos en un archivo CSV 
    df.to_csv("datos_practica2.csv", index=False)
    print("Datos guardados en 'datos_practica2.csv'")