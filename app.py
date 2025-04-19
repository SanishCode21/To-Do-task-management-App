from application.init import create_app
from application.models import db


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

