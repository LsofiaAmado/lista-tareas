CREATE DATABASE IF NOT EXISTS lista_tareas
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE lista_tareas;

-- =====================================================
-- Tabla
-- =====================================================

CREATE TABLE IF NOT EXISTS tareas_tarea (
    id BIGINT NOT NULL AUTO_INCREMENT,
    titulo VARCHAR(200) NOT NULL,
    descripcion LONGTEXT NOT NULL,

    PRIMARY KEY (id)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;