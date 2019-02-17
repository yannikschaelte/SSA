import numpy as np
import multiprocessing as mp

from .direct import direct
from .util import get_k_stoch


class Model:

    def __init__(
            self,
            reactants: np.ndarray,
            products: np.ndarray,
            x0: np.ndarray,
            k: np.ndarray,
            k_is_det: bool = True,
            volume: float = 1.0,
            use_na: bool = False,
            t_max = None,
            engine = None):
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
        self.reactants = reactants
        self.products = products
        self.x0 = x0

        self.k_stoch = None
        self.k_is_det = k_is_det
        self.volume = volume
        self.use_na = use_na
        self.update_k_stoch()

        self.t_max = t_max

        # dimensions
        self.nr, self.ns = reactants.shape

        # set shapes
        self.x0.shape = (self.ns, 1)
        self.k_stoch.shape = (1, self.nr)

    def update_k_stoch(
            self,
            k: np.ndarray,
            k_is_det: bool = None,
            volume: float = None,
            use_na: bool = None):
        if k is None:
            return

        if k_is_det is not None:
            self.k_is_det = k_is_det
        if volume is not None:
            self.volume = volume
        if use_na is not None:
            self.use_na = use_na

        if self.k_is_det:
            self.k_stoch = get_k_stoch(
                k, self.reactants, self.volume, self.na)
        else:
            self.k_stoch = k

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
                
