#! /usr/bin/env python3
'''Take Filename and Subject line and generate a HTML table row
'''
from os import listdir
from os.path import getsize, getmtime, isdir, splitext
from datetime import datetime
from bread_crumbs import DATE_FORMAT, ignore_items


def get_dirsize(dir_name):
    '''Argument: dir_name
Return: Total file count of dir_name
    '''
    i = 0
    item_list = listdir(dir_name)
    for entry in item_list:
        if not entry.startswith('.') and entry not in ignore_items:
            i += 1
    return i


def sizeof_fmt(num, suffix="b"):
    """Argument: bytes, optional: char for bytes (B or b)
Returns meaningful metrics
    """
    for unit in ["", "k", "m", "g", "t", "p", "e", "z"]:
        if abs(num) < 1024.0:
            num = round(num)
            return f"{num}{unit}{suffix}"
        num /= 1024.0
    num = round(num)
    return f"{num}y{suffix}"


def generate_table_row(item_name, item_subject):
    """Arguments: file link, subject line
Returns html table row
    """
    item_date = datetime.fromtimestamp(
        getmtime(item_name)).strftime(DATE_FORMAT)
    if isdir(item_name):
        item_size = get_dirsize(item_name)
        item_type = '.dir'
    else:
        item_size = sizeof_fmt(getsize(item_name))
        item_name, item_type = splitext(item_name)
        item_name = f'{item_name}{item_type}'
    print(f'<tr class="d {item_type[1:]}">\
<td class="n"><a href="{item_name}">{item_subject}</a></td>\
<td class="m">{item_date}</td>\
<td class="s">{item_size}</td>\
<td class="t">{item_type[1:]}</td></tr>')


if __name__ == '__main__':
    generate_table_row('bread_crumbs.py', 'bread_crumbs.py')
