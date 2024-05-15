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

# Module: aws_cryptographic_materialproviders.internaldafny.generated.Structure

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BranchKeyContext_q(m):
        def lambda7_(forall_var_4_):
            d_109_k_: _dafny.Seq = forall_var_4_
            return not ((d_109_k_) in ((m).keys)) or (ComAmazonawsDynamodbTypes.default__.IsValid__AttributeName(d_109_k_))

        return (((((((((((((default__.BRANCH__KEY__IDENTIFIER__FIELD) in (m)) and ((default__.TYPE__FIELD) in (m))) and ((default__.KEY__CREATE__TIME) in (m))) and ((default__.HIERARCHY__VERSION) in (m))) and ((default__.TABLE__FIELD) in (m))) and ((default__.KMS__FIELD) in (m))) and ((default__.BRANCH__KEY__FIELD) not in ((m).keys))) and ((0) < (len((m)[default__.BRANCH__KEY__IDENTIFIER__FIELD])))) and ((0) < (len((m)[default__.TYPE__FIELD])))) and (_dafny.quantifier(((m).keys).Elements, True, lambda7_))) and (((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) in (m)) == ((True) and (((m)[default__.TYPE__FIELD]) == (default__.BRANCH__KEY__ACTIVE__TYPE))))) and (not ((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) in (m)) or ((True) and ((default__.BRANCH__KEY__TYPE__PREFIX) < ((m)[default__.BRANCH__KEY__ACTIVE__VERSION__FIELD]))))) and (((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) not in (m)) == ((((m)[default__.TYPE__FIELD]) == (default__.BEACON__KEY__TYPE__VALUE)) or ((default__.BRANCH__KEY__TYPE__PREFIX) < ((m)[default__.TYPE__FIELD]))))

    @staticmethod
    def ToAttributeMap(encryptionContext, encryptedKey):
        def iife2_():
            coll2_ = _dafny.Map()
            compr_2_: _dafny.Seq
            for compr_2_ in ((((encryptionContext).keys) | (_dafny.Set({default__.BRANCH__KEY__FIELD}))) - (_dafny.Set({default__.TABLE__FIELD}))).Elements:
                d_110_k_: _dafny.Seq = compr_2_
                if ComAmazonawsDynamodbTypes.AttributeName._Is(d_110_k_):
                    if (d_110_k_) in ((((encryptionContext).keys) | (_dafny.Set({default__.BRANCH__KEY__FIELD}))) - (_dafny.Set({default__.TABLE__FIELD}))):
                        coll2_[d_110_k_] = (ComAmazonawsDynamodbTypes.AttributeValue_N((encryptionContext)[default__.HIERARCHY__VERSION]) if (d_110_k_) == (default__.HIERARCHY__VERSION) else (ComAmazonawsDynamodbTypes.AttributeValue_B(encryptedKey) if (d_110_k_) == (default__.BRANCH__KEY__FIELD) else ComAmazonawsDynamodbTypes.AttributeValue_S((encryptionContext)[d_110_k_])))
            return _dafny.Map(coll2_)
        return iife2_()
        

    @staticmethod
    def ToBranchKeyContext(item, logicalKeyStoreName):
        def iife3_():
            coll3_ = _dafny.Map()
            compr_3_: _dafny.Seq
            for compr_3_ in ((((item).keys) - (_dafny.Set({default__.BRANCH__KEY__FIELD}))) | (_dafny.Set({default__.TABLE__FIELD}))).Elements:
                d_111_k_: _dafny.Seq = compr_3_
                if (d_111_k_) in ((((item).keys) - (_dafny.Set({default__.BRANCH__KEY__FIELD}))) | (_dafny.Set({default__.TABLE__FIELD}))):
                    coll3_[d_111_k_] = (((item)[d_111_k_]).N if (d_111_k_) == (default__.HIERARCHY__VERSION) else (logicalKeyStoreName if (d_111_k_) == (default__.TABLE__FIELD) else ((item)[d_111_k_]).S))
            return _dafny.Map(coll3_)
        return iife3_()
        

    @staticmethod
    def ToBranchKeyMaterials(encryptionContext, plaintextKey):
        d_112_versionInformation_ = ((encryptionContext)[default__.BRANCH__KEY__ACTIVE__VERSION__FIELD] if (default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) in (encryptionContext) else (encryptionContext)[default__.TYPE__FIELD])
        d_113_branchKeyVersion_ = _dafny.Seq((d_112_versionInformation_)[len(default__.BRANCH__KEY__TYPE__PREFIX)::])
        def lambda8_(d_115_e_):
            return AwsCryptographyKeyStoreTypes.Error_KeyStoreException(d_115_e_)

        d_114_valueOrError0_ = (UTF8.default__.Encode(d_113_branchKeyVersion_)).MapFailure(lambda8_)
        if (d_114_valueOrError0_).IsFailure():
            return (d_114_valueOrError0_).PropagateFailure()
        elif True:
            d_116_branchKeyVersionUtf8_ = (d_114_valueOrError0_).Extract()
            d_117_valueOrError1_ = default__.ExtractCustomEncryptionContext(encryptionContext)
            if (d_117_valueOrError1_).IsFailure():
                return (d_117_valueOrError1_).PropagateFailure()
            elif True:
                d_118_customEncryptionContext_ = (d_117_valueOrError1_).Extract()
                return Wrappers.Result_Success(AwsCryptographyKeyStoreTypes.BranchKeyMaterials_BranchKeyMaterials((encryptionContext)[default__.BRANCH__KEY__IDENTIFIER__FIELD], d_116_branchKeyVersionUtf8_, d_118_customEncryptionContext_, plaintextKey))

    @staticmethod
    def ToBeaconKeyMaterials(encryptionContext, plaintextKey):
        d_119_valueOrError0_ = default__.ExtractCustomEncryptionContext(encryptionContext)
        if (d_119_valueOrError0_).IsFailure():
            return (d_119_valueOrError0_).PropagateFailure()
        elif True:
            d_120_customEncryptionContext_ = (d_119_valueOrError0_).Extract()
            return Wrappers.Result_Success(AwsCryptographyKeyStoreTypes.BeaconKeyMaterials_BeaconKeyMaterials((encryptionContext)[default__.BRANCH__KEY__IDENTIFIER__FIELD], d_120_customEncryptionContext_, Wrappers.Option_Some(plaintextKey), Wrappers.Option_None()))

    @staticmethod
    def ExtractCustomEncryptionContext(encryptionContext):
        def iife4_():
            coll4_ = _dafny.Set()
            compr_4_: _dafny.Seq
            for compr_4_ in (encryptionContext).keys.Elements:
                d_122_k_: _dafny.Seq = compr_4_
                if ((d_122_k_) in (encryptionContext)) and ((default__.ENCRYPTION__CONTEXT__PREFIX) < (d_122_k_)):
                    coll4_ = coll4_.union(_dafny.Set([(UTF8.default__.Encode(_dafny.Seq((d_122_k_)[len(default__.ENCRYPTION__CONTEXT__PREFIX)::])), UTF8.default__.Encode((encryptionContext)[d_122_k_]))]))
            return _dafny.Set(coll4_)
        d_121_encodedEncryptionContext_ = iife4_()

        def lambda9_(forall_var_5_):
            d_124_i_: tuple = forall_var_5_
            return not ((d_124_i_) in (d_121_encodedEncryptionContext_)) or ((((d_124_i_)[0]).is_Success) and (((d_124_i_)[1]).is_Success))

        d_123_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier((d_121_encodedEncryptionContext_).Elements, True, lambda9_), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Unable to encode string")))
        if (d_123_valueOrError0_).IsFailure():
            return (d_123_valueOrError0_).PropagateFailure()
        elif True:
            def iife5_():
                coll5_ = _dafny.Map()
                compr_5_: tuple
                for compr_5_ in (d_121_encodedEncryptionContext_).Elements:
                    d_125_i_: tuple = compr_5_
                    if (d_125_i_) in (d_121_encodedEncryptionContext_):
                        coll5_[((d_125_i_)[0]).value] = ((d_125_i_)[1]).value
                return _dafny.Map(coll5_)
            return Wrappers.Result_Success(iife5_()
)

    @staticmethod
    def DecryptOnlyBranchKeyEncryptionContext(branchKeyId, branchKeyVersion, timestamp, logicalKeyStoreName, kmsKeyArn, customEncryptionContext):
        def iife6_():
            coll6_ = _dafny.Map()
            compr_6_: _dafny.Seq
            for compr_6_ in (customEncryptionContext).keys.Elements:
                d_126_k_: _dafny.Seq = compr_6_
                if (d_126_k_) in (customEncryptionContext):
                    coll6_[(default__.ENCRYPTION__CONTEXT__PREFIX) + (d_126_k_)] = (customEncryptionContext)[d_126_k_]
            return _dafny.Map(coll6_)
        return (_dafny.Map({default__.BRANCH__KEY__IDENTIFIER__FIELD: branchKeyId, default__.TYPE__FIELD: (default__.BRANCH__KEY__TYPE__PREFIX) + (branchKeyVersion), default__.KEY__CREATE__TIME: timestamp, default__.TABLE__FIELD: logicalKeyStoreName, default__.KMS__FIELD: kmsKeyArn, default__.HIERARCHY__VERSION: _dafny.Seq("1")})) | (iife6_()
        )

    @staticmethod
    def ActiveBranchKeyEncryptionContext(decryptOnlyEncryptionContext):
        return (decryptOnlyEncryptionContext) | (_dafny.Map({default__.BRANCH__KEY__ACTIVE__VERSION__FIELD: (decryptOnlyEncryptionContext)[default__.TYPE__FIELD], default__.TYPE__FIELD: default__.BRANCH__KEY__ACTIVE__TYPE}))

    @staticmethod
    def BeaconKeyEncryptionContext(decryptOnlyEncryptionContext):
        return (decryptOnlyEncryptionContext) | (_dafny.Map({default__.TYPE__FIELD: default__.BEACON__KEY__TYPE__VALUE}))

    @staticmethod
    def NewVersionFromActiveBranchKeyEncryptionContext(activeBranchKeyEncryptionContext, branchKeyVersion, timestamp):
        return ((activeBranchKeyEncryptionContext) | (_dafny.Map({default__.TYPE__FIELD: (default__.BRANCH__KEY__TYPE__PREFIX) + (branchKeyVersion), default__.KEY__CREATE__TIME: timestamp}))) - (_dafny.Set({default__.BRANCH__KEY__ACTIVE__VERSION__FIELD}))

    @staticmethod
    def BranchKeyItem_q(m):
        def lambda10_(forall_var_6_):
            d_127_k_: _dafny.Seq = forall_var_6_
            return not ((d_127_k_) in (((m).keys) - (_dafny.Set({default__.BRANCH__KEY__FIELD, default__.HIERARCHY__VERSION})))) or (((m)[d_127_k_]).is_S)

        return ((((((((((((((((((((default__.BRANCH__KEY__IDENTIFIER__FIELD) in (m)) and (((m)[default__.BRANCH__KEY__IDENTIFIER__FIELD]).is_S)) and ((default__.TYPE__FIELD) in (m))) and (((m)[default__.TYPE__FIELD]).is_S)) and ((default__.KEY__CREATE__TIME) in (m))) and (((m)[default__.KEY__CREATE__TIME]).is_S)) and ((default__.HIERARCHY__VERSION) in (m))) and (((m)[default__.HIERARCHY__VERSION]).is_N)) and ((default__.TABLE__FIELD) not in (m))) and ((default__.KMS__FIELD) in (m))) and (((m)[default__.KMS__FIELD]).is_S)) and ((default__.BRANCH__KEY__FIELD) in (m))) and (((m)[default__.BRANCH__KEY__FIELD]).is_B)) and ((0) < (len(((m)[default__.BRANCH__KEY__IDENTIFIER__FIELD]).S)))) and ((0) < (len(((m)[default__.TYPE__FIELD]).S)))) and (_dafny.quantifier((((m).keys) - (_dafny.Set({default__.BRANCH__KEY__FIELD, default__.HIERARCHY__VERSION}))).Elements, True, lambda10_))) and (((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) in (m)) == ((True) and ((((m)[default__.TYPE__FIELD]).S) == (default__.BRANCH__KEY__ACTIVE__TYPE))))) and (not ((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) in (m)) or ((True) and ((default__.BRANCH__KEY__TYPE__PREFIX) < (((m)[default__.BRANCH__KEY__ACTIVE__VERSION__FIELD]).S))))) and (((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) not in (m)) == (((((m)[default__.TYPE__FIELD]).S) == (default__.BEACON__KEY__TYPE__VALUE)) or ((default__.BRANCH__KEY__TYPE__PREFIX) < (((m)[default__.TYPE__FIELD]).S))))) and (ComAmazonawsKmsTypes.default__.IsValid__CiphertextType(((m)[default__.BRANCH__KEY__FIELD]).B))

    @staticmethod
    def ActiveBranchKeyItem_q(m):
        return ((((default__.BranchKeyItem_q(m)) and ((((m)[default__.TYPE__FIELD]).S) == (default__.BRANCH__KEY__ACTIVE__TYPE))) and ((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) in (m))) and (((m)[default__.BRANCH__KEY__ACTIVE__VERSION__FIELD]).is_S)) and ((default__.BRANCH__KEY__TYPE__PREFIX) < (((m)[default__.BRANCH__KEY__ACTIVE__VERSION__FIELD]).S))

    @staticmethod
    def VersionBranchKeyItem_q(m):
        return ((default__.BranchKeyItem_q(m)) and ((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) not in (m))) and ((default__.BRANCH__KEY__TYPE__PREFIX) < (((m)[default__.TYPE__FIELD]).S))

    @staticmethod
    def BeaconKeyItem_q(m):
        return ((default__.BranchKeyItem_q(m)) and ((default__.BRANCH__KEY__ACTIVE__VERSION__FIELD) not in (m))) and ((((m)[default__.TYPE__FIELD]).S) == (default__.BEACON__KEY__TYPE__VALUE))

    @_dafny.classproperty
    def BRANCH__KEY__IDENTIFIER__FIELD(instance):
        return _dafny.Seq("branch-key-id")
    @_dafny.classproperty
    def TYPE__FIELD(instance):
        return _dafny.Seq("type")
    @_dafny.classproperty
    def KEY__CREATE__TIME(instance):
        return _dafny.Seq("create-time")
    @_dafny.classproperty
    def HIERARCHY__VERSION(instance):
        return _dafny.Seq("hierarchy-version")
    @_dafny.classproperty
    def TABLE__FIELD(instance):
        return _dafny.Seq("tablename")
    @_dafny.classproperty
    def KMS__FIELD(instance):
        return _dafny.Seq("kms-arn")
    @_dafny.classproperty
    def BRANCH__KEY__FIELD(instance):
        return _dafny.Seq("enc")
    @_dafny.classproperty
    def BRANCH__KEY__ACTIVE__VERSION__FIELD(instance):
        return _dafny.Seq("version")
    @_dafny.classproperty
    def BRANCH__KEY__ACTIVE__TYPE(instance):
        return _dafny.Seq("branch:ACTIVE")
    @_dafny.classproperty
    def BRANCH__KEY__TYPE__PREFIX(instance):
        return _dafny.Seq("branch:version:")
    @_dafny.classproperty
    def BEACON__KEY__TYPE__VALUE(instance):
        return _dafny.Seq("beacon:ACTIVE")
    @_dafny.classproperty
    def ENCRYPTION__CONTEXT__PREFIX(instance):
        return _dafny.Seq("aws-crypto-ec:")

class BranchKeyContext:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Map({})
    def _Is(source__):
        d_128_m_: _dafny.Map = source__
        return default__.BranchKeyContext_q(d_128_m_)

class BranchKeyItem:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Map({})
    def _Is(source__):
        d_129_m_: _dafny.Map = source__
        return default__.BranchKeyItem_q(d_129_m_)

class ActiveBranchKeyItem:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Map({})
    def _Is(source__):
        d_130_m_: _dafny.Map = source__
        return default__.ActiveBranchKeyItem_q(d_130_m_)

class VersionBranchKeyItem:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Map({})
    def _Is(source__):
        d_131_m_: _dafny.Map = source__
        return default__.VersionBranchKeyItem_q(d_131_m_)

class BeaconKeyItem:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Map({})
    def _Is(source__):
        d_132_m_: _dafny.Map = source__
        return default__.BeaconKeyItem_q(d_132_m_)
