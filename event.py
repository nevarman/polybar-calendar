#!/usr/bin/env python3
import datetime
from utils import get_json_file
import os
import json
from collections import namedtuple
FILE_NAME = get_json_file()


class EventsBase():
    def __init__(self):
        self._load_events()

    def _load_events(self):
        pass

    def add_event(self, date, event):
        pass

    def remove_event(self, date, event):
        pass

    def get_events(self, date) -> list:
        pass

    def _date_to_str(self, date):
        return ','.join(str(x) for x in date)

    def _str_to_date(self, jsonstr):
        l = jsonstr.split(',')
        return tuple(l)


class LocalEvents(EventsBase):
    def _load_events(self):
        if not os.path.isfile(FILE_NAME):
            self.events: dict = {}
        else:
            with open(FILE_NAME) as file:
                j = json.load(file)
                self.events = j  # read from file or database

    def add_event(self, date, event):
        str_date = self._date_to_str(date)
        date_events = self.events.get(str_date)
        if date_events == None:
            self.events[str_date] = [event.toJson()]
        else:
            date_events.append(event.toJson())
        with open(FILE_NAME, 'w') as file:
            json.dump(self.events, file)

    def remove_event(self, date, event):
        str_date = self._date_to_str(date)
        date_events = self.events.get(str_date)
        if date_events == None:
            return
        else:
            date_events.remove(event)
        with open(FILE_NAME, 'w') as file:
            json.dump(self.events, file)

    def get_events(self, date) -> list:
        return self.events.get(self._date_to_str(date))


class Event():
    def __init__(self, time, subject, event):
        self.time = time
        self.subject = subject
        self.event = event

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @staticmethod
    def fromJson(str):
        return json.loads(str, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))


# events = Events()
# #events.add_event((2020, 6, 15), Event(("21", "35"), "subject", "subject"))
# events.remove_event((2020, 6, 15), Event(("21", "35"), "subject", "subject"))
# # # now = (datetime.datetime.now().hour)
# # # print(now)
# events.add_event((2020, 6, 13), Event(
#     (datetime.datetime.now().hour, datetime.datetime.now().minute), 'subject', 'event'))
# print(events.get_events((2020, 6, 13))[0])

# # print(json.loads(events.events.get(
# #     datetime.date.today().strftime("%d %b %Y"))[0]))
