import click
import uvicorn

from config import HOST, PORT


@click.group()
def cli():
    pass


@cli.command()
def run_server():
    uvicorn.run(
        'commands.run_server:main_app',
        host=HOST,
        port=PORT,
        log_level='info',
    )


if __name__ == '__main__':
    cli()
