data_count = int(input())
data = [input() for _ in range(data_count)]
search_data_count = int(input())
search_data = [input() for _ in range(search_data_count)]
for data_item in data:
    substring_index = 0
    for search_data_item in search_data:
        substring_index = data_item.find(search_data_item)
        if substring_index == -1:
            break
    if substring_index != -1:
        print(data_item)
