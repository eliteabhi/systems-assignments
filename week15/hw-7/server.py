from socket import socket, AF_INET, SOCK_STREAM
from typing import Tuple

BIND_ADDRESS = r'127.0.0.1'
LISTEN_PORT = 65432
BUFFER_SIZE = 1024

def handle_client( conn: socket ) -> Tuple[ str, str ]:

    data = None
    while data is None:
        data = conn.recv( BUFFER_SIZE )

    msg = data.decode('utf-8')
    print( f'\nMsg recieved from client: { msg }' )
    print( 'Responding with: ', end='' )

    response: str = ''

    if msg == 'hello':
        response = 'world'

    elif msg == 'exit':
        response = 'exit'

    print( response )
    conn.sendall( response.encode( 'utf-8' ) )

    return msg, response


def main() -> None:

    with socket( family=AF_INET, type=SOCK_STREAM ) as sock:

        sock.bind( ( BIND_ADDRESS, LISTEN_PORT ) )
        sock.listen()

        conn, _ = sock.accept()

        msg = None
        with conn:
            while msg != 'exit':
                msg, _ = handle_client( conn )

        print( 'closing connection' )

if __name__ == '__main__':
    main()
