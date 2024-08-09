-- Create a trigger that resets the attribute valid_email
-- only when the email has been changed.
delimiter |;

CREATE TRIGGER reset_attri AFTER UPDATE ON users.email
  FOR EACH ROW
  BEGIN
    UPDATE users SET valid_email = 0;
  END;
|

delimiter ;|
