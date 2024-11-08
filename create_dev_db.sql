-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS   Dse_Ele_Fix_store_dev_db;
CREATE USER IF NOT EXISTS 'Ele_Fix_store'@'localhost' IDENTIFIED BY 'dse_dev_pwd';
GRANT ALL PRIVILEGES ON `Dse_Ele_Fix_store_dev_db`.* TO 'Ele_Fix_store'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'Ele_Fix_store'@'localhost';
FLUSH PRIVILEGES;