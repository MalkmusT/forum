from app import app

# replace this with 0.0.0.0 for server mod
HOST="127.0.0.1"

# port to the real world, on gimli this is 8000
PORT=5000

if __name__ == "__main__" :
  app.run( debug=True, host=HOST, port=PORT )
