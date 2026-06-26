import paramiko


HOST = "test.rebex.net"
PORT = 22
USERNAME = "demo"
PASSWORD = "password"


def main():
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(
            hostname=HOST,
            port=PORT,
            username=USERNAME,
            password=PASSWORD,
            timeout=10,
            look_for_keys=False,
            allow_agent=False,
        )

        print("Połączono przez SSH.")

        sftp = client.open_sftp()
        print("Otworzono sesję SFTP przez kanał SSH.")

        print("\nPliki w katalogu głównym:")
        for item in sftp.listdir("."):
            print("-", item)

        print("\nPliki w /pub/example:")
        for item in sftp.listdir("/pub/example"):
            print("-", item)

        sftp.close()

    finally:
        client.close()
        print("\nPołączenie zamknięte.")


if __name__ == "__main__":
    main()
