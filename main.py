from screenshot import take_screenshot
from broadcaster import broadcast_file
from file_server import start_file_server


def main():

    filepath = take_screenshot()

    if filepath:
        broadcast_file(filepath)
        start_file_server(filepath)


if __name__ == "__main__":
    main()