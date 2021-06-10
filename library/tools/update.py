import json
import time

import requests
import yaml
import re


def get_seat(room):
    r = r'id="seat_(\d+)"><a[^>]*>(\d+)</a>'
    headers = {
        "COOKIE": "JSESSIONID=26CBF08C52553C726F7BE2491B4ACE33"
    }

    _res = requests.get("http://seatlib.hpu.edu.cn/mapBook/getSeatsByRoom?room=" + str(room) + "&date=2021-06-08",
                        headers=headers)
    # print(re.findall(r, _res.text.replace("\n", "").replace(" ", "")))
    return re.findall(r, _res.text.replace("\n", "").replace(" ", ""))


# rooms = yaml.safe_load(open("info.yaml", "r", encoding="utf-8"))
lib_info = json.load(open("info.json", "r", encoding="utf-8"))
a = {}
print(len(lib_info))
for _lib in range(len(lib_info)):
    for _floor in range(len(lib_info[_lib]["floors"])):
        for _room in range(len(lib_info[_lib]["floors"][_floor]["rooms"])):

            lib_info[_lib]["floors"][_floor]["rooms"][_room]["seats"] = {}
            res = get_seat(lib_info[_lib]["floors"][_floor]["rooms"][_room]["id"])

            for seat_id, seat in res:
                lib_info[_lib]["floors"][_floor]["rooms"][_room]["seats"][seat] = seat_id
# for room in range(len(rooms["rooms"])):
#     rooms["rooms"][room]["seats"] = {}
#     res = get_seat(rooms["rooms"][room]["id"])
#     for seat_id, seat in res:
#         rooms["rooms"][room]["seats"][seat] = seat_id

# json.dump(lib_info, open("rooms.json", "w", encoding="utf-8"), ensure_ascii=False, indent=4)
yaml.safe_dump(lib_info, open("info.yaml", "w", encoding='utf-8'), allow_unicode=True)
