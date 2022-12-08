from os import W_OK
import sqlite3
from sqlite3 import Error
import sqlFunctions
from tkinter import *

root = Tk()
root.title('Pokedex - World of Pokemon')
root.geometry("800x600")
global cstring
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
    def search(conn):
        cstring = str(clicked.get())
        if cstring == questions[0]:
            sqlFunctions.pokemonGenerationSearch(conn)
        if cstring == questions[1]:
            sqlFunctions.pokemonBaseStatsSpecific(conn)
        if cstring == questions[2]:
            sqlFunctions.pokeTypeSearch(conn)
        if cstring == questions[3]:
            sqlFunctions.pokeMovesSearch(conn)
        if cstring == questions[4]:
            sqlFunctions.pokeRegionSearch(conn)
        if cstring == questions[5]:
            sqlFunctions.pokeHeight_WeightSearch(conn)
        if cstring == questions[6]:
            sqlFunctions.pokeMovesetSearch(conn)
        if cstring == questions[7]:
            sqlFunctions.insertPokemon(conn)
        if cstring == questions[8]:
            sqlFunctions.deletePokemon(conn)
        if cstring == questions[9]:
            sqlFunctions.updatePokemonName(conn)
        if cstring == questions[10]:
            sqlFunctions.insertBaseStat(conn)
        if cstring == questions[11]:
            sqlFunctions.deleteBaseStat(conn)
        if cstring == questions[12]:
            sqlFunctions.updateBaseStats(conn)
        if cstring == questions[13]:
            sqlFunctions.searchLegendaryStatus(conn)
        if cstring == questions[14]:
            sqlFunctions.pokemonTypingResistances(conn)
        if cstring == questions[15]:
            sqlFunctions.generationTypingsCount(conn)
        if cstring == questions[16]:
            sqlFunctions.updateMoveset(conn)
        if cstring == questions[17]:
            sqlFunctions.searchPokemonAbilities(conn)
        if cstring == questions[18]:
            sqlFunctions.searchPokemonMoveInMoveset(conn)
        if cstring == questions[19]:
            sqlFunctions.speedSearch(conn)
        
        
    questions = [
        "pokemonGenerationSearch",
        "pokemonBaseStatsSpecific",
        "pokeTypeSearch",
        "pokeMovesSearch",
        "pokeRegionSearch",
        "pokeHeight_WeightSearch",
        "pokeMovesetSearch",
        "insertPokemon",
        "deletePokemon",
        "updatePokemonName",
        "insertBaseStat",
        "deleteBaseStat",
        "updateBaseStats",
        "searchLegendaryStatus",
        "pokemonTypingResistances",
        "generationTypingsCount",
        "updateMoveset",
        "searchPokemonAbilities",
        "searchPokemonMoveInMoveset",
        "speedSearch",
    ]
    
    


    database = r"pokedex.sqlite"

    conn = openConnection(database)

    with conn:
        #dropTable(conn)
        #createTable(conn)
        #createPokeGenTable(conn)
        #createPokeMovesSetTable(conn)
        #createPokeMovesTable(conn)
        #createPokemonTable(conn)
        #nothing here yet
        drop = OptionMenu(root, clicked, *questions)
        drop.grid(row=0,column=0)
        button = Button(root, text="Use Selected Search", command=lambda: search(conn))
        button.grid(row=0,column=1)
        e = Entry(root, width = 50)
        e.grid(row=1, column=0, columnspan=2)
        #sqlFunctions.pokemonGenerationSearch(conn)
        #sqlFunctions.pokemonBaseStatsSpecific(conn)
        #sqlFunctions.pokeTypeSearch(conn)
        #sqlFunctions.pokeMovesSearch(conn)
        #sqlFunctions.pokeRegionSearch(conn)
        #sqlFunctions.pokeHeight_WeightSearch(conn)
        #sqlFunctions.pokeMovesetSearch(conn)
        #sqlFunctions.insertPokemon(conn)
        #sqlFunctions.deletePokemon(conn)
        #sqlFunctions.updatePokemonName(conn)
        #sqlFunctions.insertBaseStat(conn)
        #sqlFunctions.deleteBaseStat(conn)
        #sqlFunctions.updateBaseStats(conn)
        #sqlFunctions.searchLegendaryStatus(conn)
        #sqlFunctions.pokemonTypingResistances(conn)
        #sqlFunctions.generationTypingsCount(conn)
        #sqlFunctions.updateMoveset(conn)
        #sqlFunctions.searchPokemonAbilities(conn)
        #sqlFunctions.searchPokemonMoveInMoveset(conn)
        #sqlFunctions.speedSearch(conn)
        
    root.mainloop()
    closeConnection(conn, database)

    



if __name__ == '__main__':
    main()