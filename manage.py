from app import app, db
from app.model.models import Post, Role, User
from flask.ext.script import Manager, Shell, prompt_bool

manager = Manager(app)

@manager.shell
def make_shell_context():
	return dict(app=app, Post = Post, User=User, Role=Role)

@manager.command
def drop():
	"Drop database tables"
	if prompt_bool("Are you sure you want to lose all your data"):
		db.drop_all()

@manager.command
def create(default_data=True, sample_data=False):
	"Creates database tables from sqlalchemy models"
	db.create_all()

@manager.command
def recreate(default_data=True, sample_data=False):
	"Recreates database tables (same as issuing 'drop' and then 'create')"
	drop()
	create(default_data, sample_data)

manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()

