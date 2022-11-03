# index_generator-py
This python3 solution generates index.html tables based on all items in a directory or on a text file with url and subject information.

The text file should have the following line format:

    file.html:Document for accounting
    
to generate such file in linux:

    $ grep ^Subject: *|sort - k 2 | sed '/Subject: //g' > titles.txt

Example:

##### titles.txt:

    [titles.txt](/images/Screenshot%202022-11-03%20at%2010.31.15.png)

##### Result:

    [index.html](/images/Screenshot%202022-11-03%20at%2010.29.57.png)
