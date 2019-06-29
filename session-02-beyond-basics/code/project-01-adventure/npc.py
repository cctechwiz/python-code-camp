class npc:
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.lines = []
        self._line_gen = self._lines()

    def _lines(self):
        while True:
            for line in self.lines:
                yield line
    
    def add_line(self, line):
        self.lines.append(line)

    def talk(self):
        print(next(self._line_gen))
