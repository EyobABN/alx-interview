import unittest


islandPerimeter = __import__('0-island_perimeter').island_perimeter


class TestIslandPerimeter(unittest.TestCase):
    def test_islandPerimeter(self):
        # Test case 1: 4x4 island with a perimeter of 16
        island = [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
        ]
        self.assertEqual(islandPerimeter(island), 16)

        # Test case 2: 1x2 island with a perimeter of 4
        island = [
            [1, 0]
        ]
        self.assertEqual(islandPerimeter(island), 4)

        # Test case 3: 2x2 island with a perimeter of 0 (i.e., no land)
        island = [
            [0, 0],
            [0, 0]
        ]
        self.assertEqual(islandPerimeter(island), 0)

        # Additional test case 1: Empty input with a perimeter of 0
        island = []
        self.assertEqual(islandPerimeter(island), 0)

        # Additional test case 2: Input with all land (1s) with perimeter equal to 2 * (number of rows + number of columns)
        island = [
            [1, 1],
            [1, 1]
        ]
        self.assertEqual(islandPerimeter(island), 8)

        # Additional test case 3: Input with all water (0s) with perimeter of 0
        island = [
            [0, 0],
            [0, 0]
        ]
        self.assertEqual(islandPerimeter(island), 0)

        # Additional test case 4: Irregularly shaped input with a perimeter of 12
        island = [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]
        ]
        self.assertEqual(islandPerimeter(island), 12)

        # Additional test case 5: Large input (50x50) with a perimeter of 200
        island = [[1] * 50 for _ in range(50)]
        self.assertEqual(islandPerimeter(island), 200)


if __name__ == '__main__':
    unittest.main()
