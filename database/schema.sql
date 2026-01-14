PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    user_role TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    answer1_hash TEXT,
    answer2_hash TEXT,
    management_status TEXT DEFAULT 'ACTIVE'
);

CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    bar_code TEXT UNIQUE DEFAULT NULL,
    product_name TEXT NOT NULL,
    category TEXT,
    product_size TEXT,
    color TEXT,
    price REAL DEFAULT 0.0,
    stock INTEGER DEFAULT 0,
    management_status TEXT DEFAULT 'ACTIVE',
    UNIQUE(product_name, category, product_size, color)
);

CREATE TABLE IF NOT EXISTS cash_register_records (
    register_id INTEGER PRIMARY KEY AUTOINCREMENT,
    opened_by_fk INTEGER,
    initial_opening_amount REAL DEFAULT 0.0,
    opening_datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
    closing_datetime DATETIME,
    expected_transfer_amount REAL DEFAULT 0.0,
    expected_card_amount REAL DEFAULT 0.0,
    expected_cash_amount REAL DEFAULT 0.0,
    system_total_sales REAL DEFAULT 0.0,
    declared_final_cash_amount REAL,
    difference REAL,
    closing_observations TEXT,
    FOREIGN KEY (opened_by_fk) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    seller_fk INTEGER,
    sale_datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
    subtotal REAL,
    taxes REAL DEFAULT 0.0,
    total_discount REAL DEFAULT 0.0,
    total REAL NOT NULL,
    sale_status TEXT DEFAULT 'COMPLETED',
    refunded_amount REAL DEFAULT 0.0,
    FOREIGN KEY (seller_fk) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS sale_items (
    sale_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sale_fk INTEGER,
    product_fk INTEGER,
    quantity_sold INTEGER NOT NULL,
    base_price REAL,
    applied_discount REAL DEFAULT 0.0,
    final_price REAL,
    returned_quantity INTEGER DEFAULT 0,
    FOREIGN KEY (sale_fk) REFERENCES sales(sale_id),
    FOREIGN KEY (product_fk) REFERENCES products(product_id)
);

CREATE TABLE IF NOT EXISTS sale_payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sale_fk INTEGER,
    payment_method TEXT NOT NULL, -- 'CASH', 'CARD', 'TRANSFER'
    amount_paid_in_method REAL NOT NULL,
    FOREIGN KEY (sale_fk) REFERENCES sales(sale_id)
);

CREATE TABLE IF NOT EXISTS expenses (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cash_shift_fk INTEGER NOT NULL,
    seller_fk INTEGER,
    amount REAL NOT NULL,
    expense_category TEXT,
    expenses_description TEXT,
    expense_datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
    payment_method TEXT,
    FOREIGN KEY (cash_shift_fk) REFERENCES cash_register_records(register_id),
    FOREIGN KEY (seller_fk) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS inventory_movements (
    movement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_fk INTEGER,
    movement_type TEXT NOT NULL, -- 'ENTRY', 'EXIT', 'SALE', 'RETURN'
    affected_quantity INTEGER NOT NULL,
    movement_datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_fk INTEGER,
    sale_fk INTEGER,
    observations TEXT,
    FOREIGN KEY (product_fk) REFERENCES products(product_id),
    FOREIGN KEY (user_fk) REFERENCES users(user_id),
    FOREIGN KEY (sale_fk) REFERENCES sales(sale_id)
);

CREATE TABLE IF NOT EXISTS product_returns (
    return_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sale_fk INTEGER,
    user_fk INTEGER,
    sale_item_fk INTEGER, 
    product_fk INTEGER,    
    refunded_amount REAL,
    return_datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
    reason TEXT,
    product_condition TEXT, -- 'GOOD', 'DAMAGED'
    FOREIGN KEY (sale_fk) REFERENCES sales(sale_id),
    FOREIGN KEY (user_fk) REFERENCES users(user_id),
    FOREIGN KEY (sale_item_fk) REFERENCES sale_items(sale_item_id),
    FOREIGN KEY (product_fk) REFERENCES products(product_id)
);

CREATE TABLE IF NOT EXISTS cash_movements (
    movement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cash_shift_fk INTEGER NOT NULL,
    seller_fk INTEGER,
    movement_type TEXT NOT NULL, -- 'BASE_ENTRY', 'WITHDRAWAL', 'RETURN_EXIT'
    amount REAL NOT NULL,
    movement_datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cash_shift_fk) REFERENCES cash_register_records(register_id),
    FOREIGN KEY (seller_fk) REFERENCES users(user_id)
);