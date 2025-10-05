class Engine:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_direction(self, direction):
        direction = direction.lower()
        if direction == "north":
            self.y += 1
        elif direction == "south":
            self.y -= 1
        elif direction == "east":
            self.x += 1
        elif direction == "west":
            self.x -= 1
        else:
            print(f"Unknown direction: {direction}")
        self.report_position()

    def move_to_coordinate(self, target_x, target_y):
        print(f"Moving to ({target_x}, {target_y})...")
        self.x = target_x
        self.y = target_y
        self.report_position()

    def report_position(self):
        print(f"Engine is now at position ({self.x}, {self.y})")


engine = Engine()

while True:
    command = input("Enter command (move_direction/move_to/exit): ").strip().lower()
    if command == "exit":
        print("Exiting the engine control.")
        break
    elif command == "move_direction":
        direction = input("Enter direction (north/south/east/west): ").strip().lower()
        engine.move_direction(direction)
    elif command == "move_to":
        try:
            x = int(input("Enter target x coordinate: "))
            y = int(input("Enter target y coordinate: "))
            engine.move_to_coordinate(x, y)
        except ValueError:
            print("Invalid coordinates. Please enter integer values.")
    else:
        print("Unknown command. Please try again.")

