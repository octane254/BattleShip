# characters (as strings):
wizard = "Wizard"
elf = "Elf"
human = "Human"
kalisi = "Kalisi"
# character HP (as integers):
wizard_hp = 150
elf_hp = 100
human_hp = 150
kalisi_hp = 900
# character Damage (as integers):
wizard_damage = 150
elf_damage = 100
human_damage = 20
kalisi_damage = 5
# Dragon Stats
dragon_hp = 300
dragon_damage = 50


while True:
    print("1) wizard")
    print("2) elf")
    print("3) human")
    print("4) Kalisi")
    print("5) exit")


    character_choice = input("Choose your character: ").lower()
    if character_choice == "wizard":
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character_choice == "elf":
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character_choice == "human":
        my_hp = human_hp
        my_damage = human_damage
        break
    elif character_choice == "kalisi":
        my_hp = kalisi_hp
        my_damage = kalisi_damage
        break
    elif character_choice == "exit":
        exit()
    else:
        print("Not a Valid character")