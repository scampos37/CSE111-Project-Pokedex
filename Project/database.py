from os import W_OK
import sqlite3
from sqlite3 import Error
import sqlFunctions


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
        sql = "DROP TABLE warehouse"
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
            
            #sqlFunctions.pokemonGenerationSearch(conn)
            #sqlFunctions.pokemonBaseStatsSpecific(conn)
            #sqlFunctions.pokeTypeSearch(conn)
            #sqlFunctions.pokeMovesSearch(conn)
            #sqlFunctions.insertPokemon(conn)
            #sqlFunctions.deletePokemon(conn)
            #sqlFunctions.updatePokemonName(conn)

        closeConnection(conn, database)



if __name__ == '__main__':
    main()