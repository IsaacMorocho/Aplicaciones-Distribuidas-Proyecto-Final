CREATE DATABASE IF NOT EXISTS app_db;
USE app_db;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    titulo VARCHAR(255) NOT NULL,
    descripcion TEXT,
    fecha_limite DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS submissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    task_id INT NOT NULL,
    respuesta TEXT NOT NULL,
    fecha_entrega DATETIME NOT NULL,
    UNIQUE KEY unique_submission (student_id, task_id),
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE
);

-- Datos semilla para Estudiantes
INSERT INTO students (username, password_hash) VALUES
('juan@epn.edu.ec', 'scrypt:32768:8:1$LH2bYVR3Rjwde4gf$6f8b43efbdf7dd6c0e549efec6b146474c78a23fedbaf953012f9f16fd1456fe7a8c85bc3da2139f456e9fe49b105ff2488a3b416f61621475cf8bcb002bf0a4'),
('maria@epn.edu.ec', 'scrypt:32768:8:1$LH2bYVR3Rjwde4gf$6f8b43efbdf7dd6c0e549efec6b146474c78a23fedbaf953012f9f16fd1456fe7a8c85bc3da2139f456e9fe49b105ff2488a3b416f61621475cf8bcb002bf0a4');

-- Datos semilla para Tareas (una vigente, una vencida, una adicional)
INSERT INTO tasks (codigo, titulo, descripcion, fecha_limite) VALUES
('PW001', 'Aplicación Flask', 'Crear una aplicación Flask utilizando Docker.', DATE_ADD(NOW(), INTERVAL 2 DAY)),
('BD001', 'Modelo Relacional', 'Diseñar la base de datos del proyecto.', DATE_SUB(NOW(), INTERVAL 2 DAY)),
('DIST01', 'Sistema Distribuido', 'Implementar Nginx y MySQL Replication.', DATE_ADD(NOW(), INTERVAL 5 DAY));
