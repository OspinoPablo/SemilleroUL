from Routes.user_routes import users_routes
from Routes.report_routes import reports_routes
from Models.users_model import db
from db.db import app


app.register_blueprint(users_routes, url_prefix="/users")
app.register_blueprint(reports_routes, url_prefix="/reports")

db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)

