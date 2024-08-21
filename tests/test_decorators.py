from src.decorators import log


def test_log(capsys) -> None:
    @log()
    def example_sum_func(x: int, y: int) -> int:
        return x + y

    example_sum_func(1, 2)
    captured = capsys.readouterr()
    assert captured.out == 'Function example_sum_func is working. Result: 3\n'

    example_sum_func(1)
    captured = capsys.readouterr()
    assert captured.out == ('An error occurred while the function was running: '
                            'test_log.<locals>.example_sum_func() missing 1 required positional '
                            'argument: \'y\'. Input data: (1,)\n')

    @log()
    def example_sum_text(str_: str) -> str:
        return str_

    example_sum_text('text')
    captured = capsys.readouterr()
    assert captured.out == 'Function example_sum_text is working. Result: text\n'
