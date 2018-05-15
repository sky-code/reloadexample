from app.inspect import plugin_subclasses


class Application:
    pass

    def __init__(self):
        self.plugin_names = []
        self.plugin_subclasses = plugin_subclasses()
        for cls in self.plugin_subclasses:
            meta = cls.meta()
            self.plugin_names.append(meta.name)


_app: Application = None


def get_app() -> Application:
    global _app
    if _app is None:
        raise RuntimeError('There is no one Application instance created, use bootstrap_app before get_app')
    return _app


def bootstrap_app() -> Application:
    global _app
    # if _app is not None:
        # raise RuntimeError('Application instance already exists, use bootstrap_app one time per process')
    # init_logging()
    _app = Application()
    # logger = _app.logger
    # logger.info('bootstrap_app.complete')

    return _app
