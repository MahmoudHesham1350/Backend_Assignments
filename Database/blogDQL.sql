-- Get all posts ordered by newest first
SELECT * FROM posts 
ORDER BY published_at DESC;

-- Get latest 3 comments on post ID 1
SELECT * FROM comments 
WHERE post = 1 
ORDER BY created_at DESC 
LIMIT 3;

-- Get the most recent user who joined
SELECT * FROM users 
ORDER BY id DESC 
LIMIT 1;

-- Get all likes for a specific post (e.g., post ID = 1)
SELECT * FROM likes 
WHERE post = 1;

-- Intro to joins
SELECT posts.id AS post_ID, posts.title, posts.published_at, users.username AS author
FROM posts, users
WHERE posts.author = users.id;

