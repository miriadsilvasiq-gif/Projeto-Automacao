CREATE TABLE sensores (
    id_sensor INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50),
    id_maquina INT,
    FOREIGN KEY (id_maquina) REFERENCES maquinas(id_maquina)
);