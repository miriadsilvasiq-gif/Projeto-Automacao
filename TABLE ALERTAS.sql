CREATE TABLE alertas (
    id_alerta INT AUTO_INCREMENT PRIMARY KEY,
    nivel VARCHAR(20),
    id_leitura INT,
    FOREIGN KEY (id_leitura) REFERENCES leituras(id_leitura)
);