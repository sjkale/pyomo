from pyomo.gdp import Disjunct, Disjunction
from abc import ABC, abstractmethod



class Branching_Strategy(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def choose_unexplored_node(self):
        pass

    @abstractmethod
    def update_strategy(self,parent,children):
        pass

    @abstractmethod
    def generate_lower_bound(self):
        pass
