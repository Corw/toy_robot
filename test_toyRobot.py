from unittest import TestCase
from toy_robot import ToyRobot
from toy_robot import Direction


class TestToyRobot(TestCase):
	def test__is_placed(self):
		toyRobot = ToyRobot()
		self.assertFalse(toyRobot._is_placed)

		toyRobot.place(0, 0, Direction.NORTH)
		self.assertTrue(toyRobot._is_placed)

	def test__is_position_valid(self):
		toyRobot = ToyRobot()
		self.assertTrue(toyRobot._is_position_valid(0, 0))
		self.assertTrue(toyRobot._is_position_valid(4, 4))
		self.assertFalse(toyRobot._is_position_valid(5, 0))
		self.assertFalse(toyRobot._is_position_valid(0, 5))
		self.assertFalse(toyRobot._is_position_valid(-1, 0))
		self.assertFalse(toyRobot._is_position_valid(0, -1))
		self.assertFalse(toyRobot._is_position_valid(None, 0))
		self.assertFalse(toyRobot._is_position_valid(0, None))

		toyRobot = ToyRobot(10, 10)
		self.assertTrue(toyRobot._is_position_valid(0, 0))
		self.assertTrue(toyRobot._is_position_valid(9, 9))
		self.assertFalse(toyRobot._is_position_valid(10, 0))
		self.assertFalse(toyRobot._is_position_valid(0, 10))


	def test__get_orientation(self):
		toyRobot = ToyRobot()
		self.assertEqual(toyRobot._get_orientation(None), None)
		self.assertEqual(toyRobot._get_orientation(Direction.NORTH), (Direction.WEST, Direction.EAST))

	def test_place(self):
		toyRobot = ToyRobot()
		toyRobot.place(0, 0, Direction.NORTH)
		self.assertEqual(toyRobot.report(), "0, 0, NORTH")

		toyRobot.place(1, 1, Direction.WEST)
		self.assertEqual(toyRobot.report(), "1, 1, WEST")

		toyRobot.place(0, 1, Direction.EAST)
		self.assertEqual(toyRobot.report(), "0, 1, EAST")

		toyRobot.place(1, 2, Direction.SOUTH)
		self.assertEqual(toyRobot.report(), "1, 2, SOUTH")

		toyRobot.place(-1, 2, Direction.SOUTH)
		self.assertNotEqual(toyRobot.report(), "-1, 2, SOUTH")

	def test_move(self):
		toyRobot = ToyRobot()

		toyRobot.place(0, 0, Direction.NORTH)

		toyRobot.move()
		self.assertEqual(toyRobot.report(), "1, 0, NORTH")

		toyRobot.move()
		self.assertEqual(toyRobot.report(), "2, 0, NORTH")

		toyRobot.move()
		self.assertEqual(toyRobot.report(), "3, 0, NORTH")

		toyRobot.move()
		self.assertEqual(toyRobot.report(), "4, 0, NORTH")

		toyRobot.move()
		self.assertEqual(toyRobot.report(), "4, 0, NORTH")  # validate not going over the edge

		toyRobot.place(0, 0, Direction.EAST)

		toyRobot.move()
		self.assertEqual(toyRobot.report(), "0, 1, EAST")

		toyRobot.move()
		self.assertEqual(toyRobot.report(), "0, 2, EAST")

		toyRobot.move()
		self.assertEqual(toyRobot.report(), "0, 3, EAST")

		toyRobot.move()
		self.assertEqual(toyRobot.report(), "0, 4, EAST")

		toyRobot.move()
		self.assertEqual(toyRobot.report(), "0, 4, EAST")  # validate not going over the edge

		toyRobot.place(0, 0, Direction.WEST)

		toyRobot.move()
		self.assertEqual(toyRobot.report(), "0, 0, WEST")  # validate not going over the edge

		toyRobot.place(0, 0, Direction.SOUTH)

		toyRobot.move()
		self.assertEqual(toyRobot.report(), "0, 0, SOUTH")  # validate not going over the edge



	def test_left(self):
		toyRobot = ToyRobot()

		toyRobot.left() # Left must not work before place
		self.assertEqual(toyRobot.report(), None)

		toyRobot.place(0, 0, Direction.NORTH)

		toyRobot.left()
		self.assertEqual(toyRobot.report(), "0, 0, WEST")

		toyRobot.left()
		self.assertEqual(toyRobot.report(), "0, 0, SOUTH")

		toyRobot.left()
		self.assertEqual(toyRobot.report(), "0, 0, EAST")

		toyRobot.left()
		self.assertEqual(toyRobot.report(), "0, 0, NORTH")


	def test_right(self):
		toyRobot = ToyRobot()

		toyRobot.right() # right must not work before place
		self.assertEqual(toyRobot.report(), None)

		toyRobot.place(0, 0, Direction.NORTH)

		toyRobot.right()
		self.assertEqual(toyRobot.report(), "0, 0, EAST")

		toyRobot.right()
		self.assertEqual(toyRobot.report(), "0, 0, SOUTH")

		toyRobot.right()
		self.assertEqual(toyRobot.report(), "0, 0, WEST")

		toyRobot.right()
		self.assertEqual(toyRobot.report(), "0, 0, NORTH")

	def test_report(self):
		toyRobot = ToyRobot()

		self.assertEqual(toyRobot.report(), None)

		toyRobot.place(0, 0, Direction.NORTH)
		self.assertEqual(toyRobot.report(), "0, 0, NORTH")

		toyRobot.place(1, 1, Direction.WEST)
		self.assertEqual(toyRobot.report(), "1, 1, WEST")

		toyRobot.place(0, 1, Direction.EAST)
		self.assertEqual(toyRobot.report(), "0, 1, EAST")

		toyRobot.place(1, 2, Direction.SOUTH)
		self.assertEqual(toyRobot.report(), "1, 2, SOUTH")
