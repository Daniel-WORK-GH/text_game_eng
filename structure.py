from typing import List
from typing import Any
from dataclasses import dataclass
import json
@dataclass
class Option:
    sub_title: str
    accepting: List[str]
    goto: str

    @staticmethod
    def from_dict(obj: Any) -> 'Option':
        _sub_title = str(obj.get("sub_title"))
        _accepting = obj.get("accepting")
        _goto = str(obj.get("goto"))
        return Option(_sub_title, _accepting, _goto)

@dataclass
class Path:
    id: str
    title: str
    options: List[Option]

    @staticmethod
    def from_dict(obj: Any) -> 'Path':
        _id = str(obj.get("id"))
        _title = str(obj.get("title"))
        _options = [Option.from_dict(y) for y in obj.get("options")]
        return Path(_id, _title, _options)

@dataclass
class Root:
    paths: List[Path]

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _paths = [Path.from_dict(y) for y in obj.get("paths")]
        return Root(_paths)

# using https://json2csharp.com/code-converters/json-to-python : 
# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
