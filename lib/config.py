################################################################################
#                                                                              #
#                     This is the module for configuration                     #
#                                                                              #
#                    @author Jack <jack@thinkingcloud.info>                    #
#                                 @version 1.0                                 #
#                          @date 2021-03-19 16:09:48                           #
#                                                                              #
################################################################################

from config import config_from_yaml, config_from_dict, config_from_env, ConfigurationSet
from os.path import expanduser, exists

_conf = None


def load_config():
    global _conf
    home = expanduser('~')
    config_folder = f'{home}/.config/holmes'
    config_file = f'{config_folder}/config.yaml'
    if exists(config_file):
        with open(config_file) as input:
            _conf = ConfigurationSet(config_from_env('HOLMES'),
                                     config_from_yaml(input))
    else:
        DEFAULT_CONFIG = {
            'storage': 'file',
            'files': {
                'frames': f'{home}/Library/ApplicationSupport/watson/frames',
                'state': f'{home}/Library/ApplicationSupport/watson/state',
            }
        }
        _conf = ConfigurationSet(config_from_dict(DEFAULT_CONFIG))


def config(key=None):
    global _conf

    if not _conf:
        load_config()

    if not key:
        return _conf
    return _conf[key]
