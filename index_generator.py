#! /usr/bin/env python3
"""Process directory or list
"""

from os import scandir
from os.path import exists, splitext
from bread_crumbs import HTML_FOOTER, HTML_HEADER, ignore_items, TITLES_TXT
from generate_table_row import generate_table_row


def process_directory():
    """Process the current directory
    """
    dir_list = []
    file_list = []

    with scandir() as dir_item:
        for entry in dir_item:
            if not entry.name.startswith('.') and entry.name not in ignore_items:
                if entry.is_dir():
                    dir_list.append(entry.name)
                if entry.is_file():
                    file_list.append(entry.name)

    dir_list = sorted(dir_list)
    for item in dir_list:
        generate_table_row(item, f'{item} /')

    file_list = sorted(file_list)
    for item in file_list:
        item_basename, item_type = splitext(item)
        generate_table_row(f'{item_basename}{item_type}', item_basename)


def process_list(titles_txt):
    """Argument: name of text file with urls and subjects
    """

    colon_pos = 0
    line = ''
    lines = ['']

    with open(titles_txt, encoding="ascii" errors='ignore') as f_handle:
        lines = f_handle.readlines()
    for line in lines:
        colon_pos = line.find(':')
        filename = line[:colon_pos]
        subject = line[colon_pos + 1:].strip()
        generate_table_row(filename, subject)


if __name__ == '__main__':
    print(f'{HTML_HEADER}')
    if exists(TITLES_TXT):
        process_list(TITLES_TXT)
    else:
        process_directory()
    print(f'{HTML_FOOTER}')
