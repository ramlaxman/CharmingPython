import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","narendra","narendra","pythonWorkshop" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS userRecord")

# Create table as per requirement
sql = """CREATE TABLE  userrecord(
            FIRST_NAME  CHAR(20) NOT NULL,
            LAST_NAME  CHAR(20),
            AGE INT,
            SEX CHAR(1),
            INCOME FLOAT )"""
cursor.execute(sql)

# disconnect from server
db.close()
