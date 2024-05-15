import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import standard_library.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.Unicode as Unicode
import standard_library.internaldafny.generated.Functions as Functions
import standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import standard_library.internaldafny.generated.FileIO as FileIO
import standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import standard_library.internaldafny.generated.MulInternals as MulInternals
import standard_library.internaldafny.generated.Mul as Mul
import standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import standard_library.internaldafny.generated.ModInternals as ModInternals

# Module: standard_library.internaldafny.generated.DivInternals

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DivPos(x, d):
        d_183___accumulator_ = 0
        while True:
            with _dafny.label():
                if (x) < (0):
                    d_183___accumulator_ = (d_183___accumulator_) + (-1)
                    in30_ = (x) + (d)
                    in31_ = d
                    x = in30_
                    d = in31_
                    raise _dafny.TailCall()
                elif (x) < (d):
                    return (0) + (d_183___accumulator_)
                elif True:
                    d_183___accumulator_ = (d_183___accumulator_) + (1)
                    in32_ = (x) - (d)
                    in33_ = d
                    x = in32_
                    d = in33_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def DivRecursive(x, d):
        if (d) > (0):
            return default__.DivPos(x, d)
        elif True:
            return (-1) * (default__.DivPos(x, (-1) * (d)))

