from collections import defaultdict
from typing import Dict, Union, List

basic_metadata_type = Union[str, int, float, bool, None]
full_metadata_type = Union[List[basic_metadata_type], basic_metadata_type, Dict[str, basic_metadata_type]]


from typing import Union, Dict, List


# modified from Original source: https://github.com/python/mypy/issues/731#issuecomment-539905783
JSONPrimitive = Union[str, int, bool, None]
JSONType = Union[JSONPrimitive, 'JSONList', 'JSONDict']


# work around mypy#731: no recursive structural types yet
class JSONList(List[JSONType]):
    pass


class JSONDict(Dict[str, JSONType]):
    pass


class WorkspaceMetadataStorage:
    def __init__(self) -> None:
        # We allow for a set of key value pairs to be stored per plugin.
        self._data = defaultdict(dict)  # type: Dict[str, Dict[str, JSONType]]

    def setEntryToStore(self, plugin_id: str, key: str, data: JSONType) -> None:
        self._data[plugin_id][key] = data

    def setAllData(self, data: Dict[str, Dict[str, JSONType]]) -> None:
        self._data = defaultdict(dict, data)

    def getAllData(self) -> Dict[str, Dict[str, JSONType]]:
        return self._data

    def getPluginMetadata(self, plugin_id: str) -> Dict[str, JSONType]:
        return self._data[plugin_id]

    def clear(self) -> None:
        self._data = defaultdict(dict)