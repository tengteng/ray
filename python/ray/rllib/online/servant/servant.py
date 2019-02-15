#! coding=utf-8
import ray

class Servant(object):
    """
    A servant wraps up an RL Agent and responds the outside requests.
    """
    def __init__(self, agent):
        self._agent = agent
        self._ready = True

    @ray.method(num_return_vals=0)
    def update(self, policy):
        """
        Update policy network.
        """
        # XXX(teng.t): We probably do not have a Update() in rllib.agents.Agent
        # class.
        # So here we can simply construct a new agent using input policy
        # then replace the servant. As the first step.
        raise NotImplementedError


ServantActor = ray.remote(num_cpus=2)(Servant)
