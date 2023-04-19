import logging
import os
import random
import traceback


class HelperLib:
    """
    Helper lib Class
    """

    API_KEY = os.environ.get("API_KEY")

    @staticmethod
    def get_some_int() -> int:
        """
        Make pep happy

        :return:  int
        """
        return random.randint(0, 10)
