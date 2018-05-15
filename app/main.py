from pathlib import Path

import aiohttp_jinja2
import jinja2
from aiohttp import web

from app.app import bootstrap_app
from .settings import Settings
from .views import index, message_data, messages


THIS_DIR = Path(__file__).parent
BASE_DIR = THIS_DIR.parent


def setup_routes(app):
    app.router.add_get('/', index, name='index')
    app.router.add_route('*', '/messages', messages, name='messages')
    app.router.add_get('/messages/data', message_data, name='message-data')


def create_app():
    bootstrap_app()
    app = web.Application()
    settings = Settings()
    app.update(
        name='reloadexample',
        settings=settings
    )

    jinja2_loader = jinja2.FileSystemLoader(str(THIS_DIR / 'templates'))
    aiohttp_jinja2.setup(app, loader=jinja2_loader)

    setup_routes(app)
    return app
