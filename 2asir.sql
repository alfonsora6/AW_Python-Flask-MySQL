--Primero accedemos con -> mysql -u root -p

--Creación de BD y usuario (Definiendole los privilegios)

CREATE DATABASE 2asir;
CREATE USER 'alfonso'@'%' IDENTIFIED BY 'passbd';
GRANT ALL PRIVILEGES ON 2asir.* to 'alfonso'@'%';
FLUSH PRIVILEGES;
USE 2asir;

--Luego podremos acceder a la base de datos desde el programa, con las credenciales del usuario que hemos definido.

--Creación de tablas

CREATE TABLE Profesor
(
    DNI VARCHAR(9),
    Nombre VARCHAR(20),
    Apellido VARCHAR(20),
    FechaNac DATE,
    CONSTRAINT ck_dni CHECK(DNI REGEXP '^[0-9]{8}[A-Z]$'),
    CONSTRAINT ck_inicialesnommayus CHECK(Nombre REGEXP ('^[A-Z]')),
	CONSTRAINT ck_inicialesapemayus CHECK(Nombre REGEXP ('^[A-Z]')),
    CONSTRAINT pk_presidente PRIMARY KEY(DNI)
);

CREATE TABLE Asignatura
(
	Nombre VARCHAR(60),
	DNI_Profesor VARCHAR(9),
    Curso VARCHAR(30),
	CONSTRAINT fk_profesor FOREIGN KEY (DNI_Profesor) REFERENCES Profesor(DNI),
    CONSTRAINT pk_asignatura PRIMARY KEY(Nombre)
);


--Insercción de datos

INSERT INTO Profesor VALUES
	('48392938H','Rafael','Bornes','1987-02-18'),
	('47362737N','Pedro','Guerrero','1976-11-13'),
	('74632918F','Lucas','Fernández','1986-12-05'),
	('38462728G','Marta','López','1995-09-29');

INSERT INTO Asignatura VALUES
	('Servicios de Red e Internet','48392938H','2º ASIR'),
	('Seguridad y alta disponibilidad','38462728G','2º ASIR'),
	('Empresa administrativa y emprendedora','47362737N','2º ASIR'),
	('Implantación de aplicaciones web','74632918F','2º ASIR');

	
