-- Change email validation status to 0
-- Create Trigger that change vali_email to 0 ON user UPDATE
DELIMITER $$
CREATE
TRIGGER verify_email
BEFORE UPDATE ON `users`
FOR EACH ROW
BEGIN
IF NOT NEW.email = OLD.email THEN
SET NEW.valid_email = 0;
END IF;
END$$
DELIMITER ;
