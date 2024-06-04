import http.server
import socketserver

# Set the directory you want to serve files from
directory = '.' 

# Define the port you want to run the server on
port = 8000 

# Set up the handler to serve files from the current directory
Handler = http.server.SimpleHTTPRequestHandler 

# Set up the server to listen on all available interfaces
with socketserver.TCPServer(("0.0.0.0", port), Handler) as httpd:
    print("Server started at 0.0.0.0:" + str(port))
    # Serve the files forever
    httpd.serve_forever()

