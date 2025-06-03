CREATE TABLE warehouses (
    warehouse_id SERIAL PRIMARY KEY,
    address TEXT NOT NULL,
    manager TEXT,
    phone VARCHAR(20)
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    type VARCHAR(20) CHECK (type IN ('жіночий', 'чоловічий', 'дитячий')),
    name TEXT NOT NULL,
    manufacturer TEXT,
    warehouse_id INTEGER REFERENCES warehouses(warehouse_id) ON DELETE SET NULL,
    quantity INTEGER CHECK (quantity >= 0),
    price NUMERIC(10, 2)
);

CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT,
    phone VARCHAR(20),
    contact_person TEXT
);

CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    sale_date DATE NOT NULL,
    client_id INTEGER REFERENCES clients(client_id) ON DELETE CASCADE,
    product_id INTEGER REFERENCES products(product_id) ON DELETE SET NULL,
    quantity INTEGER CHECK (quantity > 0),
    discount NUMERIC(5,2) CHECK (discount >= 0 AND discount <= 100)
);
