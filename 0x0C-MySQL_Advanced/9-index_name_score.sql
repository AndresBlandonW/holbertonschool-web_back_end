-- Creates an index idx_name_first_score on table names
-- Only the first letter of name and score must be indexed
CREATE INDEX idx_name_first_score ON names(name(1), score);