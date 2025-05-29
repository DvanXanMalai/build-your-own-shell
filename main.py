import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        command = input()

        # exit funciton
        if command == "exit 0":
            sys.exit(0)

        # echo function
        elif command.startswith("echo "):
            echo_text = command.split("echo ")
            if len(echo_text) > 1:
                print(echo_text[1])
            else:
                print("")
            # sys.stdout.write("$ ")

        # type function
        elif command.startswith("type "):
            type_text = command.split("type ")
            if len(type_text) > 1:
                if type_text[1] in ("exit", "echo", "type"):
                    print(type_text[1], "is a shell builtin")
                else:
                    print(f"{type_text[1]}: not found")
            # sys.exit(0)
            else:
                # Handle "type" with no arguments
                print("type: usage: type command_name")
        else:
            print(f"{command}: command not found")

    # Wait for user input


if __name__ == "__main__":
    main()
