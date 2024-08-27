create database Proyecto
USE Proyecto

CREATE TABLE CompanyProfiles (
 Symbol VARCHAR (255),
 Company VARCHAR (255),
 Sector VARCHAR (255),
 Headquarters VARCHAR (255),
 Fechafundada VARCHAR (255)
 );


 CREATE TABLE Companies (
 Date date,
 Symbol VARCHAR (255),
 PriceClose float
 );

 ALTER TABLE Companies
 ALTER COLUMN Symbol VARCHAR (255) NOT NULL

  ALTER TABLE CompanyProfiles 
 ALTER COLUMN Symbol VARCHAR (255)  NOT NULL

  ALTER TABLE Companies
 ALTER COLUMN Date date NOT NULL

 --Crear llaves Primarias
 ALTER TABLE CompanyProfiles 
ADD CONSTRAINT PK_CompanyProfiles PRIMARY KEY (Symbol);

 ALTER TABLE Companies
ADD CONSTRAINT PK_Companies PRIMARY KEY (Date);

-- Crear LLave Foraneas FK

ALTER TABLE Companies
ADD CONSTRAINT FK_CompaniesProfiles
FOREIGN KEY (Symbol) REFERENCES CompanyProfiles (Symbol);

select * from [Proyecto].[dbo].[Companies]

select * from [Proyecto].[dbo].[CompanyProfiles]



