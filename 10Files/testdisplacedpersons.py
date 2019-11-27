#-------------------------------------------------------------------------------
#  Author:       Alwin Tareen
#  Created:      Dec 06, 2018
#  Last updated: Dec 06, 2018
#
#  Execution:    python testdisplacedpersons.py
#
#  This is the PyUnit test bench for displacedpersons.py
#
#-------------------------------------------------------------------------------

from displacedpersons import *
import unittest

class TestDisplacedPersons(unittest.TestCase):
    def testone(self):
        expected = 175
        actual = destinations()
        self.assertEqual(expected, actual)

    def testtwo(self):
        expected = ['Afghanistan', 'Eritrea', 'Iran (Islamic Rep. of)', 'Iraq', 'Myanmar', 'Nepal', 'Pakistan', 'Palestinian', 'Qatar', 'Somalia', 'Sri Lanka', 'Stateless', 'Sudan', 'Syrian Arab Rep.', 'Tunisia', 'Various/Unknown']
        actual = origins("Qatar")
        self.assertEqual(expected, actual)

    def testthree(self):
        expected = 843490
        actual = largestinflux("United States of America")
        self.assertEqual(expected, actual)
    
    def testfour(self):
        expected = ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bangladesh', 'Belarus', 'Cameroon', 'Cuba', 'Dem. Rep. of the Congo', 'Georgia', 'Ghana', 'Iran (Islamic Rep. of)', 'Iraq', 'Kenya', 'Kyrgyzstan', 'Latvia', 'Lithuania', 'Nigeria', 'Pakistan', 'Palestinian', 'Russian Federation', 'Sierra Leone', 'Somalia', 'Sri Lanka', 'Stateless', 'Sudan', 'Syrian Arab Rep.', 'Tajikistan', 'Turkey', 'Uzbekistan', 'Various/Unknown']
        actual = origins("Latvia")
        self.assertEqual(expected, actual)
    
    def testfive(self):
        expected = 980000
        actual = largestinflux("Germany")
        self.assertEqual(expected, actual)
    
    def testsix(self):
        expected = ['Angola', 'Burundi', 'Dem. Rep. of the Congo', 'Eritrea', 'Ethiopia', 'Kenya', 'Rwanda', 'Sierra Leone', 'Somalia', 'Sudan', 'Uganda', 'Various/Unknown', 'Zambia', 'Zimbabwe']
        actual = origins("Malawi")
        self.assertEqual(expected, actual)
    
    def testseven(self):
        expected = 50432
        actual = largestinflux("Norway")
        self.assertEqual(expected, actual)
    
    def testeight(self):
        expected = ['Afghanistan', 'Bangladesh', 'Bhutan', 'Cameroon', 'China', 'Egypt', 'Ethiopia', 'Iran (Islamic Rep. of)', 'Iraq', 'Liberia', 'Myanmar', 'Nepal', 'Niger', 'Nigeria', 'Pakistan', 'Sierra Leone', 'Somalia', 'Sri Lanka', 'Sudan', 'Tibetan', 'Various/Unknown']
        actual = origins("Nepal")
        self.assertEqual(expected, actual)
    
    def testnine(self):
        expected = 157220
        actual = largestinflux("Sweden")
        self.assertEqual(expected, actual)
    
if __name__ == '__main__':
    unittest.main()
