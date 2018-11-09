from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('buttons.html')


@app.route('/products')
def product_page():
    return render_template('product-page.html')

@app.route('/checkout')
def checkout_page():
    return render_template('checkout-page.html')

@app.route('/signup')
def form_page():
    return render_template('form.html')

@app.route('/home-page')
def home_page():
    return render_template('home-page.html')

@app.route('/offline.html')
def offline():
    return app.send_static_file('offline.html')


@app.route('/service-worker.js')
def sw():
    return app.send_static_file('service-worker.js')

@app.route('/OneSignalSDKUpdaterWorker.js')
def sw_update():
    return app.send_static_file('OneSignalSDKUpdaterWorker.js')

@app.route('/manifest.json')
def manifest():
    return app.send_static_file('manifest.json')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8100)
