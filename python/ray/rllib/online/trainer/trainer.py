#! coding=utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ray.rllib.utils.annotations import DeveloperAPI


@DeveloperAPI
class Trainer(object):
    """
    Trainer first trains a policy network using historical logs in off-policy mode.
    When offline model is ready, the trainer will send a signal to the driver, tell the
    driver to initiates the online service.
    Then the trainer will switch to online training mode, under such mode the trainer
    will use the online realtime feedback log to do the off-policy training and
    periodically ship the model to the scheduler.
    """
    @DeveloperAPI
    def __init__(self):
        """
        """

        raise NotImplementedError
