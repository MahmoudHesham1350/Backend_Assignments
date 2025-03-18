CREATE DATABASE blog_db;

USE blog_db;
CREATE TABLE users(
	id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    `password` VARCHAR(255) NOT NULL
);

USE blog_db;
CREATE TABLE posts(
	id INT AUTO_INCREMENT PRIMARY KEY,
    author INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    published_at DATETIME NOT NULL,
    FOREIGN KEY (author) REFERENCES users(id) ON DELETE CASCADE  -- adding constraint on author as a foreign key
);

USE blog_db;
CREATE TABLE `comments`(
	id INT AUTO_INCREMENT,
    post INT NOT NULL,
	PRIMARY KEY(id, post),
    `user` INT NOT NULL,
    `comment` TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    FOREIGN KEY (post) REFERENCES posts(id) ON DELETE CASCADE,
    FOREIGN KEY (`user`) REFERENCES users(id) ON DELETE CASCADE
    
);

USE blog_db;
CREATE TABLE likes(
	post INT NOT NULL,
    `user` INT NOT NULL,
    PRIMARY KEY(post, `user`),
	FOREIGN KEY (`user`) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (post) REFERENCES posts(id) ON DELETE CASCADE
);

