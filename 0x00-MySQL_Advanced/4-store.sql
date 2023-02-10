-- SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
-- Trigger that update item table each we INSERT an order
DELIMITER $$
CREATE
TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
UPDATE items
SET quantity=(quantity - NEW.number)
WHERE `name`=NEW.item_name;
END$$
DELIMITER ;
