from typing import List, NamedTuple
from collections import OrderedDict
import json
from dataclasses import dataclass
import attr


@attr.s
class base_:
    type_: str = attr.ib()
    id_: str = attr.ib()

    def to_jsonld(self, context=False):
        x = attr.asdict(self, recurse=False)
        for i in x:
            if i == "type_":
                x["@type"] = x.pop(i)
            elif i == "id_":
                x["@id"] = x.pop(i)
            elif isinstance(x[i], list):
                t = []
                for j in x[i]:
                    print("YYY", j)
                    if isinstance(j, base_):
                        t.append(j.to_jsonld())
                x[i] = t
            elif isinstance(x[i], base_):
                print("XXX", x[i])
                return x[i].to_jsonld()
        return x


@attr.s
class Canvas(base_):
    label: str = attr.ib()
    height: int = attr.ib()
    width: int = attr.ib()
    type_: str = attr.ib(default="canvas")


@attr.s
class Sequence(base_):

    canvases: List[Canvas] = attr.ib(factory=list)
    type_: str = attr.ib(default="sequence")


@attr.s
class Manifest(base_):
    label: str = attr.ib()
    sequences: List[Sequence] = attr.ib(factory=list)
    type_: str = attr.ib(default="manifest")


if __name__ == "__main__":
    m = Manifest(label="My manifest", id_="1", sequences=[
        Canvas(label="my canvas", id_="2", width=1, height=1), Canvas(label="my canvas 2", id_="3", width=1, height=1)])

    print("out", m.to_jsonld())
