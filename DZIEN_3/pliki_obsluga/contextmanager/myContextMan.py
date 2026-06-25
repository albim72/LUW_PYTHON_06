class MyFileManager:
    def __init__(self,filename,mode,encoding='utf-8'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = None
    def __enter__(self):
        print('otwieram plik....')
        self.file = open(self.filename,self.mode,encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('zamykam plik....')
        self.file.close()

        if exc_type is not None:
            print(f'wystąpił błąd : {exc_type}')
        return False

with MyFileManager(filename='test.txt',mode='r',encoding='utf-8') as file:
    print(file.read())

print(file.closed)
