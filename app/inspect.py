import importlib
import pkgutil
from inspect import isclass
from typing import Type, List, Optional

from app.abc import AbstractPlugin


def get_subclasses(cls: Optional[Type], depth: Optional[int] = None) -> List[Type]:
    """recursive get subclasses for cls

    Args:
        cls: python class or any object, if you pass object, class of that object will be used
        depth: options depth of subclass search

    Returns:
        List of cls subclasses
    """
    if cls is None:
        return []
    if not isclass(cls):
        cls = cls.__class__
    if depth == 1:
        return type.__subclasses__(cls)
    else:
        if depth is not None:
            depth -= 1
        cls_subclasses = type.__subclasses__(cls)
        subclasses = list(cls_subclasses)
        for subcls in cls_subclasses:
            subclasses += get_subclasses(subcls, depth)
    return subclasses


def _plugin_subclasses(base_type: Type) -> List[Type]:
    """import all packages and modules in app.plugins package and return all subclass of *base_type*

    Args:
        base_type: AbstractPlugin or some subclass of it

    Returns:
        List of AbstractPlugin subclasses
    """
    import app.plugins
    prefix = app.plugins.__name__ + "."
    for importer, package, _unused in pkgutil.walk_packages(app.plugins.__path__, prefix):
        try:
            importlib.import_module(package, app.plugins.__name__)
        except ImportError as e:
            print(f'import audit module "{package}" error: {e}')

    subclasses = get_subclasses(base_type)
    subclasses = list(filter(lambda x: x.__module__.startswith(prefix), subclasses))
    return subclasses


def plugin_subclasses() -> List[Type[AbstractPlugin]]:
    """import all packages and modules in natrix.audits package and return all subclass of AbstractAudit

    Returns:
        List of AbstractAudit subclasses
    """
    return _plugin_subclasses(AbstractPlugin)
