import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_materialproviders.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptography_primitives.internaldafny.generated.ExternRandom as ExternRandom
import aws_cryptography_primitives.internaldafny.generated.Random as Random
import aws_cryptography_primitives.internaldafny.generated.AESEncryption as AESEncryption
import aws_cryptography_primitives.internaldafny.generated.ExternDigest as ExternDigest
import aws_cryptography_primitives.internaldafny.generated.Digest as Digest
import aws_cryptography_primitives.internaldafny.generated.HMAC as HMAC
import aws_cryptography_primitives.internaldafny.generated.WrappedHMAC as WrappedHMAC
import aws_cryptography_primitives.internaldafny.generated.HKDF as HKDF
import aws_cryptography_primitives.internaldafny.generated.WrappedHKDF as WrappedHKDF
import aws_cryptography_primitives.internaldafny.generated.Signature as Signature
import aws_cryptography_primitives.internaldafny.generated.KdfCtr as KdfCtr
import aws_cryptography_primitives.internaldafny.generated.RSAEncryption as RSAEncryption
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
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
import standard_library.internaldafny.generated.UUID as UUID
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
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_materialproviders.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws as Com_Amazonaws
import com_amazonaws_dynamodb.internaldafny.generated.Com as Com
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography_Primitives as Aws_Cryptography_Primitives
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography as Aws_Cryptography
import aws_cryptography_primitives.internaldafny.generated.Aws as Aws
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC

# Module: aws_cryptographic_materialproviders.internaldafny.generated.StormTracker

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DefaultStorm():
        return AwsCryptographyMaterialProvidersTypes.StormTrackingCache_StormTrackingCache(1000, Wrappers.Option_Some(1), 10, 1, 20, 20, 20)


class CacheState:
    @classmethod
    def default(cls, ):
        return lambda: CacheState_EmptyWait()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_EmptyWait(self) -> bool:
        return isinstance(self, CacheState_EmptyWait)
    @property
    def is_EmptyFetch(self) -> bool:
        return isinstance(self, CacheState_EmptyFetch)
    @property
    def is_Full(self) -> bool:
        return isinstance(self, CacheState_Full)

class CacheState_EmptyWait(CacheState, NamedTuple('EmptyWait', [])):
    def __dafnystr__(self) -> str:
        return f'StormTracker.CacheState.EmptyWait'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CacheState_EmptyWait)
    def __hash__(self) -> int:
        return super().__hash__()

class CacheState_EmptyFetch(CacheState, NamedTuple('EmptyFetch', [])):
    def __dafnystr__(self) -> str:
        return f'StormTracker.CacheState.EmptyFetch'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CacheState_EmptyFetch)
    def __hash__(self) -> int:
        return super().__hash__()

class CacheState_Full(CacheState, NamedTuple('Full', [('data', Any)])):
    def __dafnystr__(self) -> str:
        return f'StormTracker.CacheState.Full({_dafny.string_of(self.data)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CacheState_Full) and self.data == __o.data
    def __hash__(self) -> int:
        return super().__hash__()


