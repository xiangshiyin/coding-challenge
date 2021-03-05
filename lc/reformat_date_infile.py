import re
import datetime

def read_large_file(file_object):
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data

def process_file(path_in, path_out):
    out_p = open(path_out, 'w')
    try:
        with open(path_in) as fp:
            index = 0
            for line in read_large_file(fp):
                if index>0:
                    ## split the line
                    splitted = re.split(',(?=")', line)
                    ## format the date string
                    date = splitted[0].strip('"')
                    date2 = '"{}"'.format(str(datetime.datetime.strptime(date, '%B %d, %Y')).split()[0]) 
                    splitted[0] = date2
                    ## output
                    # print()
                    out_p.write(','.join(splitted))
                else:
                    out_p.write(line)
                index += 1
    except (IOError, OSError):
        print("Error handling the file")

if __name__ == '__main__':
    path_in = 'abc'
    path_out = 'def'
    process_file(path_in, path_out)
