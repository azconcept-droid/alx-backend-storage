-- Create a trigger that resets the attribute valid_email
-- only when the email has been changed.
delimiter |;

CREATE TRIGGER reset_attri AFTER INSERT ON orders
  FOR EACH ROW
  BEGIN
    UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
  END;
|

delimiter ;|
