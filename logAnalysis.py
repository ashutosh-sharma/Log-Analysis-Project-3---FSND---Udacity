#!/usr/bin/env python3
#
# All views defintion are in the README file.
#
import psycopg2


# A function to connect to database.
def connect():
    return psycopg2.connect("dbname=news")


# A function to get the result of the query
def run_query(q):
    con = connect()
    c = con.cursor()
    c.execute(q)
    res = c.fetchall()
    con.close()
    return res


# A function to print output to standard output unit
def output_result(res):
    for r in res:
        print('\t' + str(r[0]) + "  ----  " + str(r[1]) + " views")


# A function to print result of third query to standard output unit
def third_output(res):
    for r in res:
        print('\t' + str(r[0]) + " ---- " + str(r[1]) + "%")


# Query 1: The most popular three articles of all time?
first_query = """SELECT a.title,b.count FROM articles AS a,
            articleStat AS b WHERE a.slug = b.art LIMIT 3;"""

# Query 2: The most popular article authors of all time?
second_query = """SELECT name, sum(count) FROM popAuthor
             GROUP BY author,name ORDER BY sum(count) DESC;"""

# Query 3: On which days did more than 1% of requests lead to errors?
third_query = """SELECT a.date, round(cASt(((a.fail::float/b.count::float)*100)
               AS numeric), 2) AS perfail FROM logFailReq AS a, logTotalReq AS
               b WHERE a.date = b.date AND
               ((a.fail::float/b.count::float)*100) > 1;"""

if __name__ == "__main__":
    result_of_first_query = run_query(first_query)
    print("\nThe most popular three articles of all time:")
    output_result(result_of_first_query)

    result_of_sec_query = run_query(second_query)
    print("\n\nThe most popular article authors of all time:")
    output_result(result_of_sec_query)

    result_of_third_query = run_query(third_query)
    print("\n\nDays on which more than 1% of requests lead to errors:")
    third_output(result_of_third_query)

    print('\n \n')
