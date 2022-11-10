from os import W_OK
import sqlite3
from sqlite3 import Error

#1/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
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

#2/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

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

#3/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

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

#4/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def pokeMovesSearch(conn):
    print("--------------------------------------------")
    moveName = input("Enter name of move for a description of move: ")

    try:
        sql = """SELECT id, move, description
                FROM moves
                WHERE move = ?"""
        args = [moveName]
        cur = conn.cursor()
        cur.execute(sql, args)
        l = '{:<15} {:<25} {:<10}'.format("ID", "Move", "Description")
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

#5/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def insertPokemon(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Pokemon")
    iNum = input("What's the index number of your new Pokemon: ")
    pNum = input("What's the pokedex number of your new Pokemon: ")
    pName = input("What's the name of your new Pokemon: ")
    gen = input("What's the generation number of your new Pokemon: ")
    status = input("What's the legendary status of your new Pokemon: ")
    typeNum = int(input("How many typings does your new Pokemon have: "))
    type1 = input("What's the primary typing of your new Pokemon: ")
    type2 = ""
    if typeNum == 2:
        type2 = input("What's the secondary typing of your new Pokemon: ")
    height = input("What's the base height of your new Pokemon in meters: ")
    weight = input("What's the base weight of your new Pokemon in kilograms: ")
    abilityNum = int(input("How many abilities does your new Pokemon have: "))
    ability1, ability2, abilityh = "", "", ""
    if abilityNum == 1:
        htrue = input("Is your ability a hidden ability? Y or N: ")
        if htrue == "Y":
            abilityh = input("What's your new Pokemon's hidden ability: ")
        else:
            ability1 = input("What's your new Pokemon's first ability: ")
    elif abilityNum == 2:
        ability1 = input("What's your new Pokemon's first ability: ")
        abilityh = input("What's your new Pokemon's hidden ability: ")
    elif abilityNum == 3:
        ability1 = input("what's your new Pokemon's first ability: ")
        ability2 = input("What's your new Pokemon's secondary ability: ")
        abilityh = input("What's your new Pokemon's hidden ability: ")
    try:
        sql = "INSERT INTO pokemon VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?)"
        args = [iNum, pNum, pName, gen, status, typeNum, type1, type2, height, weight, abilityNum, ability1, ability2, abilityh]
        conn.execute(sql, args)
        conn.commit()
        print("successfully inserted " + pName + " into the Pokemon table")
    except Error as e:
        conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

#6/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def pokeRegionSearch(conn):
    print("--------------------------------------------")
    regName = input("What region of pokemon are you looking for?: ")

    

    try:
        sql = """SELECT region_name, pokemon.generation, name
                FROM pokemon, gen
                WHERE 
                    pokemon.generation = gen.generation AND 
                    region_name = ?"""
        args = [regName]
        cur = conn.cursor()
        cur.execute(sql, args)
        l = '{:<15} {:<10} {:<10}'.format("Region", "Generation", "Pokemon_name")
        print(l)
        print("-------------------------------")
        rows = cur.fetchall()
        for row in rows:
            l = '{:<15} {:<10} {:<10}'.format(row[0], row[1], row[2])
            print(l)
    except Error as e:
        conn.rollback()
        print(e)
    print("--------------------------------------------")

#7/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def pokeHeight_WeightSearch(conn):
    print("--------------------------------------------")
    #heightNum, weightNum = float(input("Enter Height: ")), float(input("Enter Weight: "))

    try:
        sql = """SELECT pokedex_number, name, height_m, weight_kg
                FROM pokemon
                WHERE 
                    height_m > 1 AND 
                    weight_kg > 50"""
        #args = [heightNum, weightNum]
        cur = conn.cursor()
        cur.execute(sql)
        #cur.execute(sql, args)
        l = '{:<15} {:<25} {:<10} {:<10}'.format("Pokedex_ID", "Pokemon_name", "Height", "Weight")
        print(l)
        print("-------------------------------")
        rows = cur.fetchall()
        for row in rows:
            l = '{:<15} {:<25} {:<10} {:<10}'.format(row[0], row[1], row[2], row[3])
            print(l)
    except Error as e:
        conn.rollback()
        print(e)
    print("--------------------------------------------")

#8/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def pokeMovesetSearch(conn):
    print("--------------------------------------------")
    
    try:
        sql = """SELECT pokedex_number, name, move1, description
                FROM pokemon, moveset, moves
                WHERE 
                    pokedex_number = ndex AND
                    move1 LIKE '%Scratch' AND
                    move = 'Scratch'

                    """
    
        cur = conn.cursor()
        cur.execute(sql)

        l = '{:<15} {:<25} {:<20} {:<15}'.format("Pokedex_ID", "Pokemon_name", "move1", "Description")
        print(l)
        print("-------------------------------")
        rows = cur.fetchall()
        for row in rows:
            l = '{:<15} {:<25} {:<20} {:<15}'.format(row[0], row[1], row[2], row[3])
            print(l)
    except Error as e:
        conn.rollback()
        print(e)
    print("--------------------------------------------")

#9/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def deletePokemon(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Deleting Pokemon from pokemon table by index_number")
    iNum = input("Which index_number would you like to delete from the Pokemon Table: ")
    try:
        sql = """DELETE FROM pokemon
                WHERE index_number = ?"""
        args = [iNum]
        conn.execute(sql, args)
        conn.commit()
        print("successfully deleted " + iNum + " from Pokemon Table")
    except Error as e:
        conn.rollback()
        print(e)
    print("--------------------------------------------") 

