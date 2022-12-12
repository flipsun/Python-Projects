
import sqlite3

conn = sqlite3.connect('filescript.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        col_filename TEXT)")
    conn.commit()

conn = sqlite3.connect('filescript.db')

# Tuple list of file names
fileList = ('information.docx','Hello.txt', 'myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

# Loop through each object in list to find files that end in .txt
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            # Value for each row will be one file name out of the list
            # Therefore (x, ) will denote a one element tuple/list for each file name
            # ending with .txt.
            cur.execute("INSERT INTO tbl_files (col_filename) VALUES (?)", (x,))
            print(x)
