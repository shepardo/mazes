from colored_grid import ColoredGrid
from sidewinder import Sidewinder
from hunt_and_kill import HuntAndKill

height, width = [50, 50]

grid = ColoredGrid(height,width)
HuntAndKill.mutate(grid)

start = grid.grid[int(height/2)][int(width/2)]

grid.distances = start.distances()

grid.maximum = grid.distances.max()[1]

grid.to_svg()