class StormTracker:
    def  __init__(self):
        self.wrapped: LocalCMC.LocalCMC = None
        self.inFlight: DafnyLibraries.MutableMap = None
        self.gracePeriod: int = None
        self.graceInterval: int = None
        self.fanOut: int = None
        self.inFlightTTL: int = None
        self.lastPrune: int = None
        self.sleepMilli: int = None
        pass

    def __dafnystr__(self) -> str:
        return "StormTracker.StormTracker"
    def ctor__(self, cache):
        nw31_ = LocalCMC.LocalCMC()
        nw31_.ctor__((cache).entryCapacity, ((cache).entryPruningTailSize).UnwrapOr(1))
        (self).wrapped = nw31_
        nw32_ = DafnyLibraries.MutableMap()
        (self).inFlight = nw32_
        (self).gracePeriod = (cache).gracePeriod
        (self).graceInterval = (cache).graceInterval
        (self).fanOut = (cache).fanOut
        (self).inFlightTTL = (cache).inFlightTTL
        (self).sleepMilli = (cache).sleepMilli
        (self).lastPrune = 0

    def InFlightSize(self):
        d_798_x_ = (self.inFlight).Size()
        if (d_798_x_) <= (StandardLibrary_UInt.default__.INT64__MAX__LIMIT):
            return d_798_x_
        elif True:
            return StandardLibrary_UInt.default__.INT64__MAX__LIMIT

    def FanOutReached(self, now):
        res: bool = False
        (self).PruneInFlight(now)
        res = (self.fanOut) <= ((self).InFlightSize())
        return res
        return res

    def AddLong(self, x, y):
        if (x) < ((StandardLibrary_UInt.default__.INT64__MAX__LIMIT) - (y)):
            return (x) + (y)
        elif True:
            return StandardLibrary_UInt.default__.INT64__MAX__LIMIT

    def CheckInFlight(self, identifier, result, now):
        output: CacheState = CacheState.default()()
        d_799_fanOutReached_: bool
        out129_: bool
        out129_ = (self).FanOutReached(now)
        d_799_fanOutReached_ = out129_
        if d_799_fanOutReached_:
            output = CacheState_Full(result)
            return output
        elif ((result).expiryTime) <= (now):
            out130_: CacheState
            out130_ = (self).CheckNewEntry(identifier, now)
            output = out130_
        elif (now) < (((result).expiryTime) - (self.gracePeriod)):
            output = CacheState_Full(result)
            return output
        elif True:
            if (self.inFlight).HasKey(identifier):
                d_800_entry_: int
                d_800_entry_ = (self.inFlight).Select(identifier)
                if ((self).AddLong(d_800_entry_, self.graceInterval)) > (now):
                    output = CacheState_Full(result)
                    return output
            (self.inFlight).Put(identifier, now)
            output = CacheState_EmptyFetch()
            return output
        return output

    def PruneInFlight(self, now):
        if (self.fanOut) > ((self).InFlightSize()):
            return
        if (self.lastPrune) == (now):
            return
        (self).lastPrune = now
        d_801_keySet_: _dafny.Set
        d_801_keySet_ = (self.inFlight).Keys()
        d_802_keys_: _dafny.Seq
        d_802_keys_ = SortedSets.default__.SetToSequence(d_801_keySet_)
        hi7_ = len(d_802_keys_)
        for d_803_i_ in range(0, hi7_):
            d_804_v_: int
            d_804_v_ = (self.inFlight).Select((d_802_keys_)[d_803_i_])
            if (now) >= ((self).AddLong(d_804_v_, self.inFlightTTL)):
                (self.inFlight).Remove((d_802_keys_)[d_803_i_])

    def CheckNewEntry(self, identifier, now):
        output: CacheState = CacheState.default()()
        d_805_fanOutReached_: bool
        out131_: bool
        out131_ = (self).FanOutReached(now)
        d_805_fanOutReached_ = out131_
        if d_805_fanOutReached_:
            output = CacheState_EmptyWait()
            return output
        elif (self.inFlight).HasKey(identifier):
            d_806_entry_: int
            d_806_entry_ = (self.inFlight).Select(identifier)
            if ((self).AddLong(d_806_entry_, self.graceInterval)) > (now):
                output = CacheState_EmptyWait()
                return output
        (self.inFlight).Put(identifier, now)
        output = CacheState_EmptyFetch()
        return output
        return output

    def GetFromCacheWithTime(self, input, now):
        output: Wrappers.Result = Wrappers.Result.default(CacheState.default())()
        d_807_result_: Wrappers.Result
        out132_: Wrappers.Result
        out132_ = (self.wrapped).GetCacheEntryWithTime(input, now)
        d_807_result_ = out132_
        if (d_807_result_).is_Success:
            d_808_newResult_: CacheState
            out133_: CacheState
            out133_ = (self).CheckInFlight((input).identifier, (d_807_result_).value, now)
            d_808_newResult_ = out133_
            output = Wrappers.Result_Success(d_808_newResult_)
            return output
        elif ((d_807_result_).error).is_EntryDoesNotExist:
            d_809_newResult_: CacheState
            out134_: CacheState
            out134_ = (self).CheckNewEntry((input).identifier, now)
            d_809_newResult_ = out134_
            output = Wrappers.Result_Success(d_809_newResult_)
            return output
        elif True:
            output = Wrappers.Result_Failure((d_807_result_).error)
            return output
        return output

    def GetFromCache(self, input):
        output: Wrappers.Result = Wrappers.Result.default(CacheState.default())()
        d_810_now_: int
        out135_: int
        out135_ = Time.default__.CurrentRelativeTime()
        d_810_now_ = out135_
        out136_: Wrappers.Result
        out136_ = (self).GetFromCacheWithTime(input, d_810_now_)
        output = out136_
        return output

    def GetCacheEntry(self, input):
        output: Wrappers.Result = None
        d_811_result_: Wrappers.Result
        out137_: Wrappers.Result
        out137_ = (self).GetFromCache(input)
        d_811_result_ = out137_
        if (d_811_result_).is_Failure:
            output = Wrappers.Result_Failure((d_811_result_).error)
            return output
        elif ((d_811_result_).value).is_Full:
            output = Wrappers.Result_Success(((d_811_result_).value).data)
            return output
        elif True:
            output = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_EntryDoesNotExist(_dafny.Seq("Entry does not exist")))
            return output
        return output

    def PutCacheEntry(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        (self.inFlight).Remove((input).identifier)
        out138_: Wrappers.Result
        out138_ = (self.wrapped).PutCacheEntry_k(input)
        output = out138_
        return output

    def DeleteCacheEntry(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        (self.inFlight).Remove((input).identifier)
        out139_: Wrappers.Result
        out139_ = (self.wrapped).DeleteCacheEntry_k(input)
        output = out139_
        return output

    def UpdateUsageMetadata(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out140_: Wrappers.Result
        out140_ = (self.wrapped).UpdateUsageMetadata_k(input)
        output = out140_
        return output

