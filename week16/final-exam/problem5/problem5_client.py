from socket import socket, AF_INET, SOCK_STREAM

HOST_ADDRESS = r'127.0.0.1'
DEFAULT_PORT = 65432
BUFFER_SIZE = 1024

def main() -> None:

    port = input( "\nEnter server port: " )

    if not port.isdigit():
        print( '\nInvalid port number' )
        print( "Defaulting to port '65432'" )
        port = DEFAULT_PORT

    else:
        port = int( port )

    print( '----------------------------------------------------------------' )
    print( f"\nAttempting to connect to server on '{ HOST_ADDRESS }:{ port }...'")

    with socket( family=AF_INET, type=SOCK_STREAM ) as sock:

        try:
            sock.connect( ( HOST_ADDRESS, port ) )

        except ConnectionRefusedError:
            print( '\nConnection refused by server' )
            return

        print( '\nConnected to server!\n' )

        msg = input( "Enter message to send: " ).strip()

        if len( msg ) == 0:
            print( '\nNo message' )
            print( 'Defaulting to "Hello, World!"')
            msg = "Hello, World!"

        print( f'\nSending message: "{ msg }"' )
        sock.sendall( msg.encode( 'utf-8' ) )

        response = sock.recv( BUFFER_SIZE )
        print( f'Response from server: "{ response.decode( 'utf-8' ) }"' )

        print( '\n...Closing connection' )

if __name__ == '__main__':
    main()
