from collections import Counter


def name(data_person):
    data_name = []
    for x in data_person:
        data_name.append(x.user_name)
    return data_name


def surname(data_person):
    data_surname = []
    for x in data_person:
        data_surname.append(x.user_surname)
    return data_surname


def worth(data_person):
    data_worth = []
    for x in data_person:
        data_worth.append(x.net_worth)
    return data_worth


def technology(data_person):
    global t
    tech = []
    for x in data_person:
        tech.append(x.industry)
        t = dict(Counter(tech).most_common(5))
    return t


def country(data_person):
    global c
    cnt = []
    for x in data_person:
        cnt.append(x.country)
        c = dict(Counter(cnt).most_common(5))
    return c







