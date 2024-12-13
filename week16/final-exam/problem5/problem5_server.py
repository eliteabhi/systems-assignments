from socket import socket, AF_INET, SOCK_STREAM

BIND_ADDRESS = r'127.0.0.1'
DEFAULT_PORT = 65432
BUFFER_SIZE = 1024

def handle_client( conn: socket ) -> None:

    data: bytes = None
    while not data:
        data = conn.recv( BUFFER_SIZE )

    msg: str = data.decode('utf-8')
    print( f'\nMsg recieved from client: "{ msg }"' )
    print( 'Responding with: ', end='' )

    response: str = msg[ ::-1 ]

    print( f'"{ response }"' )
    conn.sendall( response.encode( 'utf-8' ) )

def main() -> None:

    port = input( "\nEnter server port: " )

    if not port.isdigit():
        print( '\nInvalid port number' )
        print( "Defaulting to port '65432'" )
        port = DEFAULT_PORT

    else:
        port = int( port )

    print( '----------------------------------------------------------------' )
    print( f"\nServer listening on '{ BIND_ADDRESS }:{ port }'...\n")

    with socket( family=AF_INET, type=SOCK_STREAM ) as sock:

        sock.bind( ( BIND_ADDRESS, port ) )
        sock.listen()

        conn, _ = sock.accept()

        with conn:
            print( 'Client connected!' )
            handle_client( conn )

        print( '\n...Closing connection' )

if __name__ == '__main__':
    main()