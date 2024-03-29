import sys
import prettytable
# https://stackoverflow.com/questions/19125237/a-text-table-writer-printer-for-python
# pip3 install prettytable
def print_table(albums):
    headers = ["Artist", "Album", "Release year", "Genre", "Duration"]

    table = prettytable.PrettyTable(headers)
    for album in albums:
        table.add_row(album)
    
    print(table)

def display_logo():
    print('''
   ███╗   ███╗██╗   ██╗███████╗██╗ ██████╗    ██╗     ██╗██████╗ ██████╗  █████╗ ██████╗ ██╗   ██╗
   ████╗ ████║██║   ██║██╔════╝██║██╔════╝    ██║     ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
   ██╔████╔██║██║   ██║███████╗██║██║         ██║     ██║██████╔╝██████╔╝███████║██████╔╝ ╚████╔╝ 
   ██║╚██╔╝██║██║   ██║╚════██║██║██║         ██║     ██║██╔══██╗██╔══██╗██╔══██║██╔══██╗  ╚██╔╝  
   ██║ ╚═╝ ██║╚██████╔╝███████║██║╚██████╗    ███████╗██║██████╔╝██║  ██║██║  ██║██║  ██║   ██║   
   ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝    ╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝ ''')

def display_menu():
    print("\nWelcome to the music library!")
    print("Please make a choice: \n")
    choice = input(
        "1 - to view all imported albums\n"
        "2 - to find albums by genre\n"
        "3 - to find all albums created by given artist\n"  
        "4 - to find album by given name\n" 
        "5 - to find album by time range\n"
        "6 - to find the shortest album\n"
        "7 - to find the longest album\n"
        "8 - to add new album\n"
        "0 - to exit\n\n"
        "What's your choice?:")
    return choice
    