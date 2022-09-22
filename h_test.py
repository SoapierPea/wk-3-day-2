from unittest import TestCase, main
from homework_zeros import nozlist


class nozlistTestCase(TestCase):    
    def test_1_base(self):
        self.assertEqual(nozlist[0,3,0,4,2],[3,4,2])
    def test_2_zeroes_front(self):
        self.assertEqual(nozlist[0,0,4,6], [4,6])
    def test_3_no_zeros(self):
        self.assertEqual(nozlist[2,6,9], [2,6,9])
    


if __name__ =='__main__':
    main()