import datetime
import traceback

from .api import User


def _logger(info):
    """
    记录日志
    :param info:
    :return: 日志格式的信息
    """
    log = f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\tERROR:\t\t\t{str(info)}\n'
    with open("seat_log.log", "a", encoding="utf-8") as f:
        f.write(log)
    return log


def get_day(days: int = 0):
    """
    返回的日期格式 %Y-%m-%d
    :param days: 距离今天的天数
    :return: 格式 %Y-%m-%d
    """
    return (datetime.datetime.now() + datetime.timedelta(days=days)).strftime("%Y-%m-%d")


def get_time(str_time: str, fix=True):
    """
    获取分钟时间
    :param fix: 获取以30分钟为分度的分钟时间
    :param str_time: 格式 %H:%M 范围: 7:30 - 22:30
    :return: int: 分钟
    """
    hour = int(str_time.split(":")[0])
    minute = int((int(str_time.split(":")[1]) // 30) * 30) if fix else int(str_time.split(":")[1])
    return minute + hour * 60


def info(user: User):
    try:
        info_json = user.get_user_info()
        if info_json["status"] == "success":
            return True, info_json["data"]
        else:
            return False, info_json["message"]
    except:
        return False, "用户信息接口错误"


def book(user: User, seat_id, start_time, end_time, date):
    """
    返回预约结果
    :param user:
    :param seat_id:
    :param start_time:
    :param end_time:
    :param date:
    :return:
    """
    try:
        book_json = user.book_seat(seat_id=seat_id, start_time=start_time, end_time=end_time, date=date)
        if book_json["status"] == "success":
            return True, book_json["data"]["onDate"], book_json["data"]["begin"], book_json["data"]["end"], \
                   book_json["data"]["location"]
        else:
            return False, book_json["message"]
    except:
        _logger(traceback.format_exc())
        return False, "请求失败，请查看接口是否变更"


def search(user: User, start_time, end_time, date, room_id):
    """
    返回座位列表
    :param user:
    :param start_time:
    :param end_time:
    :param date:
    :param room_id:
    :return:
    """
    try:
        search_json = user.search_seat(start_time, end_time, date, room_id)
        if search_json["status"]:
            return True, search_json["data"]["seats"]
        else:
            return False, "查询失败，请查看日志"
    except:
        _logger(traceback.format_exc())
        return False, "请求失败，请查看接口是否变更"


def reservation(user: User):
    """
    预约列表
    :param user:
    :return:
    """
    try:
        reservation_json = user.get_reservation()
        if reservation_json["status"] == "success":
            return True, reservation_json["data"][0]
        else:
            return True, {}
    except:
        _logger(traceback.format_exc())
        return False, "预约信息接口错误"


def layout(user: User, room_id, date=get_day()):
    """
    房间布局信息
    :param user:
    :param room_id:
    :param date:
    :return:
    """
    try:
        layout_json = user.get_room_status(room_id=room_id, date=date)
        if layout_json["status"] == "success":
            return True, layout_json["data"]["id"], layout_json["data"]["name"], layout_json["data"]["layout"]
        else:
            return True, room_id, str(room_id), {}
    except:
        _logger(traceback.format_exc())
        return False, "布局接口错误"


def violation(user: User):
    """
    违约信息
    :param user:
    :return:
    """
    try:
        violation_json = user.get_violation()
        if violation_json["status"]:
            return True, violation_json["data"]
        else:
            return True, {}
    except:
        _logger(traceback.format_exc())
        return False, "违约信息接口错误"


def library(user: User, lib_id, date=get_day()):
    """
    图书馆信息
    :param user:
    :param lib_id:
    :param date:
    :return:
    """
    try:
        library_json = user.get_lib_status(lib_id=lib_id, date=date)
        if library_json["status"] == "success":
            return True, library_json["data"]
        else:
            return True, []
    except:
        _logger(traceback.format_exc())
        return False, "馆内信息接口错误"


def history(user: User):
    """
    历史记录
    :param user:
    :return:
    """
    try:
        history_json = user.get_history()
        if history_json["status"] == "success":
            return True, history_json["data"]["reservations"]
        else:
            return True, []
    except:
        _logger(traceback.format_exc())
        return False, "历史信息接口错误"


def cancel(user: User, reserve_id=""):
    """
    取消预约
    :param user:
    :param reserve_id:
    :return:
    """
    if not reserve_id:
        try:
            res = reservation(user)
            if res[0]:
                reserve_id = res[1]["id"]
            cancel_json = user.cancel_book(reserve_id=reserve_id)
            if cancel_json["status"] == "success":
                return True, cancel_json["data"]["totalCancelled"], cancel_json["data"]["allowedCancel"]
            else:
                return False, cancel_json["message"]
        except:
            _logger(traceback.format_exc())
            return False, "取消预约失败"


def release(user: User):
    """
    释放座位
    :param user:
    :return:
    """
    try:
        release_json = user.release_seat()
        if release_json["status"] == "success":
            return True
        else:
            return False, release_json["message"]
    except:
        _logger(traceback.format_exc())
        return False, "结束预约失败"
