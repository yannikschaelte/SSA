import numpy as np


class ArrayResult:
    """
    Result only for the same given timepoints for all replicates.
    """

    def __init__(
            self,
            ts,
            matrix_xs):
        self.ts = ts
        self.matrix_xs = matrix_xs


class FullResult:
    """
    The entire trajectories generated and output, possibly for different
    timepoints for different replicates.
    """

    def __init__(
            self,
            list_ts,
            list_xs):
        self.list_ts = list_ts
        self.list_xs = list_xs

    def for_timepoints(self, ts = None) -> ArrayResult:
        """
        Generate an `ArrayResult` for the given timepoints. Note that if
        no timepoints are passed and the xs and ts were generated using
        an ArrayOutput, then the values in the ArrayResult will be exactly
        those in the FullResult already.
        """
        if ts is None:
            # take union of all time points
            ts = np.concatenate(self.list_ts)
            ts = np.unique(ts)  # also sorts

        nr = len(self.list_ts)
        nt = len(ts)
        nx = len(self.list_xs[0][0])

        # initialize matrix
        matrix_xs = np.zeros((nr, nt, nx))
        for ir, (_ts, _xs) in enumerate(zip(self.list_ts, self.list_xs)):
            ind = np.searchsorted(a=_ts, v=ts, side='left')
            ind = np.minimum(ind, len(_ts) - 1)
            matrix_xs[ir, ...] = _xs[ind, ...]

        return ArrayResult(ts, matrix_xs)
