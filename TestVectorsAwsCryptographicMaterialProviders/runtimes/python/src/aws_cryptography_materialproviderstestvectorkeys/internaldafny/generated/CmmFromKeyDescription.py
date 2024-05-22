import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
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
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import standard_library.internaldafny.generated.Base64 as Base64
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import standard_library.internaldafny.generated.Actions as Actions
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws as Com_Amazonaws
import com_amazonaws_dynamodb.internaldafny.generated.Com as Com
import aws_cryptographic_materialproviders.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import standard_library.internaldafny.generated.Time as Time
import aws_cryptographic_materialproviders.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import standard_library.internaldafny.generated.SortedSets as SortedSets
import aws_cryptographic_materialproviders.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_materialproviders.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import standard_library.internaldafny.generated.UUID as UUID
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.CMM as CMM
import aws_cryptographic_materialproviders.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_materialproviders.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_materialproviders.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersOperations as AwsCryptographyMaterialProvidersOperations
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialProviders as MaterialProviders
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_materialproviders.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
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
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.MplManifestOptions as MplManifestOptions
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllAlgorithmSuites as AllAlgorithmSuites
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.WrappedMaterialProviders as WrappedMaterialProviders
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AwsCryptographyMaterialProvidersTestVectorKeysTypes as AwsCryptographyMaterialProvidersTestVectorKeysTypes
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
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Objects as JSON_ZeroCopy_Deserializer_Objects
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ArrayParams as JSON_ZeroCopy_Deserializer_ArrayParams
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Arrays as JSON_ZeroCopy_Deserializer_Arrays
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Constants as JSON_ZeroCopy_Deserializer_Constants
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Values as JSON_ZeroCopy_Deserializer_Values
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_API as JSON_ZeroCopy_Deserializer_API
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer as JSON_ZeroCopy_Deserializer
import standard_library.internaldafny.generated.JSON_ZeroCopy_API as JSON_ZeroCopy_API
import standard_library.internaldafny.generated.JSON_ZeroCopy as JSON_ZeroCopy
import standard_library.internaldafny.generated.JSON_API as JSON_API
import standard_library.internaldafny.generated.JSON as JSON
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.JSONHelpers as JSONHelpers
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyDescription as KeyDescription
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyMaterial as KeyMaterial
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CreateStaticKeyrings as CreateStaticKeyrings
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CreateStaticKeyStores as CreateStaticKeyStores
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyringFromKeyDescription as KeyringFromKeyDescription

