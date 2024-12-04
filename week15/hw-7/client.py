from socket import socket, AF_INET, SOCK_STREAM

HOST_ADDRESS = r'127.0.0.1'
LISTEN_PORT = 65432
BUFFER_SIZE = 1024

def main() -> None:

    with socket( family=AF_INET, type=SOCK_STREAM ) as sock:

        sock.connect( ( HOST_ADDRESS, LISTEN_PORT ) )

        print( '\nMsg to send: hello' )
        sock.sendall( 'hello'.encode( 'utf-8' ) )

        response = sock.recv( BUFFER_SIZE )
        print( f'Response from server: { response.decode( 'utf-8' ) }\n' )

        print( 'Msg to send: exit' )
        sock.sendall( 'exit'.encode( 'utf-8' ) )

        response = sock.recv( BUFFER_SIZE )
        print( f'Response from server: { response.decode( 'utf-8' ) }' )

        print( 'closing connection' )

if __name__ == '__main__':
    main()
