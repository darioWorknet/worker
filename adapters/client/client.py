import logging
from pathlib import Path


logger = logging.getLogger('main_logger')


class DataClient:

    def get_info(self) -> list[str]:
        """
        Opens ./data folder. Reads all *.txt files.
        Appends each line of the files to an array.

        :returns: A list of strings with every line in folder files.
        """
        logger.debug("Reading files from folder /data")

        str_list = []

        for file in Path('./data').glob('*.txt'):
            with open(file) as f:
                for line in f:
                    str_list.append(line.strip())

        return str_list
