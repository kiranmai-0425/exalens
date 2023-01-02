blocks = [
    {"gym": 'false',
     "school": 'true',
     "store": "false"
     },
    {"gym": 'true',
     "school": 'false',
     "store": "false"
     },
    {"gym": 'true',
     "school": 'true',
     "store": "false"
     },
    {"gym": 'false',
     "school": 'true',
     "store": "false"
     },
    {"gym": 'true',
     "school": 'true',
     "store": "true"
     }

]

# index_count = int(input("enter index number: "))
choices = ["gym","school","store"]


def shortest_path():
    """Function helps to find the smallest and farthest index of the requirement choices """
    global blocks, choices
    data = {}

    try:
        for block in enumerate(blocks):
            temp_data = []
            for requirement in block[1]:
                if requirement in choices and block[1][requirement] == 'true':
                    if len(data) < 1:
                        data["index_short"] = block[0]+1
                        data["short_key"] = requirement
                        output_text = f" {data['index_short']} // shortest index is {data['index_short']}, at index {data['index_short']} you will find " \
                                 f" {data['short_key']}. No blocks has greater than one requirement"
                    else:
                        temp_data.append((block[0]+1, requirement))

            if len(temp_data) > 1:   # to get more than one requirement choices
                count = 0
                farthest_keys = []
                for output in temp_data:
                    count += 1
                    data["index_far"] = output[0]
                    data["far_key" + str(count)] = output[1]
                    farthest_keys.append(output[1])
                output_text = f"{data['index_far']} // optimal distance index is {data['index_far']}, at index " \
                              f"{data['index_far']} you will find  {','.join(farthest_keys)}. shortest index is " \
                              f"{data['index_short']} at index {data['index_short']} you will find {data['short_key']}"
                return output_text

        if len(data) < 1:
            output_text = f" No blocks has atleast one requirement"

        return output_text

    except Exception as e:
        print("error", str(e))
        data['message'] = "Something went wrong"

    return data


shortest_index = shortest_path()

print(shortest_index)