#10/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def updatePokemonName(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Updating a Pokemon's name from pokemon table by index_number")
    iNum = input("Which index_number would you like to update from the Pokemon Table: ")
    pName = input("What is the updated name you want for the Pokemon?: ")
    try:
        sql = """UPDATE pokemon
                SET name = ?
                WHERE index_number = ?"""
        args = [pName, iNum]
        conn.execute(sql, args)
        conn.commit()
        print("successfully updated " + iNum + " from Pokemon Table to " + pName)
    except Error as e:
        conn.rollback()
        print(e)
    print("--------------------------------------------") 

#11/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def insertBaseStat(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Inserting new Pokemon's base stats")
    iNum = input("What's the index number of the Pokemon: ")
    pNum = input("What's the pokedex number of the Pokemon:")
    hp = input("What's the base hp stat of the Pokemon: ")
    attack = input("What's the base attack stat of the Pokemon: ")
    defense = input("What's the base defense stat of the Pokemon: ")
    sp_attack = input("What's the base special attack stat of the Pokemon: ")
    sp_defense = input("What's the base special defense stat of the Pokemon: ")
    speed = input("What's the base hp stat of the Pokemon: ")
    try:
        sql = """INSERT INTO baseStats VALUES(?, ?, ?, ?, ?, ?, ?, ?)"""
        args = [iNum, pNum, hp, attack, defense, sp_attack, sp_defense, speed]
        conn.execute(sql, args)
        conn.commit()
        print("successfully inserted " + iNum + " into the base stat table")
    except Error as e:
        conn.rollback()
        print(e)
    print("--------------------------------------------") 

#12/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def deleteBaseStat(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Deleting Pokemon base stats from baseStats table by index_number")
    iNum = input("Which index_number would you like to delete from the baseStats Table: ")
    try:
        sql = """DELETE FROM baseStats
                WHERE index_number = ?"""
        args = [iNum]
        conn.execute(sql, args)
        conn.commit()
        print("successfully deleted " + iNum + " from baseStats Table")
    except Error as e:
        conn.rollback()
        print(e)
    print("--------------------------------------------") 

#13/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def updateBaseStats(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Updating a Pokemon's base stats")
    iNum = input("What's the index number of the Pokemon: ")
    hp = input("What's the new base hp stat of the Pokemon: ")
    attack = input("What's the new base attack stat of the Pokemon: ")
    defense = input("What's the new base defense stat of the Pokemon: ")
    sp_attack = input("What's the new base special attack stat of the Pokemon: ")
    sp_defense = input("What's the new base special defense stat of the Pokemon: ")
    speed = input("What's the new base hp stat of the Pokemon: ")
    try:
        sql = """UPDATE baseStats
                SET hp = ?, attack = ?, defense = ?, sp_attack = ?, sp_defense = ?, speed = ?
                WHERE index_number = ? """
        args = [hp, attack, defense, sp_attack, sp_defense, speed, iNum]
        conn.execute(sql, args)
        conn.commit()
        print("successfully updated the base stats of " + iNum + " in the base stat table")
    except Error as e:
        conn.rollback()
        print(e)
    print("--------------------------------------------") 

#14/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def searchLegendaryStatus(conn):
    print("--------------------------------------------")
    status = input("What legendary status does your pokemon have: ")
    try:
        sql = """SELECT pokedex_number, name, status
                FROM pokemon
                WHERE status = ?"""
        args = [status]
        cur = conn.cursor()
        cur.execute(sql, args)
        l = '{:<15} {:<25} {:<10}'.format("Pokedex_Number", "Pokemon_Name", "Status")
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

#15/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def pokemonTypingResistances(conn):
    print("--------------------------------------------")
    typeNum = int(input("Does your pokemon have one or two typings: "))
    type1 = input("What's the primary typing: ")
    if (typeNum == 2):
        type2 = input("What's the secondary typing: ")
    try:
        if (typeNum == 1):
            sql = """SELECT pokedex_number, name, type_1, normal, fire, water, electric, grass, ice, fighting, poison, ground, flying, psychic, bug, rock, ghost, dragon, dark, steel, fairy
                    FROM pokemon, typing
                    WHERE type_1 = ?
                        AND type_2 = "" 
                        AND type_1 = defense_type1
                        AND type_2 = defense_type2 """
            args = [type1]
            cur = conn.cursor()
            cur.execute(sql, args)
            l = '{:<15} {:<25} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}'.format("Pokedex_Number","Pokemon_Name", "Type", "normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy")
            print(l)
            print("-------------------------------")

            rows = cur.fetchall()
            for row in rows:
                l = '{:<15} {:<25} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20])
                print(l)
        if (typeNum == 2):
            sql = """SELECT pokedex_number, name, type_1, type_2, normal, fire, water, electric, grass, ice, fighting, poison, ground, flying, psychic, bug, rock, ghost, dragon, dark, steel, fairy
                    FROM pokemon, typing
                    WHERE type_1 = ?
                        AND type_2 = ? 
                        AND type_1 = defense_type1
                        AND type_2 = defense_type2 """
            args = [type1, type2]
            cur = conn.cursor()
            cur.execute(sql, args)
            l = '{:<15} {:<25} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}'.format("Pokedex_Number","Pokemon_Name", "Type1", "Type2", "normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy")
            print(l)
            print("-------------------------------")

            rows = cur.fetchall()
            for row in rows:
                l = '{:<15} {:<25} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21])
                print(l)

    except Error as e:
        conn.rollback()
        print(e)