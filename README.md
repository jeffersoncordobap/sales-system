# 🚀 Sistema de Escritorio para Administración de Tienda de Calzado

**(Ventas – Inventario – Contabilidad – Facturación – Reportes)**

## 🎯 Objetivo General

Diseñar y desarrollar un sistema de escritorio robusto que permita gestionar de manera eficiente las operaciones internas de la tienda: ventas, inventario, facturación, costos, gastos e ingresos, proporcionando información clara y organizada para apoyar la toma de decisiones.

## 📄 Alcance del Proyecto

### Incluye:
* Gestión de inventario.
* Registro de ventas.
* Facturación simple.
* Registro de gastos.
* Registro de costos de productos.
* Cierres de caja.
* Reportes consolidados (diarios, mensuales, anuales).
* Exportación de reportes básicos (PDF/Excel).
* Interfaz moderna y amigable.

### No incluye:
* Ventas en línea.
* Sincronización en la nube.
* Aplicación web o móvil.

---

## 💻 Arquitectura Técnica

| Componente | Tecnología Principal | Detalles |
| :--- | :--- | :--- |
| **Aplicación de Escritorio** | **Python + PySide6** | Interfaz de usuario robusta y multiplataforma. |
| **Base de Datos** | **SQLite** | Motor de base de datos local (archivo único). |

## ⚙️ Requerimientos de Hardware Mínimo

* PC con **Windows 10** o superior.
* **4GB RAM**.
* **200 MB** de espacio libre.
* Impresora opcional para facturas.

---

## 🧩 Módulos del Sistema

| Módulo | Funcionalidades Clave | Entidades Principales |
| :--- | :--- | :--- |
| **1. Módulo POS (Punto de Venta)** | Registro de ventas, búsqueda rápida (código/nombre), cálculo de totales, descuentos y facturación. | `ventas`, `detalle_venta`, `pagos_venta`. |
| **2. Módulo de Inventario** | Registro/Edición de productos, control automático de stock, entradas de inventario, alertas de bajo stock. | `productos`. |
| **3. Módulo de Caja y Flujo** | Apertura/cierre de caja, registro de gastos operativos, manejo de devoluciones y retiros. | `registro_caja`, `movimientos_caja`, `gastos`. |
| **4. Módulo de Reportes y Análisis** | Generación de reportes (ventas, utilidad, inventario, gastos), exportación (PDF/Excel). | Lectura de todas las tablas de transacción. |
| **5. Módulo de Administración y Seguridad** | Login/Logout, gestión de roles y permisos, copias de respaldo, recuperación de contraseña. | `usuarios`. |

---

## ✅ Requerimientos Funcionales (RF)

| ID | Requerimiento Funcional | Descripción Breve |
| :--- | :--- | :--- |
| **RF1** | Gestión de productos | Permitir registrar, editar y eliminar productos (código, nombre, categoría, talla, precio y costo). |
| **RF2** | Control de inventario | Actualización automática de stock por venta o entrada. |
| **RF3** | Entradas de inventario | Permitir agregar cantidades nuevas y registrar fecha/motivo. |
| **RF4** | Alertas de bajo inventario | Mostrar alertas cuando el stock esté por debajo del mínimo establecido. |
| **RF5** | Registro de ventas | Registrar ventas (productos, cantidades, método de pago, vendedor). |
| **RF6** | Cálculo automático | Calcular subtotal, impuestos y total final de la venta. |
| **RF7** | Facturación simple | Generar facturas básicas en formato imprimible o PDF. |
| **RF8** | Gestión de costos y gastos | Registrar gastos por categoría y costos de inventario. |
| **RF9** | Cierre de caja | Generar resumen diario con ventas, gastos, ingresos y utilidad. |
| **RF10** | Reportes del sistema | Generar reportes de Ventas, Productos más vendidos, Utilidad, Inventario y Gastos. |
| **RF11** | Exportación de reportes | Permitir exportar reportes a PDF o Excel. |
| **RF12** | Seguridad mínima de acceso | Permitir que un usuario inicie sesión con credenciales válidas. |
| **RF13** | Asignación de Roles | Permitir al administrador asignar roles específicos (Vendedor, Gerente) a usuarios. |
| **RF14** | Restricción de Permisos | Restringir funciones sensibles (anular venta, cambiar precios) solo a Administrador. |
| **RF15** | Recuperación de Contraseña | Permitir restablecer contraseña con preguntas de seguridad. |
| **RF16** | Registro de Transacciones | Registrar el nombre de usuario que realiza cada transacción. |
| **RF17** | Gestión de Copias de Respaldo | Función manual o automática para crear y restaurar copias de respaldo de SQLite. |
| **RF18** | Apertura de Caja (Monto Inicial) | Requerir y registrar un monto inicial de apertura de caja. |
| **RF19** | Aplicación de Descuentos | Permitir aplicar porcentaje o valor fijo de descuento por producto. |
| **RF20** | Búsqueda Rápida de Productos | Permitir buscar y añadir productos por nombre o código de barras (escaneo). |
| **RF21** | Gestión de Devoluciones y Anulaciones | Permitir anular venta (revertir stock) y registrar la salida de dinero (afectando RDI07 y RDI09). |

