CREATE TABLE leituras (
    id_leitura INT AUTO_INCREMENT PRIMARY KEY,
    valor DECIMAL(5,2),
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_sensor INT,
    FOREIGN KEY (id_sensor) REFERENCES sensores(id_sensor)
);