import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == "exit 0":
            sys.exit(0)
        if command.startswith("echo "):
            echo_text = command.split("echo ")
            if len(echo_text) > 1:
                print(echo_text[1])
            # sys.exit(0)
        else:
            print(f"{command}: command not found")

    # Wait for user input


if __name__ == "__main__":
    main()
