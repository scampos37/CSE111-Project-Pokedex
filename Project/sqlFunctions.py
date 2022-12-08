from os import W_OK
import sqlite3
from sqlite3 import Error
from tkinter import *

#1/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
def pokemonGenerationSearch(conn, my_tree, genNum):
    print("--------------------------------------------")
    my_tree
    my_tree['columns'] = ("Pokedex_Number", "Pokemon_Name", "Generation")
    my_tree.column("#0", width=10)
    my_tree.column("Pokedex_Number", anchor=CENTER, width=120)
    my_tree.column("Pokemon_Name", anchor=W, width=120)
    my_tree.column("Generation", anchor=W, width=120)
    my_tree.heading("#0", text = "List", anchor=W)
    my_tree.heading("Pokedex_Number", text = "Pokedex_Number", anchor=W)
    my_tree.heading("Pokemon_Name", text = "Pokemon_Name", anchor=W)
    my_tree.heading("Generation", text = "Generation", anchor=W)

    try:
        sql = """SELECT pokedex_number, name as pokemon_name, generation
                FROM pokemon
                WHERE generation = ?"""
        args = [genNum]
        cur = conn.cursor()
        cur.execute(sql, args)
        
        print("-------------------------------")
        rows = cur.fetchall()
        for row in rows: 
            my_tree.insert("", 'end', text="",
               values =(row[0],row[1],row[2]))
    except Error as e:
        conn.rollback()
        print(e)
    print("--------------------------------------------") 

