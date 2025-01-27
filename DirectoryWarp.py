#!/usr/bin/env python3
import os
import sys

BOOKMARKS_FILE = os.path.expanduser("~/.directory_warp")

def warp(key):
    bookmarks = load_bookmarks()
    if key in bookmarks:
        target = bookmarks[key]
        if os.path.exists(target):
            print(target)
        else:
            print(f"Directory {target} no longer exists. Removing bookmark.")
            del bookmarks[key]
            save_bookmarks(bookmarks)
    else:
        print(f"Directory {key} not found.")


def load_bookmarks():
    bookmarks = {}
    if os.path.exists(BOOKMARKS_FILE):
        with open(BOOKMARKS_FILE, "r") as f:
            for line in f:
                bookmark = line.strip().split(" ", 1)
                if len(bookmark) == 2:
                    bookmarks[bookmark[0]] = bookmark[1]
    return bookmarks

def save_bookmarks(bookmarks):
    with open(BOOKMARKS_FILE, "w") as f:
        for bookmark, path in bookmarks.items():
            f.write(f"{bookmark} {path}\n")

def set_directory(directory):
    bookmarks = load_bookmarks()
    bookmarks[directory] = os.getcwd()
    save_bookmarks(bookmarks)
    print(f"Directory saved: {directory} -> {os.getcwd()}")

def list_directories():
    bookmarks = load_bookmarks()
    if bookmarks:
        for bookmark, path in bookmarks.items():
            print(f"{bookmark}: {path}")
    else:
        print("No directories saved.")

def remove_directory(directory):
    bookmarks = load_bookmarks()
    if directory in bookmarks:
        del bookmarks[directory]
        save_bookmarks(bookmarks)
        print(f"Removed directory: {directory}")
    else:
        print(f"Directory {directory} not found.")

def clear_directories():
    if os.path.exists(BOOKMARKS_FILE):
        os.remove(BOOKMARKS_FILE)
        print("All bookmarks have been cleared.")
    else:
        print("There were no directories in memory.")

def print_help():
    print("DirectoryWarp Help")
    print("Usage: dw [name] - Warps to the directory saved as [name].")
    print("dw set [name] - Saves the current directory as [name].")
    print("dw ls - Lists all saved directories.")
    print("dw rm [name] - Removes the directory saved as [name].")
    print("dw clear - Removes all saved directories.")
    print("dw help - Displays this help message.")

def main():
    if len(sys.argv) < 2:
        print("Usage: DirectoryWarp.py [command] [arguments]")
        return
    
    elif len(sys.argv) == 2:
        command = sys.argv[1]
        if command == "help":
            print_help()
        elif command == "ls":
            list_directories()
        elif command == "clear":
            clear_directories()
        else:
            warp(command)

    elif len(sys.argv) == 3:    
        command = sys.argv[1]
        if command == "set":
            set_directory(sys.argv[2])
        elif command == "rm":
            remove_directory(sys.argv[2])
        else:
            print("Invalid command. Type 'help' for a list of commands.")
            return
    else:
        print("Invalid command. Use 'dw help' for a list of commands.")
        return

if __name__ == "__main__":
    main()
