import numpy as np
import numbers
import multiprocessing as mp

from .direct import direct
from .util import get_k_stoch


class Model:
    """
    A chemical reaction network model.

    Attributes
    ----------

    reactants: np.ndarray, shape = (nr, ns)
    products: np.ndarray, shape = (nr, ns)
    x0: np.ndarray, shape = (nr, )
    k: np.ndarray, shape = (ns, )
    t_max: numbers.Number
    """

    def __init__(
            self,
            reactants: np.ndarray,
            products: np.ndarray,
            x0: np.ndarray,
            t_max: numbers.Number):
        """
        Parameters
        ----------

        reactants: np.ndarray, shape = (nr, ns)
        products: np.ndarray, shape = (nr, ns)
        x0: np.ndarray, size = ns
        k_det:: np.ndarray, size = nr
        volume: float, optional (default = 1.0)
        use_na: bool, optional (default = False)
        """
        self._reactants = reactants
        self._products = products
        self._x0 = x0
        self._t_max = t_max
        self._k = None

        # dimensions
        self._nr, self._ns = reactants.shape

        # set shapes
        self._configure()

    def set_k(
            self,
            k: np.ndarray,
            is_det: bool = True,
            volume: float = 1.0,
            use_na: bool = True):
        """
        Parameters
        ----------

        k: np.ndarray, shape = (nr, 1)
            The reaction rate constants.
        is_det: bool, optional (default = True)
            Whether k is to be interpreted as deterministic reaction rate
            constants. In that case, it must be converted to stochastic
            rates working on single molecules.

        if is_det:
            self.k = get_k_stoch(
                k, self.reactants, self.volume, self.na)
        self.k_stoch.shape = (1, self.nr)

    def update_t_max(
            self,
            t_max):
        if t_max is not None:
            self.t_max = t_max

    def check_consistency(self):
        if not isinstance(self.t_max, int) or not np.isfinite(self.t_max):
            raise ValueError("t_max must be a finite integer.")

    def simulate(
            alg = None,
            k: np.ndarray = None,
            k_is_det: bool = None,
            volume: floate = None,
            use_na: bool = None,
            t_max: float = None,
            n_reps: int = 1,
            n_procs: int = 1,
            alg = None,
            **kwargs):
        # choose algorithm
        if alg is None:
            alg = direct

        # update model parameters
        self.update_k_stoch(k, k_is_det, volume, use_na)
        self.update_t_max(t_max)

        # check consistency
        self.check_consistency()

        # run
        alg_args = dict(
            reactants = self.reactants,
            products = self.products,
            x0 = self.x0,
            k_stoch = self.k_stoch,
            t_max = self.t_max,
            **kwargs)

        # define tasks
        tasks = []
        for _ in n_reps:
            task = SimulationTask(

        
        ret = self.engine.execute(tasks=tasks)
        
        list_ts = []
        list_xs = []
        for ts, xs in ret:
            list_ts.append(ts)
            list_xs.append(xs)
        
        return Result(list_ts=list_ts, list_xs=list_xs)

        if n_procs == 1:
            result = alg(**alg_args)
        else:
            with mp.Pool(processes=n_procs) as pool:
                results = pool.map(alg, alg_args)
                
