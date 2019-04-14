class MenuUI:
    
    def __init__(self):
        self.allowed = ["gen", "web", "ps", "sc", "exit", "rawhex", "winrawhex"]
        
    def is_an_option(self, input):
        if input in self.allowed:
            return True
        return False
