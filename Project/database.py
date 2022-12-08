from os import W_OK
import sqlite3
from sqlite3 import Error
import sqlFunctions
from tkinter import *

root = Tk()
root.title('Pokedex - World of Pokemon')
root.geometry("800x600")
global cstring
Q1,Q2,Q3,Q4,Q5 = Label(root),Label(root),Label(root),Label(root),Label(root)
Q6,Q7,Q8,Q9,Q10 = Label(root),Label(root),Label(root),Label(root),Label(root)
Q11,Q12,Q13,Q14 =Label(root),Label(root),Label(root),Label(root)
e1,e2,e3,e4,e5 = Entry(root),Entry(root),Entry(root),Entry(root),Entry(root)
e6,e7,e8,e9,e10 = Entry(root),Entry(root),Entry(root),Entry(root),Entry(root)
e11,e12,e13,e14 =Entry(root),Entry(root),Entry(root),Entry(root)

cstring = ""

def openConnection(pokefile):
    print("--------------------------------------------")
    print("Opening pokedex: ", pokefile)

    conn = None

    try:
        conn = sqlite3.connect(pokefile)
        print("success")
    
    except Error as e:
        print(e)


    print("--------------------------------------------")
    return conn


def closeConnection(conn, pokefile):
    print("--------------------------------------------")
    print("Close database: ", pokefile)

    try:
        conn.close()
        print("success")
    except Error as e:
        print(e)

    print("--------------------------------------------")


def dropTable(conn):
    print("--------------------------------------------")
    print("Drop tables")

    try:
        sql = "DROP TABLE typing"
        conn.execute(sql)

        conn.commit()
        print("success")

    except Error as e:
        conn.rollback()
        print(e)

    print("--------------------------------------------")

def createTable(conn):
    print("--------------------------------------------")
    print("Create table")

    try:
        sql = 0

        conn.execute(sql)

        conn.commit()
        print("success")
    except Error as e:
        conn.rollback()
        print(e)
        

    print("--------------------------------------------")

def createPokeGenTable(conn):
    print("--------------------------------------------")
    print("Create table")

    try:
        sql = """CREATE TABLE pokeGeneration ()"""

        conn.execute(sql)

        conn.commit()
        print("success")
    except Error as e:
        conn.rollback()
        print(e)
        

    print("--------------------------------------------")

def createPokeMovesSetTable(conn):
    print("--------------------------------------------")
    print("Create table")

    try:
        sql = """CREATE TABLE PokeMovesSet ()"""

        conn.execute(sql)

        conn.commit()
        print("success")
    except Error as e:
        conn.rollback()
        print(e)
        

    print("--------------------------------------------")   

def createPokeMovesTable(conn):
    print("--------------------------------------------")
    print("Create table")

    try:
        sql = """CREATE TABLE Moves ()"""

        conn.execute(sql)

        conn.commit()
        print("success")
    except Error as e:
        conn.rollback()
        print(e)
        

    print("--------------------------------------------")

def createPokemonTable(conn):
    print("--------------------------------------------")
    print("Create table")

    try:
        sql = """CREATE TABLE Pokemon ()"""

        conn.execute(sql)

        conn.commit()
        print("success")
    except Error as e:
        conn.rollback()
        print(e)
        

    print("--------------------------------------------") 



