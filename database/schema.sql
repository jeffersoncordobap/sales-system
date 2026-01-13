-- Habilitar claves foráneas
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    rol TEXT NOT NULL,
    hash_contrasena TEXT NOT NULL,
    hash_respuesta1 TEXT,
    hash_respuesta2 TEXT,
    estado TEXT DEFAULT 'ACTIVO'
);

CREATE TABLE IF NOT EXISTS productos (
    id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_barras TEXT UNIQUE DEFAULT NULL,
    nombre TEXT NOT NULL,
    categoria TEXT,
    talla TEXT,
    color TEXT,
    precio_venta REAL DEFAULT 0.0,
    stock_actual INTEGER DEFAULT 0,
    estado_gestion TEXT DEFAULT 'ACTIVO',
    UNIQUE(nombre, categoria, talla, color)
);

CREATE TABLE IF NOT EXISTS registro_caja (
    id_caja INTEGER PRIMARY KEY AUTOINCREMENT,
    fk_vendedor_abre INTEGER,
    monto_inicial_apertura REAL DEFAULT 0.0,
    fecha_hora_apertura DATETIME DEFAULT CURRENT_TIMESTAMP,
    fecha_hora_cierre DATETIME,
    monto_esperado_transferencia REAL DEFAULT 0.0,
    monto_esperado_tarjeta REAL DEFAULT 0.0,
    monto_esperado_efectivo REAL DEFAULT 0.0,
    total_ventas_sistema REAL DEFAULT 0.0,
    monto_final_efectivo_declarado REAL,
    diferencia REAL,
    observaciones_cierre TEXT,
    FOREIGN KEY (fk_vendedor_abre) REFERENCES usuarios(id_usuario)
);

CREATE TABLE IF NOT EXISTS ventas (
    id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
    fk_vendedor INTEGER,
    fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    subtotal REAL,
    impuestos REAL DEFAULT 0.0,
    descuento_total REAL DEFAULT 0.0,
    total REAL NOT NULL,
    estado_venta TEXT DEFAULT 'COMPLETADA',
    monto_devuelto REAL DEFAULT 0.0,
    FOREIGN KEY (fk_vendedor) REFERENCES usuarios(id_usuario)
);

CREATE TABLE IF NOT EXISTS items_venta (
    id_item_venta INTEGER PRIMARY KEY AUTOINCREMENT,
    fk_venta INTEGER,
    fk_producto INTEGER,
    cantidad_vendida INTEGER NOT NULL,
    precio_base REAL,
    descuento_aplicado REAL DEFAULT 0.0,
    precio_final REAL,
    cantidad_devuelta INTEGER DEFAULT 0,
    FOREIGN KEY (fk_venta) REFERENCES ventas(id_venta),
    FOREIGN KEY (fk_producto) REFERENCES productos(id_producto)
);

CREATE TABLE IF NOT EXISTS pagos_venta (
    id_pago INTEGER PRIMARY KEY AUTOINCREMENT,
    fk_venta INTEGER,
    medio_pago TEXT NOT NULL, -- 'EFECTIVO', 'TARJETA', 'TRANSFERENCIA'
    monto_pagado_en_ese_medio REAL NOT NULL,
    FOREIGN KEY (fk_venta) REFERENCES ventas(id_venta)
);

CREATE TABLE IF NOT EXISTS gastos (
    id_gasto INTEGER PRIMARY KEY AUTOINCREMENT,
    fk_caja_turno INTEGER NOT NULL,
    fk_vendedor INTEGER,
    monto REAL NOT NULL,
    categoria_gasto TEXT,
    descripcion TEXT,
    fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    metodo_pago TEXT,
    FOREIGN KEY (fk_caja_turno) REFERENCES registro_caja(id_caja),
    FOREIGN KEY (fk_vendedor) REFERENCES usuarios(id_usuario)
);

CREATE TABLE IF NOT EXISTS movimientos_inventario (
    id_movimiento INTEGER PRIMARY KEY AUTOINCREMENT,
    fk_producto INTEGER,
    tipo_movimiento TEXT NOT NULL, -- 'ENTRADA', 'SALIDA', 'VENTA', 'DEVOLUCION'
    cantidad_afectada INTEGER NOT NULL,
    fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    fk_usuario INTEGER,
    fk_venta INTEGER,
    observaciones TEXT,
    FOREIGN KEY (fk_producto) REFERENCES productos(id_producto),
    FOREIGN KEY (fk_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (fk_venta) REFERENCES ventas(id_venta)
);

CREATE TABLE IF NOT EXISTS devoluciones (
    id_devolucion INTEGER PRIMARY KEY AUTOINCREMENT,
    fk_venta INTEGER,
    fk_usuario INTEGER,
    fk_item_venta INTEGER, 
    fk_producto INTEGER,   
    monto_reembolsado REAL,
    fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    motivo TEXT,
    estado_producto TEXT, -- 'BUENO', 'DAÑADO'
    FOREIGN KEY (fk_venta) REFERENCES ventas(id_venta),
    FOREIGN KEY (fk_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (fk_item_venta) REFERENCES items_venta(id_item_venta),
    FOREIGN KEY (fk_producto) REFERENCES productos(id_producto)
);

CREATE TABLE IF NOT EXISTS movimientos_caja (
    id_movimiento INTEGER PRIMARY KEY AUTOINCREMENT,
    fk_caja_turno INTEGER NOT NULL,
    fk_vendedor INTEGER,
    tipo_movimiento TEXT NOT NULL, -- 'ENTRADA_BASE', 'RETIRO', 'SALIDA_DEVOLUCION'
    monto REAL NOT NULL,
    fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (fk_caja_turno) REFERENCES registro_caja(id_caja),
    FOREIGN KEY (fk_vendedor) REFERENCES usuarios(id_usuario)
);