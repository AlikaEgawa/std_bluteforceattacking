import pwd, string,random, zipfile

file_path = '[zipfile_path]' #enter zipfile path into [ ]

size = 4
chars = string.digits
count = 0

with zipfile.ZipFile(file_path, "r") as zf:
    for i in range(10000):
        pwd = bytes(''.join(random.choices(chars, k=size)), 'UTF-8')
        print(pwd)
        try:
            zf.extractall(path='.', pwd=pwd)
            print('success : password : {}'.format(pwd))
            break
        except Exception as e:
            count +=1

print('tried passwords : ' , count)