---

## 🛡️ Requerimientos No Funcionales (RNF)

| ID | Requerimiento No Funcional | Criterio de Aceptación |
| :--- | :--- | :--- |
| **RNF01** | Rendimiento | El sistema debe iniciar en **menos de 5 segundos**. |
| **RNF02** | Usabilidad | La interfaz debe ser **intuitiva y fácil de usar** para personal no técnico. |
| **RNF03** | Portabilidad | El sistema debe ejecutarse correctamente en **Windows 10 o superior**. |
| **RNF04** | Confiabilidad | Los datos deben guardarse de forma segura en SQLite **sin riesgo de corrupción**. |
| **RNF05** | Seguridad local | Proteger el archivo de base de datos mediante permisos locales. |
| **RNF06** | Mantenibilidad | Código organizado por módulos, uso de **PEP8** y comentarios explicativos. |
| **RNF07** | Escalabilidad | Permitir agregar nuevos módulos **sin reescribir los existentes**. |
| **RNF08** | Seguridad de Contraseña | Almacenar contraseñas y respuestas de seguridad cifradas con **algoritmo de hash fuerte (ej. bcrypt)**. |
| **RNF09** | Proceso de Sesión | Inicio de sesión y cambio de usuario debe completarse en **menos de 3 segundos**. |
| **RNF10** | Bloqueo de Cuenta | Bloquear temporalmente una cuenta después de **5 intentos fallidos**. |
| **RNF11** | Contraseña Temporal | Forzar al usuario a cambiar la contraseña en el próximo inicio de sesión después de un restablecimiento por el administrador. |
| **RNF12** | Eficiencia en Venta | Procesar la lectura de un código de barras e incluir el producto en la venta en **menos de 1 segundo**. |
| **RNF13** | Restricción de Descuentos | Capacidad de aplicar descuentos mayores a un porcentaje predefinido (ej. 40%) restringida al rol de Gerente/Administrador. |

---

## 💾 Requerimientos de Información (RDI) y Esquema de BD

### Esquema Relacional de la Base de Datos

| Entidad | Clave Primaria (PK) | Atributos Principales |
| :--- | :--- | :--- |
| **usuarios** | `id_usuario` | `nombre`, `rol`, `hash_contrasena`, `hash_respuesta1`, `hash_respuesta2`, `estado` |
| **productos** (RDI04) | `id_producto` | `codigo_barras`, `nombre`, `categoria`, `talla`, `precio_venta`, `costo_compra`, `stock_actual`, `stock_minimo`, `estado_gestion` |
| **ventas** (RDI05) | `id_venta` | `fk_vendedor`, `fecha_hora`, `monto_total`, `subtotal`, `impuestos`, `descuento_total`, `estado_venta` |
| **items_venta** (RDI06) | `(fk_venta, fk_producto)` | `cantidad_vendida`, `costo_unitario_al_momento_venta`, `precio_base`, `descuento_aplicado`, `precio_final` |
| **pagos_venta** (RDI09) | `id_pago` | `fk_venta`, `medio_pago`, `monto_pagado_en_ese_medio` |
| **registro_caja** (RDI07) | `id_caja` | `fk_vendedor_abre`, `monto_inicial_apertura`, `fecha_hora_apertura`, `fecha_hora_cierre`, `monto_esperado_efectivo`, `monto_final_declarado`, `diferencia`, `observaciones_cierre` |
| **gastos** (RDI08) | `id_gasto` | `fk_caja_turno`, `fk_vendedor`, `monto`, `categoria_gasto`, `descripcion`, `fecha_hora`, `metodo_pago` |
| **movimientos_caja** (RDI10) | `id_movimiento` | `fk_caja_turno`, `fk_vendedor`, `tipo_movimiento`, `monto`, `fecha_hora` |
| **movimientos_inventario** (RDI11) | `id_movimiento` | `fk_producto`, `tipo_movimiento`, `cantidad_afectada`, `fecha_hora`, `fk_usuario`, `fk_venta`, `observaciones` |

### Reglas de Negocio: Estado de Gestión de Producto

