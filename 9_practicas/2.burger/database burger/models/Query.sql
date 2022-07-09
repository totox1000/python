INSERT INTO restaurants (name)
VALUES (" happy Time Burgers ") , ("fun times Burgers") , ( " what did I just Eat ");

INSERT INTO burgers  (name, bun, meat, calories, restaurant_id)
VALUES (" The destroyer ", "Seaseme Seed", "Mystery", 1400,3), ( "Tofu Delight", "Pretzel", "Tofu",  300,2), 
(" Creamy Chicken",1000,2), 
("Gut Buster", "Crispy Ramen Noodles", "Spicy Beef", 700,3),
( "The Omen", "Fire", "Turkey", 400,2 ),
(" The TurDuckey", "White Bread", "Turkey and Duck", 500,2);

SELECT * FROM restaurants
JOIN burgers ON burgers.restaurant_id = restaurant_id
WHERE restaurant_id = 1;