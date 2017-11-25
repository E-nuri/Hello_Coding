def played_song_list():
    myPlayList = {"RADIOHEAD" : 156,
                  "KISHORE KUMAR" : 141,
                  "THE BLACK KEYS" : 35,
                  "NEUTRAL MILK HOTEL" : 94,
                  "BECK" : 88,
                  "THE STROKES" : 61,
                  "WILCO" : 111
                  }

    for song in myPlayList:
        print(song, myPlayList[song])

    return myPlayList


def find_lowest_played_song(originalList):
    lowestPlayedSongTitle = list(originalList.keys())[0]
    lowestPlayedSongCount = list(originalList.values())[0]

    for title, count in originalList.items():
        if lowestPlayedSongCount > count:
            lowestPlayedSongCount = count
            lowestPlayedSongTitle = title

    lowestPlayedSong = {lowestPlayedSongTitle : lowestPlayedSongCount}

    return lowestPlayedSong


def selection_sort(originalList):
    sortedList = {}
    file = open('result.txt', 'w')

    for count in range(len(originalList)):
        lowestPlayedSong = find_lowest_played_song(originalList)
        sortedList = {list(lowestPlayedSong.keys())[0]:list(lowestPlayedSong.values())[0]}
        file.write(str(sortedList))
        file.write("\n")
        print(sortedList)
        del originalList[list(lowestPlayedSong.keys())[0]]

    file.close()
    if originalList.keys() is {}:
        print("ddddd")
    return True

print("========================")
print("선택정렬 전 플레이리스트")
originalList = played_song_list()

print("========================")
print("선택정렬 후 플레이리스트")
selection_sort(originalList)
