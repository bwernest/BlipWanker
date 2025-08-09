"""___Modules_______________________________________________________________"""

# Python
import numpy as np

"""___Functions_____________________________________________________________"""

def assertEqual(arg1: any, arg2: any, error_msg: str = None) -> None:
    error_msg = error_msg if error_msg is not None else f"Arguments inégaux ! <{arg1}> / <{arg2}>"
    if isinstance(arg1, np.ndarray):
        assert np.array_equal(arg1, arg2), error_msg
    else:
        assert arg1 == arg2, error_msg

def assertNotEqual(arg1: any, arg2: any) -> None:
    assert arg1 != arg2, f"Arguments égaux ! {arg1} / {arg2}"

def assertTrue(arg1: bool) -> None:
    assert arg1, f"C'est faux."

def assertFalse(arg1: bool) -> None:
    assert not arg1, f"C'est vrai."

def assertIsInstance(arg1: any, _type: type) -> None:
    assert isinstance(arg1, _type), f"Argument est de type {type(arg1)} et non de type {_type}"

def assertListEqual(arg1: any, arg2: any) -> None:
    for elem1, elem2 in zip(arg1, arg2):
        assertEqual(elem1, elem2)

def assertDictEqual(arg1: dict, arg2: dict) -> None:
    len1, len2 = len(list(arg1.keys())), len(list(arg2.keys()))
    assertEqual(len1, len2, f"Longeurs de dictionnaires différentes ! {len1} / {len2}")
    for key, value in arg1.items():
        assertEqual(arg1[key], arg2[key])

def assertIn(arg1: any, arg2: any) -> None:
    assert arg1 in arg2
