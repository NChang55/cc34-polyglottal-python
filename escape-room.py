class Game:
    def __init__(self):
        self.inventory = []
        self.rooms = {
            "B1_is_lit": False,
            "ladder_is_positioned": False,
            "door_is_unlocked": False,
            "B1_C": {
                "description": "You are of course in a dark basement. You can't see anything. You are feeling slightly uneasy.",
                "items": [],
                "north": "ladder_position_B1_N",
                "south": "desk_position_B1_S",
                "east": "light_switch_position_B1_E",
                "west": "B1_W",
            },
            "ladder_position_B1_N": {
                "description": "You kicked something on the floor, but you cannot see what it is. Now your toe hurts.",
                "items": [],
                "south": "B1_C",
                "up": None,
                "east": "B1_NE",
                "west": "floor_board_position_B1_NW",
                "north": None
            },
            "desk_position_B1_S": {
                "description": "You ran into something, but you cannot see what it is.",
                "items": [],
                "north": "B1_C",
                "east": "B1_SE",
                "west": "B1_SW",
                "south": None
            },
            "floor_board_position_B1_NW": {
                "description": "You stepped on something, but you cannot see what it is.",
                "items": [],
                "east": "ladder_position_B1_N",
                "north": None,
                "south": "B1_W",
                "west": None
            },
            "B1_NE": {
                "description": "You cannot see anything.",
                "items": [],
                "east": "9_3/4",
                "north": None,
                "south": "light_switch_position_B1_E",
                "west": "ladder_position_B1_N"
            },
            "light_switch_position_B1_E": {
                "description": "You felt a switch on the wall.",
                "items": [],
                "east": None,
                "west": "B1_C",
                "south": "B1_SE",
                "north": "B1_NE"
            },
            "B1_SE": {
                "description": "You cannot see anything.",
                "items": [],
                "east": None,
                "west": "desk_position_B1_S",
                "south": None,
                "north": "light_switch_position_B1_E"
            },
            "B1_SW": {
                "description": "You cannot see anything.",
                "items": [],
                "east": "desk_position_B1_S",
                "west": None,
                "south": None,
                "north": "B1_W"
            },
            "B1_W": {
                "description": "You cannot see anything.",
                "items": [],
                "east": "B1_C",
                "west": None,
                "south": "B1_SW",
                "north": "floor_board_position_B1_NW"
            },
            "9_3/4": {
                "description": "Platform 9 3/4 actually had a bug and connects here as well. No train is coming though, school is in session. Please go back. And do not tell anyone about this.",
                "items": [],
                "west": "B1_NE",
                "north": None,
                "south": None,
                "east": None
            },
            "L1_C": {
                "description": "You are now on the first floor, with a ladder leading down.",
                "items": [],
                "north": "door_L1_N",
                "down": "ladder_position_B1_N",
                "west": "L1_W",
                "east": "L1_E",
                "south": "mirror_L1_S"
            },
            "mirror_L1_S": {
                "description": "You saw a mirror on the wall.",
                "items": [],
                "north": "L1_C",
                "south": None,
                "west": "carpet_L1_SW",
                "east": "L1_SE",
            },
            "computer_room_L1_WWC": {
                "description": "You are now in a small study.",
                "items": [],
                "east": "L1_W",
                "north": "computer_L1_WWN",
                "south": "safe_L1_WWS",
                "west": None,
            },
            "safe_L1_WWS": {
                "description": "You see a safe.",
                "items": ["dime"],
                "east": None,
                "west": None,
                "south": None,
                "north": "computer_room_L1_WWC"
            },
            "computer_L1_WWN": {
                "description": "You see a computer.",
                "items": [],
                "east": None,
                "west": None,
                "south": "computer_room_L1_WWC",
                "north": None
            },
            "L1_W": {
                "description": "You see a room to the west.",
                "items": [],
                "east": "L1_C",
                "west": "computer_room_L1_WWC",
                "south": "carpet_L1_SW",
                "north": "scribble_L1_NW"
            },
            "scribble_L1_NW": {
                "description": "There are some tiny scribbles at the corner of the wall.",
                "items": [],
                "east": "door_L1_N",
                "west": None,
                "south": "L1_W",
                "north": None
            },
            "carpet_L1_SW": {
                "description": "You see a carpet on the floor.",
                "items": ["penny"],
                "east": "mirror_L1_S",
                "west": None,
                "south": None,
                "north":"L1_W"
            },
            "door_L1_N": {
                "description": "The door is locked. Please provide the password.",
                "items": [],
                "east": "bathroom_L1_NE",
                "west": "scribble_L1_NW",
                "south": "L1_C",
                "north": None
            },
            "bathroom_L1_NE": {
                "description": "You found yourself in the bathroom. You see a toilet and a vent.",
                "items": ["nickle"],
                "east": None,
                "west": "door_L1_N",
                "south": "L1_E",
                "north": None
            },
            "L1_E": {
                "description": "You see a room to the east.",
                "items": [],
                "east": "bedroom_L1_EEC",
                "west": "L1_C",
                "south": "L1_SE",
                "north": "bathroom_L1_NE"
            },
            "L1_SE": {
                "description": "There is nothing here.",
                "items": [],
                "east": None,
                "west": "mirror_L1_S",
                "south": None,
                "north": "L1_E"
            },
            "bedroom_L1_EEC": {
                "description": "You find yourself in a bedroom.",
                "items": [],
                "east": None,
                "west": "L1_E",
                "south": "bed_L1_EES",
                "north": "closet_L1_EEN"
            },
            "closet_L1_EEN": {
                "description": "You see a closet against the wall. Feel free to take something if you are cold.",
                "items": ["coat"],
                "east": None,
                "west": None,
                "south": "bedroom_L1_EEC",
                "north": None
            },
            "bed_L1_EES": {
                "description": "You see a bed with a pillow.",
                "items": ["floppy_disk"],
                "east": None,
                "west": None,
                "south": None,
                "north": "bedroom_L1_EEC"
            }
        }
        self.current_room = "B1_C"
    
    def play(self):
        print("Welcome! You got tossed into total darkness for fun.\n")
        print("Type 'help' to see a list of commands.\n")
        print("Important tip: please connect any item with two or more words with understore. i.e. enter 'coffee_beans' for 'coffee beans'\n")
        while True:
            self.describe_room()
            command = input("> ").strip().lower()
            if command == "quit":
                print("Thanks for playing :)")
                break
            elif command == "help":
                self.show_help()
            elif command == "inventory":
                self.show_inventory()
            elif command.startswith("go "):
                self.move(command.split(" ")[1])
            elif command.startswith("take "):
                self.take_item(command.split(" ")[1])
            elif command.startswith("use "):
                self.use_item(command.split(" ")[1])
            elif command.startswith("flip switch"):
                self.flip_switch()
            elif command.startswith("open drawer"):
                self.open_drawer()
            elif command.startswith("open closet"):
                self.open_closet()
            elif command.startswith("remove floor_board"):
                self.remove_board()
            elif command.startswith("position ladder"):
                self.position_ladder()
            elif command.startswith("wear "):
                self.wear_coat()
            elif command.startswith("remove pillow"):
                self.remove_pillow()
            elif command.startswith("remove carpet"):
                self.remove_carpet()
            elif command.startswith("insert "):
                self.insert_floppy_disk()
            elif command.startswith("talk"):
                self.talk_to_mirror()
            elif command.startswith("0909"):
                self.unlock_door()
            else:
                print("I don't understand that command.")
    
    def describe_room(self):
        room = self.rooms[self.current_room]
        print(room['description'])
    
    def move(self, direction):
        room = self.rooms[self.current_room]
        if direction in room and room[direction] is not None:
            self.current_room = room[direction]
        elif room == "door_L1_N" and self.rooms["door_is_unlocked"] == False:
            print("Door is locked.")
        else:
            print("You can't go that way.")
    
    def take_item(self, item):
        room = self.rooms[self.current_room]
        if item in room["items"]:
            room["items"].remove(item)
            self.inventory.append(item)
            print(f"You picked up the {item}.")
        elif item == "magnifying_glass" and self.current_room == "desk_position_B1_S" and self.rooms["B1_is_lit"]:
            self.inventory.append(item)
            print(f"You picked up the {item}.")
        else:
            print("There is no such item here.")
    
    def use_item(self, item):
        if item not in self.inventory:
            print("You don't have that item.")
            return
        
        if item == "key" and self.current_room == "safe_L1_WWS":
            print("You use the key to unlock safe. You see a dime.")
        elif item == "screw_driver" and self.current_room == "bathroom_L1_NE":
            print("You use the screw driver to remove the screws from the vent. You see a nickle.")
        elif item == "magnifying_glass" and self.current_room == "scribble_L1_NW":
            print("You used the magnifying glass to exam the scribbles on the wall. '16 cents'")
        else:
            print("You can't use that here.")
    
    def flip_switch(self):
        if self.current_room == "light_switch_position_B1_E":
            if self.rooms['B1_is_lit'] == False:
                print("Let there be light!")
                self.rooms['B1_is_lit'] = True
                self.rooms["B1_C"]["description"] = (
                    "You are in a lit basement. Move around to check things out."
                )
                self.rooms["ladder_position_B1_N"]["items"] = ["ladder"]
                self.rooms["ladder_position_B1_N"]["description"] = (
                    "You found a ladder lying on the floor."
                )
                self.rooms["floor_board_position_B1_NW"]["description"] = (
                    "You found a loose floor board."
                )
                self.rooms["desk_position_B1_S"]["items"] = ["screw_driver"]
                self.rooms["desk_position_B1_S"]["description"] = (
                    "You found a desk with a screw driver on top, and it has a drawer."
                )
                self.rooms["B1_NE"]["description"] = (
                    "There is nothing here."
                )
                self.rooms["B1_SE"]["description"] = (
                    "There is nothing here."
                )
                self.rooms["B1_W"]["description"] = (
                    "There is nothing here."
                )
                self.rooms["B1_SW"]["description"] = (
                    "There is nothing here."
                )
                self.rooms["light_switch_position_B1_E"]["description"] = (
                    "You see a light switch on the wall."
                )
                print("You flip the switch and the basement lights up.")
            else:
                print("The light is already on. This is a magical/defective light which you cannot switch it off again lol.")
        else:
            print("There's no switch here.")
    
    def open_drawer(self):
        if self.current_room == "desk_position_B1_S" and self.rooms["B1_is_lit"]:
            if "magnifying_glass" not in self.inventory:
                print("You open the drawer and find a magnifying glass.")
            else:
                print("You already took the magnifying glass from the drawer.")
        else:
            print("There's no drawer here.")
    
    def open_closet(self):
        if self.current_room == "closet_L1_EEN":
            if "coat" not in self.inventory:
                print("You open the closet and find a coat.")
            else:
                print("You already took the coat from the closet.")
        else:
            print("There's no closet here.")
            
    def wear_coat(self):
        if "coat" in self.inventory:
            print("You put on the coat and feel warmer now. The coat is now part of you.")
        else:
            print("You haven't found the coat yet!")
    
    def remove_board(self):
        if self.current_room == "floor_board_position_B1_NW" and self.rooms["B1_is_lit"]:
            if "key" not in self.inventory:
                self.rooms["floor_board_position_B1_NW"]["items"] = ["key"]
                print("You remove the floor board and find a key.")
            else:
                print("You already took the key from under the floor board.")
        else:
            print("There is no floor board here.")
    
    def remove_pillow(self):
        if self.current_room == "bed_L1_EES":
            if "floppy_disk" not in self.inventory:
                print("You remove the pillow and find a floppy disk.")
            else: 
                print("You already took the floppy disk from under the pillow.")
        else:
            print("There is no pillow here.")
            
    def remove_carpet(self):
        if self.current_room == "carpet_L1_SW":
            if "penny" not in self.inventory:
                print("You removed the carpet and find a penny.")
            else:
                print("You already took the penny from under the carpet.")
        else:
            print("There is no carpet here.")
            
    def insert_floppy_disk(self):
        if self.current_room == "computer_L1_WWN":
            print("The screen showed '0909'.")
        else:
            print("You cannot do that here.")
            
    def position_ladder(self):
        if self.current_room == "ladder_position_B1_N" and self.rooms["B1_is_lit"] and self.rooms["ladder_is_positioned"] == False:
            self.rooms["ladder_is_positioned"] = True
            self.rooms["ladder_position_B1_N"]["up"] = ("L1_C")
            print("The ladder is in position. You may climb up now.")
            self.rooms["ladder_position_B1_N"]["description"] = (
                    "You see a ladder leading up."
                )
            
    def talk_to_mirror(self):
        if self.current_room == "mirror_L1_S":
            print("'Thou, O Queen, art the fairest of them all!'")
    
    def unlock_door(self):
        if self.current_room == "door_L1_N":
            self.rooms["door_is_unlocked"] = True
            if all(item in self.inventory for item in ["penny", "dime", "nickle"]):
                print("Congratulations! You have completed the secret mission and collected all the coins: penny, dime, and nickle.")
                print("Here is your secret password: '1436'; go find Ning!")
            print("You have successfully unlocked the door and found your way out! Thank you so much fo playing!")
            exit()
    
    def show_help(self):
        print("\nAvailable commands:")
        print("  go [direction] - Move in a direction (north, south, east, west, up, down)")
        print("  take [item] - Pick up an item")
        print("  use [item] - Use an item from your inventory")
        print("  position [] - Position something")
        print("  flip [] - Flip something")
        print("  open [] - Open something")
        print("  remove [] - Remove something")
        print("  wear [] - Wear something")
        print("  insert [] - Insert something")
        print("  inventory - Show your inventory")
        print("  help - Show this help message")
        print("  quit - Quit the game\n")
    
    def show_inventory(self):
        if self.inventory:
            print("You are carrying: " + ", ".join(self.inventory))
        else:
            print("You are not carrying anything.")
    
if __name__ == "__main__":
    game = Game()
    game.play()