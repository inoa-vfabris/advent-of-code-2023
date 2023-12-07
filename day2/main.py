import re
#first part
with open("input.txt") as doc:
    lines = doc.readlines()
    limits = {"red": 12,"green": 13,"blue": 14}
    minimum_set = {}
    multiplication_list = []
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
    id_sum=sum(games_list)
    print("Sum of IDs:", id_sum)

#second part
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
                if color in minimum_set:
                    if minimum_set[color] < number:
                        minimum_set[color] = number
                else:
                    minimum_set[color] = number
                if limits[color] > number and game_id in games_list:
                        games_list.remove(game_id)
        multiplication = 1
        for number in minimum_set.values():
            multiplication = multiplication * number
        minimum_set = {}
        multiplication_list.append(multiplication)
    sum = sum(multiplication_list)
    print("Sum of minimim set power:",sum)