#! /usr/bin/env python3

'''Define constants and variables for the entire application
'''
from os import getcwd

DATE_FORMAT = "%b %d %Y"
current_directory = getcwd()
if 'www.production' in current_directory:
    DOCUMENT_ROOT = '/srv/html/%production%/'
elif 'www.test' in current_directory:
    DOCUMENT_ROOT = '/srv/html/www.%test%/'
else:
    DOCUMENT_ROOT = current_directory

FILE_WITH_SUBJECTLINES = 'titles.txt'
ignore_items = ['.', '..', 'css', 'favicon.ico', 'images',
    'index.html', 'index-php.html', 'index.php',
    'js', 'ls-lRt', '.message', '.message.ftp.txt',
    'scripts', 'theme', FILE_WITH_SUBJECTLINES]
SERVER_NAME = 'https://%test%'
STYLE_SHEET = '/css/index-generator.css'
TITLES_TXT = 'titles.txt'


def generate_breadcrumbs(base_url):
    '''Generate bread crumbs string.
takes base url as argument
    '''
    document_root_len = len(DOCUMENT_ROOT)
    url = current_directory[document_root_len:]
    subdir = ''
    subdirs = url.split('/')

    bread_crumbs = f'<a href="{base_url}/">Home /</a>'
    for subdir in subdirs:
        if subdir:
            bread_crumbs = \
                f'{bread_crumbs}<a href="{base_url}/{subdir}/">{subdir} /</a>'
            base_url = f'{base_url}/{subdir}'
    return {'bread_crumbs': bread_crumbs, 'location': subdir}


html_vars = generate_breadcrumbs(SERVER_NAME)

HTML_FOOTER = '''</tbody>
</table>
</body>
<script>
    function searchTable() {
        var input, filter, found, table, tr, td, i, j;
        input = document.getElementById("filter");
        filter = input.value.toUpperCase();
        table = document.getElementById("indexlist");
        tr = table.getElementsByTagName("tr");
        for (i = 0; i < tr.length; i++) {
            td = tr[i].getElementsByTagName("td");
            for (j = 0; j < td.length; j++) {
                if (td[j].innerHTML.toUpperCase().indexOf(filter) > -1) {
                    found = true;
                }
            }
            if (found) {
                tr[i].style.display = "";
                found = false;
            } else {
                tr[i].style.display = "none";
            }
        }
    }
</script>
</html>'''
HTML_HEADER = f'''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="{STYLE_SHEET}" />
    <title>{html_vars['location']}</title>
  </head>
  <body>
    <div id="navbar">
    <form><input id="filter" onkeyup="searchTable()" type="search" placeholder="Type to filter..." /></form>
    {html_vars['bread_crumbs']}
    </div>
    <div id="content">
      <table id="indexlist" cellpadding="0" cellspacing="0">
        <thead>
          <tr>
            <th class="n">Name</th>
            <th class="m">Last Modified</th>
            <th class="s">Size</th>
            <th class="t">Type</th>
          </tr>
        </thead>
        <tbody>'''

if __name__ == '__main__':
    html_vars = generate_breadcrumbs(SERVER_NAME)
    print(
        f'bread_crumbs: [{html_vars["bread_crumbs"]}]\nlocation: [{html_vars["location"]}]')
