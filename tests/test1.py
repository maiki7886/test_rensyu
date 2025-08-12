import unittest

from test_rensyu.CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):

    #テストケース1
    def test_read(self):
        printer = CSVPrinter('sample.csv')
        #printer = CSVPrinter('sample2.csv')
        line = printer.read()
        print(line)
        self.assertEqual( 3, len(line))
        #self.assertEqual(2, len(line))

    #テストケース2
    def test_row(self):
        printer = CSVPrinter('sample.csv')
        line = printer.read()
        #print(line)
        self.assertEqual(4, len(line[0]))

    #テストケース3
    def test_file(self):
        with self.assertRaises(FileNotFoundError):
            printer = CSVPrinter('sample3.csv')
            line = printer.read()
            print(line)
        #print("error")

