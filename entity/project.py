class Project:
    def __init__(self, id=None, name=None, description=None, start_date=None, status=None):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__start_date = start_date
        self.__status = status

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_start_date(self):
        return self.__start_date

    def set_start_date(self, start_date):
        self.__start_date = start_date

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status
