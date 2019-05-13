#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Simon Liu"

import os
import glob
import logging
import pandas as pd
from CSVFile import file_dir, user_file_path, output_file


LOG_PATH = os.path.join('/'.join(os.path.dirname(__file__).split('/')[:-2]), 'Log')


class PandasOperation(object):
    def __init__(self):
        self.filepath = user_file_path
        self.data = None

    def read_csv(self):
        try:
            data = pd.read_csv(self.filepath)
            self.data = data
            self.data = data.loc[data['NAME'].str.contains('H')].loc[data['AGE'] < 50]
        except Exception as e:
            self.logging('read_csv_fail', 'error', e)

    def write_csv(self):
        try:
            if isinstance(self.data, pd.DataFrame):
                self.data.to_csv(output_file, index=False)
        except Exception as e:
            self.logging('write_csv_fail', 'error', e)

    def logging(self, filename, flag, msg):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s \r%(filename)s [line:%(lineno)d] %(levelname)s %(message)s\r\n',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='{}/{}.log'.format(LOG_PATH, filename),
                            filemode='a')
        if flag == 'debug':
            logging.debug(msg)
        elif flag == 'error':
            logging.error(msg)
        elif flag == 'info':
            logging.info(msg)
        elif flag == 'critical':
            logging.critical(msg)
        else:
            logging.warning(msg)

    @classmethod
    def scale_operate_file(cls):
        all_data_frame = []
        for destfile in glob.glob(os.path.join(file_dir, 'user*')):
            data_frame = pd.read_csv(destfile)
            all_data_frame.append(data_frame)
        data_frame_concat = pd.concat(all_data_frame, axis=0, ignore_index=True)
        print data_frame_concat
        data_frame_concat.to_csv(output_file, index=False)


if __name__ == '__main__':
    csv = PandasOperation()
    csv.scale_operate_file()