# Module: aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CmmFromKeyDescription

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ToCmm(mpl, keys, description, forOperation):
        output: Wrappers.Result = None
        d_437_material_: Wrappers.Option
        d_437_material_ = KeyringFromKeyDescription.default__.GetKeyMaterial(keys, description)
        source15_ = description
        if source15_.is_Kms:
            d_438___mcc_h0_ = source15_.Kms
            if True:
                d_439_keyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
                d_440_valueOrError1_: Wrappers.Result = None
                out20_: Wrappers.Result
                out20_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_440_valueOrError1_ = out20_
                if (d_440_valueOrError1_).IsFailure():
                    output = (d_440_valueOrError1_).PropagateFailure()
                    return output
                d_439_keyring_ = (d_440_valueOrError1_).Extract()
                d_441_output_k_: Wrappers.Result
                out21_: Wrappers.Result
                out21_ = (mpl).CreateDefaultCryptographicMaterialsManager(AwsCryptographyMaterialProvidersTypes.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_439_keyring_))
                d_441_output_k_ = out21_
                def lambda32_(d_442_e_):
                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_442_e_)

                output = (d_441_output_k_).MapFailure(lambda32_)
        elif source15_.is_KmsMrk:
            d_443___mcc_h2_ = source15_.KmsMrk
            if True:
                d_444_keyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
                d_445_valueOrError1_: Wrappers.Result = None
                out22_: Wrappers.Result
                out22_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_445_valueOrError1_ = out22_
                if (d_445_valueOrError1_).IsFailure():
                    output = (d_445_valueOrError1_).PropagateFailure()
                    return output
                d_444_keyring_ = (d_445_valueOrError1_).Extract()
                d_446_output_k_: Wrappers.Result
                out23_: Wrappers.Result
                out23_ = (mpl).CreateDefaultCryptographicMaterialsManager(AwsCryptographyMaterialProvidersTypes.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_444_keyring_))
                d_446_output_k_ = out23_
                def lambda33_(d_447_e_):
                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_447_e_)

                output = (d_446_output_k_).MapFailure(lambda33_)
        elif source15_.is_KmsMrkDiscovery:
            d_448___mcc_h4_ = source15_.KmsMrkDiscovery
            if True:
                d_449_keyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
                d_450_valueOrError1_: Wrappers.Result = None
                out24_: Wrappers.Result
                out24_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_450_valueOrError1_ = out24_
                if (d_450_valueOrError1_).IsFailure():
                    output = (d_450_valueOrError1_).PropagateFailure()
                    return output
                d_449_keyring_ = (d_450_valueOrError1_).Extract()
                d_451_output_k_: Wrappers.Result
                out25_: Wrappers.Result
                out25_ = (mpl).CreateDefaultCryptographicMaterialsManager(AwsCryptographyMaterialProvidersTypes.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_449_keyring_))
                d_451_output_k_ = out25_
                def lambda34_(d_452_e_):
                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_452_e_)

                output = (d_451_output_k_).MapFailure(lambda34_)
        elif source15_.is_RSA:
            d_453___mcc_h6_ = source15_.RSA
            if True:
                d_454_keyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
                d_455_valueOrError1_: Wrappers.Result = None
                out26_: Wrappers.Result
                out26_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_455_valueOrError1_ = out26_
                if (d_455_valueOrError1_).IsFailure():
                    output = (d_455_valueOrError1_).PropagateFailure()
                    return output
                d_454_keyring_ = (d_455_valueOrError1_).Extract()
                d_456_output_k_: Wrappers.Result
                out27_: Wrappers.Result
                out27_ = (mpl).CreateDefaultCryptographicMaterialsManager(AwsCryptographyMaterialProvidersTypes.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_454_keyring_))
                d_456_output_k_ = out27_
                def lambda35_(d_457_e_):
                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_457_e_)

                output = (d_456_output_k_).MapFailure(lambda35_)
        elif source15_.is_AES:
            d_458___mcc_h8_ = source15_.AES
            if True:
                d_459_keyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
                d_460_valueOrError1_: Wrappers.Result = None
                out28_: Wrappers.Result
                out28_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_460_valueOrError1_ = out28_
                if (d_460_valueOrError1_).IsFailure():
                    output = (d_460_valueOrError1_).PropagateFailure()
                    return output
                d_459_keyring_ = (d_460_valueOrError1_).Extract()
                d_461_output_k_: Wrappers.Result
                out29_: Wrappers.Result
                out29_ = (mpl).CreateDefaultCryptographicMaterialsManager(AwsCryptographyMaterialProvidersTypes.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_459_keyring_))
                d_461_output_k_ = out29_
                def lambda36_(d_462_e_):
                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_462_e_)

                output = (d_461_output_k_).MapFailure(lambda36_)
        elif source15_.is_Static:
            d_463___mcc_h10_ = source15_.Static
            if True:
                d_464_keyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
                d_465_valueOrError1_: Wrappers.Result = None
                out30_: Wrappers.Result
                out30_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_465_valueOrError1_ = out30_
                if (d_465_valueOrError1_).IsFailure():
                    output = (d_465_valueOrError1_).PropagateFailure()
                    return output
                d_464_keyring_ = (d_465_valueOrError1_).Extract()
                d_466_output_k_: Wrappers.Result
                out31_: Wrappers.Result
                out31_ = (mpl).CreateDefaultCryptographicMaterialsManager(AwsCryptographyMaterialProvidersTypes.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_464_keyring_))
                d_466_output_k_ = out31_
                def lambda37_(d_467_e_):
                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_467_e_)

                output = (d_466_output_k_).MapFailure(lambda37_)
        elif source15_.is_KmsRsa:
            d_468___mcc_h12_ = source15_.KmsRsa
            if True:
                d_469_keyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
                d_470_valueOrError1_: Wrappers.Result = None
                out32_: Wrappers.Result
                out32_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_470_valueOrError1_ = out32_
                if (d_470_valueOrError1_).IsFailure():
                    output = (d_470_valueOrError1_).PropagateFailure()
                    return output
                d_469_keyring_ = (d_470_valueOrError1_).Extract()
                d_471_output_k_: Wrappers.Result
                out33_: Wrappers.Result
                out33_ = (mpl).CreateDefaultCryptographicMaterialsManager(AwsCryptographyMaterialProvidersTypes.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_469_keyring_))
                d_471_output_k_ = out33_
                def lambda38_(d_472_e_):
                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_472_e_)

                output = (d_471_output_k_).MapFailure(lambda38_)
        elif source15_.is_Hierarchy:
            d_473___mcc_h14_ = source15_.Hierarchy
            if True:
                d_474_keyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
                d_475_valueOrError1_: Wrappers.Result = None
                out34_: Wrappers.Result
                out34_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_475_valueOrError1_ = out34_
                if (d_475_valueOrError1_).IsFailure():
                    output = (d_475_valueOrError1_).PropagateFailure()
                    return output
                d_474_keyring_ = (d_475_valueOrError1_).Extract()
                d_476_output_k_: Wrappers.Result
                out35_: Wrappers.Result
                out35_ = (mpl).CreateDefaultCryptographicMaterialsManager(AwsCryptographyMaterialProvidersTypes.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_474_keyring_))
                d_476_output_k_ = out35_
                def lambda39_(d_477_e_):
                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_477_e_)

                output = (d_476_output_k_).MapFailure(lambda39_)
        elif source15_.is_Multi:
            d_478___mcc_h16_ = source15_.Multi
            if True:
                d_479_keyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
                d_480_valueOrError1_: Wrappers.Result = None
                out36_: Wrappers.Result
                out36_ = KeyringFromKeyDescription.default__.ToKeyring(mpl, keys, description)
                d_480_valueOrError1_ = out36_
                if (d_480_valueOrError1_).IsFailure():
                    output = (d_480_valueOrError1_).PropagateFailure()
                    return output
                d_479_keyring_ = (d_480_valueOrError1_).Extract()
                d_481_output_k_: Wrappers.Result
                out37_: Wrappers.Result
                out37_ = (mpl).CreateDefaultCryptographicMaterialsManager(AwsCryptographyMaterialProvidersTypes.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(d_479_keyring_))
                d_481_output_k_ = out37_
                def lambda40_(d_482_e_):
                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_482_e_)

                output = (d_481_output_k_).MapFailure(lambda40_)
        elif True:
            d_483___mcc_h18_ = source15_.RequiredEncryptionContext
            d_484_cmm_ = d_483___mcc_h18_
            if True:
                d_485_underlying_: AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager
                d_486_valueOrError0_: Wrappers.Result = None
                out38_: Wrappers.Result
                out38_ = default__.ToCmm(mpl, keys, (d_484_cmm_).underlying, forOperation)
                d_486_valueOrError0_ = out38_
                if (d_486_valueOrError0_).IsFailure():
                    output = (d_486_valueOrError0_).PropagateFailure()
                    return output
                d_485_underlying_ = (d_486_valueOrError0_).Extract()
                d_487_output_k_: Wrappers.Result
                out39_: Wrappers.Result
                out39_ = (mpl).CreateRequiredEncryptionContextCMM(AwsCryptographyMaterialProvidersTypes.CreateRequiredEncryptionContextCMMInput_CreateRequiredEncryptionContextCMMInput(Wrappers.Option_Some(d_485_underlying_), Wrappers.Option_None(), (d_484_cmm_).requiredEncryptionContextKeys))
                d_487_output_k_ = out39_
                def lambda41_(d_488_e_):
                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_488_e_)

                output = (d_487_output_k_).MapFailure(lambda41_)
        return output

