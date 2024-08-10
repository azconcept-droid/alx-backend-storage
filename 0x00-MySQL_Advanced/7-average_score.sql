-- Create procedure that compute average score
delimiter $$;
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
	BEGIN
        -- Declare variable
        DECLARE user_scores INT;
		-- Calculate average score
        SELECT score INTO user_scores FROM corrections WHERE user_id = user_id;
        UPDATE users SET average_score = AVG(user_scores) WHERE id = user_id; 
	END
$$
delimiter ;$$
