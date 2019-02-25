import numpy as np
import numbers
import multiprocessing as mp

from .direct import direct
from .util import get_k_stoch
from .output import Output
from .result import Result


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
            t_max: numbers.Number,
            k: np.ndarray,
            output: Output,
            k_is_det: bool = True,
            volume: float = 1.0,
            use_na: bool = False,
            engine: None):
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
        
        self.reaction_matrix = products - reactants

        self.x0 = x0
        self.t_max = t_max
        self.k = None
        self.set_k(k, reactants, k_is_det, volume, use_na)

        self.output = output

        if engine is None:
            engine = MultiProcessEngine()
        self.engine = engine

        self.nr, self.ns = reactants.shape

        self._configure()

    def set_k(
            self,
            k: np.ndarray,
            reactants,
            k_is_det: bool = True,
            volume: float = 1.0,
            use_na: bool = False):
        """
        Parameters
        ----------

        k: np.ndarray, shape = (nr, 1)
            The reaction rate constants.
        is_det: bool, optional (default = True)
            Whether k is to be interpreted as deterministic reaction rate
            constants. In that case, it must be converted to stochastic
            rates working on single molecules.
        """
        if k_is_det:
            self.k = get_k_stoch(k, reactants, volume, use_na)

    def _configure(self):
        self.reactants.shape = (self.nr, self.ns)
        self.products.shape = (self.nr, self.ns)
        self.reaction_matrix.shape = (self.nr, self.ns)
        self.x0.flatten() #shape = (self.ns, 1)
        self.k.flatten() #shape = (self.nr, 1)
        if not isinstance(self.t_max, numbers.Number) or not np.isfinite(self.t_max):
            raise ValueError("t_max must be a finite integer.")

    def simulate(
            self,
            alg = None,
            n_reps: int = 1,
            **kwargs):
        # choose algorithm
        if alg is None:
            alg = direct

        # run
        alg_args = dict(
            reactants = self.reactants,
            reaction_matrix = self.reaction_matrix,
            x0 = self.x0,
            k = self.k,
            t_max = self.t_max,
            output = self.output.create_empty(),
            **kwargs)

        self.engine.execute(alg, alg_args, n_reps)
        list_ts = []
        list_xs = []
        for _ in range(n_reps):
            ts, xs = alg(**alg_args)
            list_ts.append(ts)
            list_xs.append(xs)
        
        return Result(list_ts, list_xs)

