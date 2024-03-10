from datetime import datetime


def make_readable(seconds):
    if seconds < 0:
        return '00:00:00'

    res = seconds // 86400 * 24
    res2 = seconds % 86400

    seconds2 = datetime.fromtimestamp(res2)
    hours = res
    conv_seconds = int(seconds2.strftime("%H"))
    if len(str(conv_seconds + hours)) == 1:
        final = seconds2.strftime(f"0{conv_seconds + hours}:%M:%S")
    else:
        final = seconds2.strftime(f"{conv_seconds + hours}:%M:%S")
    return final


print(make_readable(86400))