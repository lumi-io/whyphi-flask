from api import create_app

# sets up the app
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
