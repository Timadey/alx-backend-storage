-- SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

-- Select origin and fans (ranked)
SELECT (SUM(fans)) AS nb_fans WHERE orig = origin