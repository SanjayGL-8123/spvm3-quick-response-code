CREATE DATABASE IF NOT EXISTS qr_studio CHARACTER SET utf8mb4;
USE qr_studio;
CREATE TABLE IF NOT EXISTS qr_codes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(120) NOT NULL,
  qr_type VARCHAR(30) NOT NULL,
  content TEXT NOT NULL,
  module_shape TINYINT NOT NULL DEFAULT 0,
  eye_style TINYINT NOT NULL DEFAULT 0,
  fg_color CHAR(7) NOT NULL,
  bg_color CHAR(7) NOT NULL,
  png_data MEDIUMTEXT,
  frame_style TINYINT DEFAULT 0,
  occasion TINYINT DEFAULT 0,
  frame_text VARCHAR(120) DEFAULT '',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- If you already created the table earlier, run this instead:
-- ALTER TABLE qr_codes ADD frame_style TINYINT DEFAULT 0, ADD occasion TINYINT DEFAULT 0, ADD frame_text VARCHAR(120) DEFAULT '';
