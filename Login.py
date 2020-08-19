import mysql.connector

while(True):
    mydb = mysql.connector.connect(
        host="localhost", user="ss", password="", database="pythonlogin")
    mycursor = mydb.cursor()
    usernamesSQL = []
    mycursor.execute("SELECT username FROM users")
    results = mycursor.fetchall()
    for i in results:
        k = i[-1]
        usernamesSQL.append(k)

    choice = input("Login or Signup? (l/s): ").lower()
    if(choice == "l"):
        usernameInput = input("Username: ")
        passwordInput = input("Password: ")
        usernameGood = False
        for i in usernamesSQL:
            if(usernameInput == i):
                usernameGood = True
                currUser = usernamesSQL[usernamesSQL.index(i)]
                mycursor.execute(
                    f"SELECT password FROM users WHERE username='{currUser}'")
                password = str(mycursor.fetchone()[-1])
        if(usernameGood):
            if(passwordInput == password):
                break
        else:
            print("Invalid Username or Password")
            continue
    elif(choice == "s"):
        usernameInput = input("Username: ")
        passwordInput = input("Password: ")
        continueToNext = False
        if(usernameInput == "" or passwordInput == ""):
            print("Invalid Username or Password")
            continue
        for i in usernamesSQL:
            if(usernameInput == i):
                print("Username already in use")
                continueToNext = True
                break
        if(continueToNext):
            continue
        insrtTable = "INSERT INTO users (username, password) VALUES (%s, %s)"
        val = (usernameInput, passwordInput)
        mycursor.execute(insrtTable, val)
        mydb.commit()
        print("Signed Up. Now you may login.")
    else:
        print("invalid option")
        continue

print("Logged in!")
