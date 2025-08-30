from typing import TypeVar

from pydantic import RootModel

T = TypeVar("T")
def map_root_model(model: RootModel[T]) -> T:
  return model.root