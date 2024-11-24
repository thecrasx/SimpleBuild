from sb.sb import SimpleBuild
from sb.Database.database import Database
from sb.config import Config
import click
import os


@click.group()
def commands():
    pass


@click.command(help = "Initialize SimpleBuild")
def init():
    if not os.path.exists("./.sb"):
        os.mkdir("./.sb")
        os.mkdir("./.sb/lib")

        db = Database()
        db.addTables()
        db.close()

    if not os.path.exists("./config.toml"):
        config = Config()
        config.makeFile()

    click.echo("sb Initialized")


@click.command()
def compile():
    if not os.path.exists("./.sb") or not os.path.exists("./config.toml"):
        click.echo("sb not initialized")
        click.echo("    Run: sb init")
        return
    
    sb = SimpleBuild()
    sb.compile()


@click.command()
def reset():
    if not os.path.exists("./.sb"):
        click.echo("sb not initialized")
        click.echo("    Run: sb init")
        return

    db = Database()
    db.removeAllFiles()
    db.close()


commands.add_command(init)
commands.add_command(compile)
commands.add_command(reset)



if __name__ == "__main__":
    commands()