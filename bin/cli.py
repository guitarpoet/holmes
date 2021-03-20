################################################################################
#                                                                              #
#               This is the commandline interface for the system               #
#                                                                              #
#                    @author Jack <jack@thinkingcloud.info>                    #
#                                 @version 1.0                                 #
#                          @date 2021-03-19 16:13:15                           #
#                                                                              #
################################################################################

from lib.config import config
from lib.model import State
from lib.storage import storage
import arrow

s = State(project='Hello', start=arrow.utcnow().timestamp, tags=['a', 'b', 'c'])

print(s.to_frame())
print(storage().frames)
