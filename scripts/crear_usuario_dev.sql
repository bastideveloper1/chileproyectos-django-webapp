-- Crear la base de datos para desarrollo
CREATE DATABASE chileproyectos_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Crear el usuario de desarrollo
CREATE USER 'chileproyectos_user'@'localhost' IDENTIFIED BY 'dev_pass';

-- Darle permisos completos sobre la base de datos
GRANT ALL PRIVILEGES ON chileproyectos_db.* TO 'chileproyectos_user'@'localhost';

-- Aplicar los cambios de permisos
FLUSH PRIVILEGES;
