-- SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans 
-- Rank each origin using their total SUM 
WITH origin_fans AS (
  SELECT 
    origin, 
    SUM(fans) AS fans
  FROM metal_bands 
  GROUP BY origin
)
SELECT 
  origin, 
  nb_fans 
FROM origin_fans 
ORDER BY nb_fans DESC;
