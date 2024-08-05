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
import standard_library.internaldafny.generated.DivInternals as DivInternals
import standard_library.internaldafny.generated.DivMod as DivMod
import standard_library.internaldafny.generated.Power as Power
import standard_library.internaldafny.generated.Logarithm as Logarithm
import standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.UTF8 as UTF8
import standard_library.internaldafny.generated.Time as Time
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.SortedSets as SortedSets
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64 as Base64
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import standard_library.internaldafny.generated.Actions as Actions
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import standard_library.internaldafny.generated.JSON_Utils_Views_Core as JSON_Utils_Views_Core
import standard_library.internaldafny.generated.JSON_Utils_Views_Writers as JSON_Utils_Views_Writers
import standard_library.internaldafny.generated.JSON_Utils_Views as JSON_Utils_Views
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import standard_library.internaldafny.generated.JSON_Utils_Lexers as JSON_Utils_Lexers
import standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq
import standard_library.internaldafny.generated.JSON_Utils_Vectors as JSON_Utils_Vectors
import standard_library.internaldafny.generated.JSON_Utils as JSON_Utils
import standard_library.internaldafny.generated.JSON_Errors as JSON_Errors
import standard_library.internaldafny.generated.JSON_Values as JSON_Values
import standard_library.internaldafny.generated.JSON_Spec as JSON_Spec
import standard_library.internaldafny.generated.JSON_Grammar as JSON_Grammar
import standard_library.internaldafny.generated.JSON_Serializer_ByteStrConversion as JSON_Serializer_ByteStrConversion
import standard_library.internaldafny.generated.JSON_Serializer as JSON_Serializer
import standard_library.internaldafny.generated.JSON_Deserializer_Uint16StrConversion as JSON_Deserializer_Uint16StrConversion
import standard_library.internaldafny.generated.JSON_Deserializer_ByteStrConversion as JSON_Deserializer_ByteStrConversion
import standard_library.internaldafny.generated.JSON_Deserializer as JSON_Deserializer
import standard_library.internaldafny.generated.JSON_ConcreteSyntax_Spec as JSON_ConcreteSyntax_Spec
import standard_library.internaldafny.generated.JSON_ConcreteSyntax_SpecProperties as JSON_ConcreteSyntax_SpecProperties
import standard_library.internaldafny.generated.JSON_ConcreteSyntax as JSON_ConcreteSyntax
import standard_library.internaldafny.generated.JSON_ZeroCopy_Serializer as JSON_ZeroCopy_Serializer
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Core as JSON_ZeroCopy_Deserializer_Core
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Strings as JSON_ZeroCopy_Deserializer_Strings
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Numbers as JSON_ZeroCopy_Deserializer_Numbers
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ObjectParams as JSON_ZeroCopy_Deserializer_ObjectParams

