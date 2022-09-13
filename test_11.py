import pytest

Days = dict()
Days['Понедельник'] = 1
Days['Вторник'] = 2
Days['Среда'] = 3
Days['Четверг'] = 4
Days['Пятница'] = 5
Days['Суббота'] = 6
Days['Воскресенье'] = 7

def test_dict_1():
    assert 'Среда' in Days

def test_dict_2():
    assert 'Среда' == 'Пятница' in Days


@pytest.mark.parametrize("input1, input2, output" ,[(2 ,4 ,8) ,(12 ,2 ,24)])
def test_int_1(input1, input2, output):
    assert input1 * input2 == output, "failed"

def test_int_2():
    assert 0 / 10


def test_int_3():
    x = 9
    y = 10
    assert x + 1 == y, 'test passed'
