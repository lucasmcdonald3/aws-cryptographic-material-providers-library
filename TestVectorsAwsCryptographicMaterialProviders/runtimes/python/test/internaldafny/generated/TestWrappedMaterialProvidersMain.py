import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UTF8
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types
import JSON_Utils_Views_Core
import JSON_Utils_Views_Writers
import JSON_Utils_Views
import JSON_Utils_Lexers_Core
import JSON_Utils_Lexers_Strings
import JSON_Utils_Lexers
import JSON_Utils_Cursors
import JSON_Utils_Parsers
import GeneralInternals
import MulInternalsNonlinear
import MulInternals
import Mul
import ModInternalsNonlinear
import DivInternalsNonlinear
import ModInternals
import DivInternals
import DivMod
import Power
import Logarithm
import JSON_Utils_Str_CharStrConversion
import JSON_Utils_Str_CharStrEscaping
import JSON_Utils_Str
import JSON_Utils_Seq
import JSON_Utils_Vectors
import JSON_Utils
import JSON_Errors
import JSON_Values
import Relations
import Seq_MergeSort
import Math
import Seq
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import JSON_Spec
import JSON_Grammar
import JSON_Serializer_ByteStrConversion
import JSON_Serializer
import JSON_Deserializer_Uint16StrConversion
import JSON_Deserializer_ByteStrConversion
import JSON_Deserializer
import JSON_ConcreteSyntax_Spec
import JSON_ConcreteSyntax_SpecProperties
import JSON_ConcreteSyntax
import JSON_ZeroCopy_Serializer
import JSON_ZeroCopy_Deserializer_Core
import JSON_ZeroCopy_Deserializer_Strings
import JSON_ZeroCopy_Deserializer_Numbers
import JSON_ZeroCopy_Deserializer_ObjectParams
import JSON_ZeroCopy_Deserializer_Objects
import JSON_ZeroCopy_Deserializer_ArrayParams
import JSON_ZeroCopy_Deserializer_Arrays
import JSON_ZeroCopy_Deserializer_Constants
import JSON_ZeroCopy_Deserializer_Values
import JSON_ZeroCopy_Deserializer_API
import JSON_ZeroCopy_Deserializer
import JSON_ZeroCopy_API
import JSON_ZeroCopy
import JSON_API
import JSON
import JSONHelpers
import Base64
import KeyDescription
import HexStrings
import KeyMaterial
import CreateStaticKeyrings
import CreateStaticKeyStores
import AwsArnParsing
import KeyringFromKeyDescription
import CmmFromKeyDescription
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Actions
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Constants
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC
import WrappedHMAC
import HKDF
import WrappedHKDF
import Signature
import KdfCtr
import RSAEncryption
import AwsCryptographyPrimitivesOperations
import software_amazon_cryptography_primitives_internaldafny
import Aws_Cryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import DafnyLibraries
import Time
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import SortedSets
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import UUID
import AwsKmsHierarchicalKeyring
import AwsKmsRsaKeyring
import RawAESKeyring
import RawRSAKeyring
import CMM
import Defaults
import Commitment
import DefaultCMM
import DefaultClientSupplier
import RequiredEncryptionContextCMM
import AwsCryptographyMaterialProvidersOperations
import software_amazon_cryptography_materialproviders_internaldafny
import software_amazon_cryptography_materialproviders_internaldafny_wrapped
import KeysVectorOperations
import FileIO
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny
import MplManifestOptions
import AllAlgorithmSuites
import TestVectors
import AllHierarchy
import AllKms
import AllKmsMrkAware
import AllKmsMrkAwareDiscovery
import AllKmsRsa
import AllRawAES
import AllRawRSA
import AllDefaultCmm
import AllRequiredEncryptionContextCmm
import AllMulti
import WriteJsonManifests
import CompleteVectors
import ParseJsonManifests
import TestManifests
import WrappedMaterialProvidersMain
import AesKdfCtr
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_keystore_internaldafny
import StandardLibraryInterop
import Streams
import Sorting
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64Lemmas

# Module: TestWrappedMaterialProvidersMain

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestGenerateEncryptManifest():
        d_0_result_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = CompleteVectors.default__.WriteStuff(MplManifestOptions.ManifestOptions_EncryptManifest(_dafny.Seq("dafny/TestVectorsAwsCryptographicMaterialProviders/test/")))
        d_0_result_ = out0_
        if (d_0_result_).is_Failure:
            _dafny.print(_dafny.string_of((d_0_result_).error))
        if not((d_0_result_).is_Success):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/test/RunMain.dfy(25,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestEncryptManifest():
        d_1_result_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = TestManifests.default__.StartEncrypt(MplManifestOptions.ManifestOptions_Encrypt(_dafny.Seq("dafny/TestVectorsAwsCryptographicMaterialProviders/test/"), _dafny.Seq("dafny/TestVectorsAwsCryptographicMaterialProviders/"), Wrappers.Option_None()))
        d_1_result_ = out1_
        if (d_1_result_).is_Failure:
            _dafny.print(_dafny.string_of((d_1_result_).error))
        if not((d_1_result_).is_Success):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/test/RunMain.dfy(39,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestDecryptManifest():
        d_2_result_: Wrappers.Result
        out2_: Wrappers.Result
        out2_ = TestManifests.default__.StartDecrypt(MplManifestOptions.ManifestOptions_Decrypt(_dafny.Seq("dafny/TestVectorsAwsCryptographicMaterialProviders/"), Wrappers.Option_None()))
        d_2_result_ = out2_
        if (d_2_result_).is_Failure:
            _dafny.print(_dafny.string_of(d_2_result_))
        if not((d_2_result_).is_Success):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/test/RunMain.dfy(51,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