#2/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def pokemonBaseStatsSpecific(conn, my_tree, e):
    print("--------------------------------------------")
    x = e[0]
    my_tree['columns'] = ("PokedexNumber", "PokemonName", "HP", "Attack", "Defense", "SP_Attack", "SP_Defense", "Speed", "Height_m", "Weight_kg")
    my_tree.column("#0", width=10)
    my_tree.column("PokedexNumber", anchor=CENTER, width=120)
    my_tree.column("PokemonName", anchor=W, width=120)
    my_tree.column("HP", anchor=W, width=50)
    my_tree.column("Attack", anchor=W, width=50)
    my_tree.column("Defense", anchor=W, width=50)
    my_tree.column("SP_Attack", anchor=W, width=50)
    my_tree.column("SP_Defense", anchor=W, width=50)
    my_tree.column("Speed", anchor=W, width=50)
    my_tree.column("Height_m", anchor=W, width=50)
    my_tree.column("Weight_kg", anchor=W, width=50)
    my_tree.heading("#0", text = "List", anchor=W)
    my_tree.heading("PokedexNumber", text = "PokedexNumber", anchor=W)
    my_tree.heading("PokemonName", text = "PokemonName", anchor=W)
    my_tree.heading("HP", text = "HP", anchor=W)
    my_tree.heading("Attack", text = "Attack", anchor=W)
    my_tree.heading("Defense", text = "Defense", anchor=W)
    my_tree.heading("SP_Attack", text = "SP_Attack", anchor=W)
    my_tree.heading("SP_Defense", text = "SP_Defense", anchor=W)
    my_tree.heading("Speed", text = "Speed", anchor=W)
    my_tree.heading("Height_m", text = "Height_m", anchor=W)
    my_tree.heading("Weight_kg", text = "Weight_kg", anchor=W)

    try:
        if (x == "name") :
            pname = e[1]
            sql = """SELECT pokemon.pokedex_number, name as pokemon_name, hp, attack, defense, sp_attack, sp_defense, speed, height_m, weight_kg
                    FROM pokemon, baseStats
                    WHERE pokemon_name = ?
                        AND pokemon.pokedex_number = baseStats.pokedex_number"""
            args = [pname]
        else:
            pdnum = e[1]
            sql = """SELECT pokemon.pokedex_number, name as pokemon_name, hp, attack, defense, sp_attack, sp_defense, speed, height_m, weight_kg
                    FROM pokemon, baseStats
                    WHERE pokemon.pokedex_number = ?
                        AND pokemon.pokedex_number = baseStats.pokedex_number"""
            args = [pdnum]
        
        cur = conn.cursor()
        cur.execute(sql, args)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows: 
            my_tree.insert("", 'end', text="",
               values =(row[0],row[1],row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
    except Error as e:
        conn.rollback()
        print(e)
    print("--------------------------------------------") 

#3/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def pokeTypeSearch(conn, my_tree, e):
    print("--------------------------------------------")
    print(e)
    if (e[0] == "1"):
        typeName = e[1]

        my_tree['columns'] = ("Pokedex_Number", "Pokemon_Name", "Type_1")
        my_tree.column("#0", width=10)
        my_tree.column("Pokedex_Number", anchor=CENTER, width=120)
        my_tree.column("Pokemon_Name", anchor=W, width=120)
        my_tree.column("Type_1", anchor=W, width=120)
        my_tree.heading("#0", text = "List", anchor=W)
        my_tree.heading("Pokedex_Number", text = "Pokedex_Number", anchor=W)
        my_tree.heading("Pokemon_Name", text = "Pokemon_Name", anchor=W)
        my_tree.heading("Type_1", text = "Type_1", anchor=W)


        try:
            sql = """SELECT pokedex_number, name, type_1
                    FROM pokemon
                    WHERE type_1 = ?"""
            args = [typeName]
            cur = conn.cursor()
            cur.execute(sql, args)

            print("-------------------------------")
            rows = cur.fetchall()
            for row in rows: 
                my_tree.insert("", 'end', text="",
                    values =(row[0],row[1],row[2]))

        except Error as e:
            conn.rollback()
            print(e)

    elif (e[0] == "2"):
         
        typeName1, typeName2 = e[1], e[2]

        my_tree['columns'] = ("Pokedex_Number", "Pokemon_Name", "Type_1", "Type_2")
        my_tree.column("#0", width=10)
        my_tree.column("Pokedex_Number", anchor=CENTER, width=120)
        my_tree.column("Pokemon_Name", anchor=W, width=120)
        my_tree.column("Type_1", anchor=W, width=120)
        my_tree.column("Type_2", anchor=W, width=120)

        my_tree.heading("#0", text = "List", anchor=W)
        my_tree.heading("Pokedex_Number", text = "Pokedex_Number", anchor=W)
        my_tree.heading("Pokemon_Name", text = "Pokemon_Name", anchor=W)
        my_tree.heading("Type_1", text = "Type_1", anchor=W)
        my_tree.heading("Type_2", text = "Type_2", anchor=W)

        try:
            sql = """SELECT pokedex_number, name, type_1, type_2
                    FROM pokemon
                    WHERE type_1 = ?
                        AND type_2 = ?"""
                        
            args = [typeName1, typeName2]
            cur = conn.cursor()
            cur.execute(sql, args)

            print("-------------------------------")
            rows = cur.fetchall()
            for row in rows: 
                my_tree.insert("", 'end', text="",
                    values =(row[0],row[1],row[2], row[3]))

        except Error as e:
            conn.rollback()
            print(e)

#4/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def pokeMovesSearch(conn, my_tree, e):
    print("--------------------------------------------")
    moveName = e
    my_tree['columns'] = ("Index_Number", "Move", "Description")
    my_tree.column("#0", width=10)
    my_tree.column("Index_Number", anchor=CENTER, width=120)
    my_tree.column("Move", anchor=W, width=120)
    my_tree.column("Description", anchor=W, width=120)
    my_tree.heading("#0", text = "List", anchor=W)
    my_tree.heading("Index_Number", text = "Index_Number", anchor=W)
    my_tree.heading("Move", text = "Move", anchor=W)
    my_tree.heading("Description", text = "Description", anchor=W)

    try:
        sql = """SELECT id, move, description
                FROM moves
                WHERE move = ?"""
        args = [moveName]
        cur = conn.cursor()
        cur.execute(sql, args)

        print("-------------------------------")
        rows = cur.fetchall()
        for row in rows: 
            my_tree.insert("", 'end', text="",
               values =(row[0],row[1],row[2]))
    except Error as e:
        conn.rollback()
        print(e)
    print("--------------------------------------------")

#5/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def insertPokemon(conn, root, e):
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

def pokeRegionSearch(conn, my_tree, e):
    print("--------------------------------------------")
    regName = e
    my_tree['columns'] = ("Region_Name", "Generation", "Pokemon_Name")
    my_tree.column("#0", width=10)
    my_tree.column("Region_Name", anchor=CENTER, width=120)
    my_tree.column("Generation", anchor=W, width=120)
    my_tree.column("Pokemon_Name", anchor=W, width=120)
    my_tree.heading("#0", text = "List", anchor=W)
    my_tree.heading("Region_Name", text = "Region_Name", anchor=W)
    my_tree.heading("Generation", text = "Generation", anchor=W)
    my_tree.heading("Pokemon_Name", text = "Pokemon_Name", anchor=W)

    try:
        sql = """SELECT region_name, pokemon.generation, name
                FROM pokemon, gen
                WHERE 
                    pokemon.generation = gen.generation AND 
                    region_name = ?"""
        args = [regName]
        cur = conn.cursor()
        cur.execute(sql, args)
        
        print("-------------------------------")
        rows = cur.fetchall()
        for row in rows: 
            my_tree.insert("", 'end', text="",
               values =(row[0],row[1],row[2]))
    except Error as e:
        conn.rollback()
        print(e)
    print("--------------------------------------------")

#7/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def pokeHeight_WeightSearch(conn, my_tree, e):
    print("--------------------------------------------")
    #heightNum, weightNum = float(input("Enter Height: ")), float(input("Enter Weight: "))
    my_tree['columns'] = ("Pokedex_Number", "Pokemon_Name", "Height", "Weight")
    my_tree.column("#0", width=10)
    my_tree.column("Pokedex_Number", anchor=CENTER, width=120)
    my_tree.column("Pokemon_Name", anchor=W, width=120)
    my_tree.column("Height", anchor=W, width=120)
    my_tree.column("Weight", anchor=W, width=120)
    my_tree.heading("#0", text = "List", anchor=W)
    my_tree.heading("Pokedex_Number", text = "Pokedex_Number", anchor=W)
    my_tree.heading("Pokemon_Name", text = "Pokemon_Name", anchor=W)
    my_tree.heading("Height", text = "Height", anchor=W)
    my_tree.heading("Weight", text = "Weight", anchor=W)


    try:
        sql = """SELECT pokedex_number, name, height_m, weight_kg
                FROM pokemon
                WHERE 
                    height_m > 1 AND 
                    weight_kg > 50"""
        #args = [heightNum, weightNum]
        cur = conn.cursor()
        cur.execute(sql)
       
        print("-------------------------------")
        rows = cur.fetchall()
        for row in rows: 
            my_tree.insert("", 'end', text="",
               values =(row[0],row[1],row[2], row[3]))
    except Error as e:
        conn.rollback()
        print(e)
    print("--------------------------------------------")

#8/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def pokeMovesetSearch(conn, my_tree, e):
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

def deletePokemon(conn, root, e):
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

def updatePokemonName(conn, root, e):
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

def insertBaseStat(conn, root, e):
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

def deleteBaseStat(conn, root, e):
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

def updateBaseStats(conn, root, e):
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

def searchLegendaryStatus(conn, my_tree, e):
    print("--------------------------------------------")
    status = e
    my_tree['columns'] = ("Pokedex_Number", "Pokemon_Name", "Status")
    my_tree.column("#0", width=10)
    my_tree.column("Pokedex_Number", anchor=CENTER, width=120)
    my_tree.column("Pokemon_Name", anchor=W, width=120)
    my_tree.column("Status", anchor=W, width=120)
    
    my_tree.heading("#0", text = "List", anchor=W)
    my_tree.heading("Pokedex_Number", text = "Pokedex_Number", anchor=W)
    my_tree.heading("Pokemon_Name", text = "Pokemon_Name", anchor=W)
    my_tree.heading("Status", text = "Status", anchor=W)
   


    try:
        sql = """SELECT pokedex_number, name, status
                FROM pokemon
                WHERE status = ?"""
        args = [status]
        cur = conn.cursor()
        cur.execute(sql, args)
        
        print("-------------------------------")
        rows = cur.fetchall()
        for row in rows: 
            my_tree.insert("", 'end', text="",
               values =(row[0],row[1],row[2]))
    except Error as e:
        conn.rollback()
        print(e)
    print("--------------------------------------------")

#15/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def pokemonTypingResistances(conn, my_tree, e):
    print("--------------------------------------------")
    typeNum = e[0]
    type1 = e[1]

    if (typeNum == "2"):
        type2 = e[2]

    my_tree['columns'] = ("Pokedex_Number", "Pokemon_Name", "Type_1", "Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psyhic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy")
    my_tree.column("#0", width=10)
    my_tree.column("Pokedex_Number", anchor=CENTER, width=120)
    my_tree.column("Pokemon_Name", anchor=W, width=120)
    my_tree.column("Type_1", anchor=W, width=10)
    my_tree.column("Normal", anchor=W, width=10)
    my_tree.column("Fire", anchor=W, width=10)
    my_tree.column("Water", anchor=W, width=10)
    my_tree.column("Electric", anchor=W, width=10)
    my_tree.column("Grass", anchor=W, width=10)
    my_tree.column("Ice", anchor=W, width=10)
    my_tree.column("Fighting", anchor=W, width=10)
    my_tree.column("Poison", anchor=W, width=10)
    my_tree.column("Ground", anchor=W, width=10)
    my_tree.column("Flying", anchor=W, width=10)
    my_tree.column("Psyhic", anchor=W, width=10)
    my_tree.column("Bug", anchor=W, width=10)
    my_tree.column("Rock", anchor=W, width=10)
    my_tree.column("Ghost", anchor=W, width=10)
    my_tree.column("Dragon", anchor=W, width=10)
    my_tree.column("Dark", anchor=W, width=10)
    my_tree.column("Steel", anchor=W, width=10)
    my_tree.column("Fairy", anchor=W, width=10)
    
    my_tree.heading("#0", text = "List", anchor=W)
    my_tree.heading("Pokedex_Number", text = "Pokedex_Number", anchor=W)
    my_tree.heading("Pokemon_Name", text = "Pokemon_Name", anchor=W)
    my_tree.heading("Type_1", text = "Type_1", anchor=W)
    my_tree.heading("Normal", text = "Normal", anchor=W)
    my_tree.heading("Fire", text = "Fire", anchor=W)
    my_tree.heading("Water", text = "Water", anchor=W)
    my_tree.heading("Electric", text = "Electric", anchor=W)
    my_tree.heading("Grass", text = "Grass", anchor=W)
    my_tree.heading("Ice", text = "Ice", anchor=W)
    my_tree.heading("Fighting", text = "Fighting", anchor=W)
    my_tree.heading("Poison", text = "Poison", anchor=W)
    my_tree.heading("Ground", text = "Ground", anchor=W)
    my_tree.heading("Flying", text = "Flying", anchor=W)
    my_tree.heading("Psyhic", text = "Psyhic", anchor=W)
    my_tree.heading("Bug", text = "Bug", anchor=W)
    my_tree.heading("Rock", text = "Rock", anchor=W)
    my_tree.heading("Ghost", text = "Ghost", anchor=W)
    my_tree.heading("Dragon", text = "Dragon", anchor=W)
    my_tree.heading("Dark", text = "Dark", anchor=W)
    my_tree.heading("Steel", text = "Steel", anchor=W)
    my_tree.heading("Fairy", text = "Fairy", anchor=W)

    try:
        if (typeNum == "1"):
            sql = """SELECT pokedex_number, name, type_1, normal, fire, water, electric, grass, ice, fighting, poison, ground, flying, psychic, bug, rock, ghost, dragon, dark, steel, fairy
                    FROM pokemon, typing
                    WHERE type_1 = ?
                        AND type_2 = "" 
                        AND type_1 = defense_type1
                        AND type_2 = defense_type2 """
            args = [type1]
            cur = conn.cursor()
            cur.execute(sql, args)
           
            print("-------------------------------")

            rows = cur.fetchall()
            for row in rows: 
                my_tree.insert("", 'end', text="",
                    values =(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20]))
        if (typeNum == "2"):


            my_tree['columns'] = ("Pokedex_Number", "Pokemon_Name", "Type_1", "Type_2", "Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psyhic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy")
            my_tree.column("#0", width=10)
            my_tree.column("Pokedex_Number", anchor=CENTER, width=120)
            my_tree.column("Pokemon_Name", anchor=W, width=120)
            my_tree.column("Type_1", anchor=W, width=10)
            my_tree.column("Type_2", anchor=W, width=10)
            my_tree.column("Normal", anchor=W, width=10)
            my_tree.column("Fire", anchor=W, width=10)
            my_tree.column("Water", anchor=W, width=10)
            my_tree.column("Electric", anchor=W, width=10)
            my_tree.column("Grass", anchor=W, width=10)
            my_tree.column("Ice", anchor=W, width=10)
            my_tree.column("Fighting", anchor=W, width=10)
            my_tree.column("Poison", anchor=W, width=10)
            my_tree.column("Ground", anchor=W, width=10)
            my_tree.column("Flying", anchor=W, width=10)
            my_tree.column("Psyhic", anchor=W, width=10)
            my_tree.column("Bug", anchor=W, width=10)
            my_tree.column("Rock", anchor=W, width=10)
            my_tree.column("Ghost", anchor=W, width=10)
            my_tree.column("Dragon", anchor=W, width=10)
            my_tree.column("Dark", anchor=W, width=10)
            my_tree.column("Steel", anchor=W, width=10)
            my_tree.column("Fairy", anchor=W, width=10)
            
            my_tree.heading("#0", text = "List", anchor=W)
            my_tree.heading("Pokedex_Number", text = "Pokedex_Number", anchor=W)
            my_tree.heading("Pokemon_Name", text = "Pokemon_Name", anchor=W)
            my_tree.heading("Type_1", text = "Type_1", anchor=W)
            my_tree.heading("Type_2", text = "Type_2", anchor=W)
            my_tree.heading("Normal", text = "Normal", anchor=W)
            my_tree.heading("Fire", text = "Fire", anchor=W)
            my_tree.heading("Water", text = "Water", anchor=W)
            my_tree.heading("Electric", text = "Electric", anchor=W)
            my_tree.heading("Grass", text = "Grass", anchor=W)
            my_tree.heading("Ice", text = "Ice", anchor=W)
            my_tree.heading("Fighting", text = "Fighting", anchor=W)
            my_tree.heading("Poison", text = "Poison", anchor=W)
            my_tree.heading("Ground", text = "Ground", anchor=W)
            my_tree.heading("Flying", text = "Flying", anchor=W)
            my_tree.heading("Psyhic", text = "Psyhic", anchor=W)
            my_tree.heading("Bug", text = "Bug", anchor=W)
            my_tree.heading("Rock", text = "Rock", anchor=W)
            my_tree.heading("Ghost", text = "Ghost", anchor=W)
            my_tree.heading("Dragon", text = "Dragon", anchor=W)
            my_tree.heading("Dark", text = "Dark", anchor=W)
            my_tree.heading("Steel", text = "Steel", anchor=W)
            my_tree.heading("Fairy", text = "Fairy", anchor=W)


            sql = """SELECT pokedex_number, name, type_1, type_2, normal, fire, water, electric, grass, ice, fighting, poison, ground, flying, psychic, bug, rock, ghost, dragon, dark, steel, fairy
                    FROM pokemon, typing
                    WHERE type_1 = ?
                        AND type_2 = ? 
                        AND type_1 = defense_type1
                        AND type_2 = defense_type2 """
            args = [type1, type2]
            cur = conn.cursor()
            cur.execute(sql, args)
           
            print("-------------------------------")

            rows = cur.fetchall()
            for row in rows: 
                my_tree.insert("", 'end', text="",
                    values =(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21]))

    except Error as e:
        conn.rollback()
        print(e)

