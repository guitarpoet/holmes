################################################################################
#                                                                              #
#                     This is the driver for file storage                      #
#                                                                              #
#                    @author Jack <jack@thinkingcloud.info>                    #
#                                 @version 1.0                                 #
#                          @date 2021-03-19 17:51:50                           #
#                                                                              #
################################################################################

from .driver import Driver
from ..config import config
import json
from os import path
from ..model import State, Frame


class FileDriver(Driver):
    _frames: list = None
    _state: dict = None

    def __init__(self):
        f = config('files')

        if path.exists(f.frames):
            with open(f.frames) as input:
                self._frames = []
                for frame in json.load(input):
                    start, stop, project, id, tags, update_at = frame
                    self._frames.append(
                        Frame(start=start,
                              stop=stop,
                              id=id,
                              project=project,
                              tags=tags,
                              update_at=update_at))
        else:
            raise Exception('No frame file found')
        if path.exists(f.state):
            with open(f.state) as input:
                self._state = State(**json.load(input))
        else:
            raise Exception('No state file found')

    def get_state(self):
        return self._state

    def get_frames(self, **filters):
        return self._frames
