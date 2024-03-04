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
import Base64
import AlgorithmSuites
import Materials
import Keyring
import Relations
import Seq_MergeSort
import Math
import Seq
import MultiKeyring
import AwsArnParsing
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
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_keystore_internaldafny
import AesKdfCtr
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import FileIO
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
import StandardLibraryInterop
import Streams
import Sorting
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64Lemmas
import MplManifestOptions
import AllAlgorithmSuites
import software_amazon_cryptography_materialproviders_internaldafny_wrapped
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types
import JSON_Utils_Views_Core
import JSON_Utils_Views_Writers
import JSON_Utils_Views
import JSON_Utils_Lexers_Core
import JSON_Utils_Lexers_Strings
import JSON_Utils_Lexers
import JSON_Utils_Cursors
import JSON_Utils_Parsers
import JSON_Utils_Str_CharStrConversion
import JSON_Utils_Str_CharStrEscaping
import JSON_Utils_Str
import JSON_Utils_Seq
import JSON_Utils_Vectors
import JSON_Utils
import JSON_Errors
import JSON_Values
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
import KeyDescription
import KeyMaterial
import CreateStaticKeyrings
import CreateStaticKeyStores
import KeyringFromKeyDescription
import CmmFromKeyDescription
import KeysVectorOperations
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny
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

