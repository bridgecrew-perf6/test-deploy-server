from prometheus_client import Histogram


class CustomMetrics:

    def __init__(self, service_name: str):
        self.service_name = service_name
        self._model_latency_histogram = None

    @property
    def model_latency_histogram(self):
        if self._model_latency_histogram is None:
            self._model_latency_histogram = Histogram(
                name=self.service_name + '_model_latency_seconds',
                documentation='Model latency (seconds)')

        return self._model_latency_histogram
