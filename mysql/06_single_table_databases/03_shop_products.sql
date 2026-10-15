CREATE DATABASE IF NOT EXISTS ah_shop;
USE ah_shop;

CREATE TABLE IF NOT EXISTS products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(80) NOT NULL,
    category VARCHAR(40) NOT NULL,
    unit_price DECIMAL(7,2) NOT NULL,
    stock_quantity INT NOT NULL,
    available BOOLEAN NOT NULL
);

INSERT INTO products (product_id, product_name, category, unit_price, stock_quantity, available) VALUES
(1, 'Notebook', 'Stationery', 2.50, 42, TRUE),
(2, 'Blue Pen', 'Stationery', 1.20, 68, TRUE),
(3, 'Desk Lamp', 'Home', 18.99, 7, TRUE),
(4, 'Water Bottle', 'Outdoors', 12.00, 0, FALSE),
(5, 'Canvas Bag', 'Accessories', 9.75, 15, TRUE),
(6, 'Plant Pot', 'Home', 6.40, 11, TRUE),
(7, 'Lunch Box', 'Outdoors', 8.25, 4, TRUE),
(8, 'Pencil Set', 'Stationery', 3.60, 23, TRUE);

SELECT * FROM products;