#16/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def generationTypingsCount(conn, my_tree, genNum):
    print("--------------------------------------------")
    genNum = e[0]
    typeNum = e[1]
    type1 = e[2]
    if (typeNum == "2"):
        type2 = e[3]

    my_tree['columns'] = ("Generation", "Type_Count", "Defense_Type1")
    my_tree.column("#0", width=10)
    my_tree.column("Generation", anchor=CENTER, width=120)
    my_tree.column("Type_Count", anchor=W, width=120)
    my_tree.column("Defense_Type1", anchor=W, width=120)

    my_tree.heading("#0", text = "List", anchor=W)
    my_tree.heading("Generation", text = "Generation", anchor=W)
    my_tree.heading("Type_Count", text = "Type_Count", anchor=W)
    my_tree.heading("Defense_Type1", text = "Defense_Type1", anchor=W)

    try:
        if (typeNum == "1"):
            sql = """SELECT gen.generation, count(pokemon.pokedex_number), defense_type1
                    FROM pokemon, typing, gen
                    WHERE pokemon.type_1 = ?
                        AND pokemon.type_2 = "" 
                        AND pokemon.type_1 = typing.defense_type1
                        AND pokemon.type_2 = typing.defense_type2
                        AND gen.generation = ?
                        AND gen.generation = pokemon.generation """
            args = [type1, genNum]
            cur = conn.cursor()
            cur.execute(sql, args)
            
            print("-------------------------------")
            rows = cur.fetchall()
            for row in rows: 
                my_tree.insert("", 'end', text="",
                    values =(row[0],row[1],row[2]))


        if (typeNum == "2"):

            my_tree['columns'] = ("Generation", "Type_Count", "Defense_Type1", "Defense_Type2")
            my_tree.column("#0", width=10)
            my_tree.column("Generation", anchor=CENTER, width=120)
            my_tree.column("Type_Count", anchor=W, width=120)
            my_tree.column("Defense_Type1", anchor=W, width=120)
            my_tree.column("Defense_Type2", anchor=W, width=120)

            my_tree.heading("#0", text = "List", anchor=W)
            my_tree.heading("Generation", text = "Generation", anchor=W)
            my_tree.heading("Type_Count", text = "Type_Count", anchor=W)
            my_tree.heading("Defense_Type1", text = "Defense_Type1", anchor=W)
            my_tree.heading("Defense_Type2", text = "Defense_Type2", anchor=W)


            sql = """SELECT gen.generation, count(pokemon.pokedex_number), typing.defense_type1, typing.defense_type2
                    FROM pokemon, typing, gen
                    WHERE pokemon.type_1 = ?
                        AND pokemon.type_2 = ? 
                        AND pokemon.type_1 = typing.defense_type1
                        AND pokemon.type_2 = typing.defense_type2
                        AND gen.generation = ?
                        AND gen.generation = pokemon.generation """
            args = [type1, type2, genNum]
            cur = conn.cursor()
            cur.execute(sql, args)

            print("-------------------------------")
            rows = cur.fetchall()
            for row in rows: 
                my_tree.insert("", 'end', text="",
                    values =(row[0],row[1],row[2],row[3]))

    except Error as e:
        conn.rollback()
        print(e)

