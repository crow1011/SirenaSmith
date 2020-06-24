from flask.cli import FlaskGroup

from sirena import app

cli = FlaskGroup(app)

@cli.command("check")
def create_db():
    print('all_done!')
    return True


if __name__ == "__main__":
    cli()