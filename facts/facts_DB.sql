-- Creating DB
CREATE DATABASE space_game
-- Using 'character set' to enable special characters use
CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;

-- Disabling safe updates
SET SQL_SAFE_UPDATES = 0;
USE space_game;

-- Creating table to store game facts
CREATE TABLE facts
(
fact_id INT AUTO_INCREMENT PRIMARY KEY,
fact TEXT NOT NULL
);

-- Inserting facts into DB
INSERT INTO facts (fact) VALUES
('A year on Mercury is just 88 days long!'
),
('Venus is the second brightest object in the night sky!'
),
('Earth is the only planet not named after a god!'
),
('Sunsets on Mars are blue!'
),
('A day on Jupiter is the shortest of all planets, at 9 hours and 55 minutes!'
),
('Saturn has 82 moons, thats more than any other planet!'
),
('Uranus is the coldest planet, with temperatures at -225 degrees celsius!'
),
('Neptune has 6 faint rings surrounding it!'
),
('Christina Koch will be the first woman on the moon in the Artemis II mission 2024.'
),
('Caroline Herschel was the first woman to discover a comet!'
),
('Valentina Tereshkova was the first woman to go into space!'
),
('Neil Armstrong was the first person to walk on the Moon!'
),
('The first human space flight was on April 12, 1961!'
),
('Our solar system is about 4.571 billion years old!'
);
