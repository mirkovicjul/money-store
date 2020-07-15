import re
from datetime import datetime

import database


def filter_none(l):
    return list(filter(lambda x: x is not None, l))


def filter_empty_lists(lists):
    return list(filter(lambda x: True if x else False, lists))[0]


def get_timestamp(date):
    try:
        datetime.fromtimestamp(int(date.string))
        return int(date.string)
    except ValueError:
        print("Ooops! Not a valid date... Try again!")


def full_date_to_timestamp(date):
    try:
        datetime_object = datetime.strptime(date.string, "%Y-%m-%d@%H:%M")
        timestamp = int(datetime.timestamp(datetime_object))
        return timestamp
    except ValueError:
        print("Ooops! Not a valid date... Try again!")


def date_to_timestamp(date):
    try:
        datetime_object = datetime.strptime(date.string, "%Y-%m-%d")
        timestamp = int(datetime.timestamp(datetime_object))
        return timestamp
    except ValueError:
        print("Ooops! Not a valid date... Try again!")


def time_to_timestamp(time):
    try:
        datetime_object = datetime.today()
        hours_minutes = time.string.split(":")
        hours = int(hours_minutes[0])
        minutes = int(hours_minutes[1])
        datetime_object = datetime_object.replace(hour=hours, minute=minutes, second=0)
        timestamp = int(datetime.timestamp(datetime_object))
        return timestamp
    except ValueError:
        print("Ooops! Not a valid date... Try again!")


def check_date(date):
    print("date entered: " + date)
    re_timestamp = re.compile("^[0-9]+$")
    re_datetime = re.compile("^[0-9]{4}-[0-9]{2}-[0-9]{2}@[0-9]{2}:[0-9]{2}$")
    re_date = re.compile("^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
    re_time = re.compile("^[0-9]{2}:[0-9]{2}$")
    return filter_empty_lists(
        [
            list(map(get_timestamp, filter_none([re_timestamp.match(date)]))),
            list(map(full_date_to_timestamp, filter_none([re_datetime.match(date)]))),
            list(map(date_to_timestamp, filter_none([re_date.match(date)]))),
            list(map(time_to_timestamp, filter_none([re_time.match(date)]))),
        ]
    )


def transact(transaction_args):
    amount = transaction_args["amount"]
    comment = transaction_args["comment"]
    date = check_date(transaction_args["date"])
    tags = transaction_args["tags"]
    params = {"amount": amount, "comment": comment, "date": date[0]}
    print(params)

    new_transaction = database.add_new_transaction(amount, comment, date[0])

    for t in tags:
        tag = database.find_tag(t)
        database.add_new_tag_by_transaction(new_transaction, tag)


def stats(stats_args):
    print(stats_args)
    print("In progress...")
