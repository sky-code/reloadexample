from app.abc import AbstractPlugin, PluginMeta


class PluginSecond(AbstractPlugin):
    @classmethod
    def meta(cls):
        return PluginMeta(cls)
