class SignalBus:

    def __init__(self):

        self.values = {}
        self.history = {}

    def publish(
        self,
        name,
        value,
        time
    ):

        self.values[name] = value

        if name not in self.history:
            self.history[name] = []

        self.history[name].append(
            (time, value)
        )

    def read(
        self,
        name,
        default=None
    ):

        return self.values.get(
            name,
            default
        )