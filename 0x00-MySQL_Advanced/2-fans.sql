-- SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans 
-- Rank each origin using their total SUM 
SELECT origin, nb_fans FROM (SELECT origin, SUM(fans) AS total_fans FROM metal_bands GROUP BY origin) ORDER BY nb_fans DESC;
