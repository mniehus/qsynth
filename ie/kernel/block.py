class Block:

    def __init__(
        self,
        name,
        period,
        latency=0.0,
        priority=10
    ):

        self.name = name
        self.period = period
        self.latency = latency
        self.priority = priority

        self.enabled = True

    def reset(self):
        pass

    def update(
        self,
        t,
        bus
    ):
        raise NotImplementedError