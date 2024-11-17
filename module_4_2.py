def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()  # Ничего не напечатает, нужно вызвать tets_function.

inner_function()      # Ошибка: Имя 'inner_function' не определено, потому что, отсюда её не видно.