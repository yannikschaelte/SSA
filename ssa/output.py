from abc import ABC, abstractmethod
import numpy as np
import numba as nb


class Output(ABC):

    @abstractmethod
    def __init__(self):
        super().__init__()
        self.t_max = None

    def create_empty(self):
        return Output()

    def initialize(self, t_max):
        self.t_max = t_max

    def finalize(self):
        pass

    def append(self, t, x):
        pass

    def as_ndarrays(self):
        pass


class FullOutput(Output):

    def __init__(self):
        super().__init__()
        self.ts = []
        self.xs = []

    def create_empty(self):
        return FullOutput()

    def append(self, t, x):
        if t > self.t_max:
            return
        self.ts.append(t)
        self.xs.append(x)

    def as_ndarrays(self):
        ts = np.array(self.ts)
        xs = np.array(self.xs)
        return ts, xs


class ArrayOutput(Output):

    def __init__(self, ts: np.ndarray):
        super().__init__()
        self.ts = ts
        self.xs = None

    def create_empty(self):
        return ArrayOutput(self.ts)

    def append(self, t, x):
        pass

    def as_ndarray(self):
        ts = np.array(self.ts)
        xs = np.array(self.xs)
        return ts, xs
