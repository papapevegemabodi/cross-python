import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="shopdb",
    user="shopuser",
    password="shoppass"
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS warehouses (
    id SERIAL PRIMARY KEY,
    address TEXT NOT NULL,
    manager TEXT NOT NULL,
    phone VARCHAR(20)
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS clients (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    phone VARCHAR(20),
    contact_person TEXT
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    type TEXT NOT NULL,
    name TEXT NOT NULL,
    manufacturer TEXT NOT NULL,
    warehouse_id INTEGER REFERENCES warehouses(id),
    quantity INTEGER,
    price NUMERIC(10,2)
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    sale_date DATE,
    client_id INTEGER REFERENCES clients(id),
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER,
    discount NUMERIC(5,2)
);
""")

conn.commit()
cur.close()
conn.close()
print("✅ Таблиці створено.")