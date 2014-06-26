#assignment3b.py
import assignment3a as a3a
import sqlite3

sql = {'average':"SELECT avg(num) FROM randnums",
			'maximum':"SELECT max(num) FROM randnums",
			'minimum':"SELECT min(num) FROM randnums",
			'sum':"SELECT sum(num) FROM randnums",
			'count':"SELECT count(num) FROM randnums"
			}

commands=list(sql.keys())
commands.append('refresh')
commands.append('quit')



while True:

    for i in range(len(commands)):
        print (str(i+1)+".) "+commands[i])

    usrinput=input("Make a selection: ")

    try:
        ans=commands[int(usrinput)-1]
        print ("Command found using integer input")

    except IndexError:
        print("Input interpreted as integer but integer option doesn't exist")
        ans=usrinput

    except TypeError and ValueError:
        print("Option could not be converted to an integer")
        print("Trying to find text in dict")
        try:
            ans_index=commands.index(usrinput)
            ans=usrinput
            print ("Command found using text input")
        except ValueError:
            print("Could not interpret input as a command")
            ans=usrinput

    if ans == commands[-1] or usrinput == len(commands):
        print ("BYE")
        break

    elif ans ==commands[-2] or usrinput == len(commands)-1:
        odb=a3a.refresh_db(100)
        print ("database was refreshed")
    elif ans in sql:
        with sqlite3.connect('newnum.db') as connection:
            c = connection.cursor()
            c.execute(sql[ans])
            result = c.fetchone()
            print(ans+": "+str(result[0]))
    else:
        print ("Choice was: "+ans)
        print ("I don't know what to do with that")
