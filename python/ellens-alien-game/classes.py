"""Solution to Ellen's Alien Game exercise."""
import abc


class IAlien(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def collision_detection(self, other):
        raise NotImplementedError()


class Alien(IAlien):
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
"""

    total_aliens_created = 0

    def __init__(self, x, y) -> None:
        self.x_coordinate = x
        self.y_coordinate = y
        self.health = 3
        Alien.total_aliens_created = Alien.total_aliens_created + 1

    def hit(self):
        self.health = self.health - 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y

    def collision_detection(self, other):
        pass


def new_aliens_collection(alien_position_list):
    alien_list = []
    for position in alien_position_list:
        x, y = position
        alien_list.append(Alien(x, y))
    return alien_list
