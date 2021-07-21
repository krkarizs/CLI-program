
--CREATE DATABASE workplace;

CREATE TABLE agent (id SERIAL PRIMARY KEY, name varchar(255) NOT NULL);
CREATE TABLE project (id SERIAL PRIMARY KEY, name varchar(255) NOT NULL);

CREATE TABLE Logs (id SERIAL PRIMARY KEY, logintime DATE, logouttime DATE NOT NULL, startclock TEXT NOT NULL, endclock TEXT NOT NULL, worktime INT NOT NULL,
metadata varchar(255) NOT NULL);

ALTER TABLE Logs ADD agent_id int;
ALTER TABLE Logs ADD project_id int;
ALTER TABLE Logs ADD CONSTRAINT fk_agent_id FOREIGN KEY (agent_id) REFERENCES agent(id);
ALTER TABLE Logs ADD CONSTRAINT fk_project_id FOREIGN KEY (project_id) REFERENCES project(id);