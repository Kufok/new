import random
import sys
brawlers =
Spike = {
    "Name" : "Spike",
    "Hp": 4000,
    "Min. Dmg" : 1120,
    "Max Dmg" : 2500,
    "Min. Crit. chance" : 30,
    "Max Crit. chance" : 40,
}
Leon = {
    "Name" : "Leon",
    "Hp" : 6000,
    "Min. Dmg" : 960,
    "Max Dmg" : 3840,
    "Min. Crit. chance" : 15,
    "Max Crit. chance" : 20,
}
Crow = {
    "Name" : "Crow",
    "Hp": 4300,
    "Min. Dmg" : 640,
    "Max Dmg" : 1920,
    "Min. Crit. chance" : 50,
    "Max Crit. chance" : 60,
}
Dynamike = {
    "Name" : "Dynamike",
    "Hp" : 5000,
    "Min. Dmg" : 1600,
    "Max Dmg" : 3200,
    "Min. Crit. chance" : 20,
    "Max Crit. chance" : 30,
}
print(Spike)
print(Leon)
print(Crow)
print(Dynamike)
print("Vyber si postavicku")
print("A = Spike")
print("B = Leon")
print("C = Crow")
print("D = Dynamike")
user_brawl = input()
if user_brawl == "A":
    chosen_brawl = Spike
elif user_brawl == "B":
    chosen_brawl = Leon
elif user_brawl == "C":
    chosen_brawl = Crow
elif user_brawl == "D":
    chosen_brawl = Dynamike
else:
    sys.exit()
pocitac_brawler = random.randint[]
print("Pocitac si vybral")
print("vybral si", chosen_brawl["Name"])
def make_dmg(min, max):
    dmg = random.randint(min,max)
    return dmg
print("privni uder za:")
print(make_dmg(chosen_brawl["Min. Dmg"], chosen_brawl["Max Dmg"]))
