from unittest import TestCase, main
from demo_game import demo_game
from pygame.locals import K_RIGHT


class TestDemoGameRightMovement(TestCase):

    def test_right_key(self):
        expected = "x: 363, y: 691"
        result = demo_game.run(K_RIGHT)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
