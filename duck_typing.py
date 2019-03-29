class Pycharm:
    def execute(self):
        print("Compile")
        print("Run")

class Notepad:
    def execute(self):
        print("save")
        print("Compile")
        print("Run")

class Laptop:
    def code(self,ide):
        ide.execute()

ide = Pycharm()
ide2 = Notepad()
lap = Laptop()
lap.code(ide2)