from factory_function import *
import unittest


class Tests(unittest.TestCase):
    def test_dough(self):
        self.assertEqual(make_dough('water', 'flour'), 'dough')
        self.assertEqual(make_dough('flour', 'water'), 'dough')
        self.assertEqual(make_dough('flour', 'redbull'), 'not dough')

    def test_bread(self):
        self.assertEqual(bake_bread('dough'), 'bread')
        self.assertEqual(bake_bread('not dough'), 'not bread')

    def test_whole_dough(self):
        self.assertEqual(wholewheat_dough('water', 'wholewheat flour'), 'wholewheat dough')
        self.assertEqual(wholewheat_dough('wholewheat flour', 'water'), 'wholewheat dough')
        self.assertEqual(wholewheat_dough('flour', 'redbull'), 'not wholewheat dough')

    def test_whole_bread(self):
        self.assertEqual(wholewheat_bread('wholewheat dough'), 'wholewheat bread')
        self.assertEqual(wholewheat_bread('not wholewheat dough'), 'not wholewheat bread')


if __name__ == '__main__':
    unittest.main()