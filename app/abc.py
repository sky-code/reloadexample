from typing import Type


class AbstractPlugin:
    pass


class PluginMeta:
    """Describe plugin
    """
    plugin_class: Type
    name: str

    def __init__(self, plugin_class: Type):
        self.plugin_class = plugin_class
        self.name = plugin_class.__name__
