-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
-- Calculate the select the bands and calculate their lifespan
SELECT band_name, (formed - split) AS lifespan
FROM metal_bands WHERE style = 'Glam rock';