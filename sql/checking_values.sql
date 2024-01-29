SELECT *
FROM dtp JOIN vehicle ON dtp.id = vehicle.dtp_id
JOIN participant on vehicle.id = participant.vehicle_id;

SELECT COUNT(*) FROM dtp;

WITH cte_name (interval, count_dtp) AS (
SELECT (date_trunc('hour', datetime::time) + interval '15 minutes' * floor(EXTRACT(MINUTE FROM datetime::time) / 15))::time AS interval_start,
       COUNT(*) AS count
FROM public.dtp
GROUP BY interval_start
ORDER BY interval_start
)
SELECT SUM(count_dtp)
FROM cte_name;


