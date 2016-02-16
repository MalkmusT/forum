from app import app

# host, default localhost
HOST='127.0.0.1'

# port, default 
PORT=5000

if __name__ == "__main__" :
  app.run( debug=True, host=HOST, port=PORT )
