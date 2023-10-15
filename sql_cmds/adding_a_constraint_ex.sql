-- Add a CHECK constraint to restrict values in the existing column
ALTER TABLE artwork
ADD CONSTRAINT year_range CHECK (date_created_year >= 0000 AND date_created_year <= 2100);


select * from artwork