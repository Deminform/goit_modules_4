from datetime import datetime, timedelta
import re
import time
from pathlib import Path


Path('events').mkdir(exist_ok=True)
Path('events/events.txt').touch(exist_ok=True)


def make_event():
    user_date = input('Please input a DATE in format: "YYYY-MM-DD": ')
    user_time = input('Please input the TIME in format: "HH:MM": ')
    user_notes = input('Type the EVENT NAME: ')
    save_events_to_file(user_date, user_time, user_notes)


def get_timedelta_result(string_date_time: str) -> str:
    try:
        input_date = datetime.strptime(string_date_time, "%Y-%m-%d %H:%M")
        current_date = datetime.now()
        days_delta_result = input_date - current_date
        time_delta_result = seconds_to_hh_mm_ss(days_delta_result.seconds)
        return f'{days_delta_result.days} days {time_delta_result}'
    except ValueError:
        raise ValueError("Please use a valid date and time in the format 'YYYY-MM-DD HH:MM'")


def seconds_to_hh_mm_ss(seconds: int) -> str:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}h {minutes:02}min {seconds:02}sec"


def save_events_to_file(user_date: str, user_time: str, user_notes: str):
    with open(Path('events/events.txt'), 'a') as write_file:
        write_file.write(f'{user_date}, {user_time}, {user_notes}\n')


def read_events_from_file():
    events = []
    try:
        with open(Path('events/events.txt'), 'r+') as read_file:
            for line in read_file:
                event_date, event_time, event_name = line.split(', ', maxsplit=2)
                events.append({'event_name': event_name.removesuffix('\n'), 'event_date': event_date + ' ' + event_time})
            return events
    except FileNotFoundError:
        raise ValueError('Event file not found')
    except PermissionError:
        raise ValueError('Permission denied')


def print_events(events: list):
    events_list_str = ''
    for event in events:
        line = f'For the "{event['event_name']}" there are {get_timedelta_result(event['event_date'])} left'
        if len(events_list_str) > 0:
            events_list_str += '   |   ' + line
        else:
            events_list_str += line
    print(f'\r{events_list_str}', end='')


while True:
    choice = input(f'Create an event? y/n: ').lower()
    match choice:
        case 'n':
            pass
        case 'y':
            make_event()
        case _:
            print('Invalid input')

    events_list = read_events_from_file()
    if len(events_list):
        while True:

            print_events(events_list)
            time.sleep(1)
    else:
        choice = input(f'You don`t have any events yet. Create an event? y/n: ').lower()
        match choice:
            case 'n':
                break
            case 'y':
                make_event()
            case _:
                print('Invalid input')







    # print(f'\r{datetime.now().time().strftime('%H:%M:%S')}', end='')
    # time.sleep(1)