#17/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def updateMoveset(conn, root, e):
    print("++++++++++++++++++++++++++++++++++")
    print("Updating a Pokemon's moveset")
    forme = input("Which Pokemon's moveset do you want to update: ")
    moveNum = int(input("Which move number do you want to update do you want to update: "))
    moveName = input("What's the name of the move: ")
    try:
        if (moveNum == 1):
            sql = """UPDATE moveset
                    SET move1 = ?
                    WHERE forme = ? """
        elif (moveNum == 2):
            sql = """UPDATE moveset
                    SET move2 = ?
                    WHERE forme = ? """
        elif (moveNum == 3):
            sql = """UPDATE moveset
                    SET move3 = ?
                    WHERE forme = ? """
        elif (moveNum == 4):
            sql = """UPDATE moveset
                    SET move4 = ?
                    WHERE forme = ? """
        elif (moveNum == 5):
            sql = """UPDATE moveset
                    SET move5 = ?
                    WHERE forme = ? """
        elif (moveNum == 6):
            sql = """UPDATE moveset
                    SET move6 = ?
                    WHERE forme = ? """
        elif (moveNum == 7):
            sql = """UPDATE moveset
                    SET move7 = ?
                    WHERE forme = ? """
        elif (moveNum == 8):
            sql = """UPDATE moveset
                    SET move8 = ?
                    WHERE forme = ? """
        elif (moveNum == 9):
            sql = """UPDATE moveset
                    SET move9 = ?
                    WHERE forme = ? """
        args = [moveName, forme]
        conn.execute(sql, args)
        conn.commit()
        print("successfully updated the moveset for " + forme + " in the moveset table")
    except Error as e:
        conn.rollback()
        print(e)
    print("--------------------------------------------") 

