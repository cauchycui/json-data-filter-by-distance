#!/usr/bin/python
'''
Hengguan Cui    test functionality
python 2.7.9

'''

import unittest
from string import whitespace
import inviteCustomer

class myTest(unittest.TestCase):
	def test(self):
		inviteCustomer.sort_out_invites('customers.txt')
		with open('result.txt') as rf:	
			first = rf.readline().translate(None, whitespace)
			self.assertEqual(first, 'IanKehoe4')

			
if __name__ == '__main__':
    unittest.main()		