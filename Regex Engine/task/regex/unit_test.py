import unittest
import regex

stage_2 = (('apple|apple', True), ('.pple|apple', True), ('appl.|apple', True), ('.....|apple', True),
           ('peach|apple', False))

stage_3 = (('apple|apple', True), ('ap|apple', True), ('le|apple', True), ('a|apple', True), ('.|apple', True),
           ('apwle|apple', False), ('peach|apple', False))

stage_4 = (('^app|apple', True), ('le$|apple', True), ('^a|apple', True), ('.$|apple', True),
           ('apple$|taste apple', True), ('^apple|apple pie', True), ('^apple$|apple', True),
           ('^apple$|taste apple', False), ('^apple$|apple pie', False), ('^app$|apple', False), ('^le|apple', False))

stage_5 = (('colou?r|color', True), ('colou?r|colour', True), ('colou?r|colouur', False), ('colou*r|color', True),
           ('colou*r|colour', True), ('colou*r|colouur', True), ('col.*r|color', True), ('col.*r|colour', True),
           ('col.*r|colr', True), ('col.*r|collar', True), ('col.*r$|colors', False))

stage_6 = ((r'\.$|end.', True), (r'3\+3|3+3=6', True), (r'\?|Is this working?', True), (r'\\|\'', True),
           (r'colou\?r|color',  False), (r'colou\?r|colour',  False))


class TestRegex(unittest.TestCase):

    def test_match_2(self):
        for args in stage_2:
            self.assertEqual(regex.match_rec(*args[0].split('|')), args[1])

    def test_match_3(self):
        for args in stage_3:
            self.assertEqual(regex.match_ite(*args[0].split('|')), args[1])

    def test_match_4(self):
        for args in stage_4:
            self.assertEqual(regex.match_bounds(*args[0].split('|')), args[1])

    def test_match_5(self):
        for args in stage_5:
            self.assertEqual(regex.match_bounds(*args[0].split('|')), args[1])

    def test_match_6(self):
        for args in stage_6:
            self.assertEqual(regex.match_bounds(*args[0].split('|')), args[1])


if __name__ == "__main__":
    unit_test.main()