#18/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def searchPokemonAbilities(conn, my_tree, e):
    print("++++++++++++++++++++++++++++++++++")
    abName = e

    my_tree['columns'] = ("Pokemon_Number", "Pokemon_Name", "Ability_1", "Ability_2", "Ability_Hidden")
    my_tree.column("#0", width=10)
    my_tree.column("Pokemon_Number", anchor=CENTER, width=120)
    my_tree.column("Pokemon_Name", anchor=W, width=120)
    my_tree.column("Ability_1", anchor=W, width=120)
    my_tree.column("Ability_2", anchor=W, width=120)
    my_tree.column("Ability_Hidden", anchor=W, width=120)

    my_tree.heading("#0", text = "List", anchor=W)
    my_tree.heading("Pokemon_Number", text = "Pokemon_Number", anchor=W)
    my_tree.heading("Pokemon_Name", text = "Pokemon_Name", anchor=W)
    my_tree.heading("Ability_1", text = "Ability_1", anchor=W)
    my_tree.heading("Ability_2", text = "Ability_2", anchor=W)
    my_tree.heading("Ability_Hidden", text = "Ability_Hidden", anchor=W)


    try:
        sql = """SELECT pokedex_number, name, ability_1, ability_2, ability_hidden
                    FROM pokemon
                    WHERE ability_1 = ?
                        OR ability_2 = ?
                        OR ability_hidden = ?"""
        args = [abName, abName, abName]
        cur = conn.cursor()
        cur.execute(sql, args)
        
        print("-------------------------------")
        rows = cur.fetchall()
        for row in rows: 
            my_tree.insert("", 'end', text="",
                values =(row[0],row[1],row[2],row[3],row[5]))
    except Error as e:
        conn.rollback()
        print(e)
    print("--------------------------------------------")

