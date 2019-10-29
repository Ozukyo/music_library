#import display
from display import * # importuje wszystko



def read_albums(file_path):
    data = []
    with open(file_path) as file:
        lines = file.readlines()

    for line in lines:
        splitted_line = line.strip().split(",")
        data.append(splitted_line)
    return data

def find_genre(albums):
    genre = input("What genre are you looking for?: ")
    albums_with_genre = []
    for album in albums:
        if genre == album[3]:
            albums_with_genre.append(album[1])
    return albums_with_genre


def find_name_artist(albums):
    artist = input("Which artist album(s) are you looking for?: ")
    albums_with_artist = []
    for album in albums:
        if artist == album[0]:
            albums_with_artist.append(album[1])
    return albums_with_artist


def find_album(albums):
    album_name = input("What album are you looking for?: ")
    albums_with_album_name = []
    for album in albums:
        if album_name == album[1]:
            albums_with_album_name.append(album)
    return albums_with_album_name

def get_time_float():
    minutes = int(input("minutes: "))
    seconds = int(input("seconds: "))

    seconds_and_minutes = minutes + seconds/100
    return seconds_and_minutes

def album_by_time_range(albums):
    print("Enter time range:")
    print("from:")
    from_time = get_time_float()
    print("to:")
    to_time = get_time_float()

    albums_in_time_range = []
    for album in albums:
        album_time_string = album[4]
        album_time_float = float(album_time_string.replace(":", "."))
        if album_time_float >= from_time and album_time_float <= to_time:
            albums_in_time_range.append(album)
    
    return albums_in_time_range


def main():
    
    path = "text_albums_data.txt"
    result = []
    while(True):
        display_logo()
        albums = read_albums(path)
        if len(result) != 0:
            print_table(result)
        choice = display_menu()

        if choice == "1":
            result = albums
        elif choice =="2":
            result = find_genre(albums)
        elif choice =="3":
            result = find_name_artist(albums)
        elif choice =="4":
            result = find_album(albums)
        elif choice =="5":
            result = album_by_time_range(albums)
        elif choice =="0":
            break
        else:
            print("No such choice")
    
        
    
main()