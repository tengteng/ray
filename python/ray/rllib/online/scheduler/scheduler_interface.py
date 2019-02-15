#! coding=utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ray.rllib.utils.annotations import DeveloperAPI


@DeveloperAPI
class SchedulerInterface(object):
    """
    Base Scheduler interface. Sub-classes can implement different scheduling
    /updating/dynamic extending logics.
    """
    @DeveloperAPI
    def add_servant(self):
        """
        Init and add a servant.
        Returns:
            added: bool.
        """

        raise NotImplementedError

    def remove_servant(self, idx=-1):
        """
        Remove a random servant if `idx` is -1.
        Returns:
            removed: bool. True if successfully removed servant. False otherwise.
        """

        raise NotImplementedError

    @DeveloperAPI
    def update_servants(self, target_policy):
        """
        Select 1 or multiple servants based on some mechanism then update its policy
        model.

        Returns:
            servant_ids: List of Int64 IDs of updated servants.
        """

        raise NotImplementedError

    @DeveloperAPI
    def accept_batch_feedback(self, batch_feedback):
        """
        Accept a batch of feedback logs.

        Returns:
            accepted: bool. Returns False if feedback queue is full.
            idx: int. Last accepted fb log index.
        """

        raise NotImplementedError
