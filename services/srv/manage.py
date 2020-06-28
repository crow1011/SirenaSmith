from flask.cli import FlaskGroup
import os
from sirena import app

cli = FlaskGroup(app)

@cli.command("check")
def create_db():
    print('all_done!')
    return True

@cli.command("test")
def test():
    os.system('pytest')

if __name__ == "__main__":
    cli()