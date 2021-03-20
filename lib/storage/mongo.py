################################################################################
#                                                                              #
#                      This is the mongodb storage module                      #
#                                                                              #
#                    @author Jack <jack@thinkingcloud.info>                    #
#                                 @version 1.0                                 #
#                          @date 2021-03-19 16:23:41                           #
#                                                                              #
################################################################################

from .driver import Driver
from pymongo import MongoClient
from ..config import config


class MongoDriver(Driver):
    client: MongoClient = None
    db: any = None

    def __init__(self):
        c = config('mongodb')
        self.client = MongoClient(host=c.host, port=c.port)
        self.db = client[c.database]
