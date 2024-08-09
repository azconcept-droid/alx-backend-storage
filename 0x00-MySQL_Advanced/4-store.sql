-- creates a trigger that decreases the quantity of an item
-- after adding a new order.
CREATE TRIGGER decr_quantity AFTER INSERT ON orders
FOR EACH ROW
BEGIN
SET items.quantity = items.quantity - NEW.number;
END
