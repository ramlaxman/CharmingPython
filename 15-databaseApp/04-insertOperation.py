import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","narendra","narendra","pythonWorkshop" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "insert into employee values('narendra', 'swami', 28)"
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
