#Importing library
from flask import Flask,request,jsonify,redirect
import pyshorteners
import datetime
app = Flask(__name__)

urlmapping = dict()

urlmapping['tinyurl.com/23g6ep75'] = 'https://github.com/ByteByteGoHq/system-design-101?tab=readme-ov-file'

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
    
@app.get('/api/shorten/<alias>')
def redirect_to_url(alias):
    print(alias)
    long_url = urlmapping.get(alias)  # Retrieve the long URL
    print(long_url)
    if long_url:
        return redirect(long_url)  # Redirect to the original URL
    else:
        return jsonify({"error": "Alias not found"}), 404 



if __name__ == '__main__':
    app.run(debug=True)




