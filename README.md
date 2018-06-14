# Log-Analysis-Project-3---FSND---Udacity
This repository contains project 3 Log Analysis of Udacity's Full Stack Nano Degree.

How to run?
1. Download the project along with the newsdata database.
2. Run the python file using 'python logAnalysis.py'

__________________________________________________________________________________________________
Views definiton : 
1. articleStat ->
SELECT count(log.id) AS count,  right(log.path, char_length(log.path) - 9) AS art
  FROM log
  GROUP BY (right(log.path, char_length(log.path) - 9))
  ORDER BY (count(log.id)) DESC;

2. popAuthor ->
  SELECT b.count, a.author,c.name
   FROM articleStat b,articles a,authors c
  WHERE a.slug = b.art AND a.author = c.id;

3. logFailReq and logTotalReq
•logFailReq ->  SELECT count(log.status) AS fail, log.status, log."time"::date AS date
   	FROM log
  	WHERE log.status like '404%'::text
  	GROUP BY log.status, (log.time::date)
	  ORDER BY (log.time::date);

•logTotalReq -> SELECT count(log.status) AS count,log.time::date AS date
    	          FROM log
            	         GROUP BY (log.time::date);

__________________________________________________________________________________________________

