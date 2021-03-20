################################################################################
#                                                                              #
#                  This is the implementation for the storage                  #
#                                                                              #
#                    @author Jack <jack@thinkingcloud.info>                    #
#                                 @version 1.0                                 #
#                          @date 2021-03-19 17:27:07                           #
#                                                                              #
################################################################################

from ..config import config
from .driver import Driver
from .mongo import MongoDriver
from .file import FileDriver


class Storage:
    driver: Driver = None

    def __init__(self):
        storage = config('storage')
        if storage == 'mongo':
            self.driver = MongoDriver()
        if storage == 'file':
            self.driver = FileDriver()

    @property
    def state(self):
        return self.driver.state

    @property
    def frames(self):
        return self.driver.frames

    def query_frames(self, **filters):
        return self.driver.filters
