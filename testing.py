import os
import unittest


def analyze_text(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        x = [1 for n in f if n.find('\n') != -1]


        return sum(x)


class TextAnalysisTests(unittest.TestCase):

    def setUp(self):
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, mode='wt', encoding='utf-8') as f:
            f.write('sdf asdf asdf asdf asdf \n asdf asdf asdf asdf asdf asdf \n sdfgsdfg sdfg sdfg sdfg sdfg \n fin')

    def tearDown(self):
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        self.assertEqual(analyze_text(self.filename), 3)

    def test_bad_file(self):
        with self.assertRaises(IOError):
            analyze_text('foofoo')


if __name__ == '__main__':

    unittest.main()
