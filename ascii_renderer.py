def expand_rmap(rmap, newlen):
    len(rmap)
    for i in range(newlen):
        rmap.append('')
    return rmap


def get_attr_extremes_in_range(obj_list, a):
    min_attr = max_attr = 0

    for o in obj_list:
        obj_attr = getattr(o, a)
        min_attr = obj_attr if obj_attr < min_attr else min_attr
        max_attr = obj_attr if obj_attr > max_attr else max_attr

    return min_attr, max_attr


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Bounds(object):

    def __init__(self, points=[], fillchar='█'):
        self.points = points
        self.fillchar = fillchar

    def get_outer_bounds(self):
        minx, maxx = get_attr_extremes_in_range(self.points, 'x')
        miny, maxy = get_attr_extremes_in_range(self.points, 'y')
        minp = Point(minx, miny)
        maxp = Point(maxx, maxy)
        return minp, maxp

    def get_points_at_height(self, height):
        points = []
        for p in self.points:
            if p.y == height:
                points.append(p)
        return points

    def get_map(self):
        minp, maxp = self.get_outer_bounds()
        mheight = maxp.y - minp.y
        mwidth = maxp.x - minp.x
        rmap = []
        rmap = expand_rmap(rmap, mheight)
        for i in range(mheight):
            points = self.get_points_at_height(i)
            if not points:
                rmap[i] = rmap[i - 1]
            elif len(points) == 1:
                # prev_points = []
                # while not prev_points:
                #     pass
                rmap[i] = rmap[i - 1]
            else:
                minx, maxx = get_attr_extremes_in_range(points, 'x')
                for j in range(mwidth):
                    if j < minx or j > maxx:
                        rmap[i].append(' ')
                    else:
                        rmap[i].append(self.fillchar)

        return rmap


class RenderMap(object):

    def __init__(self):
        pass


class Component(object):

    def __init__(self):
        self.bounds = Bounds()
        self.rmap = self.bounds.get_map()


class Preset(object):
    pass


class ASCIIRenderer(object):

    def __init__(self, components=[], rmap=[]):
        self.components = components
        self.rmap = rmap

    def add_component_to_rmap(self, component, x=0, y=0):
        pass


    def print_map(self):
        for line in self.rmap:
            print(line)

