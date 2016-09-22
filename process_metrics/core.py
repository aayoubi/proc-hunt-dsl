class FetchException(Exception):
    pass

class Fetcher:

    def __init__(self, metric):
        self.metric = metric
        self.host = 'localhost'
        self.pid = -1
        self.output = None

    def on(self, host):
        return self

    def of(self, pid):
        return self

    def echo_to(self, stream):
        if self.output is None:
             raise FetchException("output has not been retrieved yet")
        with open(stream, 'w') as f:
            f.write(self.output)
            f.write('\n')
            f.flush()
        return self

    def value(self):
        return self.output

    def retrieve(self):
        self.output = self.metric.get()
        return self

    @staticmethod
    def metric(metric):
        retriever = Fetcher(metric())
        return retriever
