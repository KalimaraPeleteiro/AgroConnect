CREATE TABLE users(cpf VARCHAR(11) PRIMARY KEY, 
                   email VARCHAR(255),
                   password VARCHAR(225))

CREATE TABLE requests(user_cpf VARCHAR(11),
                      request_number VARCHAR(255),
                      product VARCHAR(255),
                      payment_method VARCHAR(255))

ALTER TABLE requests ADD CONSTRAINT requests_users_fk
FOREIGN KEY (user_cpf)
REFERENCES users(cpf)

INSERT INTO users VALUES('00011122233', 'randomperson@gmail.com', '1234')
INSERT INTO users VALUES('44455566677', 'hitman@gmail.com', '12345')
INSERT INTO requests VALUES('00011122233', '00000', 'Fruit', 'PIX')
INSERT INTO requests VALUES('00011122233', '00001', 'Banana', 'PIX')
INSERT INTO requests VALUES('44455566677', '00002', 'Lemon', 'PIX')

SELECT requests.request_number, requests.product, requests.payment_method FROM users 
INNER JOIN requests ON users.cpf = requests.user_cpf WHERE users.cpf = '00011122233'