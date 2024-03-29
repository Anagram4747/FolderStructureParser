import os

def generate_file_name():
    import datetime
    now = datetime.datetime.now()
    formatted_datetime = now.strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"output_{formatted_datetime}.txt"
    return file_name

def search_folders(folder, indent, output_file):
    items = os.listdir(folder)
    items.sort(key=lambda x: os.path.isdir(os.path.join(folder, x)), reverse=True)  # フォルダを先に処理する
    for i, item in enumerate(items):
        new_indent = indent + "│   "
        if i == len(items) - 1:
            output_file.write(indent + "└── " + item + "\n")
            new_indent = indent + "    "
        else:
            output_file.write(indent + "├── " + item + "\n")
        full_path = os.path.join(folder, item)
        if os.path.isdir(full_path):
            search_folders(full_path, new_indent, output_file)

def main():
    file_name = generate_file_name()
    with open(file_name, "w") as output_file:
        print("実行ディレクトリのフォルダ階層情報を出力しています...")
        search_folders(".", "", output_file)
        print(f"フォルダ階層情報が {file_name} に保存されました。")

if __name__ == "__main__":
    main()
