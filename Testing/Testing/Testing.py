import unittest

class Alignment:
    US = 1
    THEM = 2
    CHAOTIC = 3

class Ship:
    def __init__(self,name, x,y, max_health, range, attack_power, alignment):
        self._name = name
        self._x_location = x
        self._y_location = y
        self.max_health = max_health
        self.range = range
        self.attack_power = attack_power
        self.alignment = alignment
        self.current_health = max_health

    def assess_damage(self, damage):
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0
        elif self.current_health > self.max_health:
            self.current_health = self.max_health

    def get_x_location(self):
        return self._x_location

    def get_y_location(self):
        return self._y_location

class Battleship(Ship):
    pass

class TestShip(unittest.TestCase):

    def setUp(self):
        self.test_ship = Ship("USS Enterprise", 0, 1, 100, 50, 10, Alignment.US)

    def test_ship_init(self):
        self.assertEqual( self.test_ship._name, "USS Enterprise")
        self.assertEqual( self.test_ship._x_location, 0 )
        self.assertEqual( self.test_ship._y_location, 1 )
        self.assertEqual( self.test_ship.max_health, 100)
        self.assertEqual( self.test_ship.range, 50)
        self.assertEqual( self.test_ship.attack_power, 10)
        self.assertEqual( self.test_ship.alignment, Alignment.US )
        self.assertEqual( self.test_ship.current_health, 100 )

    def test_ship_assess_damage_health_doesnt_go_below_zero(self):
        self.test_ship.assess_damage(10000)
        self.assertEqual( self.test_ship.current_health, 0 )

    def test_ship_assess_damage_health_doesnt_go_above_max(self):
        self.test_ship.assess_damage(-10000)
        self.assertEqual( self.test_ship.current_health, 100 )

    def test_ship_assess_damage_health_changes(self):
        self.test_ship.assess_damage(50)
        self.assertEqual( self.test_ship.current_health, 50 )

    def test_ship_get_x_location(self):
        self.assertEqual( self.test_ship.get_x_location(), 0 )

    def test_ship_get_y_location(self):
        self.assertEqual( self.test_ship.get_y_location(), 1 )
        
class TestBattleship(unittest.TestCase):

    def test_battleship_init(self):
        test_battleship = Battleship("USS Death Star", 1, 2, 1000, 500, 10000, Alignment.THEM)
        self.assertEqual(test_battleship._name, "USS Death Star")

    def test_battleship_inherits_from_ship(self):
        test_battleship = Battleship("USS Death Star", 1, 2, 1000, 500, 10000, Alignment.THEM)
        self.assertIsInstance(test_battleship, Ship)
        self.assertIsInstance(test_battleship, Battleship)
