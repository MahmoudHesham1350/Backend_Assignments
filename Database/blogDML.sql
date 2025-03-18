-- Inserting dummy data

INSERT INTO users (username, `password`) VALUES 
('alice', 'hashed_password_1'),
('bob', 'hashed_password_2'),
('charlie', 'hashed_password_3');

INSERT INTO posts (author, title, published_at) VALUES 
(1, 'First Post', '2024-03-18 10:00:00'),
(2, 'Second Post', '2024-03-18 11:00:00'),
(3, 'Third Post', '2024-03-18 12:00:00');

INSERT INTO comments (id, post, `user`, `comment`, created_at) VALUES 
(1, 1, 2, 'Nice post!', '2024-03-18 10:05:00'),
(2, 1, 3, 'Thanks for sharing!', '2024-03-18 10:10:00'),
(3, 2, 1, 'Interesting read!', '2024-03-18 11:15:00');

INSERT INTO likes (post, `user`) VALUES 
(1, 2), 
(1, 3), 
(2, 1), 
(3, 2);

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- Updateing data
UPDATE users 
SET username = 'AliceUpdated' 
WHERE id = 1;

UPDATE posts 
SET title = 'Updated First Post' 
WHERE id = 1;

UPDATE comments 
SET comment = 'Really nice post!' 
WHERE id = 1 AND post = 1;

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


-- Delete a Specific Comment
DELETE FROM comments 
WHERE id = 1 AND post = 1;

-- Delete All Comments on a Specific Post
DELETE FROM comments 
WHERE post = 1;

-- Removing a Like on post 
DELETE FROM likes 
WHERE post = 1 AND user = 2;
