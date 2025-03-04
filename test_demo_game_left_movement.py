from unittest import TestCase, main
from demo_game import demo_game
from pygame.locals import K_LEFT


class TestDemoGameLeftMovement(TestCase):

    def test_left_key(self):
        expected = "x: 353, y: 691"
        result = demo_game.run(K_LEFT)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
