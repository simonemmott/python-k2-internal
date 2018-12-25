'''
Created on 25 Dec 2018

@author: simon
'''
import unittest, shutil, os
from k2 import K2Config
from k2_domain import DomainConfig
from k2_internal import write_server_home


class TestK2Internal(unittest.TestCase):


    def test_write_home(self):
        config = K2Config(title='Test K2 Title')
        example_domain = DomainConfig('example domain')
        config.add_domain_config(example_domain)
        
        shutil.rmtree('homes/test_home_1')
        
        write_server_home('homes/test_home_1', config)
        
        self.assertTrue(os.path.exists('homes/test_home_1'))
        self.assertTrue(os.path.exists('homes/test_home_1/bin'))
        self.assertTrue(os.path.exists('homes/test_home_1/bin/domains'))
        self.assertTrue(os.path.exists('homes/test_home_1/bin/domains/example_domain'))
        self.assertTrue(os.path.exists('homes/test_home_1/bin/widgets'))
        self.assertTrue(os.path.exists('homes/test_home_1/conf'))
        self.assertTrue(os.path.exists('homes/test_home_1/conf/k2.conf'))        
        self.assertTrue(os.path.exists('homes/test_home_1/data'))
        
        c2 = K2Config(file='homes/test_home_1/conf/k2.conf')
        
        self.assertEqual('Test K2 Title', c2.title)
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()