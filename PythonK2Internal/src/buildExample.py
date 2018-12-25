'''
Created on 25 Dec 2018

@author: simon
'''

from k2_internal import write_server_home
from k2 import K2Config
from k2_domain import DomainConfig

EXAMPLE_PATH = '../../pythonK2Example/src/k2_home'

if __name__ == '__main__':
    conf = K2Config(domains=[DomainConfig('example_domain')])
    write_server_home(EXAMPLE_PATH, conf, update=True)