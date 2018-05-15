from app.abc import AbstractPlugin, PluginMeta


class PluginFirst(AbstractPlugin):
    @classmethod
    def meta(cls):
        return PluginMeta(cls)
