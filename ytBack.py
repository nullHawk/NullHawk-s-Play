from ytmusicapi import YTMusic

ytmusic = YTMusic("oauth.json")

#search result
def search(name):
    l = []
    search_results = ytmusic.search(name,filter="songs")
    for i in search_results:
        if "title" in i.keys() :
            temp = []
            temp.append(i["title"])
            temp.append(i["videoId"])
            l.append(temp)

    
    return l

def get_song_detail(videoID):
    detail = ytmusic.get_song(videoId = videoID)
    microformat = detail["microformat"]["microformatDataRenderer"]
    music_detail = detail["videoDetails"]
    cleanDetail = {}
    cleanDetail['url'] = microformat["urlCanonical"]
    cleanDetail['title'] = microformat['title']
    cleanDetail['img_link'] = microformat['thumbnail']['thumbnails']
    cleanDetail['artist'] = music_detail['author']
    return cleanDetail


    

#search
print(get_song_detail(search("Yummy")[0][1]))