| Intención de Negocio | Tipo de Transición | Regla Implementada |
| :--- | :--- | :--- |
| El producto se agotó. (Evento) | **AUTOMÁTICA** | `Stock_Actual = 0` $\rightarrow$ `Estado = DESCONTINUADO` |
| Quiero volver a pedir este modelo. (Decisión Gerencial) | **SEMI-AUTOMÁTICA** | Intentar Reponer $\rightarrow$ Sistema Pregunta $\rightarrow$ Usuario Confirma $\rightarrow$ `Estado = ACTIVO` |
| Quiero archivar este modelo para siempre. (Decisión Gerencial) | **MANUAL** | Modificar Producto (CU-INV02) $\rightarrow$ `Estado = 'OBSOLETO'` |


---

## 🙋 Historias de Usuario (HU)

### Módulo 1: Ventas y Caja (POS)

| ID | Historia de Usuario | Requisitos Asociados |
| :--- | :--- | :--- |
| **HU-V01** | **Apertura de Turno de Caja** Como Vendedor, quiero registrar un monto inicial de apertura de caja para tener un fondo de cambio exacto y registrar el inicio de mi turno. | RF18, RDI07, RF16 |
| **HU-V02** | **Registro Rápido de Producto** Como Vendedor, quiero poder buscar y agregar productos a la venta usando el código de barras o el nombre para agilizar la atención al cliente. | RF5, RF20, RNF12 |
| **HU-V03** | **Aplicación de Descuentos (Regateo)** Como Vendedor, quiero aplicar un descuento por línea de producto o al total de la venta para poder negociar y cerrar la venta. | RF5, RF19, RNF13 |
| **HU-V04** | **Cálculo y Finalización de Venta** Como Vendedor, quiero finalizar la transacción calculando totales, registrando el medio de pago y el valor recibido para completar la venta y dar el cambio. | RF5, RF6, RDI05 |
| **HU-V05** | **Cierre de Turno de Caja** Como Vendedor, quiero registrar el cierre de mi turno y el conteo final del dinero para generar mi reporte parcial y entregar la caja al siguiente responsable. | RF9, RDI07, RF16 |

### Módulo 2: Gestión de Inventario

| ID | Historia de Usuario | Requisitos Asociados |
| :--- | :--- | :--- |
| **HU-I01** | **Registro de Nuevo Producto** Como Administrador, quiero registrar un nuevo producto con todos sus atributos (código, talla, precios) para agregarlo al inventario y ponerlo a la venta. | RF1, RDI04 |
| **HU-I02** | **Actualización de Inventario (Entrada)** Como Administrador, quiero registrar la entrada de nuevas cantidades de productos para actualizar el stock después de una compra a proveedores. | RF2, RF3, RDI08 |
| **HU-I03** | **Alerta de Stock Mínimo** Como Gerente, quiero recibir alertas visuales cuando el stock de un producto cae por debajo del mínimo establecido para poder realizar pedidos a tiempo. | RF4, RDI04 |
| **HU-I04** | **Edición y Eliminación de Producto** Como Administrador, quiero poder editar o eliminar un producto o sus atributos (ej. un cambio de precio) para mantener la información de inventario actualizada. | RF1, RNF14 |

### Módulo 5: Administración y Seguridad

| ID | Historia de Usuario | Requisitos Asociados |
| :--- | :--- | :--- |
| **HU-S01** | **Inicio y Cambio de Sesión** Como Usuario (Vendedor o Admin), quiero iniciar sesión con mis credenciales para acceder a mis permisos y que mis transacciones queden registradas bajo mi nombre. | RF12, RF16, RNF09 |
| **HU-S02** | **Recuperación de Contraseña** Como Usuario, quiero restablecer mi contraseña sin ayuda del administrador respondiendo a mis preguntas de seguridad en caso de olvido. | RF15, RDI02 |
| **HU-S03** | **Gestión de Cuentas y Roles** Como Administrador, quiero crear, modificar y asignar roles a los usuarios (Vendedores) para controlar sus accesos y permisos. | RF13, RF14, RDI01 |
| **HU-S04** | **Gestión de Copia de Respaldo** Como Administrador, quiero crear y restaurar copias de respaldo de la base de datos para prevenir la pérdida total de información. | RF17, RNF04 |

---

## 🛠️ Casos de Uso (CU) y Flujos Detallados

### Módulo 1: POS (Punto de Venta y Caja)

| Caso de Uso (CU) | Objetivo | Actor Principal | Requisitos Asociados |
| :--- | :--- | :--- | :--- |
| **CU-POS01** | Registrar una Venta Completa | Vendedor | RF5, RF6, RDI05, RDI06, RDI09, RDI11 |
| **CU-POS02** | Anular una Venta o Ítem | Vendedor / Gerente | RF7 (Devolución/Anulación) |
| **CU-POS03** | Apertura de Caja (Inicio de Turno) | Vendedor | RF18, RDI07 |
| **CU-POS04** | Cierre de Caja (Fin de Turno) | Vendedor | RF9, RDI07 |