# Module: JSON_ZeroCopy_Deserializer_Objects

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Object(cs, json):
        d_758_valueOrError0_ = default__.Bracketed(cs, json)
        if (d_758_valueOrError0_).IsFailure():
            return (d_758_valueOrError0_).PropagateFailure()
        elif True:
            d_759_sp_ = (d_758_valueOrError0_).Extract()
            return Wrappers.Result_Success(d_759_sp_)

    @staticmethod
    def Open(cs):
        d_760_valueOrError0_ = (cs).AssertByte(JSON_ZeroCopy_Deserializer_ObjectParams.default__.OPEN)
        if (d_760_valueOrError0_).IsFailure():
            return (d_760_valueOrError0_).PropagateFailure()
        elif True:
            d_761_cs_ = (d_760_valueOrError0_).Extract()
            return Wrappers.Result_Success((d_761_cs_).Split())

    @staticmethod
    def Close(cs):
        d_762_valueOrError0_ = (cs).AssertByte(JSON_ZeroCopy_Deserializer_ObjectParams.default__.CLOSE)
        if (d_762_valueOrError0_).IsFailure():
            return (d_762_valueOrError0_).PropagateFailure()
        elif True:
            d_763_cs_ = (d_762_valueOrError0_).Extract()
            return Wrappers.Result_Success((d_763_cs_).Split())

    @staticmethod
    def BracketedFromParts(open, elems, close):
        d_764_sp_ = JSON_Utils_Cursors.Split_SP(JSON_Grammar.Bracketed_Bracketed((open).t, (elems).t, (close).t), (close).cs)
        return d_764_sp_

    @staticmethod
    def AppendWithSuffix(elems, elem, sep):
        d_765_suffixed_ = JSON_Grammar.Suffixed_Suffixed((elem).t, JSON_Grammar.Maybe_NonEmpty((sep).t))
        d_766_elems_k_ = JSON_Utils_Cursors.Split_SP(((elems).t) + (_dafny.Seq([d_765_suffixed_])), (sep).cs)
        return d_766_elems_k_

    @staticmethod
    def AppendLast(elems, elem, sep):
        d_767_suffixed_ = JSON_Grammar.Suffixed_Suffixed((elem).t, JSON_Grammar.Maybe_Empty())
        d_768_elems_k_ = JSON_Utils_Cursors.Split_SP(((elems).t) + (_dafny.Seq([d_767_suffixed_])), (elem).cs)
        return d_768_elems_k_

    @staticmethod
    def Elements(json, open, elems):
        while True:
            with _dafny.label():
                d_769_valueOrError0_ = JSON_ZeroCopy_Deserializer_ObjectParams.default__.Element((elems).cs, json)
                if (d_769_valueOrError0_).IsFailure():
                    return (d_769_valueOrError0_).PropagateFailure()
                elif True:
                    d_770_elem_ = (d_769_valueOrError0_).Extract()
                    if ((d_770_elem_).cs).EOF_q:
                        return Wrappers.Result_Failure(JSON_Utils_Cursors.CursorError_EOF())
                    elif True:
                        d_771_sep_ = JSON_ZeroCopy_Deserializer_Core.default__.TryStructural((d_770_elem_).cs)
                        d_772_s0_ = (((d_771_sep_).t).t).Peek()
                        if ((d_772_s0_) == (default__.SEPARATOR)) and (((((d_771_sep_).t).t).Length()) == (1)):
                            d_773_sep_ = d_771_sep_
                            d_774_elems_ = default__.AppendWithSuffix(elems, d_770_elem_, d_773_sep_)
                            in226_ = json
                            in227_ = open
                            in228_ = d_774_elems_
                            json = in226_
                            open = in227_
                            elems = in228_
                            raise _dafny.TailCall()
                        elif ((d_772_s0_) == (JSON_ZeroCopy_Deserializer_ObjectParams.default__.CLOSE)) and (((((d_771_sep_).t).t).Length()) == (1)):
                            d_775_sep_ = d_771_sep_
                            d_776_elems_k_ = default__.AppendLast(elems, d_770_elem_, d_775_sep_)
                            d_777_bracketed_ = default__.BracketedFromParts(open, d_776_elems_k_, d_775_sep_)
                            return Wrappers.Result_Success(d_777_bracketed_)
                        elif True:
                            d_778_separator_ = default__.SEPARATOR
                            d_779_pr_ = Wrappers.Result_Failure(JSON_Utils_Cursors.CursorError_ExpectingAnyByte(_dafny.Seq([JSON_ZeroCopy_Deserializer_ObjectParams.default__.CLOSE, d_778_separator_]), d_772_s0_))
                            return d_779_pr_
                break

    @staticmethod
    def Bracketed(cs, json):
        d_780_valueOrError0_ = JSON_ZeroCopy_Deserializer_Core.default__.Structural(cs, JSON_Utils_Parsers.Parser___Parser(default__.Open))
        if (d_780_valueOrError0_).IsFailure():
            return (d_780_valueOrError0_).PropagateFailure()
        elif True:
            d_781_open_ = (d_780_valueOrError0_).Extract()
            d_782_elems_ = JSON_Utils_Cursors.Split_SP(_dafny.Seq([]), (d_781_open_).cs)
            if (((d_781_open_).cs).Peek()) == (JSON_ZeroCopy_Deserializer_ObjectParams.default__.CLOSE):
                d_783_p_ = JSON_Utils_Parsers.Parser___Parser(default__.Close)
                d_784_valueOrError1_ = JSON_ZeroCopy_Deserializer_Core.default__.Structural((d_781_open_).cs, d_783_p_)
                if (d_784_valueOrError1_).IsFailure():
                    return (d_784_valueOrError1_).PropagateFailure()
                elif True:
                    d_785_close_ = (d_784_valueOrError1_).Extract()
                    return Wrappers.Result_Success(default__.BracketedFromParts(d_781_open_, d_782_elems_, d_785_close_))
            elif True:
                return default__.Elements(json, d_781_open_, d_782_elems_)

    @_dafny.classproperty
    def SpecViewOpen(instance):
        return JSON_ZeroCopy_Deserializer_Core.default__.SpecView
    @_dafny.classproperty
    def SpecViewClose(instance):
        return JSON_ZeroCopy_Deserializer_Core.default__.SpecView
    @_dafny.classproperty
    def SEPARATOR(instance):
        return ord(',')

class jopen:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_Utils_Views_Core.View__.OfBytes(_dafny.Seq([JSON_ZeroCopy_Deserializer_ObjectParams.default__.OPEN]))

class jclose:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_Utils_Views_Core.View__.OfBytes(_dafny.Seq([JSON_ZeroCopy_Deserializer_ObjectParams.default__.CLOSE]))
