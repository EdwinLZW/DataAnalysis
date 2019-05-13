#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Simon Liu"

import os
import csv
import glob
from CSVFile import *


USER_FILE_PATH = user_file_path


class CsvOperationWithSimple(object):
    def __init__(self):
        self.filereadpath = USER_FILE_PATH
        self.filewritepath = None

    def read_csvfile(self):
        with open(self.filereadpath, 'r') as filereader:
            header = filereader.readline().strip()
            file_list = csv.reader(filereader, delimiter=',')
            for row in file_list:
                # print row
                if len(row) == len(header.split(',')):
                    continue
                else:
                    print "format Error :{}".format(row)

    def write_csvfile(self, msg):
        with open(self.filewritepath, 'w') as filerwriter:
            filerwriter.write(msg)

    def filter_specific_row(self):
        pass

    def scale_operate_file(self):
        first_file = True
        for destfile in glob.glob(os.path.join(file_dir, 'user*')):
            with open(destfile, 'r') as csv_read_file:
                with open(output_file, 'a') as csv_write_file:
                    filereader = csv.reader(csv_read_file)
                    filewriter = csv.writer(csv_write_file)
                    if first_file:
                        for row in filereader:
                            if len(row) == 0:
                                continue
                            filewriter.writerow(row)
                            first_file = False
                    else:
                        header = next(filereader, None)
                        for row in filereader:
                            if len(row) == 0:
                                continue
                            filewriter.writerow(row)


if __name__ == '__main__':
    csvop = CsvOperationWithSimple()
    csvop.scale_operate_file()