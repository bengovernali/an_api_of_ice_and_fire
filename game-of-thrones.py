from characters import characters
from pprint import pprint
from houses import houses
#print(len(characters))
# jon_snow = {"url":"https://anapioficeandfire.com/api/characters/583","name":"Jon Snow","gender":"Male","culture":"Northmen","born":"In 283 AC","died":"","titles":["Lord Commander of the Night's Watch"],"aliases":["Lord Snow","Ned Stark's Bastard","The Snow of Winterfell","The Crow-Come-Over","The 998th Lord Commander of the Night's Watch","The Bastard of Winterfell","The Black Bastard of the Wall","Lord Crow"],"father":"","mother":"","spouse":"","allegiances":["https://anapioficeandfire.com/api/houses/362"],"books":["https://anapioficeandfire.com/api/books/5"],"povBooks":["https://anapioficeandfire.com/api/books/1","https://anapioficeandfire.com/api/books/2","https://anapioficeandfire.com/api/books/3","https://anapioficeandfire.com/api/books/8"],"tvSeries":["Season 1","Season 2","Season 3","Season 4","Season 5","Season 6"],"playedBy":["Kit Harington"]}

# # print out the key names individually
# # for k in jon_snow:
# #     print(k)

# # print out just the values
# # for k in jon_snow:
# #     print(jon_snow[k])

# # print both the key and the value
# for k in jon_snow:
#     print("%s: %s" % (k, jon_snow[k]))

"""
def starts_with_A(characters):
    count = 0
    for character in characters:
        if character['name'][0] == 'A':
            count += 1
    return count

print(starts_with_A(characters)) 
"""
"""
def starts_with_Z(characters):
    count = 0
    for character in characters:
        if character['name'][0] == 'Z':
            count += 1
    return count

print(starts_with_Z(characters))
"""
"""
def is_dead(characters):
    count = 0
    for character in characters:
        if character['died'] != "":
            count += 1
    return count

print(is_dead(characters))
"""
"""
def most_titles(characters):
    title_count = 0
    name = ''
    for character in characters:
        if len(character['titles']) > title_count:
            title_count = len(character['titles'])
            name = character['name']
    return "%s has the most titles with %d titles" % (name, title_count)

print(most_titles(characters))
"""
"""
def is_valyrian(characters):
    count = 0
    for character in characters:
        if character['culture'] == 'Valyrian':
            count += 1
    return "There are %d Valyrians" % count

print(is_valyrian(characters))
"""
"""
def is_hot_pie(characters):
    actor = ''
    for character in characters:
        if character['name'] == 'Hot Pie':
            actor = character['playedBy']
    return '%s plays Hot Pie' % actor

print(is_hot_pie(characters))
"""
"""
def not_in_show(characters):
    count = 0
    for character in characters:
        if character['tvSeries'] == [""]:
            count += 1
    return "There are %d characters not in the tv series" % count

print(not_in_show(characters))
"""
"""
def amount_of_targaryen(characters):
    count = 0
    for character in characters:
        name = character["name"].split()
        if "Targaryen" in name:
            count += 1
    return "There are %d Targaryens" % count

print(amount_of_targaryen(characters))
"""
def allegiance_histogram(characters):
    houses_dict = {}
    for character in characters:
        if character["allegiances"]:
            for allegiance in character["allegiances"]:
                name = houses[allegiance]
                if name not in houses_dict:
                    houses_dict[name] = 1
                else:
                    houses_dict[name] += 1
    return houses_dict

pprint(allegiance_histogram(characters))

