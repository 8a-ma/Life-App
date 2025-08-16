from src import create_app
from config import config

env = config['dev']
app = create_app(env)

if __name__ == "__main__":
    app.run(debug=True)