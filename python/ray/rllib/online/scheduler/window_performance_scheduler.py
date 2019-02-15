#! coding=utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ray.rllib.utils.annotations import DeveloperAPI
from ray.rllib.online.scheduler import SchedulerInterface

from contextlib import ExitStack
from functools import partial
import queue


@DeveloperAPI
class WindowPerformanceScheduler(SchedulerInterface):
    """
    WindowPerformanceScheduler collects servants' reward within the time window.
    It applies an inferior eliminated mechanism on servants: Every time it only
    updates the worse performer and then refresh the time window performance stats.
    """

    def __init__(self, buf_size, log_parser):
        """
        """
        self._fb_queue = queue.Queue(buf_size) # queue feedback log
        self._fb_collector = CollectorThread(self._fb_queue, self)
        self._log_parser = log_parser
        self.perf_window = {}
        self._fb_collector.start()

    @DeveloperAPI
    def _refresh(self):
        """
        """
        raise NotImplementedError

    @override(SchedulerInterface)
    def update_servants(self, target_policy):
        """
        """
        with ExitStack() as stack:
            stack.callback(partial(self._refresh))
            idx = self._select()
        self._servants[idx].update(target_policy)
        return idx

    @override(SchedulerInterface)
    def accept_batch_feedback(self, batch_feedback):
        accepted_idx = 0
        for log in self._log_parser(batch_feedback):
            try:
                self._fb_queue.put_nowait(log)
            except queue.Full:
                return False, accepted_idx
            accepted_idx += 1
        return True, accepted_idx


class CollectorThread(threading.Thread):
    """
    This is a log consumer thread.
    """

    def __init__(self, fb_queue, scheduler):
        threading.Thread.__init__(self)
        self._fb_queue = fb_queue
        self._scheduler = scheduler

    def run(self):
        while True:
            if not self._fb_queue.empty():
                fb_log = self._fb_queue.get()
                # Parse and aggregate some performance stats in self._scheduler
                # self._record(fb_log)
                # TODO(teng.t): Consider auto-extending capacity if self._fb_queue.full()
            else:
                time.sleep(2)
        return
