from World import *

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world = None):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0
        if world == None:
            self.world = World(20)
            self.gen_world = World(20)
        else:
            self.world = world
            self.gen_world = world

    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution. Also sets world
        Implements age limit for cells.

        :return: New state of the world.
        """
        self.generation += 1

        agelimit = 5
        birth = [3]
        survive = [2, 3]

        new = World(self.world.width, self.world.height)
        current = self.world

        for i in range(current.height):
            for j in range(current.width):
                cell = current.get(j, i)
                agecell = self.gen_world.get(j, i)
                neighbors = current.get_neighbours(j, i)
                if agecell > agelimit-1:
                    self.gen_world.set(j, i, 0)
                elif cell == 1:
                    if neighbors.count(1) in survive:
                        if agecell == 0:
                            self.gen_world.set(j, i, agecell + 2)
                        else:
                            self.gen_world.set(j, i, agecell + 1)
                        new.set(j, i)
                    else:
                        self.gen_world.set(j, i, 0)
                elif cell == 0:
                    if neighbors.count(1) in birth:
                        new.set(j, i)
                        self.gen_world.set(j, i, agecell+1)


        self.set_world(new)

        return new

    def get_generation(self):
        """
        Returns the value of the current generation of the simulated Game of Life.

        :return: generation of simulated Game of Life.
        """
        return self.generation

    def get_world(self):
        """
        Returns the current version of the ``World``.

        :return: current state of the world.
        """
        return self.world

    def set_world(self, world: World) -> None:
        """
        Changes the current world to the given value.

        :param world: new version of the world.

        """
        self.world = world