# Log-Analysis-Project-3---FSND---Udacity

## How to run?

### PreRequisites:

1. [VirtualBox](https://www.virtualbox.org)

2. [Python](https://www.python.org)

3. [Vagrant](https://www.vagrantup.com)

### Setup Project:
1. Install Vagrant and VirtualBox. See steps form links provided above.
2. Virtual Machine - Download or Clone [fullstack-nanodegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm).
3. Download the [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
4. Unzip this file and find newsdata.sql.
5. [Download or clone this project](https://github.com/ashutosh-sharma/Log-Analysis-Project-3---FSND---Udacity) and place newsdata.sql file in the same folder.

### Launching the Virtual Machine:

**1. Launch the Vagrant VM using command:**
```
  $ vagrant up
```
**2. Log into VM using command ssh login:**
```
  $ vagrant ssh
```
**3. Change directory to /vagrant and move to project using 'ls' and 'cd' commands**

**4. Use command `psql -d news -f newsdata.sql` to load database.**
	
	- use `\c` to connect to `database="news"`
	- use `\dv` to see the views in database
	- use `\q` to quit the database 
	- use `\dt` to see the tables in database
	
### Some views for proper and efficient functioning of the project.Create these views in your project.

**1. articleStat**
```sql
	SELECT count(log.id) AS count,  right(log.path, char_length(log.path) - 9) AS art
	FROM log
	GROUP BY (right(log.path, char_length(log.path) - 9))
	ORDER BY (count(log.id)) DESC;
```
**2. popAuthor**
```sql
	SELECT b.count, a.author,c.name
  	FROM articleStat b,articles a,authors c
  	WHERE a.slug = b.art AND a.author = c.id;
```
**3. logFailReq and logTotalReq**

 &emsp; **logFailReq**
```sql
	SELECT count(log.status) AS fail, log.status, log."time"::date AS date
   	FROM log
  	WHERE log.status like '404%'::text
  	GROUP BY log.status, (log.time::date)
	ORDER BY (log.time::date);
```

 &emsp; **logTotalReq**
```sql
	SELECT count(log.status) AS count,log.time::date AS date
    	FROM log
        GROUP BY (log.time::date);
```

## Run the python file logAnalysis.py, this contains all the queries:
```
	$ python logAnalysis.py
```

## You can see output of the the python code in output_logAnalysis.txt

☮️ Peace ☮️
