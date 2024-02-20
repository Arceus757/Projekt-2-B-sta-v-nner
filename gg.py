from colors import bcolors

__author__  = "Dmytro Malanchuk"
__version__ = "1.0.0"
__email__   = "dmytro.malanchuk@elev.ga.ntig.se"




# Min vänlista
Friends_list = ["Dmytro"]

def Show_list(name_lista):
    print("======================")
    print(bcolors.CYAN + "Vänner i listan:")
    for name in name_lista:
        print(bcolors.GREEN + name)

# Lägga till en vän i listan
def add_name(name_lista):
    new_name = input("Ange vännen du vill lägga till: ")
    name_lista.append(new_name)
    print(f"{new_name} har lagts till i listan.")

# Ta bort ett namn från listan
def remove_name(name_lista):
    print("Välj vilken vän du vill ta bort genom att ange dess nummer:")
    for i, name in enumerate(name_lista):
        print(f"{i+1}. {name}")
    
    try:
        choice = int(input("Ange numret här: "))
        if 1 <= choice <= len(name_lista):
            removed_name = name_lista.pop(choice - 1)
            print(f"{removed_name} har tagits bort från listan.")
        else:
            print("Ogiltigt val. Var snäll och ange ett nummer inom intervallet.")
    except ValueError:
        print("Ogiltigt val. Var snäll och ange ett heltal.")



while True:
    print("******************")
    print("\nVälj en åtgärd:")
    print("1. Visa listan")
    print("2. Lägg till en vän")
    print("3. Ta bort en vän")
    print("4. Avsluta programet")
    print(bcolors.DEFAULT + "\n*******************")
    
    choice = input(bcolors.CYAN + "Vad vill du göra: ")
    
    if choice == "1":
        Show_list(Friends_list)
    elif choice == "2":
        add_name(Friends_list)
    elif choice == "3":
        remove_name(Friends_list)
    elif choice == "4":
        break
    else:
        print(bcolors.RED + "Du får bara välja mella 1 och 4, var snäll och försök igen men utan dumheter den här gången.")
