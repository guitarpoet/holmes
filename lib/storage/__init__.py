################################################################################
#                                                                              #
#                        This is the module for storage                        #
#                                                                              #
#                    @author Jack <jack@thinkingcloud.info>                    #
#                                 @version 1.0                                 #
#                          @date 2021-03-19 16:21:37                           #
#                                                                              #
################################################################################

from .mongo import MongoDriver
from .storage import Storage

_storage = None


def storage():
    global _storage
    if not _storage:
        _storage = Storage()
    return _storage