#19/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def searchPokemonMoveInMoveset(conn, my_tree, e):
    print("++++++++++++++++++++++++++++++++++")
    abName = e

    my_tree['columns'] = ("Pokemon_Number", "Pokemon_Name", "move1", "move2", "move3", "move4", "move5", "move6", "move7", "move8", "move9",)
    my_tree.column("#0", width=1)
    my_tree.column("Pokemon_Number", anchor=CENTER, width=120)
    my_tree.column("Pokemon_Name", anchor=W, width=120)
    my_tree.column("move1", anchor=W, width=60)
    my_tree.column("move2", anchor=W, width=60)
    my_tree.column("move3", anchor=W, width=60)
    my_tree.column("move4", anchor=W, width=60)
    my_tree.column("move5", anchor=W, width=60)
    my_tree.column("move6", anchor=W, width=60)
    my_tree.column("move7", anchor=W, width=60)
    my_tree.column("move8", anchor=W, width=60)
    my_tree.column("move9", anchor=W, width=60)
   

    my_tree.heading("#0", text = "List", anchor=W)
    my_tree.heading("Pokemon_Number", text = "Pokemon_Number", anchor=W)
    my_tree.heading("Pokemon_Name", text = "Pokemon_Name", anchor=W)
    my_tree.heading("move1", text = "move1", anchor=W)
    my_tree.heading("move2", text = "move2", anchor=W)
    my_tree.heading("move3", text = "move3", anchor=W)
    my_tree.heading("move4", text = "move4", anchor=W)
    my_tree.heading("move5", text = "move5", anchor=W)
    my_tree.heading("move6", text = "move6", anchor=W)
    my_tree.heading("move7", text = "move7", anchor=W)
    my_tree.heading("move8", text = "move8", anchor=W)
    my_tree.heading("move9", text = "move9", anchor=W)
    

    try:
        sql = """SELECT pokemon.pokedex_number, pokemon.name, move1, move2, move3, move4, move5, move6, move7, move8, move9
                FROM moveset, pokemon
                WHERE ? in (move1, move2, move3, move4, move5, move6, move7, move8, move9)
                    AND moveset.ndex = pokemon.pokedex_number
            """
        args = [abName]
        cur = conn.cursor()
        cur.execute(sql, args)
        
        print("-------------------------------")
        rows = cur.fetchall()
        for row in rows: 
            my_tree.insert("", 'end', text="",
                values =(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
    except Error as e:
        conn.rollback()
        print(e)
    print("--------------------------------------------")

#20/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

def speedSearch(conn, my_tree, genNum):
    print("--------------------------------------------")
    #status = input("")
    try:
        sql = """SELECT pokemon.index_number, name
                FROM pokemon, gen, baseStats 
                WHERE
                    pokemon.generation = gen.generation AND
                    region_name = 'Alola'
                GROUP BY name
                HAVING
                    speed < 50
                """
        #args = [status]
        cur = conn.cursor()
        cur.execute(sql)
        l = '{:<15} {:<25}'.format("ID_Number","Pokemon_Name")
        print(l)
        print("-------------------------------")
        rows = cur.fetchall()
        for row in rows:
            l = '{:<15} {:<25}'.format(row[0], row[1])
            print(l)
    except Error as e:
        conn.rollback()
        print(e)
    print("--------------------------------------------")

