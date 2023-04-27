CREATE TABLE Camera (Camera_ID INT Auto_Increment PRIMARY KEY, Longitude FLOAT, Latitude FLOAT, Instalacao_Data DATE);
CREATE TABLE Dados (Dados_ID INT Auto_Increment PRIMARY KEY, Contador INT, Data_Tempo DATETIME, Camera_ID INT);

ALTER TABLE Dados ADD FOREIGN KEY (Camera_ID) REFERENCES Camera(Camera_ID);

INSERT INTO Camera (Longitude, Latitude, Instalacao_Data) VALUES (-8.052240, -34.928612,'2023-04-27');