def log(filename=None):
    """Декоратор принимает необязательный параметр filename и записывает в файл выход функции, в  том числе ошибки.
    Если имя файла не указано, то выводит в консоль"""
    def process(func):
        """Дополнительный декоратор, принимающий на вход функцию"""
        def wrapper(*args, **kwargs) -> None:
            """Функция-обертка, в которой обрабатываются все выходные данные функции"""
            try:
                result = func(*args, **kwargs)
                text = f'Function {func.__name__} is working. Result: {result}'
            except Exception as error:
                text = (f'An error occurred while the function was running: {str(error)}. Input data: {args}, {kwargs};'
                        f' filename: {filename}')
            if filename:
                f = open(filename, 'a')
                f.write(text + '\n')
                f.close()
            else:
                print(text)
        return wrapper
    return process
