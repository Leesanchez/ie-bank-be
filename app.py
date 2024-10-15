from iebank_api import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # This ensures the database schema is created.
    app.run(debug=True)