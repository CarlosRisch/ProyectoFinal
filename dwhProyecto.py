DDL_DWH = '''
CREATE TABLE dimArticulo(
idarticulo INT PRIMARY KEY,
codigo VARCHAR(50),
nombre_x VARCHAR(100),
precio_venta DECIMAL(11,2),
stock INT,
descripcion_x	VARCHAR(100),
nombre_y 	VARCHAR(50)
);

CREATE TABLE dimCliente(
idpersona INT PRIMARY KEY,
tipo_persona VARCHAR(20),
nombre	VARCHAR(100),
tipo_documento	VARCHAR(20),
num_documento VARCHAR(20),
direccion VARCHAR(70),
telefono VARCHAR(20),
email	VARCHAR(50)
);

CREATE TABLE dimUsuario(
idusuario	INT PRIMARY KEY,
nombre_x	VARCHAR(100),
tipo_documento VARCHAR(20),
num_documento	VARCHAR(20),
direccion	VARCHAR(70),
telefono	VARCHAR(20),
email	VARCHAR(50),
nombre_y	VARCHAR(30)
);


CREATE TABLE dimFecha(
fecha	DATE,
anio	INT,
mes	INT,
trimestre	INT,
dia	INT,
semana	INT,
dayofweek	INT,
is_weekend	BOOLEAN
);

CREATE TABLE factVentas(
idventa INT,
idcliente INT,
idusuario INT,
tipo_comprobante	VARCHAR(20),
serie_comprobante	VARCHAR(7),
num_comprobante	VARCHAR(10),
fecha	DATETIME,
impuesto DECIMAL(4,2),
total	DECIMAL(11,2),
idarticulo INT,
cantidad INT,
precio DECIMAL(11,2),
descuento DECIMAL(11,2)
);
'''