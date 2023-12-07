import re
with open("input.txt") as doc:
    lines = doc.readlines()
    limits = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    games_list = list(range(1, 101))
    for line in lines:
        sets = line.split(";")
        game = line.split(";")[0]
        game_id = int(re.findall(r'\d+', game)[0])
        for set in sets:
            dots = set.find(":")
            set = set[dots+1:]
            cubes = set.split(",")
            for cube in cubes:
                number = int(re.sub('[^0-9]', '', cube))
                color = re.sub('[^a-zA-Z]', '', cube)
                if limits[color] < number and game_id in games_list:
                        games_list.remove(game_id)
    id_sum=sum(map(int, games_list))
    print(id_sum)