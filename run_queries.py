import psycopg2
from tabulate import tabulate

conn = psycopg2.connect(
    host="localhost",
    database="shopdb",
    user="shopuser",
    password="shoppass"
)
cur = conn.cursor()

queries = [
    {
        "title": "🔷 Покупки (дата, товар, клієнт, кількість, ціна)",
        "sql": """
        SELECT 
            s.sale_date, 
            p.name AS product_name, 
            c.name AS client_name, 
            s.quantity, 
            p.price
        FROM sales s
        JOIN products p ON s.product_id = p.id
        JOIN clients c ON s.client_id = c.id
        ORDER BY c.name;
        """
    },
    {
        "title": "🔷 Одяг за типом (параметр: 'жіночий')",
        "sql": """
        SELECT * FROM products WHERE type = 'жіночий';
        """
    },
    {
        "title": "🔷 Кількість покупок по кожному клієнту",
        "sql": """
        SELECT 
            c.name AS client_name, 
            COUNT(s.id) AS total_purchases
        FROM clients c
        LEFT JOIN sales s ON s.client_id = c.id
        GROUP BY c.name
        ORDER BY c.name;
        """
    },
    {
        "title": "🔷 Вартість кожної покупки без і з урахуванням знижки",
        "sql": """
        SELECT 
            s.id AS sale_id,
            c.name AS client_name,
            p.name AS product_name,
            s.quantity,
            p.price,
            s.discount,
            (s.quantity * p.price) AS total_without_discount,
            (s.quantity * p.price * (1 - s.discount / 100)) AS total_with_discount
        FROM sales s
        JOIN clients c ON s.client_id = c.id
        JOIN products p ON s.product_id = p.id;
        """
    },
    {
        "title": "🔷 Загальна сума, витрачена кожним клієнтом",
        "sql": """
        SELECT 
            c.name AS client_name,
            ROUND(SUM(s.quantity * p.price * (1 - s.discount / 100)), 2) AS total_spent
        FROM clients c
        JOIN sales s ON s.client_id = c.id
        JOIN products p ON s.product_id = p.id
        GROUP BY c.name
        ORDER BY total_spent DESC;
        """
    },
    {
        "title": "🔷 Кількість кожного виду одягу на кожному складі",
        "sql": """
        SELECT 
            w.address AS warehouse,
            p.name AS product_name,
            p.quantity
        FROM warehouses w
        JOIN products p ON p.warehouse_id = w.id
        ORDER BY w.address, p.name;
        """
    }
]

for q in queries:
    print(f"\n{q['title']}")
    cur.execute(q["sql"])
    rows = cur.fetchall()
    headers = [desc[0] for desc in cur.description]
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

cur.close()
conn.close()
