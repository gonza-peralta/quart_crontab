import asyncio
import click
import json
from quart.cli import AppGroup

from .quart_crontab import _Crontab
user_cli = AppGroup('crontab')


@user_cli.command('add')
def add():
    asyncio.get_event_loop().run_until_complete(async_add())


async def async_add():
    from .factory import create_app
    app = create_app()
    async with app.app_context():
        with _Crontab(verbose=True) as c:
            c.remove_jobs()
            c.add_jobs()

