"""
READ Operation on any database means to fetch some useful information from the database.

fetchone(): It fetches the next row of a query result set. A result set is an object that is returned when a cursor object is used to query a table.
fetchall(): It fetches all the rows in a result set. If some rows have already been extracted from the result set, then it retrieves the remaining rows from the result set.
rowcount: This is a read-only attribute and returns the number of rows that were affected by an execute() method.
"""
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","narendra","narendra","pythonWorkshop" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "select * from employee where firstName = \'narendra\'"
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        # Now print fetched result
        print("fname=%s,lname=%s,age=%d" % \
                (fname, lname, age))
except:
    print("Error: unable to fecth data")

# disconnect from server
db.close()
