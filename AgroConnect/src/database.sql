-- Tabelas
CREATE TABLE users(cpf VARCHAR(11) PRIMARY KEY, 
                   email VARCHAR(255),
                   password VARCHAR(225),
                   name VARCHAR(225))

CREATE TABLE companies(cnpj VARCHAR(14) PRIMARY KEY,
                       email VARCHAR(255),
                       password VARCHAR(225))

CREATE TABLE requests(user_cpf VARCHAR(11),
                      request_number VARCHAR(255),
                      product VARCHAR(255),
                      payment_method VARCHAR(255),
                      description VARCHAR(10000),
                      cellphone VARCHAR(255),
                      status VARCHAR(1))


-- Foreign Keys
ALTER TABLE requests ADD CONSTRAINT requests_users_fk
FOREIGN KEY (user_cpf)
REFERENCES users(cpf)


-- Valores Padrão
INSERT INTO users VALUES('00011122233', 'randomperson@gmail.com', '1234', 'Josimar da Silva')
INSERT INTO users VALUES('44455566677', 'hitman@gmail.com', '12345', 'Fabinho Caxias')
INSERT INTO companies VALUES('00001111222233', 'mycompany@gmail.com', 123)
INSERT INTO requests VALUES('00011122233', '1132', 'Maçã', 'PIX', 'Caixa de 40 maçãs', '71 9345 6781', '1')


-- Queries
SELECT requests.request_number, requests.product, requests.payment_method FROM users 
INNER JOIN requests ON users.cpf = requests.user_cpf WHERE users.cpf = '00011122233'

SELECT users.name FROM users INNER JOIN requests ON users.cpf = requests.user_cpf 
WHERE requests.user_cpf = '00011122233'

UPDATE requests SET status = '1' WHERE request_number = '1132'