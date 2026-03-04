from screenshot import take_screenshot
from broadcaster import broadcast_file


def main():
    
    file_path = take_screenshot()

    if file_path:
        broadcast_file(file_path)


if __name__ == "__main__":
    main()