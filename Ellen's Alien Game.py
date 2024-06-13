class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    total_aliens_created: int
        Total number of aliens created (class attribute).
    x_coordinate: int
        Position on the x-axis.
    y_coordinate: int
        Position on the y-axis.
    health: int
        Number of health points.

    Methods
    -------
    hit():
        Decrement Alien health by one point.
    is_alive():
        Return a boolean indicating if Alien is alive (if health > 0).
    teleport(new_x_coordinate, new_y_coordinate):
        Move Alien object to new coordinates.
    collision_detection(other):
        Implementation TBD.
    """

    total_aliens_created = 0  # Class attribute to keep track of total aliens created

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        """Decrement Alien health by one point."""
        self.health -= 1

    def is_alive(self):
        """Return a boolean indicating if Alien is alive (if health > 0)."""
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        """Move Alien object to new coordinates."""
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other):
        """Placeholder for collision detection logic."""
        pass


def new_aliens_collection(coordinates):
    """Create a list of Alien objects from a list of coordinates.

    Parameters
    ----------
    coordinates: list of tuple
        A list of (x, y) tuples representing coordinates.

    Returns
    -------
    list of Alien
        A list of Alien objects created from the given coordinates.
    """
    return [Alien(x, y) for x, y in coordinates]

# Example usage:
aliens = new_aliens_collection([(0, 0), (1, 2), (3, 5)])
for alien in aliens:
    print(f'Alien at ({alien.x_coordinate}, {alien.y_coordinate}) with health {alien.health}')
