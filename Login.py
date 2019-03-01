'''
SignUp - creates account
SignupPrompt - asks if you have signed up
'''

import sqlite3
from sqlite3 import Error
import re


PROMPT = "Have you signed up? [yes, no]:"
def main():
        signUpPrompt()
        if isSignedUp == False:
            signUp()
        else:
            signIn()

'''
    @Function: Takes one argument of string type and checks each of them for issues based on arrays written in the function
    @params: signedUp
    @output: confirms data put in by the user is correct and meaninful
'''
def checksSignupResponse(signedUp):
    global isSignedUp
    yes = ["yes", "y", "1"]
    no = ["no", "n", "0"]
    signedUp.strip()
    signedUp = signedUp.lower()
    for i in range(len(yes)):
        if signedUp == no[i] or signedUp == yes[i]:
            if signedUp == yes[i]:
                # TODO - create functions to call that will insert data into DB Table
                    print("Please login")
                    isSignedUp = True
                    break
            else:
                if signedUp == no[i]:
                    isSignedUp = False
                    break
        else:
            if i == len(yes) - 1:
                print("Please enter yes, y, 1 or no, n, 0")
                signUpPrompt()
                break

'''
    @Function: Primes userInput and calls function that checks signup prompt response
    @params: none
    @output: Same as checksSignupResponse output - which confirms data is correctly input into the terminal
'''
def signUpPrompt():
    signedUp = str(input(PROMPT))
    checksSignupResponse(signedUp)

'''
    @Function: Attempts to connect to the Database and throws exception if fails
    @params: dbFile
    @output: hopefully DB is connected
'''
def connectToDB(dbFile):
    try:
        connect = sqlite3.connect(dbFile)
        return connect
    except Error as e:
        print(e + "\nFailed to connect to Database, check the database file")
    return None

'''
    @Function: Asks for username and password to signup
    @params: none
    @output: Accepts username and password and inserts them into database
'''
def signUp():
    database = "login.db"
    conn = connectToDB(database)
    username = str(input("Create username: "))
    password = str(input("Create password: "))
    username.strip("\s+")
    password.strip("\s+")
    checkAndAcceptCredintials(conn, username, password)



'''
    @Function: Asks for username and password to sign in
    @params: none
    @output: Accepts user input and queries from DB
'''
def signIn():
    database = "login.db"
    conn = connectToDB(database)
    username = str(input("Username: "))
    password = str(input("Password: "))
    username.strip("\s+")
    password.strip("\s+")

    queryCredintials(conn, username, password)
'''
    @Function: Allows users to create account if userData does not exist
    @params: connect, username and password
    @output: Create Accounts for users that do not have one
'''
def checkAndAcceptCredintials(connect, username, password):
    sql = "INSERT INTO loginData VALUES ('{Uname}','{Pword}');"\
        .format(Uname = username, Pword = password)

    cursr = connect.cursor()
    cursr.execute(sql)
    connect.commit()

'''
    @Function: asks for data in the database
    @params: connect, username, and password
    @output: none
'''
def queryCredintials(connect, username, password):
    #TODO - Create a means for data to be checked and queried - run before var sql in check&Accewpt method
    userPasswordSQL = "(" + "'" + username + "'" + "," + " '" + password + "'" + ")"
    sql = "SELECT * FROM loginData WHERE userName = '{Uname}' AND password = '{Pword}'"\
        .format(Uname = username, Pword = password)

    cursr = connect.cursor()
    cursr.execute(sql)
    loginData = cursr.fetchone()
    if str(loginData) != userPasswordSQL:
        print("You can not get in")
    else:
        print("Your In")

main()




