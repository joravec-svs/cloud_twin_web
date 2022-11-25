from flask_login import current_user
from flask import redirect, url_for
from app.models import User,Role,SensorData,VirtualData,InputData
from app import admin, db
from flask_admin.contrib.sqla import ModelView

class DTwinModelView(ModelView):
    create_modal = True
    edit_modal = True
    page_size = 500
    can_export = True

    def is_accessible(self):
        return current_user.is_admin()

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('main.index'))

admin.add_view(DTwinModelView(User, db.session))
admin.add_view(DTwinModelView(SensorData, db.session))
admin.add_view(DTwinModelView(VirtualData, db.session))
admin.add_view(DTwinModelView(InputData, db.session))
admin.add_view(DTwinModelView(Role, db.session))
