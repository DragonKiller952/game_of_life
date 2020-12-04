from unittest import TestCase
from Simulator import *
from copy import deepcopy


class TestSimulator(TestCase):
    """
    Tests for ``Simulator`` implementation.
    """
    def setUp(self):
        self.sim = Simulator()

    def test_update(self):
        """
        Tests that the update functions returns an object of World type.
        """
        self.assertIsInstance(self.sim.update(), World)

        sampleworld = World(self.sim.world.width, self.sim.world.height)

        def setting(rawplain, set):
            plain = deepcopy(rawplain)
            preset = set
            for i in preset:
                plain.set(i[0], i[1])
            return plain

        def tester(rules, rulestest):
            self.sim.set_world(rules)
            compareArray = self.sim.update().world == rulestest.world
            self.assertTrue(compareArray.all())

        rules1 = setting(sampleworld, [(5, 1), (11, 1), (5, 2), (11, 2), (5, 3), (6, 3), (10, 3), (11, 3), (1, 5),
                                       (2, 5), (3, 5), (6, 5), (7, 5), (9, 5), (10, 5), (13, 5), (14, 5), (15, 5),
                                       (3, 6), (5, 6), (7, 6), (9, 6), (11, 6), (13, 6), (5, 7), (6, 7), (10, 7),
                                       (11, 7), (5, 9), (6, 9), (10, 9), (11, 9), (3, 10), (5, 10), (7, 10), (9, 10),
                                       (11, 10), (13, 10), (1, 11), (2, 11), (3, 11), (6, 11), (7, 11), (9, 11),
                                       (10, 11), (13, 11), (14, 11), (15, 11), (5, 13), (6, 13), (10, 13), (11, 13),
                                       (5, 14), (11, 14), (5, 15), (11, 15)])
        rulestest1 = setting(sampleworld, [(4, 2), (5, 2), (11, 2), (12, 2), (5, 3), (6, 3), (10, 3), (11, 3), (2, 4),
                                           (5, 4), (7, 4), (9, 4), (11, 4), (14, 4), (2, 5), (3, 5), (4, 5), (6, 5),
                                           (7, 5),
                                           (9, 5), (10, 5), (12, 5), (13, 5), (14, 5), (3, 6), (5, 6), (7, 6), (9, 6),
                                           (11, 6), (13, 6), (4, 7), (5, 7), (6, 7), (10, 7), (11, 7), (12, 7), (4, 9),
                                           (5, 9), (6, 9), (10, 9), (11, 9), (12, 9), (3, 10), (5, 10), (7, 10),
                                           (9, 10),
                                           (11, 10), (13, 10), (2, 11), (3, 11), (4, 11), (6, 11), (7, 11), (9, 11),
                                           (10, 11), (12, 11), (13, 11), (14, 11), (2, 12), (5, 12), (7, 12), (9, 12),
                                           (11, 12), (14, 12), (5, 13), (6, 13), (10, 13), (11, 13), (4, 14), (5, 14),
                                           (11, 14), (12, 14)])

        tester(rules1, rulestest1)

        rules2 = setting(sampleworld, [(4, 2), (5, 2), (11, 2), (12, 2), (5, 3), (6, 3), (10, 3), (11, 3), (2, 4),
                                       (5, 4), (7, 4), (9, 4), (11, 4), (14, 4), (2, 5), (3, 5), (4, 5), (6, 5), (7, 5),
                                       (9, 5), (10, 5), (12, 5), (13, 5), (14, 5), (3, 6), (5, 6), (7, 6), (9, 6),
                                       (11, 6), (13, 6), (4, 7), (5, 7), (6, 7), (10, 7), (11, 7), (12, 7), (4, 9),
                                       (5, 9), (6, 9), (10, 9), (11, 9), (12, 9), (3, 10), (5, 10), (7, 10), (9, 10),
                                       (11, 10), (13, 10), (2, 11), (3, 11), (4, 11), (6, 11), (7, 11), (9, 11),
                                       (10, 11), (12, 11), (13, 11), (14, 11), (2, 12), (5, 12), (7, 12), (9, 12),
                                       (11, 12), (14, 12), (5, 13), (6, 13), (10, 13), (11, 13), (4, 14), (5, 14),
                                       (11, 14), (12, 14)])
        rulestest2 = setting(sampleworld, [(4, 2), (5, 2), (6, 2), (10, 2), (11, 2), (12, 2), (2, 4), (7, 4), (9, 4),
                                           (14, 4), (2, 5), (7, 5), (9, 5), (14, 5), (2, 6), (7, 6), (9, 6), (14, 6),
                                           (4, 7), (5, 7), (6, 7), (10, 7), (11, 7), (12, 7), (4, 9), (5, 9), (6, 9),
                                           (10, 9), (11, 9), (12, 9), (2, 10), (7, 10), (9, 10), (14, 10), (2, 11),
                                           (7, 11), (9, 11), (14, 11), (2, 12), (7, 12), (9, 12), (14, 12), (4, 14),
                                           (5, 14), (6, 14), (10, 14), (11, 14), (12, 14)])
        tester(rules2, rulestest2)

        ages = setting(sampleworld, [(9, 9), (10, 9), (9, 10), (10, 10)])
        agestest = deepcopy(sampleworld)

        self.sim.set_world(ages)
        self.sim.update()
        self.sim.update()
        self.sim.update()
        self.sim.update()
        self.sim.update()
        compareArray = self.sim.get_world().world == agestest.world
        self.assertTrue(compareArray.all())



    def test_get_generation(self):
        """
        Tests whether get_generation returns the correct value:
            - Generation should be 0 when Simulator just created;
            - Generation should be 2 after 2 updates.
        """
        self.assertIs(self.sim.generation, self.sim.get_generation())
        self.assertEqual(self.sim.get_generation(), 0)
        self.sim.update()
        self.sim.update()
        self.assertEqual(self.sim.get_generation(), 2)

    def test_get_world(self):
        """
        Tests whether the object passed when get_world() is called is of World type, and has the required dimensions.
        When no argument passed to construction of Simulator, world is square shaped with size 20.
        """
        self.assertIs(self.sim.world, self.sim.get_world())
        self.assertEqual(self.sim.get_world().width, 20)
        self.assertEqual(self.sim.get_world().height, 20)

    def test_set_world(self):
        """
        Tests functionality of set_world function.
        """
        world = World(10)
        self.sim.set_world(world)
        self.assertIsInstance(self.sim.get_world(), World)
        self.assertIs(self.sim.get_world(), world)
