from app import app, db
from app.model.models import Post, Role, User
from flask.ext.script import Manager, Shell, prompt_bool
from flask.ext.migrate import Migrate, MigrateCommand


manager = Manager(app)

@manager.shell
def make_shell_context():
	return dict(app=app, Post = Post, User=User, Role=Role)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

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
def insertadmin(default_data=True, sample_data=False):
	"Insert roles into Role table"
	Role.insert_roles()
	admin_role = Role.query.filter_by(name='Administrator').first()
	admin = User(username='admin', role_id=admin_role.id, password='admin')
	db.session.add(admin)
	db.session.commit()

@manager.command
def insertroles(default_data=True, sample_data=False):
	"Insert roles into User table"
	Role.insert_roles()	

@manager.command
def recreate(default_data=True, sample_data=False):
	"Recreates database tables (same as issuing 'drop' and then 'create')"
	drop()
	create(default_data, sample_data)



manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()

