-- SCHEMA
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8mb4;
USE `mydb`;

-- CLASSES DE USUÁRIOS
CREATE TABLE classes_usuarios (
  id_classe_usuario INT AUTO_INCREMENT PRIMARY KEY,
  nome_classe_usuario VARCHAR(45) NOT NULL
) ENGINE=InnoDB;

-- USUÁRIOS
CREATE TABLE usuarios (
  id_usuario INT AUTO_INCREMENT PRIMARY KEY,
  nome_usuario VARCHAR(50) NOT NULL,
  sobrenome_usuario VARCHAR(100) NOT NULL,
  email_usuario VARCHAR(70) NOT NULL UNIQUE,
  id_classe_usuario INT NOT NULL,
  FOREIGN KEY (id_classe_usuario) REFERENCES classes_usuarios(id_classe_usuario)
) ENGINE=InnoDB;

-- STATUS DO PORTE
CREATE TABLE status_porte (
  id_status_porte INT AUTO_INCREMENT PRIMARY KEY,
  nome_status_porte VARCHAR(45) NOT NULL
) ENGINE=InnoDB;

-- TIPOS DE PORTE
CREATE TABLE tipos_porte (
  id_tipo_porte INT AUTO_INCREMENT PRIMARY KEY,
  nome_tipo_porte VARCHAR(45) NOT NULL
) ENGINE=InnoDB;

-- ABRANGÊNCIA DO PORTE
CREATE TABLE abrangencia_porte (
  id_abrangencia_porte INT AUTO_INCREMENT PRIMARY KEY,
  nome_abrangencia_porte VARCHAR(45) NOT NULL
) ENGINE=InnoDB;

-- SEXO PORTADOR
CREATE TABLE sexos_portador (
  id_sexo_portador INT AUTO_INCREMENT PRIMARY KEY,
  nome_sexo_portador VARCHAR(45) NOT NULL
) ENGINE=InnoDB;

-- ESPÉCIES DE ARMA
CREATE TABLE especies_arma (
  id_especie_arma INT AUTO_INCREMENT PRIMARY KEY,
  nome_especie_arma VARCHAR(45) NOT NULL
) ENGINE=InnoDB;

-- MARCAS DE ARMA
CREATE TABLE marcas_arma (
  id_marca_arma INT AUTO_INCREMENT PRIMARY KEY,
  nome_marca_arma VARCHAR(45) NOT NULL
) ENGINE=InnoDB;

-- CALIBRES
CREATE TABLE calibres_arma (
  id_calibre_arma INT AUTO_INCREMENT PRIMARY KEY,
  nome_calibre_arma VARCHAR(45) NOT NULL
) ENGINE=InnoDB;

-- UF
CREATE TABLE uf (
  id_uf INT AUTO_INCREMENT PRIMARY KEY,
  nome_uf VARCHAR(100) NOT NULL
) ENGINE=InnoDB;

-- ARMAS
CREATE TABLE armas (
  id_arma INT AUTO_INCREMENT PRIMARY KEY,
  id_marca_arma INT NOT NULL,
  id_calibre_arma INT NOT NULL,
  id_especie_arma INT NOT NULL,
  quantidade_armas INT NOT NULL DEFAULT 1,
  FOREIGN KEY (id_marca_arma) REFERENCES marcas_arma(id_marca_arma),
  FOREIGN KEY (id_calibre_arma) REFERENCES calibres_arma(id_calibre_arma),
  FOREIGN KEY (id_especie_arma) REFERENCES especies_arma(id_especie_arma)
) ENGINE=InnoDB;

-- PORTES
CREATE TABLE portes (
  id_porte INT AUTO_INCREMENT PRIMARY KEY,
  id_usuario INT NOT NULL,
  id_status_porte INT NOT NULL,
  id_tipo_porte INT NOT NULL,
  id_abrangencia_porte INT NOT NULL,
  id_sexo_portador INT NOT NULL,
  id_arma INT NOT NULL,
  id_uf INT NOT NULL,
  ano_emissao YEAR NOT NULL,
  mes_emissao TINYINT NOT NULL,
  FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
  FOREIGN KEY (id_status_porte) REFERENCES status_porte(id_status_porte),
  FOREIGN KEY (id_tipo_porte) REFERENCES tipos_porte(id_tipo_porte),
  FOREIGN KEY (id_abrangencia_porte) REFERENCES abrangencia_porte(id_abrangencia_porte),
  FOREIGN KEY (id_sexo_portador) REFERENCES sexos_portador(id_sexo_portador),
  FOREIGN KEY (id_arma) REFERENCES armas(id_arma),
  FOREIGN KEY (id_uf) REFERENCES uf(id_uf)
) ENGINE=InnoDB;
