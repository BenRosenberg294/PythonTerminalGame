class Plot:
    # This class represents a plot of land.
    # It can have one building on it.
    # It has methods to determin which other plots of land are nearby.
    def __init__(self, row, col, village):
        self.row = row
        self.col = col
        self.village = village
        self.plot_obj = Grass(self)

    def get_adjacent(self, radius = 1):
                
        return self.village.get_adjacent(self.row, self.col, radius)
    
class PlotObj:
    # This class represents objects that can exist in the village.
    # This is a base class and is not to be initiated.
    pass

class Grass(PlotObj):
    # This class represents a tile of grass.
    # This is the default PlotObj class every plot is initiated with. 
    def __init__(self, plot):
        self.name = 'grass'
        self.plot = plot
        self.gird_rep = "\33[48;5;2m \33[0m"
    
    def __repr__(self):
        return "grass"

class Village:
    # This class represents the whole village.
    # It contains a grid of land plots in a double indexed list.
    # It has info about which buildings exist in the village.
    ROWS = 5
    COLUMNS = 5

    def __init__(self):
        self.grid = [[Plot(row, col, self) for row in range(self.ROWS)] for col in range(self.COLUMNS)]

    def __repr__(self):
        village_repr = "  |"
        for col in range(self.COLUMNS):
            village_repr += " {} |".format(col + 1)

        village_repr += "\n"
        village_repr += "--+"
        village_repr += "---+" * self.COLUMNS
        
        for row in range(self.ROWS):
            village_repr += "\n"
            village_repr += "{} |".format(row + 1)

            for col in range(self.COLUMNS):
                village_repr += " {} |".format(self.grid[row][col].plot_obj.gird_rep)

            village_repr += "\n"    
            village_repr += "--+"
            village_repr += "---+" * self.COLUMNS
        
        return village_repr

    def get_adjacent(self, origin_row, origin_col, radius = 1):
        result = []
        for row in range(origin_row - radius, origin_row + radius + 1):
            for col in range(origin_col - radius, origin_col + radius + 1):
                if row in range(self.ROWS) and col in range(self.COLUMNS) and (row != origin_row or col != origin_col):
                    result.append(self.grid[row][col].plot_obj.name)
        
        return result
