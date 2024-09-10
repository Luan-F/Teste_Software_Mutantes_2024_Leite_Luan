import pytest
from pudb.debugger import Debugger

def reset_debugger():
    Debugger._current_debugger = []

def test_singleton_constructor():
    assert Debugger._current_debugger == []

    Debugger._current_debugger = [42]
    with pytest.raises(ValueError) as err:
        db = Debugger()
        db.__del__()

    assert str(err.value) == "a Debugger instance already exists"
    reset_debugger()

def test_ui_should_not_be_none():
    db = Debugger()
    assert db.ui != None
    db.__del__()
    reset_debugger()

def test_continue_at_start():
    """
    By default, continue_at_start should be False.
    """

    assert Debugger()._continue_at_start__setting == False
    reset_debugger()

    db = Debugger(_continue_at_start=False)
    assert db._continue_at_start__setting == False
    reset_debugger()

    db = Debugger(_continue_at_start=True)
    assert db._continue_at_start__setting == True
    reset_debugger()

def test_steal_output():
    assert Debugger().steal_output == False
    reset_debugger()

    db = Debugger(steal_output=False)
    assert db.steal_output == False
    reset_debugger()

    with pytest.raises(NotImplementedError) as err:
        db = Debugger(steal_output=True)
        assert db.steal_output == True
    assert str(err.value) == "output stealing"
    reset_debugger()
