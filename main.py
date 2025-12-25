if __name__ == '__main__':
    file_name = "./src/data.txt"
    with open(file_name, mode="r") as f:
        data = f.read()
        print(data)
        print("Type of data: ", type(data))