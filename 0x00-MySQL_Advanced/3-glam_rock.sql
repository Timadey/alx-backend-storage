-- Calculate life span of band 
-- Define a Common Table Expression (CTE) to calculate the lifespan of each band
WITH band_lifespan AS (
  SELECT 
    band_name, 
    -- Calculate the lifespan as the difference between the split and formed attributes
    (split - formed) AS lifespan 
  FROM metal_bands 
  -- Filter for bands with Glam Rock as their main style
  WHERE main_style = 'Glam Rock'
)
-- Select the band name and lifespan from the CTE, and order the result by lifespan in descending order
SELECT 
  band_name, 
  lifespan 
FROM band_lifespan 
ORDER BY lifespan DESC;
