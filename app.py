#Importing library
from flask import Flask,request,jsonify,redirect
import pyshorteners
import datetime
app = Flask(__name__)

@app.post('/api/shorten')
def create_short_url():
    try:
        data = request.get_json()
        long_url = data.get('url')

        if not long_url:
            return jsonify({'error':'URL is required'}),400
        
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(long_url)

        created_time = datetime.datetime.now()

        return jsonify({'short_url':short_url,'time-created': created_time}),200
    
    except Exception as e:
        return jsonify({'error':str(e)}),400
    
@app.get('/api/shorten/<short_url>')
def redirect_to_url(short_url):
    try:
        print(short_url)
        shortener = pyshorteners.Shortener()
        long_url = shortener.tinyurl.expand(short_url)
        return redirect(long_url)
    except Exception as e:
        return f"Error expanding URL: {str(e)}", 400



if __name__ == '__main__':
    app.run(debug=True)




