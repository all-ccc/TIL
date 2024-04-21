-- orders 테이블 생성
CREATE TABLE orders (
  order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  order_date DATE,
  total_amount Real
);

INSERT INTO
  orders(order_date, total_amount)
VALUES
  ('2024-03-22', 50.55),
  ('2024-03-12', 46.55),
  ('2024-03-03', 25.00),
  ('2024-01-22', 40.99);

-- customers 테이블 생성
CREATE TABLE customers (
  customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(30),
  email VARCHAR(50),
  phone VARCHAR(15)
);

INSERT INTO
  customers(name, email, phone)
VALUES
  ('민주', 'minju@example.com', '010-1234-5678'),
  ('승지', 'esg@example.com', '010-1234-1234'),
  ('하영', 'hy@example.com', '010-4561-5678'),
  ('은지', 'ej@example.com', '010-7894-5678');


-- 데이터 수정
DELETE FROM
  orders
WHERE
  order_id = 3;

UPDATE
  customers
SET
  name = '홍길동'
WHERE
  customer_id = 1;

-- 데이터 조회
SELECT *
FROM orders;

SELECT *
FROM customers;




