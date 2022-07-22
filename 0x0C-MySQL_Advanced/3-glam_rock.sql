-- SQL script lists all bands with Glam rock as their main style
-- Ranked by their longevity
SELECT band_name, IF(split IS NULL, 2022, split) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;