from datetime import datetime, timedelta


def format_duration(seconds):
    if seconds == 0:
        return 'now'
    date_list = [int(num) for num in datetime.fromtimestamp(seconds).strftime('%y %H %M %S').split()]
    date_list[0] -= 70
    date_list.insert(1, timedelta(seconds=seconds).days - date_list[0] * 365)
    date_dict = {0: [' year', ' years'], 1: [' day', ' days'], 2: [' hour', ' hours'], 3: [' minute', ' minutes'], 4: [' second', ' seconds']}
    date_str = '-'.join([str(num) + date_dict[index][1] if num > 1 else str(num) + date_dict[index][0] for index, num in enumerate(date_list) if num > 0])
    date_str = date_str[::-1].replace('-', ' dna ', 1)
    return date_str[::-1].replace('-', ', ')


print(format_duration(15731080))
