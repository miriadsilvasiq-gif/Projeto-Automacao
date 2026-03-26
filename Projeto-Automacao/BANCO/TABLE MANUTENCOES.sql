CREATE TABLE manutencoes (
    id_manutencao INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(200),
    data DATE,
    id_maquina INT,
    id_operador INT,
    FOREIGN KEY (id_maquina) REFERENCES maquinas(id_maquina),
    FOREIGN KEY (id_operador) REFERENCES operadores(id_operador)
);