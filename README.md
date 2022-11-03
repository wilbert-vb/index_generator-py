# index_generator-py

(you need to download all *.py svripts)

This python3 solution generates index.html tables based on all items in a directory or on a text file with url and subject information.

The text file should have the following line format:

    file.html:Document for accounting
    
to generate such file in linux:

    $ grep ^Subject: *|sort - k 2 | sed '/Subject: //g' > titles.txt

Example:

##### titles.txt:

![titles.txt](https://github.com/wilbert-vb/index_generator-py/blob/main/images/titles-txt.png "titles.txt")

##### index.html:

![index.html](https://github.com/wilbert-vb/index_generator-py/blob/main/images/index-html.png "index.html")
