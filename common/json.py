import types
import typing as t

import numpy as np
import orjson


def _default(
    obj: t.Union[np.float32, np.float64, types.MappingProxyType],
) -> t.Any:
    if isinstance(obj, (np.float32, np.float64)):
        return obj.item()
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, types.MappingProxyType):
        return dict(obj)
    if isinstance(obj, BaseException):
        return str(obj)
    raise TypeError


def orjson_dumps(
    *args: t.Any,
    default: t.Optional[t.Callable[[t.Any], t.Any]] = None,
    **kwargs: t.Any,
) -> str:
    default = kwargs.pop('default', None) or default

    return orjson.dumps(  # type: ignore[misc]
        *args,
        default=default or _default,
        **kwargs,
    ).decode('utf-8')
