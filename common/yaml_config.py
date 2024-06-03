# -*- coding: utf-8 -*-
import yaml

from common.tools import get_project_path, sep


class GetConf:

    def __init__(self):
        with open(
                file=get_project_path() + sep(['config', 'config.yaml'], add_sep_before=True),
                mode='r',
                encoding='utf-8') as f:
            self.conf = yaml.load(f, Loader=yaml.FullLoader)

    def get_username_password(self):
        return self.conf['user']['username'], self.conf['user']['password']

    def get_url(self):
        return self.conf['url']

    def get_user_data_dir(self):
        return self.conf['user-data-dir']


if __name__ == '__main__':
    print(GetConf().get_username_password())
