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

	def _is_position_valid(self, x, y):
		if x < 0 or x >= self._dimension_x:
			return False

		if y < 0 or y >= self._dimension_y:
			return False

		return True

	def place(self, x, y, f):
		if f is not type(Direction):
			return

		if self._is_position_valid(x, y) is False:
			return

		self._position_x = x
		self._position_y = y
		self._direction = f

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
