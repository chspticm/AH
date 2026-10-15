CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    unit_price_cents INTEGER NOT NULL CHECK (unit_price_cents >= 0),
    stock_quantity INTEGER NOT NULL CHECK (stock_quantity >= 0),
    available INTEGER NOT NULL CHECK (available IN (0, 1))
);

INSERT INTO products (product_id, product_name, category, unit_price_cents, stock_quantity, available) VALUES
(1, 'Notebook', 'Stationery', 250, 42, 1),
(2, 'Blue Pen', 'Stationery', 120, 68, 1),
(3, 'Desk Lamp', 'Home', 1899, 7, 1),
(4, 'Water Bottle', 'Outdoors', 1200, 0, 0),
(5, 'Canvas Bag', 'Accessories', 975, 15, 1),
(6, 'Plant Pot', 'Home', 640, 11, 1),
(7, 'Lunch Box', 'Outdoors', 825, 4, 1),
(8, 'Pencil Set', 'Stationery', 360, 23, 1);

SELECT * FROM products;
