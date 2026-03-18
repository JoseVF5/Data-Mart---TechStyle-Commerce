SELECT * FROM "Clientes";
ALTER TABLE "Clientes" RENAME COLUMN customer_id to "ID";
ALTER TABLE "Clientes" RENAME COLUMN customer_unique_id to "UniqueID";
ALTER TABLE "Clientes" RENAME COLUMN customer_zip_code_prefix to "ZipCodePrefix";
ALTER TABLE "Clientes" RENAME COLUMN customer_city to "City";
ALTER TABLE "Clientes" RENAME COLUMN customer_state to "State";
UPDATE "Clientes";


ALTER TABLE "Clientes" ALTER COLUMN "ZipCodePrefix" TYPE numeric(6);
