CREATE TABLE produtor (
    id SERIAL PRIMARY KEY,
    cpf_cnpj VARCHAR(14) UNIQUE NOT NULL,
    nome_produtor VARCHAR(100) NOT NULL,
    nome_fazenda VARCHAR(100) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    estado VARCHAR(2) NOT NULL,
    area_total DECIMAL(10, 2) NOT NULL,
    area_agricultavel DECIMAL(10, 2) NOT NULL,
    area_vegetacao DECIMAL(10, 2) NOT NULL,
)

CREATE TABLE cultura (
    id SERIAL PRIMARY KEY
    produtor_id INTEGER,
    cultura VARCHAR(100) NOT NULL,
    area DECIMAL(10, 2) NOT NULL,
 
    CONSTRAINT fk_cultura_produtor
        FOREIGN KEY(produtor_id)
            REFERENCES produtor(id)
)