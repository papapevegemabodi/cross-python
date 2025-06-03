import psycopg2

conn = psycopg2.connect(
    dbname="shopdb",
    user="shopuser",
    password="shoppass",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Приклади заповнення таблиць
cur.execute("INSERT INTO warehouses (address, manager, phone) VALUES "
            "('Київ, вул. Перемоги 1', 'Іван Іванов', '+380501234567'),"
            "('Львів, вул. Галицька 10', 'Петро Петренко', '+380931112233'),"
            "('Одеса, вул. Морська 5', 'Марія Марченко', '+380671234567');")

cur.execute("INSERT INTO clients (name, address, phone, contact_person) VALUES "
            "('ТОВ Альфа', 'Київ, Хрещатик 12', '+380501234567', 'Олег Сидоров'),"
            "('ПП Бета', 'Львів, Шевченка 8', '+380931112233', 'Ірина Коваль');")

cur.execute("INSERT INTO products (type, name, manufacturer, warehouse_id, quantity, price) VALUES "
            "('чоловічий', 'Куртка зимова', 'Nike', 1, 15, 1800.00),"
            "('жіночий', 'Сукня вечірня', 'Zara', 2, 10, 2200.00),"
            "('дитячий', 'Футболка', 'H&M', 3, 20, 400.00);")

cur.execute("INSERT INTO sales (sale_date, client_id, product_id, quantity, discount) VALUES "
            "('2024-05-12', 1, 1, 2, 10),"
            "('2024-05-13', 2, 2, 1, 0);")

conn.commit()
cur.close()
conn.close()
