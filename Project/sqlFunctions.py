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