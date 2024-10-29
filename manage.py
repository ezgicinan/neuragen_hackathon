# neura_hackathon/manage.py
import os

from flask_migrate import Migrate
from backend import create_app, db
import sys
from flask.cli import FlaskGroup

app = create_app() # app.app_context().push()
migrate = Migrate(app, db)

# Add CLI commands to allow `db` commands like init, migrate, upgrade
cli = FlaskGroup(app)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "db":
        with app.app_context():
            # Running db commands directly
            cli()
    else:
        app.run(debug=True)

