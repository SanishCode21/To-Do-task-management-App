from application.init import *
from application.models import db


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

