################################################################################
#                                                                              #
#              This is the base driver class for this application              #
#                                                                              #
#                    @author Jack <jack@thinkingcloud.info>                    #
#                                 @version 1.0                                 #
#                          @date 2021-03-19 16:52:34                           #
#                                                                              #
################################################################################

from ..model import Frame, State


class Driver:
    """
    This is the driver interface for the storage
    """
    @property
    def frames(self) -> list:
        """
        The interface method for getting all frames
        """
        return self.get_frames()

    def query_frames(self, **filters) -> list:
        """
        The interface method for getting all frames
        """
        return self.get_frames(*filters)

    @property
    def state(self) -> State:
        return self.get_state()

    def get_frames(self, **filters) -> list:
        return []

    def get_state(self) -> any:
        return None
