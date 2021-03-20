################################################################################
#                                                                              #
#                         This is the model for frame                          #
#                                                                              #
#                    @author Jack <jack@thinkingcloud.info>                    #
#                                 @version 1.0                                 #
#                          @date 2021-03-19 16:53:55                           #
#                                                                              #
################################################################################

from dataclasses import dataclass
from .base import BaseModel
import uuid
import arrow


@dataclass
class Frame(BaseModel):
    """
    The class for frame
    """
    start: int = 0  # The start time of this frame
    stop: int = 0  # The stop time of this frame
    project: str = None  # The project of this frame
    id: str = None  # The id of this frame
    tags: list = None  # The tags of this frame
    update_at: int = 0  # The update time of this frame

    @property
    def start_time(self):
        return arrow.get(self.start).to('local')

    @property
    def end_time(self):
        return arrow.get(self.end).to('local')

    @property
    def update_at_time(self):
        return arrow.get(self.update_at).to('local')

    def gen_id(self):
        if not self.id:
            self.id = uuid.uuid4()
        return self.id

    def update(self):
        self.update_at = arrow.utcnow().timestamp
