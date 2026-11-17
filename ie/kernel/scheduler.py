import heapq


class Scheduler:

    def __init__(
        self,
        bus
    ):

        self.bus = bus

        self.queue = []
        self.counter = 0

    def add_block(
        self,
        block,
        start_time=0.0
    ):

        heapq.heappush(
            self.queue,
            (
                start_time,
                block.priority,
                self.counter,
                block
            )
        )

        self.counter += 1

    def run(
        self,
        duration
    ):

        while self.queue:

            t, priority, order, block = (
                heapq.heappop(
                    self.queue
                )
            )

            if t > duration:
                break

            if block.enabled:

                block.update(
                    t,
                    self.bus
                )

            next_time = (
                t
                + block.period
            )

            heapq.heappush(
                self.queue,
                (
                    next_time,
                    block.priority,
                    self.counter,
                    block
                )
            )

            self.counter += 1