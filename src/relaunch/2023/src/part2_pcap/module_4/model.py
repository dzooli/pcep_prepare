"""
Attrs demo models with validation and a JSON decoder example.
"""
from attrs import define, field, validators


@define(kw_only=True)
class Server:
    """
    A simple server class.

    Attributes:
        server_name:    name of the server
        type:           server type
    """

    server_name: str = field(
        default=None,
        validator=validators.and_(validators.min_len(1), validators.max_len(20)),
    )
    type: str = field(
        init=True,
        default=None,
        validator=validators.optional(validators.in_(["clm", "pf"])),
    )


@define(kw_only=True)
class Network:
    """
    Network class with id and nodes.

    Attributes:
        network_id:     unique id of the network
        nodes:          list of nodes
    """

    network_id: int = field(
        default=0,
        validator=validators.and_(
            validators.instance_of(int), validators.ge(0), validators.lt(256)
        ),
    )

    nodes: list[Server] = field(
        factory=list,
        validator=validators.deep_iterable(
            validators.instance_of(Server), validators.instance_of(list)
        ),
    )


@define(kw_only=True)
class JsonDecoder:
    """
    Decode JSON dictionary to Python object.

    The decode() method is useful for json.loads(..., object_hook=Decoder.decode) calls.
    With this usage, json.loads() should call the hook upon every loaded object.

    Attributes:
        mapping: unique key to Python class mapping
        obj_class: the detected Python class
    """

    mapping: dict = field(factory=dict, init=False)
    obj_class = field(default=None, init=False, repr=False)

    def decode(self, data_dict: dict = None) -> object | None:
        """
        Decodes a JSON dictionary to a Python object.

        First searching the corresponding object class in self.mapping using
        a unique identifier in the passed JSON dictionary data.
        If found, creates the object with initialized data fields and returns it.
        If not found or on error, returns None. For demonstration puspose it also
        prints the exception if any.
        """
        res = None
        obj_found = [obj_key for obj_key in self.mapping if obj_key in data_dict]
        try:
            obj_class = self.mapping[obj_found[0]]
        except (KeyError, IndexError) as exc:
            print(exc)
            return None
        try:
            res = obj_class(**data_dict) if obj_class else None
        except (TypeError, ValueError) as exc:
            print(exc)
            return None
        return res


@define
class NetworkDecoder(JsonDecoder):
    """
    Defines the mapping of an identifying JSON attribute name to
    the corresponding Network-related Python class.

    The unique attribute name could identify the required class.
    """

    mapping: dict = {"server_name": Server, "network_id": Network}
