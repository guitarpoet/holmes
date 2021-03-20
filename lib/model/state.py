################################################################################
#                                                                              #
#                       This is the model for the state                        #
#                                                                              #
#                    @author Jack <jack@thinkingcloud.info>                    #
#                                 @version 1.0                                 #
#                          @date 2021-03-19 17:33:35                           #
#                                                                              #
################################################################################

from dataclasses import dataclass
from .base import BaseModel
import uuid
import arrow
from .frame import Frame
import uuid


@dataclass
class State(BaseModel):
    """
    The class for state
    """
    start: int = 0  # The start time of this frame
    project: str = None  # The project of this frame
    tags: list = None  # The tags of this frame

    @property
    def start_time(self):
        return arrow.get(self.start).to('local')

    def to_frame(self):
        t = arrow.utcnow().timestamp
        return Frame(project=self.project,
                     start=self.start,
                     stop=t,
                     id=uuid.uuid4(),
                     tags=self.tags,
                     update_at=t)
