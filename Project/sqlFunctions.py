from os import W_OK
import sqlite3
from sqlite3 import Error

def pokemonGenerationSearch(conn):
    print("--------------------------------------------")
    genNum = input("What generation are you looking for: ")

    try:
        sql = """SELECT pokedex_number, name as pokemon_name, generation
                FROM pokemon
                WHERE generation = ?"""
        args = [genNum]
        cur = conn.cursor()
        cur.execute(sql, args)
        l = '{:<15} {:<25} {:<10}'.format("PokedexNumber", "PokemonName", "Generation")
        print(l)
        print("-------------------------------")
        rows = cur.fetchall()
        for row in rows:
            l = '{:<15} {:<25} {:<10}'.format(row[0], row[1], row[2])
            print(l)
    except Error as e:
        conn.rollback()
        print(e)
    print("--------------------------------------------") 

def pokemonBaseStatsSpecific(conn):
    print("--------------------------------------------")
    x = ""
    while(x != "name" or x != "number"):
        x = input("Search by Pokemon Name (name) or Pokedex Number (number)")
        if (x == "name"):
            pname = input("What's the pokemon's name: ")
            break
        elif(x == "number"):
            pdnum = input("What's the pokemon's pokedex number: ")
            break

    try:
        if (x == "name") :
            sql = """SELECT pokemon.pokedex_number, name as pokemon_name, hp, attack, defense, sp_attack, sp_defense, speed, height_m, weight_kg
                    FROM pokemon, baseStats
                    WHERE pokemon_name = ?
                        AND pokemon.pokedex_number = baseStats.pokedex_number"""
            args = [pname]
        else:
            sql = """SELECT pokemon.pokedex_number, name as pokemon_name, hp, attack, defense, sp_attack, sp_defense, speed, height_m, weight_kg
                    FROM pokemon, baseStats
                    WHERE pokemon.pokedex_number = ?
                        AND pokemon.pokedex_number = baseStats.pokedex_number"""
            args = [pdnum]
        
        cur = conn.cursor()
        cur.execute(sql, args)
        l = '{:<15} {:<25} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}'.format("PokedexNumber", "PokemonName", "HP", "attack", "defense", "sp_attack", "sp_defense", "speed", "height (M)", "weight (kg)")
        print(l)
        print("-------------------------------")
        rows = cur.fetchall()
        for row in rows:
            l = '{:<15} {:<25} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            print(l)
    except Error as e:
        conn.rollback()
        print(e)
    print("--------------------------------------------") 


def pokeTypeSearch(conn):
    print("--------------------------------------------")
    typeNum = int(input("What how many typings does the pokemon you are looking for have?: "))

    if (typeNum == 1):
        typeName = input("What poke type are you looking for?: ")
        try:
            sql = """SELECT pokedex_number, name, type_1
                    FROM pokemon
                    WHERE type_1 = ?"""
            args = [typeName]
            cur = conn.cursor()
            cur.execute(sql, args)

            l = '{:<10} {:<25} {:<10}'.format("Pokedex_Number","Pokemon_Name", "Type")
            print(l)
            print("-------------------------------")

            rows = cur.fetchall()
            for row in rows:
                l = '{:<10} {:<25} {:<10}'.format(row[0], row[1], row[2])
                print(l)

        except Error as e:
            conn.rollback()
            print(e)

    elif (typeNum == 2):
         
        typeName1, typeName2 = input("What's the first typing: ") , input ("What's the second typing: ")
        try:
            sql = """SELECT pokedex_number, name, type_1, type_2
                    FROM pokemon
                    WHERE type_1 = ?
                        AND type_2 = ?"""
                        
            args = [typeName1, typeName2]
            cur = conn.cursor()
            cur.execute(sql, args)

            l = '{:<15} {:<25} {:<10} {:<10}'.format("Pokedex_Number", "Pokemon_Name", "Type1", "Type2")
            print(l)
            print("-------------------------------")

            rows = cur.fetchall()
            for row in rows:
                l = '{:<15} {:<25} {:<10} {:<10}'.format(row[0], row[1], row[2], row[3])
                print(l)

        except Error as e:
            conn.rollback()
            print(e)