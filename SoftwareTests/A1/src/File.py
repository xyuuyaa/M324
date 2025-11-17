class File:
    def create_file(filename: str):
        with open(filename, 'w') as f:
            pass

    def write_to_file(filename: str, text: str):
        with open(filename, 'w') as f:
            f.write(text)

    def read_from_file(filename: str):
        try:
            with open(filename, 'r') as f:
                print(f.read())
        except FileNotFoundError:
            print(f"Error: '{filename}' does not exist.")