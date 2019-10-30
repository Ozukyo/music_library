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
        if genre.lower() == album[3].lower():
            albums_with_genre.append(album)
    return albums_with_genre


def find_name_artist(albums):
    artist = input("Which artist album(s) are you looking for?: ")
    albums_with_artist = []
    for album in albums:
        if artist.lower() == album[0].lower():
            albums_with_artist.append(album)
    return albums_with_artist


def find_album(albums):
    album_name = input("What album are you looking for?: ")
    albums_with_album_name = []
    for album in albums:
        if album_name.lower() == album[1].lower():
            albums_with_album_name.append(album)
    return albums_with_album_name

def get_time_float_input():
    minutes = int(input("minutes: "))
    seconds = int(input("seconds: "))

    seconds_and_minutes = minutes + seconds/100
    return seconds_and_minutes

def convert_float_to_time_string(time_float):
    time_float_in_string = str(time_float)
    time_string = time_float_in_string.replace(".", ":")
    return time_string

def get_album_time_float(album):
    album_time_string = album[4]
    album_time_string_with_dot = album_time_string.replace(":", ".")
    album_time_float = float(album_time_string_with_dot)
    return album_time_float

def album_by_time_range(albums):
    print("Enter time range:")
    print("from")
    from_time = get_time_float_input()
    print("to")
    to_time = get_time_float_input()

    albums_in_time_range = []
    for album in albums:
        album_time_float = get_album_time_float(album)
        if album_time_float >= from_time and album_time_float <= to_time:
            albums_in_time_range.append(album)
    
    return albums_in_time_range

def find_longest_album(albums):
    longest_album = albums[0]

    for current_album in albums:
        current_album_time = get_album_time_float(current_album)
        longest_album_time = get_album_time_float(longest_album)

        if current_album_time > longest_album_time:
            longest_album = current_album
    
    return [longest_album]

def find_shortest_album(albums):
    shortest_album = albums[0]

    for current_album in albums:
        if get_album_time_float(current_album) < get_album_time_float(shortest_album):
            shortest_album = current_album
    
    return [shortest_album]   

def save_albums(albums, path):
    all_albums_lines = []
    for album in albums:
        joined_album = ",".join(album)
        all_albums_lines.append(joined_album)
    all_albums_string = "\n".join(all_albums_lines)
    with open (path, "w") as file:
        file.write(all_albums_string)

def add_new_album(albums, path):
    name_of_artist = input("Please enter artist name: ")
    name_of_album = input ("Please enter album name: ")
    time_of_release = input("Please enter release year: ")
    genre_of_music = input("Please enter genre: ")
    print("\nEnter album duration: ")
    time_of_album = convert_float_to_time_string(get_time_float_input())

    new_album_list = [name_of_artist, name_of_album, time_of_release, genre_of_music, time_of_album]
    albums.append(new_album_list)

    save_albums(albums, path)

    

def main():
    path = "text_albums_data.txt"
    result = []
    is_running = True
    while is_running:
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
        elif choice =="6":
            result = find_shortest_album(albums)
        elif choice =="7":
            result = find_longest_album(albums)
        elif choice == "8":
            add_new_album(albums, path)
        elif choice =="0":
            is_running = False
        else:
            print("No such choice")
    
        
    
main()