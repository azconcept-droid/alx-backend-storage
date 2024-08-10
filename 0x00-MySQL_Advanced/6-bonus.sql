-- Create bonus procedure
DELIMITER $$;
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score INT)
	BEGIN
		-- Declare new variable o hold project id
		DECLARE project_id INT;
		-- SELECT project id if it exist
		SELECT id INTO project_id
		FROM projects
		WHERE name = project_name;
		-- Create project.id if it does not exist
		IF project_id IS NULL THEN
			INSERT INTO projects (name) VALUES (project_name);
		END IF;
		-- Insert into corrections table new project_id and score
		INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
	END
$$
DELIMITER ;$$
