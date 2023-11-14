CREATE DATABASE myappdb;
USE myappdb;
-- drop database myappdb;
CREATE TABLE users (
    username VARCHAR(10) NOT NULL UNIQUE,
    email_id VARCHAR(30) NOT NULL UNIQUE,
    age INT,
    grade_12_score DECIMAL(5, 2), -- DECIMAL for grade_12_score, precision 5, scale 2
    jee_score DECIMAL(5, 2) default null, -- DECIMAL for jee_score, precision 5, scale 2
    neet_score INT default null,
    phone CHAR(10),
    gender ENUM("Male", "Female", "Prefer not to say") default "Prefer not to say",
    password VARCHAR(20),
    about varchar(50), 
    PRIMARY KEY (username)
);

DELIMITER $$

CREATE FUNCTION check_password(in_username VARCHAR(10), in_password VARCHAR(20))
RETURNS BOOLEAN DETERMINISTIC
BEGIN
    DECLARE user_password VARCHAR(20);
    SELECT password INTO user_password FROM users WHERE username = in_username;
    IF user_password = in_password THEN
        RETURN 1;
    ELSE
        RETURN 0;
    END IF;
END
$$
DELIMITER ;

DELIMITER $$

CREATE FUNCTION check_username(uname VARCHAR(255)) RETURNS INT DETERMINISTIC
BEGIN
    DECLARE user_exists INT;
    SET user_exists = (
        SELECT COUNT(*) FROM users WHERE username = uname
    );

    IF user_exists > 0 THEN
        RETURN 1;
    ELSE
        RETURN 0;
    END IF;
END $$;

DELIMITER ;

DELIMITER $$

CREATE FUNCTION add_user(uname VARCHAR(255), uemail VARCHAR(255), upassword VARCHAR(255)) RETURNS INT DETERMINISTIC
BEGIN
    INSERT INTO users (username, email_id, password)
    VALUES (uname, uemail, upassword);

    RETURN 1;
END $$;

DELIMITER ;

DELIMITER //

CREATE PROCEDURE UpdateUserProfile(
    IN p_email VARCHAR(30),
    IN p_age INT,
    IN p_gender ENUM('Male', 'Female', 'Other'),
    IN p_grade_12_score DECIMAL(5, 2),
    IN p_jee_score DECIMAL(5, 2),
    IN p_neet_score INT,
    IN p_phone_number CHAR(10)
)
BEGIN
    -- Update user details using the provided email
    UPDATE users
    SET
        age = p_age,
        gender = p_gender,
        grade_12_score = p_grade_12_score,
        jee_score = p_jee_score,
        neet_score = p_neet_score,
        phone = p_phone_number
    WHERE email_id = p_email;

    IF ROW_COUNT() > 0 THEN
        -- If the update affected one or more rows, consider it a success
        SELECT 'User profile updated successfully.' AS message;
    ELSE
        -- If no rows were updated, the user may not exist or the email may not match any records
        SELECT 'User not found or profile not updated.' AS message;
    END IF;

END //

DELIMITER ;

DELIMITER $$
CREATE PROCEDURE UpdateUserInfo(
    IN p_username VARCHAR(20),
    IN p_email VARCHAR(30),
    IN p_age INT,
    IN p_grade_12_score DECIMAL(5, 2),
    IN p_jee_score DECIMAL(5, 2),
    IN p_neet_score INT,
    IN p_phone CHAR(10),
    IN p_gender ENUM('Male', 'Female', 'Prefer not to say'),
    IN p_password VARCHAR(20),
    IN p_about VARCHAR(50)
)
BEGIN
    UPDATE users
    SET 
        email_id = p_email,
        age = p_age,
        grade_12_score = p_grade_12_score,
        jee_score = p_jee_score,
        neet_score = p_neet_score,
        phone = p_phone,
        gender = p_gender,
        about = p_about,
        password = p_password
    WHERE username = p_username;
    COMMIT;
    SELECT 1 AS result;
END $$
DELIMITER ;



