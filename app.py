from core import app

# WSGI
application = app

if __name__ == '__main__':
    app.run(debug=app.config.get('DEBUG'), host=app.config.get('HOST'),
            port=app.config.get('PORT'))
