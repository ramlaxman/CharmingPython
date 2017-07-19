"""
DELETE operation is required when you want to delete some records from your database.
"""

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","narendra","narendra","pythonWorkshop" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to DELETE required records
sql = "delete from employee where age < 30"
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

# disconnect from server
db.close()
