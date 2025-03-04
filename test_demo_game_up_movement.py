from unittest import TestCase, main
from demo_game import demo_game
from pygame.locals import K_UP


class TestDemoGameUpMovement(TestCase):

    def test_up_key(self):
        expected = "x: 358, y: 686"
        result = demo_game.run(K_UP)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
