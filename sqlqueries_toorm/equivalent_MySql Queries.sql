INSERT INTO Howarts (name, house, pet, year) VALUES ('Draco Malfoy', 'Slytherin', 'Unknown', '5');
INSERT INTO Howarts (name, house, pet, year) VALUES ('Luna Lovegood', 'Ravenclaw', 'None', '4');
INSERT INTO Howarts (name, house, pet, year) VALUES ('Padma Patil', 'Ravenclaw', 'None', '5');
SELECT * FROM Howarts where house = Ravenclaw
UPDATE Howarts SET year = '5' WHERE name = "Luna Lovegood";