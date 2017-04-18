import enum


class Direction(enum.Enum):
	NORTH = "NORTH"
	SOUTH = "SOUTH"
	EAST = "EAST"
	WEST = "WEST"


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
		if x is None or y is None:
			return False

		if x < 0 or x >= self._dimension_x:
			return False

		if y < 0 or y >= self._dimension_y:
			return False

		return True

	@staticmethod
	def _get_orientation(f):
		if f not in Direction:
			return None
		# (direction, left, right)
		orientation = \
			[
				(Direction.NORTH, Direction.WEST, Direction.EAST),
				(Direction.SOUTH, Direction.EAST, Direction.WEST),
				(Direction.EAST, Direction.NORTH, Direction.SOUTH),
				(Direction.WEST, Direction.SOUTH, Direction.NORTH),
			]

		for (direction, left, right) in orientation:
			if direction is f:
				return (left, right)

	@staticmethod
	def _get_translation(f):
		if f not in Direction:
			return None
		# (direction, move_x, move_y)
		translation = \
			[
				(Direction.NORTH, 1, 0),
				(Direction.SOUTH, -1, 0),
				(Direction.EAST, 0, 1),
				(Direction.WEST, 0, -1),
			]

		for (direction, move_x, move_y) in translation:
			if direction is f:
				return (move_x, move_y)

	def place(self, x, y, f):
		if f not in Direction:
			return

		if self._is_position_valid(x, y) is False:
			return

		self._position_x = x
		self._position_y = y
		self._direction = f

	def move(self):
		if self._is_placed is False:
			return

		(move_x, move_y) = self._get_translation(self._direction)

		new_x = self._position_x + move_x
		new_y = self._position_y + move_y

		if self._is_position_valid(new_x, new_y):
			self._position_x += move_x
			self._position_y += move_y


	def left(self):
		if self._is_placed is False:
			return

		(left, right) = self._get_orientation(self._direction)
		self._direction = left

		pass

	def right(self):
		if self._is_placed is False:
			return

		(left, right) = self._get_orientation(self._direction)
		self._direction = right

	def report(self):
		if self._is_placed is False:
			return

		return "{x}, {y}, {direction}".format(x=self._position_x, y=self._position_y, direction=self._direction.value)
