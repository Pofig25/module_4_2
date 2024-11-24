def  test_function():                                           # Создайте новую функцию test_function

    def inner_function():                                       # Создайте внутри test_function другую функцию - inner_function
        print("Я в области видимости функции test_function")    # Эта функция должна печатать значение "Я в области видимости функции test_function"

    inner_function()                                            # Вызовите функцию inner_function внутри функции test_function

# inner_function()                                              # Попробуйте вызывать inner_function вне функции test_function
                                                                # и посмотрите на результат выполнения программы
# Получаем ошибку: NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?

test_function()