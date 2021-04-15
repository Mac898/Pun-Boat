import requests
import re

avatar_list = open("profile_dump.txt", "r")
list_a = avatar_list.readlines()

for url in list_a:
    name_avatar = re.search("\/\d.................\/", url).group(0)
    name_avatar = name_avatar[1:19]
    print(name_avatar)
    print(url)
    r = requests.get(url)
    with open("./avatars/"+str(name_avatar)+".webp", "wb") as outfile:
        outfile.write(r.content)
