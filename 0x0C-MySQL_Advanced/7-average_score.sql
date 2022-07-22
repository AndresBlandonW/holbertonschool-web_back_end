-- Creates a stored procedure ComputeAverageScoreForUser
-- Computes and stores the average score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
	SET @average = (
		SELECT AVG(score) 
		FROM corrections 
		WHERE corrections.user_id = user_id);

	UPDATE users
	SET average_score = @average
	WHERE id = user_id;
END$$

DELIMITER ;