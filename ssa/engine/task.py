import logging


logger = logging.getLogger(__name__)


class Task:

    def __init__(self):
        """
        Create a task object. A task is one of a list of independent
        execution tasks that are submitted to the execution engine
        to be executed using the execute() method, commonly in parallel.
        """
        pass

    def execute(self):  # pylint: disable=R0201
        """
        Execute the task and return its results.
        """
        return NotImplementedError(
            "This is a non-functional base class.")


class SimulationTask:

    def __init__(self, alg, alg_args):
        self.alg = alg
        self.alg_args = alg_args

    def execute(self):
        return self.alg(**self.alg_args)
