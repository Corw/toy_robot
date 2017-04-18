import enum


class Direction(enum.Enum):
	NORTH = 1
	SOUTH = 2
	EAST = 3
	WEST = 4


class ToyRobot:
	_position_x = None
	_position_y = None
	_direction = None

	_dimension_x = None
	_dimension_y = None

	def __init__(self, dimension_x=5, dimension_y=5):
		self._dimension_x = dimension_x
		self._dimension_y = dimension_y

	@property
	def _is_placed(self):
		if self._position_x is None:
			return False

		if self._position_y is None:
			return False

		if self._direction is None:
			return False

		return True

	def place(x, y, f):
		pass

	def move(self):
		if self._is_placed is False:
			return

		pass

	def left(self):
		if self._is_placed is False:
			return

		pass

	def right(self):
		if self._is_placed is False:
			return

		pass

	def report(self):
		if self._is_placed is False:
			return

		pass
