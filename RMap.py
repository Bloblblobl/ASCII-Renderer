from RLine import RLine


class RMap(object):

    def __init__(self, lines=[], name='rmap', bounds=dict(x=10, y=10), emptychar='╳'):
        self.lines = lines
        self.bounds = bounds
        self.emptychar = emptychar
        self.name = name

    def __str__(self):
        return f'[RMap] Name:{self.name} Bounds:({self.bounds["x"]},{self.bounds["y"]}) Empty Char:{self.emptychar}'

    def generate_map_frame(self, bounds=None):
        if bounds:
            self.bounds = bounds
        for y in range(self.bounds['y']):
            self.lines.append(RLine('', self.bounds['x']))
            for x in range(self.bounds['x']):
                self.lines[y].contents += self.emptychar

    def generate_border(self, borderchar, override=False):
        for y in range(self.bounds['y']):
            if y == 0 or y == self.bounds['y'] - 1:
                brange = [i for i in range(self.bounds['x'])]
            else:
                brange = [0, self.bounds['x'] - 1]
            for x in brange:
                if override or self.lines[y].contents[x] == self.emptychar:
                    new_line = self.lines[y].contents[:x] + borderchar + self.lines[y].contents[x+1:]
                    self.lines[y].contents = new_line

    def _merge_conflict(self, char1, char2):
        return char1 != self.emptychar and char2 != self.emptychar

    def merge_maps(self, merge_map, x=0, y=0, override='ignore'):
        assert(self.bounds['x'] > merge_map.bounds['x'] + x and self.bounds['y'] > merge_map.bounds['y'] + y)

    def render_map(self):
        for line in self.lines:
            print(line.contents.replace(self.emptychar, ' '))

    def generate_map_from_file(self, filepath):
        f = open(filepath)
        self.lines = []
        for line in f:
            self.lines.append(RLine(line, self.bounds['x']))