#### CU-POS01: Registrar una Venta Completa

| Campo | Descripción |
| :--- | :--- |
| **Objetivo** | Ejecutar una venta, calcular montos, registrar pagos, actualizar stock y registrar movimientos. |
| **Precondición** | El Vendedor debe tener un turno de caja abierto (`registro_caja`). |
| **Postcondición** | Se crean registros en `ventas`, `detalle_venta`, `pagos_venta` y `movimientos_inventario`. El `stock_actual` de los productos se reduce. |
| **Flujo Principal (Éxito):** | 1. El actor inicia una nueva venta. <br> 2. El actor busca y agrega productos. <br> 3. El sistema calcula totales. <br> 4. El actor aplica un descuento. <br> 5. El actor selecciona medios de pago. <br> 6. El sistema procesa pago y registra `id_pago`. <br> 7. El sistema ejecuta **commit** (Registra venta, actualiza stock y registra movimientos). <br> 8. El sistema imprime recibo y muestra el cambio. |

### Módulo 2: Gestión de Inventario

| Caso de Uso (CU) | Objetivo | Actor Principal | Requisitos Asociados |
| :--- | :--- | :--- | :--- |
| **CU-INV01** | **Registrar un Nuevo Producto** | Administrador | RF1, RDI04 |
| **CU-INV02** | **Gestionar Stock (Entradas y Ajustes)** | Administrador | RF2, RF3, RDI08 |
| **CU-INV03** | **Actualizar Datos de Producto** | Administrador | RF1 |

#### CU-INV02: Gestionar Stock (Entradas y Ajustes)

| Campo | Descripción |
| :--- | :--- |
| **Objetivo** | Registrar entradas de inventario o ajustes manuales para mantener la exactitud del `stock_actual`. |
| **Precondición** | El producto debe existir en la tabla `productos`. |
| **Postcondición** | El `stock_actual` del producto se modifica. Se crea un registro en `movimientos_inventario` con `tipo_movimiento = 'ENTRADA'` o `'SALIDA (AJUSTE)'`. |
| **Flujo Principal (Entrada por Compra):** | 1. El actor selecciona el producto a reabastecer (HU-I02). <br> 2. El actor ingresa la **cantidad** y el **costo de compra**. <br> 3. El sistema calcula el nuevo stock: `stock_actual` + `cantidad`. <br> 4. El sistema ejecuta el commit: **a)** Actualiza el `stock_actual` y **b)** Crea un registro en `movimientos_inventario`. |

### Módulo 5: Administración y Seguridad

| Caso de Uso (CU) | Objetivo | Actor Principal | Requisitos Asociados |
| :--- | :--- | :--- | :--- |
| **CU-SEC01** | **Autenticación (Login)** | Vendedor / Administrador | RF12, RNF09, RNF10 |
| **CU-SEC02** | **Restablecer Contraseña** | Vendedor / Administrador | RF15, RNF08 |
| **CU-SEC03** | **Gestión de Usuarios y Roles** | Administrador | RF13, RF14 |
| **CU-SEC04** | **Crear Respaldo de BD** | Administrador | RF17, RNF04 |

#### CU-SEC01: Autenticación (Login)

| Campo | Descripción |
| :--- | :--- |
| **Objetivo** | Permitir el acceso al sistema a usuarios con credenciales válidas y aplicar las restricciones de seguridad. |
| **Precondición** | La tabla `usuarios` debe contener, al menos, un registro de administrador. |
| **Postcondición** | El usuario tiene acceso al módulo principal y se registra como usuario activo. |
| **Flujo Principal (Éxito):** | 1. El actor ingresa credenciales. <br> 2. El sistema busca usuario y **compara el hash** de la contraseña (RNF08). <br> 3. Si es correcto, el sistema concede acceso. <br> 4. El sistema carga la interfaz en **menos de 3 segundos** (RNF09). |

#### CU-SEC02: Restablecer Contraseña (Preguntas de Seguridad)

| Campo | Descripción |
| :--- | :--- |
| **Objetivo** | Permitir al usuario recuperar el acceso sin intervención manual del administrador. |
| **Precondición** | El usuario debe haber configurado previamente sus preguntas de seguridad. |
| **Postcondición** | La `hash_contrasena` del usuario es actualizada. |
| **Flujo Principal (Éxito):** | 1. El actor selecciona "Olvidé mi contraseña". <br> 2. El sistema muestra preguntas. <br> 3. El actor ingresa respuestas. <br> 4. El sistema **compara los hashes** de las respuestas. <br> 5. Si coinciden, permite establecer una nueva contraseña. <br> 6. El sistema calcula y guarda el nuevo hash (RNF08). |

