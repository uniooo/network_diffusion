"""Contains funcitons to handle actors of the multilayer network."""

from typing import Any, Dict, Tuple


class MLNetworkActor:
    """Dataclass that contain data of actor in the network."""

    def __init__(self, actor_id: str, layers_states: Dict[str, str]) -> None:
        """
        Initialise the object.

        :param actor_id: if of the actor
        :param layers_states: a dictionary keyed by layer names where the actor
            exists and valued by its state in the given layer
        """
        self.actor_id = actor_id
        self._layers_states = layers_states

    def __str__(self) -> str:
        return (
            f"actor id: {self.actor_id}, "
            f"layers and states: {self._layers_states}"
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.actor_id} at {id(self)}"

    def __eq__(self, another: Any) -> bool:
        if not isinstance(another, self.__class__):
            return False
        ids_eq = self.actor_id == another.actor_id
        lss_eq = self._layers_states == another._layers_states
        return ids_eq and lss_eq

    def __hash__(self) -> int:
        return hash(
            (
                self.actor_id,
                self.layers,
                tuple(self.states.values()),
                self.__class__,
            )
        )

    @property
    def layers(self) -> Tuple[str, ...]:
        """Get network layers where actor exists."""
        return tuple(self._layers_states.keys())

    @property
    def states(self) -> Dict[str, str]:
        """Get actor's states for where actitor exists."""
        return self._layers_states

    @states.setter
    def states(self, updated_states: Dict[str, str]) -> None:
        """Set actor's states for layers where it exists."""
        for layer_name, new_state in updated_states.items():
            assert layer_name in self._layers_states
            self._layers_states[layer_name] = new_state
