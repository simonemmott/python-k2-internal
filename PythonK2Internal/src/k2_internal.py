'''
Created on 25 Dec 2018

@author: simon
'''
import os, json
from k2_domain import DomainConfig
from utilities import strUtil, classUtil, pathUtil
from jinja2 import Environment, FileSystemLoader

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

assureDir = pathUtil.assureDir

class K2InternalError(Exception):
    pass

def _write_k2_bin(j2_env, path, config):
    assureDir(path+'/bin')
    
    with open(path+'/bin/k2-app.py', 'w') as fp:
        fp.write(j2_env.get_template('k2-app.jj2').render(description='This is a description'))
    
def _write_k2_bin_domains(j2_env, path, config):
    assureDir(path+'/bin/domains')
    for domain in config.domains:
        assureDir(path+'/bin/domains/'+domain.name)
    
def _write_k2_bin_widgets(j2_env, path, config):
    assureDir(path+'/bin/widgets')
    
def _write_k2_conf(j2_env, path, config):
    assureDir(path+'/conf')
    
    with open(path+'/conf/k2.conf', 'w') as conf:
        json.dump(classUtil.to_dict(config), conf, indent='  ')
    
def _write_k2_data(j2_env, path, config):
    abs_path = os.path.abspath(path)
    assureDir(path+'/data')
    for domain in config.domains:
        data = strUtil.env_replace(domain.data)
        abs_data = os.path.abspath(data)
        if (abs_data.startswith(abs_path)):
            assureDir(abs_data)
    

def write_server_home(path, config, **kw):
    
    j2_env = Environment(loader=FileSystemLoader(THIS_DIR+'/templates'), trim_blocks=True)
    
    if not os.path.exists(path):
        os.makedirs(path)
        
    if not os.path.isdir(path):
        raise K2InternalError('The given path %s is not a directory' % path)
    
    if os.listdir(path) and not kw.get('update'):
        raise K2InternalError('The given path %s is not empty' % path)
    
    _write_k2_bin(j2_env, path, config)
    _write_k2_bin_domains(j2_env, path, config)
    _write_k2_bin_widgets(j2_env, path, config)
    _write_k2_conf(j2_env, path, config)
    _write_k2_data(j2_env, path, config)  
 
   
        
            