
class FileDescriptor:
    """Сохраяняет все введенные пользователем данные в файл"""
    def __init__(self, file_path: str):
        self.__value = None
        if isinstance(file_path, str):
            self.__file_path = file_path

    def __in_file(self, value: object):
        with open(self.__file_path, 'a') as file:
            file.write(str(value) + '\n')

    def __get__(self, instance, owner) -> object:
        return self.__value

    def __set__(self, instance, value: object):
        self.__in_file(value)
        self.__value = value


class Test:
    att = FileDescriptor('file.txt')


test = Test()
test.att = 5
test.att = 10
test.att = 'Hello world'
test.att = True
