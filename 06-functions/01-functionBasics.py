"""
function
    -- block of code that performs a single task
    -- makes the code reusable, modular
    -- types
        -- built-in
        -- user defined
    -- always define before calling
    -- can have parameters
    -- do not define return type. why?
    -- can have multiple returns
"""

# parameterized function
def logNstars(count):
    print '*'*count

# another function
def logStars():
    print '*'*50

# function definition
def main():
    print "this is main function"
    logStars()

    count = raw_input("enter count of stars : ")
    logNstars(int(count))

# function call
main()