def main():
    clicked = StringVar()
    
    def process(event=None):
        content = e1.get() # get the contents of the entry widget
        print(content)
        print(clicked.get())
        if clicked.get() == questions[0]:
            sqlFunctions.pokemonGenerationSearch(conn, root, content)
        if clicked.get() == questions[1]:
            x = content
            if (x == "name"):
                pname = e2.get()
                vList = [x,pname]
            else:
                pdnum = e2.get()
                vList = [x,pdnum]
            print(vList)
            sqlFunctions.pokemonBaseStatsSpecific(conn, root, vList)
        if clicked.get() == questions[2]:
            x = content
            y = e2.get()
            vList = [x,y]
            if (x == "2"):
                z = e3.get()
                vList.append(z)
            sqlFunctions.pokeTypeSearch(conn, root, vList)
        if clicked.get() == questions[3]:
            sqlFunctions.pokeMovesSearch(conn, root, content)
        if clicked.get() == questions[4]:
            sqlFunctions.pokeRegionSearch(conn, root, content)
        if clicked.get() == questions[5]:
            sqlFunctions.searchLegendaryStatus(conn, root, content)
        if clicked.get() == questions[6]:
            x = content
            y = e2.get()
            vList = [x,y]
            if (x == "2"):
                z = e3.get()
                vList.append(z)
            sqlFunctions.pokemonTypingResistances(conn, root, vList)
        if clicked.get() == questions[7]:
            x = content
            y = e2.get()
            z = e3.get()
            vList = [x,y,z]
            if (y == "2"):
                w = e4.get()
                vList.append(w)
            sqlFunctions.generationTypingsCount(conn, root, vList)
        if clicked.get() == questions[8]:
            sqlFunctions.searchPokemonAbilities(conn, root, content)
        if clicked.get() == questions[9]:
            sqlFunctions.searchPokemonMoveInMoveset(conn, root, content)
            

    def search(conn):
        global Q1, Q2, Q3, Q4
        global e1, e2, e3, e4
        Q1.destroy(), Q2.destroy(), Q3.destroy(), Q4.destroy()
        e1.destroy(), e2.destroy(), e3.destroy(), e4.destroy()
        cstring = str(clicked.get())
        e1 = Entry(root, width=50)
        e1.grid(row=2, column=0, columnspan=2)
        if cstring == questions[0]:
            Q1 = Label(root, text = "What generation are you looking for: ")
            Q1.grid(row=1,column=0, columnspan=5)
            root.bind('<Return>', process)
            
        if cstring == questions[1]:
            Q1 = Label(root, text="Search by Pokemon Name (name) or Pokedex Number (number)")
            Q1.grid(row=1, column=0, columnspan=5)
            e2 = Entry(root, width=50)
            e2.grid(row=4, column=0, columnspan=2)
            Q2 = Label(root, text="You're chosen input")
            Q2.grid(row=3, column=0, columnspan=5)
            root.bind('<Return>', process)
        if cstring == questions[2]:
            Q1 = Label(root, text="What how many typings does the pokemon you are looking for have?: ")
            Q1.grid(row=1, column=0, columnspan=5)
            Q2 = Label(root, text="What's the first typing: ")
            Q2.grid(row=3, column=0, columnspan=5)
            Q3 = Label(root, text="What's the second typing: ")
            Q3.grid(row=5, column=0, columnspan=5)
            e1 = Entry(root, width=50)
            e1.grid(row=2, column=0, columnspan=2)
            e2 = Entry(root, width=50)
            e2.grid(row=4, column=0, columnspan=2)
            e3 = Entry(root, width=50)
            e3.grid(row=6, column=0, columnspan=2)
            root.bind('<Return>', process)
        if cstring == questions[3]:
            Q1 = Label(root, text="Enter name of move for a description of move: ")
            Q1.grid(row=1, column=0, columnspan=5)
            e1 = Entry(root, width=50)
            e1.grid(row=2, column=0, columnspan=2)
            root.bind('<Return>', process)
        if cstring == questions[4]:
            Q1 = Label(root, text="Which Region do you want to look for Pokemon: ")
            Q1.grid(row=1, column=0, columnspan=5)
            e1 = Entry(root, width=50)
            e1.grid(row=2, column=0, columnspan=2)
            root.bind('<Return>', process)
            sqlFunctions.pokeRegionSearch(conn, root, e)
        if cstring == questions[5]:
            Q1 = Label(root, text="What legendary status does your pokemon have: ")
            Q1.grid(row=1, column=0, columnspan=5)
            e1 = Entry(root, width=50)
            e1.grid(row=2, column=0, columnspan=2)
            root.bind('<Return>', process)
            
        if cstring == questions[6]:
            Q1 = Label(root, text="What how many typings does the pokemon you are looking for have?: ")
            Q1.grid(row=1, column=0, columnspan=5)
            Q2 = Label(root, text="What's the first typing: ")
            Q2.grid(row=3, column=0, columnspan=5)
            Q3 = Label(root, text="What's the second typing: ")
            Q3.grid(row=5, column=0, columnspan=5)
            e1 = Entry(root, width=50)
            e1.grid(row=2, column=0, columnspan=2)
            e2 = Entry(root, width=50)
            e2.grid(row=4, column=0, columnspan=2)
            e3 = Entry(root, width=50)
            e3.grid(row=6, column=0, columnspan=2)
            root.bind('<Return>', process)

        if cstring == questions[7]:
            Q1 = Label(root, text="Which generation do you wanna search: ")
            Q1.grid(row=1, column=0, columnspan=5)
            Q2 = Label(root, text="What how many typings does the pokemon you are looking for have?: ")
            Q2.grid(row=3, column=0, columnspan=5)
            Q3 = Label(root, text="What's the first typing: ")
            Q3.grid(row=5, column=0, columnspan=5)
            Q4 = Label(root, text="What's the second typing: ")
            Q4.grid(row=7, column=0, columnspan=5)
            e1 = Entry(root, width=50)
            e1.grid(row=2, column=0, columnspan=2)
            e2 = Entry(root, width=50)
            e2.grid(row=4, column=0, columnspan=2)
            e3 = Entry(root, width=50)
            e3.grid(row=6, column=0, columnspan=2)
            e4 = Entry(root, width=50)
            e4.grid(row=8, column=0, columnspan=2)
            root.bind('<Return>', process)
            
        if cstring == questions[8]:
            Q1 = Label(root, text="Which ability are you looking for: ")
            Q1.grid(row=1, column=0, columnspan=5)
            e1 = Entry(root, width=50)
            e1.grid(row=2, column=0, columnspan=2)
            root.bind('<Return>', process)
            
        if cstring == questions[9]:
            Q1 = Label(root, text="Which move are you looking for: ")
            Q1.grid(row=1, column=0, columnspan=5)
            e1 = Entry(root, width=50)
            e1.grid(row=2, column=0, columnspan=2)
            root.bind('<Return>', process)
        
        
    questions = [
        "pokemonGenerationSearch",
        "pokemonBaseStatsSpecific",
        "pokeTypeSearch",
        "pokeMovesSearch",
        "pokeRegionSearch",
        "searchLegendaryStatus",
        "pokemonTypingResistances",
        "generationTypingsCount",
        "searchPokemonAbilities",
        "searchPokemonMoveInMoveset"
    ]


    


    database = r"pokedex.sqlite"

    conn = openConnection(database)

    with conn:
        
        drop = OptionMenu(root, clicked, *questions)
        drop.grid(row=0,column=0)
        button = Button(root, text="Use Selected Search", command=lambda: search(conn))
        button.grid(row=0,column=1)
        e = Entry(root, width = 50)
        e.grid(row=2, column=0, columnspan=2)
        
        
    root.mainloop()
    closeConnection(conn, database)

    



if __name__ == '__main__':
    main()