# Module: CompleteVectors

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def WriteStuff(op):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_877_tests_: _dafny.Seq
        d_877_tests_ = SortedSets.default__.SetToSequence(default__.AllPositiveKeyringTests)
        d_878_testsJSON_: _dafny.Seq
        d_878_testsJSON_ = _dafny.Seq([])
        hi1_ = len(d_877_tests_)
        for d_879_i_ in range(0, hi1_):
            d_880_name_: _dafny.Seq
            d_881_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            out57_: Wrappers.Result
            out57_ = UUID.default__.GenerateUUID()
            d_881_valueOrError0_ = out57_
            if (d_881_valueOrError0_).IsFailure():
                output = (d_881_valueOrError0_).PropagateFailure()
                return output
            d_880_name_ = (d_881_valueOrError0_).Extract()
            d_882_test_: JSON_Values.JSON
            d_883_valueOrError1_: Wrappers.Result = Wrappers.Result.default(JSON_Values.JSON.default())()
            d_883_valueOrError1_ = WriteJsonManifests.default__.EncryptTestVectorToJson((d_877_tests_)[d_879_i_])
            if (d_883_valueOrError1_).IsFailure():
                output = (d_883_valueOrError1_).PropagateFailure()
                return output
            d_882_test_ = (d_883_valueOrError1_).Extract()
            d_878_testsJSON_ = (d_878_testsJSON_) + (_dafny.Seq([(d_880_name_, d_882_test_)]))
        d_884_mplEncryptManifest_: JSON_Values.JSON
        d_884_mplEncryptManifest_ = JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("manifest"), JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("version"), JSON_Values.JSON_Number(JSON_Values.default__.Int(4))), (_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("awses-mpl-encrypt")))]))), (_dafny.Seq("keys"), JSON_Values.JSON_String(_dafny.Seq("file://keys.json"))), (_dafny.Seq("tests"), JSON_Values.JSON_Object(d_878_testsJSON_))]))
        d_885_mplEncryptManifestBytes_: _dafny.Seq
        d_886_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda100_(d_887_e_):
            return (d_887_e_).ToString()

        d_886_valueOrError2_ = (JSON_API.default__.Serialize(d_884_mplEncryptManifest_)).MapFailure(lambda100_)
        if (d_886_valueOrError2_).IsFailure():
            output = (d_886_valueOrError2_).PropagateFailure()
            return output
        d_885_mplEncryptManifestBytes_ = (d_886_valueOrError2_).Extract()
        d_888___v0_: tuple
        d_889_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out58_: Wrappers.Result
        out58_ = default__.WriteVectorsFile(((op).encryptManifestOutput) + (_dafny.Seq("manifest.json")), d_885_mplEncryptManifestBytes_)
        d_889_valueOrError3_ = out58_
        if (d_889_valueOrError3_).IsFailure():
            output = (d_889_valueOrError3_).PropagateFailure()
            return output
        d_888___v0_ = (d_889_valueOrError3_).Extract()
        output = Wrappers.Result_Success(())
        return output

    @staticmethod
    def WriteDecryptManifest(op, keys, tests):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_890_testsJSON_: _dafny.Seq
        d_890_testsJSON_ = _dafny.Seq([])
        hi2_ = len(tests)
        for d_891_i_ in range(0, hi2_):
            d_892_name_: _dafny.Seq
            d_893_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            out59_: Wrappers.Result
            out59_ = UUID.default__.GenerateUUID()
            d_893_valueOrError0_ = out59_
            if (d_893_valueOrError0_).IsFailure():
                output = (d_893_valueOrError0_).PropagateFailure()
                return output
            d_892_name_ = (d_893_valueOrError0_).Extract()
            d_894_test_: JSON_Values.JSON
            d_895_valueOrError1_: Wrappers.Result = Wrappers.Result.default(JSON_Values.JSON.default())()
            d_895_valueOrError1_ = WriteJsonManifests.default__.DecryptTestVectorToJson((tests)[d_891_i_])
            if (d_895_valueOrError1_).IsFailure():
                output = (d_895_valueOrError1_).PropagateFailure()
                return output
            d_894_test_ = (d_895_valueOrError1_).Extract()
            d_890_testsJSON_ = (d_890_testsJSON_) + (_dafny.Seq([(d_892_name_, d_894_test_)]))
        d_896_mplDecryptManifest_: JSON_Values.JSON
        d_896_mplDecryptManifest_ = JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("manifest"), JSON_Values.JSON_Object(_dafny.Seq([(_dafny.Seq("version"), JSON_Values.JSON_Number(JSON_Values.default__.Int(4))), (_dafny.Seq("type"), JSON_Values.JSON_String(_dafny.Seq("awses-mpl-decrypt")))]))), (_dafny.Seq("client"), JSON_Values.JSON_String(_dafny.Seq("mpl-dafny"))), (_dafny.Seq("keys"), JSON_Values.JSON_String(_dafny.Seq("file://keys.json"))), (_dafny.Seq("tests"), JSON_Values.JSON_Object(d_890_testsJSON_))]))
        d_897_mplDecryptManifestBytes_: _dafny.Seq
        d_898_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda101_(d_899_e_):
            return (d_899_e_).ToString()

        d_898_valueOrError2_ = (JSON_API.default__.Serialize(d_896_mplDecryptManifest_)).MapFailure(lambda101_)
        if (d_898_valueOrError2_).IsFailure():
            output = (d_898_valueOrError2_).PropagateFailure()
            return output
        d_897_mplDecryptManifestBytes_ = (d_898_valueOrError2_).Extract()
        d_900___v1_: tuple
        d_901_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out60_: Wrappers.Result
        out60_ = default__.WriteVectorsFile(((op).decryptManifestOutput) + (_dafny.Seq("manifest.json")), d_897_mplDecryptManifestBytes_)
        d_901_valueOrError3_ = out60_
        if (d_901_valueOrError3_).IsFailure():
            output = (d_901_valueOrError3_).PropagateFailure()
            return output
        d_900___v1_ = (d_901_valueOrError3_).Extract()
        d_902_keysJsonFileName_: _dafny.Seq
        d_902_keysJsonFileName_ = _dafny.Seq("keys.json")
        d_903_keysJsonBytes_: _dafny.Seq
        d_904_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda102_(d_905_e_):
            return (d_905_e_).ToString()

        d_904_valueOrError4_ = (JSON_API.default__.Serialize(((keys).config).keysJson)).MapFailure(lambda102_)
        if (d_904_valueOrError4_).IsFailure():
            output = (d_904_valueOrError4_).PropagateFailure()
            return output
        d_903_keysJsonBytes_ = (d_904_valueOrError4_).Extract()
        d_906___v2_: tuple
        d_907_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out61_: Wrappers.Result
        out61_ = default__.WriteVectorsFile(((op).decryptManifestOutput) + (d_902_keysJsonFileName_), d_903_keysJsonBytes_)
        d_907_valueOrError5_ = out61_
        if (d_907_valueOrError5_).IsFailure():
            output = (d_907_valueOrError5_).PropagateFailure()
            return output
        d_906___v2_ = (d_907_valueOrError5_).Extract()
        output = Wrappers.Result_Success(())
        return output

    @staticmethod
    def WriteVectorsFile(location, bytes):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_908_bv_: _dafny.Seq
        d_908_bv_ = JSONHelpers.default__.BytesBv(bytes)
        out62_: Wrappers.Result
        out62_ = FileIO.default__.WriteBytesToFile(location, d_908_bv_)
        output = out62_
        return output

    @_dafny.classproperty
    def AllPositiveKeyringTests(instance):
        return ((((((((((_dafny.Set({})) | (AllDefaultCmm.default__.Tests)) | (AllHierarchy.default__.Tests)) | (AllKms.default__.Tests)) | (AllKmsMrkAware.default__.Tests)) | (AllKmsMrkAwareDiscovery.default__.Tests)) | (AllKmsRsa.default__.Tests)) | (AllRawAES.default__.Tests)) | (AllRawRSA.default__.Tests)) | (AllMulti.default__.Tests)) | (AllRequiredEncryptionContextCmm.default__.Tests)
