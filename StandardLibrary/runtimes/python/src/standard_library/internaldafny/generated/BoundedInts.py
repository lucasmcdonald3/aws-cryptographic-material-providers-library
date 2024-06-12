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

# Module: BoundedInts

class default__:
    def  __init__(self):
        pass

    @_dafny.classproperty
    def TWO__TO__THE__8(instance):
        return 256
    @_dafny.classproperty
    def UINT8__MAX(instance):
        return 255
    @_dafny.classproperty
    def TWO__TO__THE__16(instance):
        return 65536
    @_dafny.classproperty
    def UINT16__MAX(instance):
        return 65535
    @_dafny.classproperty
    def TWO__TO__THE__32(instance):
        return 4294967296
    @_dafny.classproperty
    def UINT32__MAX(instance):
        return 4294967295
    @_dafny.classproperty
    def TWO__TO__THE__64(instance):
        return 18446744073709551616
    @_dafny.classproperty
    def UINT64__MAX(instance):
        return 18446744073709551615
    @_dafny.classproperty
    def INT8__MIN(instance):
        return -128
    @_dafny.classproperty
    def INT8__MAX(instance):
        return 127
    @_dafny.classproperty
    def INT16__MIN(instance):
        return -32768
    @_dafny.classproperty
    def INT16__MAX(instance):
        return 32767
    @_dafny.classproperty
    def INT32__MIN(instance):
        return -2147483648
    @_dafny.classproperty
    def INT32__MAX(instance):
        return 2147483647
    @_dafny.classproperty
    def INT64__MIN(instance):
        return -9223372036854775808
    @_dafny.classproperty
    def INT64__MAX(instance):
        return 9223372036854775807
    @_dafny.classproperty
    def NAT8__MAX(instance):
        return 127
    @_dafny.classproperty
    def NAT16__MAX(instance):
        return 32767
    @_dafny.classproperty
    def NAT32__MAX(instance):
        return 2147483647
    @_dafny.classproperty
    def NAT64__MAX(instance):
        return 9223372036854775807
    @_dafny.classproperty
    def TWO__TO__THE__0(instance):
        return 1
    @_dafny.classproperty
    def TWO__TO__THE__1(instance):
        return 2
    @_dafny.classproperty
    def TWO__TO__THE__2(instance):
        return 4
    @_dafny.classproperty
    def TWO__TO__THE__4(instance):
        return 16
    @_dafny.classproperty
    def TWO__TO__THE__5(instance):
        return 32
    @_dafny.classproperty
    def TWO__TO__THE__24(instance):
        return 16777216
    @_dafny.classproperty
    def TWO__TO__THE__40(instance):
        return 1099511627776
    @_dafny.classproperty
    def TWO__TO__THE__48(instance):
        return 281474976710656
    @_dafny.classproperty
    def TWO__TO__THE__56(instance):
        return 72057594037927936
    @_dafny.classproperty
    def TWO__TO__THE__128(instance):
        return 340282366920938463463374607431768211456
    @_dafny.classproperty
    def TWO__TO__THE__256(instance):
        return 115792089237316195423570985008687907853269984665640564039457584007913129639936
    @_dafny.classproperty
    def TWO__TO__THE__512(instance):
        return 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084096

class uint8:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        return True

class uint16:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        return True

class uint32:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        return True

class uint64:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        return True

class int8:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        return True

class int16:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        return True

class int32:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        return True

class int64:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        return True

class nat8:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_38_x_: int = source__
        return ((0) <= (d_38_x_)) and ((d_38_x_) < (128))

class nat16:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_39_x_: int = source__
        return ((0) <= (d_39_x_)) and ((d_39_x_) < (32768))

class nat32:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_40_x_: int = source__
        return ((0) <= (d_40_x_)) and ((d_40_x_) < (2147483648))

class nat64:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_41_x_: int = source__
        return ((0) <= (d_41_x_)) and ((d_41_x_) < (9223372036854775808))

class opt__byte:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_42_c_: int = source__
        return ((-1) <= (d_42_c_)) and ((d_42_c_) < (default__.TWO__TO__THE__8))
