# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from _dafny import Map, Seq
from com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes import (
    AlgorithmSpec_RSAES__OAEP__SHA__1,
    AlgorithmSpec_RSAES__OAEP__SHA__256,
    AlgorithmSpec_RSAES__PKCS1__V1__5,
    AliasListEntry_AliasListEntry as DafnyAliasListEntry,
    CancelKeyDeletionRequest_CancelKeyDeletionRequest as DafnyCancelKeyDeletionRequest,
    CancelKeyDeletionResponse_CancelKeyDeletionResponse as DafnyCancelKeyDeletionResponse,
    ConnectCustomKeyStoreRequest_ConnectCustomKeyStoreRequest as DafnyConnectCustomKeyStoreRequest,
    ConnectCustomKeyStoreResponse_ConnectCustomKeyStoreResponse as DafnyConnectCustomKeyStoreResponse,
    ConnectionErrorCodeType_CLUSTER__NOT__FOUND,
    ConnectionErrorCodeType_INSUFFICIENT__CLOUDHSM__HSMS,
    ConnectionErrorCodeType_INTERNAL__ERROR,
    ConnectionErrorCodeType_INVALID__CREDENTIALS,
    ConnectionErrorCodeType_NETWORK__ERRORS,
    ConnectionErrorCodeType_SUBNET__NOT__FOUND,
    ConnectionErrorCodeType_USER__LOCKED__OUT,
    ConnectionErrorCodeType_USER__LOGGED__IN,
    ConnectionErrorCodeType_USER__NOT__FOUND,
    ConnectionStateType_CONNECTED,
    ConnectionStateType_CONNECTING,
    ConnectionStateType_DISCONNECTED,
    ConnectionStateType_DISCONNECTING,
    ConnectionStateType_FAILED,
    CreateAliasRequest_CreateAliasRequest as DafnyCreateAliasRequest,
    CreateCustomKeyStoreRequest_CreateCustomKeyStoreRequest as DafnyCreateCustomKeyStoreRequest,
    CreateCustomKeyStoreResponse_CreateCustomKeyStoreResponse as DafnyCreateCustomKeyStoreResponse,
    CreateGrantRequest_CreateGrantRequest as DafnyCreateGrantRequest,
    CreateGrantResponse_CreateGrantResponse as DafnyCreateGrantResponse,
    CreateKeyRequest_CreateKeyRequest as DafnyCreateKeyRequest,
    CreateKeyResponse_CreateKeyResponse as DafnyCreateKeyResponse,
    CustomKeyStoresListEntry_CustomKeyStoresListEntry as DafnyCustomKeyStoresListEntry,
    CustomerMasterKeySpec_ECC__NIST__P256,
    CustomerMasterKeySpec_ECC__NIST__P384,
    CustomerMasterKeySpec_ECC__NIST__P521,
    CustomerMasterKeySpec_ECC__SECG__P256K1,
    CustomerMasterKeySpec_RSA__2048,
    CustomerMasterKeySpec_RSA__3072,
    CustomerMasterKeySpec_RSA__4096,
    CustomerMasterKeySpec_SYMMETRIC__DEFAULT,
    DataKeyPairSpec_ECC__NIST__P256,
    DataKeyPairSpec_ECC__NIST__P384,
    DataKeyPairSpec_ECC__NIST__P521,
    DataKeyPairSpec_ECC__SECG__P256K1,
    DataKeyPairSpec_RSA__2048,
    DataKeyPairSpec_RSA__3072,
    DataKeyPairSpec_RSA__4096,
    DataKeySpec_AES__128,
    DataKeySpec_AES__256,
    DecryptRequest_DecryptRequest as DafnyDecryptRequest,
    DecryptResponse_DecryptResponse as DafnyDecryptResponse,
    DeleteAliasRequest_DeleteAliasRequest as DafnyDeleteAliasRequest,
    DeleteCustomKeyStoreRequest_DeleteCustomKeyStoreRequest as DafnyDeleteCustomKeyStoreRequest,
    DeleteCustomKeyStoreResponse_DeleteCustomKeyStoreResponse as DafnyDeleteCustomKeyStoreResponse,
    DeleteImportedKeyMaterialRequest_DeleteImportedKeyMaterialRequest as DafnyDeleteImportedKeyMaterialRequest,
    DescribeCustomKeyStoresRequest_DescribeCustomKeyStoresRequest as DafnyDescribeCustomKeyStoresRequest,
    DescribeCustomKeyStoresResponse_DescribeCustomKeyStoresResponse as DafnyDescribeCustomKeyStoresResponse,
    DescribeKeyRequest_DescribeKeyRequest as DafnyDescribeKeyRequest,
    DescribeKeyResponse_DescribeKeyResponse as DafnyDescribeKeyResponse,
    DisableKeyRequest_DisableKeyRequest as DafnyDisableKeyRequest,
    DisableKeyRotationRequest_DisableKeyRotationRequest as DafnyDisableKeyRotationRequest,
    DisconnectCustomKeyStoreRequest_DisconnectCustomKeyStoreRequest as DafnyDisconnectCustomKeyStoreRequest,
    DisconnectCustomKeyStoreResponse_DisconnectCustomKeyStoreResponse as DafnyDisconnectCustomKeyStoreResponse,
    EnableKeyRequest_EnableKeyRequest as DafnyEnableKeyRequest,
    EnableKeyRotationRequest_EnableKeyRotationRequest as DafnyEnableKeyRotationRequest,
    EncryptRequest_EncryptRequest as DafnyEncryptRequest,
    EncryptResponse_EncryptResponse as DafnyEncryptResponse,
    EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1,
    EncryptionAlgorithmSpec_RSAES__OAEP__SHA__256,
    EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT,
    Error_AlreadyExistsException,
    Error_CloudHsmClusterInUseException,
    Error_CloudHsmClusterInvalidConfigurationException,
    Error_CloudHsmClusterNotActiveException,
    Error_CloudHsmClusterNotFoundException,
    Error_CloudHsmClusterNotRelatedException,
    Error_CustomKeyStoreHasCMKsException,
    Error_CustomKeyStoreInvalidStateException,
    Error_CustomKeyStoreNameInUseException,
    Error_CustomKeyStoreNotFoundException,
    Error_DependencyTimeoutException,
    Error_DisabledException,
    Error_ExpiredImportTokenException,
    Error_IncorrectKeyException,
    Error_IncorrectKeyMaterialException,
    Error_IncorrectTrustAnchorException,
    Error_InvalidAliasNameException,
    Error_InvalidArnException,
    Error_InvalidCiphertextException,
    Error_InvalidGrantIdException,
    Error_InvalidGrantTokenException,
    Error_InvalidImportTokenException,
    Error_InvalidKeyUsageException,
    Error_InvalidMarkerException,
    Error_KMSInternalException,
    Error_KMSInvalidSignatureException,
    Error_KMSInvalidStateException,
    Error_KeyUnavailableException,
    Error_LimitExceededException,
    Error_MalformedPolicyDocumentException,
    Error_NotFoundException,
    Error_TagException,
    Error_UnsupportedOperationException,
    ExpirationModelType_KEY__MATERIAL__DOES__NOT__EXPIRE,
    ExpirationModelType_KEY__MATERIAL__EXPIRES,
    GenerateDataKeyPairRequest_GenerateDataKeyPairRequest as DafnyGenerateDataKeyPairRequest,
    GenerateDataKeyPairResponse_GenerateDataKeyPairResponse as DafnyGenerateDataKeyPairResponse,
    GenerateDataKeyPairWithoutPlaintextRequest_GenerateDataKeyPairWithoutPlaintextRequest as DafnyGenerateDataKeyPairWithoutPlaintextRequest,
    GenerateDataKeyPairWithoutPlaintextResponse_GenerateDataKeyPairWithoutPlaintextResponse as DafnyGenerateDataKeyPairWithoutPlaintextResponse,
    GenerateDataKeyRequest_GenerateDataKeyRequest as DafnyGenerateDataKeyRequest,
    GenerateDataKeyResponse_GenerateDataKeyResponse as DafnyGenerateDataKeyResponse,
    GenerateDataKeyWithoutPlaintextRequest_GenerateDataKeyWithoutPlaintextRequest as DafnyGenerateDataKeyWithoutPlaintextRequest,
    GenerateDataKeyWithoutPlaintextResponse_GenerateDataKeyWithoutPlaintextResponse as DafnyGenerateDataKeyWithoutPlaintextResponse,
    GenerateRandomRequest_GenerateRandomRequest as DafnyGenerateRandomRequest,
    GenerateRandomResponse_GenerateRandomResponse as DafnyGenerateRandomResponse,
    GetKeyPolicyRequest_GetKeyPolicyRequest as DafnyGetKeyPolicyRequest,
    GetKeyPolicyResponse_GetKeyPolicyResponse as DafnyGetKeyPolicyResponse,
    GetKeyRotationStatusRequest_GetKeyRotationStatusRequest as DafnyGetKeyRotationStatusRequest,
    GetKeyRotationStatusResponse_GetKeyRotationStatusResponse as DafnyGetKeyRotationStatusResponse,
    GetParametersForImportRequest_GetParametersForImportRequest as DafnyGetParametersForImportRequest,
    GetParametersForImportResponse_GetParametersForImportResponse as DafnyGetParametersForImportResponse,
    GetPublicKeyRequest_GetPublicKeyRequest as DafnyGetPublicKeyRequest,
    GetPublicKeyResponse_GetPublicKeyResponse as DafnyGetPublicKeyResponse,
    GrantConstraints_GrantConstraints as DafnyGrantConstraints,
    GrantListEntry_GrantListEntry as DafnyGrantListEntry,
    GrantOperation_CreateGrant,
    GrantOperation_Decrypt,
    GrantOperation_DescribeKey,
    GrantOperation_Encrypt,
    GrantOperation_GenerateDataKey,
    GrantOperation_GenerateDataKeyPair,
    GrantOperation_GenerateDataKeyPairWithoutPlaintext,
    GrantOperation_GenerateDataKeyWithoutPlaintext,
    GrantOperation_GetPublicKey,
    GrantOperation_ReEncryptFrom,
    GrantOperation_ReEncryptTo,
    GrantOperation_RetireGrant,
    GrantOperation_Sign,
    GrantOperation_Verify,
    ImportKeyMaterialRequest_ImportKeyMaterialRequest as DafnyImportKeyMaterialRequest,
    ImportKeyMaterialResponse_ImportKeyMaterialResponse as DafnyImportKeyMaterialResponse,
    KeyManagerType_AWS,
    KeyManagerType_CUSTOMER,
    KeyMetadata_KeyMetadata as DafnyKeyMetadata,
    KeySpec_ECC__NIST__P256,
    KeySpec_ECC__NIST__P384,
    KeySpec_ECC__NIST__P521,
    KeySpec_ECC__SECG__P256K1,
    KeySpec_RSA__2048,
    KeySpec_RSA__3072,
    KeySpec_RSA__4096,
    KeySpec_SYMMETRIC__DEFAULT,
    KeyState_Creating,
    KeyState_Disabled,
    KeyState_Enabled,
    KeyState_PendingDeletion,
    KeyState_PendingImport,
    KeyState_PendingReplicaDeletion,
    KeyState_Unavailable,
    KeyState_Updating,
    KeyUsageType_ENCRYPT__DECRYPT,
    KeyUsageType_SIGN__VERIFY,
    ListAliasesRequest_ListAliasesRequest as DafnyListAliasesRequest,
    ListAliasesResponse_ListAliasesResponse as DafnyListAliasesResponse,
    ListGrantsRequest_ListGrantsRequest as DafnyListGrantsRequest,
    ListGrantsResponse_ListGrantsResponse as DafnyListGrantsResponse,
    ListKeyPoliciesRequest_ListKeyPoliciesRequest as DafnyListKeyPoliciesRequest,
    ListKeyPoliciesResponse_ListKeyPoliciesResponse as DafnyListKeyPoliciesResponse,
    ListResourceTagsRequest_ListResourceTagsRequest as DafnyListResourceTagsRequest,
    ListResourceTagsResponse_ListResourceTagsResponse as DafnyListResourceTagsResponse,
    MessageType_DIGEST,
    MessageType_RAW,
    MultiRegionConfiguration_MultiRegionConfiguration as DafnyMultiRegionConfiguration,
    MultiRegionKeyType_PRIMARY,
    MultiRegionKeyType_REPLICA,
    MultiRegionKey_MultiRegionKey as DafnyMultiRegionKey,
    OriginType_AWS__CLOUDHSM,
    OriginType_AWS__KMS,
    OriginType_EXTERNAL,
    PutKeyPolicyRequest_PutKeyPolicyRequest as DafnyPutKeyPolicyRequest,
    ReEncryptRequest_ReEncryptRequest as DafnyReEncryptRequest,
    ReEncryptResponse_ReEncryptResponse as DafnyReEncryptResponse,
    ReplicateKeyRequest_ReplicateKeyRequest as DafnyReplicateKeyRequest,
    ReplicateKeyResponse_ReplicateKeyResponse as DafnyReplicateKeyResponse,
    RetireGrantRequest_RetireGrantRequest as DafnyRetireGrantRequest,
    RevokeGrantRequest_RevokeGrantRequest as DafnyRevokeGrantRequest,
    ScheduleKeyDeletionRequest_ScheduleKeyDeletionRequest as DafnyScheduleKeyDeletionRequest,
    ScheduleKeyDeletionResponse_ScheduleKeyDeletionResponse as DafnyScheduleKeyDeletionResponse,
    SignRequest_SignRequest as DafnySignRequest,
    SignResponse_SignResponse as DafnySignResponse,
    SigningAlgorithmSpec_ECDSA__SHA__256,
    SigningAlgorithmSpec_ECDSA__SHA__384,
    SigningAlgorithmSpec_ECDSA__SHA__512,
    SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__256,
    SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__384,
    SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__512,
    SigningAlgorithmSpec_RSASSA__PSS__SHA__256,
    SigningAlgorithmSpec_RSASSA__PSS__SHA__384,
    SigningAlgorithmSpec_RSASSA__PSS__SHA__512,
    TagResourceRequest_TagResourceRequest as DafnyTagResourceRequest,
    Tag_Tag as DafnyTag,
    UntagResourceRequest_UntagResourceRequest as DafnyUntagResourceRequest,
    UpdateAliasRequest_UpdateAliasRequest as DafnyUpdateAliasRequest,
    UpdateCustomKeyStoreRequest_UpdateCustomKeyStoreRequest as DafnyUpdateCustomKeyStoreRequest,
    UpdateCustomKeyStoreResponse_UpdateCustomKeyStoreResponse as DafnyUpdateCustomKeyStoreResponse,
    UpdateKeyDescriptionRequest_UpdateKeyDescriptionRequest as DafnyUpdateKeyDescriptionRequest,
    UpdatePrimaryRegionRequest_UpdatePrimaryRegionRequest as DafnyUpdatePrimaryRegionRequest,
    VerifyRequest_VerifyRequest as DafnyVerifyRequest,
    VerifyResponse_VerifyResponse as DafnyVerifyResponse,
    WrappingKeySpec_RSA__2048,
)
import com_amazonaws_kms.internaldafny.generated.module_
import com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny
from standard_library.internaldafny.generated.Wrappers import Option_None, Option_Some


def com_amazonaws_kms_AlreadyExistsException(native_input):
    return Error_AlreadyExistsException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_CloudHsmClusterInUseException(native_input):
    return Error_CloudHsmClusterInUseException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_CloudHsmClusterInvalidConfigurationException(native_input):
    return Error_CloudHsmClusterInvalidConfigurationException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_CloudHsmClusterNotActiveException(native_input):
    return Error_CloudHsmClusterNotActiveException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_CloudHsmClusterNotFoundException(native_input):
    return Error_CloudHsmClusterNotFoundException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_CloudHsmClusterNotRelatedException(native_input):
    return Error_CloudHsmClusterNotRelatedException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_CustomKeyStoreHasCMKsException(native_input):
    return Error_CustomKeyStoreHasCMKsException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_CustomKeyStoreInvalidStateException(native_input):
    return Error_CustomKeyStoreInvalidStateException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_CustomKeyStoreNameInUseException(native_input):
    return Error_CustomKeyStoreNameInUseException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_CustomKeyStoreNotFoundException(native_input):
    return Error_CustomKeyStoreNotFoundException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_DependencyTimeoutException(native_input):
    return Error_DependencyTimeoutException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_DisabledException(native_input):
    return Error_DisabledException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_ExpiredImportTokenException(native_input):
    return Error_ExpiredImportTokenException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_IncorrectKeyException(native_input):
    return Error_IncorrectKeyException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_IncorrectKeyMaterialException(native_input):
    return Error_IncorrectKeyMaterialException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_IncorrectTrustAnchorException(native_input):
    return Error_IncorrectTrustAnchorException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_InvalidAliasNameException(native_input):
    return Error_InvalidAliasNameException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_InvalidArnException(native_input):
    return Error_InvalidArnException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_InvalidCiphertextException(native_input):
    return Error_InvalidCiphertextException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_InvalidGrantIdException(native_input):
    return Error_InvalidGrantIdException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_InvalidGrantTokenException(native_input):
    return Error_InvalidGrantTokenException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_InvalidImportTokenException(native_input):
    return Error_InvalidImportTokenException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_InvalidKeyUsageException(native_input):
    return Error_InvalidKeyUsageException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_InvalidMarkerException(native_input):
    return Error_InvalidMarkerException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_KeyUnavailableException(native_input):
    return Error_KeyUnavailableException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_KMSInternalException(native_input):
    return Error_KMSInternalException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_KMSInvalidSignatureException(native_input):
    return Error_KMSInvalidSignatureException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_KMSInvalidStateException(native_input):
    return Error_KMSInvalidStateException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_LimitExceededException(native_input):
    return Error_LimitExceededException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_MalformedPolicyDocumentException(native_input):
    return Error_MalformedPolicyDocumentException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_NotFoundException(native_input):
    return Error_NotFoundException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_TagException(native_input):
    return Error_TagException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_UnsupportedOperationException(native_input):
    return Error_UnsupportedOperationException(
        message=Seq(native_input['Error']["Message"]),
    )

def com_amazonaws_kms_CancelKeyDeletionRequest(native_input):
    return DafnyCancelKeyDeletionRequest(
        KeyId=Seq(native_input["KeyId"]),
    )

def com_amazonaws_kms_CancelKeyDeletionResponse(native_input):
    return DafnyCancelKeyDeletionResponse(
        KeyId=Option_Some(Seq(native_input["KeyId"])) if "KeyId" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_ConnectCustomKeyStoreRequest(native_input):
    return DafnyConnectCustomKeyStoreRequest(
        CustomKeyStoreId=Seq(native_input["CustomKeyStoreId"]),
    )

def com_amazonaws_kms_ConnectCustomKeyStoreResponse(native_input):
    return DafnyConnectCustomKeyStoreResponse(
    )

def com_amazonaws_kms_CreateAliasRequest(native_input):
    return DafnyCreateAliasRequest(
        AliasName=Seq(native_input["AliasName"]),
        TargetKeyId=Seq(native_input["TargetKeyId"]),
    )

def com_amazonaws_kms_CreateCustomKeyStoreRequest(native_input):
    return DafnyCreateCustomKeyStoreRequest(
        CustomKeyStoreName=Seq(native_input["CustomKeyStoreName"]),
        CloudHsmClusterId=Seq(native_input["CloudHsmClusterId"]),
        TrustAnchorCertificate=Seq(native_input["TrustAnchorCertificate"]),
        KeyStorePassword=Seq(native_input["KeyStorePassword"]),
    )

def com_amazonaws_kms_CreateCustomKeyStoreResponse(native_input):
    return DafnyCreateCustomKeyStoreResponse(
        CustomKeyStoreId=Option_Some(Seq(native_input["CustomKeyStoreId"])) if "CustomKeyStoreId" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_CreateGrantRequest(native_input):
    return DafnyCreateGrantRequest(
        KeyId=Seq(native_input["KeyId"]),
        GranteePrincipal=Seq(native_input["GranteePrincipal"]),
        RetiringPrincipal=Option_Some(Seq(native_input["RetiringPrincipal"])) if "RetiringPrincipal" in native_input.keys() else Option_None(),
        Operations=Seq([com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_GrantOperation(list_element) for list_element in native_input["Operations"]]),
        Constraints=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_GrantConstraints(native_input["Constraints"])) if "Constraints" in native_input.keys() else Option_None(),
        GrantTokens=Option_Some(Seq([Seq(list_element) for list_element in native_input["GrantTokens"]])) if "GrantTokens" in native_input.keys() else Option_None(),
        Name=Option_Some(Seq(native_input["Name"])) if "Name" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_GrantOperation(native_input):
    # Convert GrantOperation
    if native_input == "Decrypt":
        return GrantOperation_Decrypt()
    elif native_input == "Encrypt":
        return GrantOperation_Encrypt()
    elif native_input == "GenerateDataKey":
        return GrantOperation_GenerateDataKey()
    elif native_input == "GenerateDataKeyWithoutPlaintext":
        return GrantOperation_GenerateDataKeyWithoutPlaintext()
    elif native_input == "ReEncryptFrom":
        return GrantOperation_ReEncryptFrom()
    elif native_input == "ReEncryptTo":
        return GrantOperation_ReEncryptTo()
    elif native_input == "Sign":
        return GrantOperation_Sign()
    elif native_input == "Verify":
        return GrantOperation_Verify()
    elif native_input == "GetPublicKey":
        return GrantOperation_GetPublicKey()
    elif native_input == "CreateGrant":
        return GrantOperation_CreateGrant()
    elif native_input == "RetireGrant":
        return GrantOperation_RetireGrant()
    elif native_input == "DescribeKey":
        return GrantOperation_DescribeKey()
    elif native_input == "GenerateDataKeyPair":
        return GrantOperation_GenerateDataKeyPair()
    elif native_input == "GenerateDataKeyPairWithoutPlaintext":
        return GrantOperation_GenerateDataKeyPairWithoutPlaintext()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)

def com_amazonaws_kms_GrantConstraints(native_input):
    return DafnyGrantConstraints(
        EncryptionContextSubset=Option_Some(Map({Seq(key): Seq(value) for (key, value) in native_input["EncryptionContextSubset"].items() })) if "EncryptionContextSubset" in native_input.keys() else Option_None(),
        EncryptionContextEquals=Option_Some(Map({Seq(key): Seq(value) for (key, value) in native_input["EncryptionContextEquals"].items() })) if "EncryptionContextEquals" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_CreateGrantResponse(native_input):
    return DafnyCreateGrantResponse(
        GrantToken=Option_Some(Seq(native_input["GrantToken"])) if "GrantToken" in native_input.keys() else Option_None(),
        GrantId=Option_Some(Seq(native_input["GrantId"])) if "GrantId" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_CreateKeyRequest(native_input):
    return DafnyCreateKeyRequest(
        Policy=Option_Some(Seq(native_input["Policy"])) if "Policy" in native_input.keys() else Option_None(),
        Description=Option_Some(Seq(native_input["Description"])) if "Description" in native_input.keys() else Option_None(),
        KeyUsage=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyUsageType(native_input["KeyUsage"])) if "KeyUsage" in native_input.keys() else Option_None(),
        CustomerMasterKeySpec=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_CustomerMasterKeySpec(native_input["CustomerMasterKeySpec"])) if "CustomerMasterKeySpec" in native_input.keys() else Option_None(),
        KeySpec=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeySpec(native_input["KeySpec"])) if "KeySpec" in native_input.keys() else Option_None(),
        Origin=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_OriginType(native_input["Origin"])) if "Origin" in native_input.keys() else Option_None(),
        CustomKeyStoreId=Option_Some(Seq(native_input["CustomKeyStoreId"])) if "CustomKeyStoreId" in native_input.keys() else Option_None(),
        BypassPolicyLockoutSafetyCheck=Option_Some(native_input["BypassPolicyLockoutSafetyCheck"]) if "BypassPolicyLockoutSafetyCheck" in native_input.keys() else Option_None(),
        Tags=Option_Some(Seq([com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_Tag(list_element) for list_element in native_input["Tags"]])) if "Tags" in native_input.keys() else Option_None(),
        MultiRegion=Option_Some(native_input["MultiRegion"]) if "MultiRegion" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_KeyUsageType(native_input):
    # Convert KeyUsageType
    if native_input == "SIGN_VERIFY":
        return KeyUsageType_SIGN__VERIFY()
    elif native_input == "ENCRYPT_DECRYPT":
        return KeyUsageType_ENCRYPT__DECRYPT()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)

def com_amazonaws_kms_CustomerMasterKeySpec(native_input):
    # Convert CustomerMasterKeySpec
    if native_input == "RSA_2048":
        return CustomerMasterKeySpec_RSA__2048()
    elif native_input == "RSA_3072":
        return CustomerMasterKeySpec_RSA__3072()
    elif native_input == "RSA_4096":
        return CustomerMasterKeySpec_RSA__4096()
    elif native_input == "ECC_NIST_P256":
        return CustomerMasterKeySpec_ECC__NIST__P256()
    elif native_input == "ECC_NIST_P384":
        return CustomerMasterKeySpec_ECC__NIST__P384()
    elif native_input == "ECC_NIST_P521":
        return CustomerMasterKeySpec_ECC__NIST__P521()
    elif native_input == "ECC_SECG_P256K1":
        return CustomerMasterKeySpec_ECC__SECG__P256K1()
    elif native_input == "SYMMETRIC_DEFAULT":
        return CustomerMasterKeySpec_SYMMETRIC__DEFAULT()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)

def com_amazonaws_kms_KeySpec(native_input):
    # Convert KeySpec
    if native_input == "RSA_2048":
        return KeySpec_RSA__2048()
    elif native_input == "RSA_3072":
        return KeySpec_RSA__3072()
    elif native_input == "RSA_4096":
        return KeySpec_RSA__4096()
    elif native_input == "ECC_NIST_P256":
        return KeySpec_ECC__NIST__P256()
    elif native_input == "ECC_NIST_P384":
        return KeySpec_ECC__NIST__P384()
    elif native_input == "ECC_NIST_P521":
        return KeySpec_ECC__NIST__P521()
    elif native_input == "ECC_SECG_P256K1":
        return KeySpec_ECC__SECG__P256K1()
    elif native_input == "SYMMETRIC_DEFAULT":
        return KeySpec_SYMMETRIC__DEFAULT()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)

def com_amazonaws_kms_OriginType(native_input):
    # Convert OriginType
    if native_input == "AWS_KMS":
        return OriginType_AWS__KMS()
    elif native_input == "EXTERNAL":
        return OriginType_EXTERNAL()
    elif native_input == "AWS_CLOUDHSM":
        return OriginType_AWS__CLOUDHSM()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)

def com_amazonaws_kms_Tag(native_input):
    return DafnyTag(
        TagKey=Seq(native_input["TagKey"]),
        TagValue=Seq(native_input["TagValue"]),
    )

def com_amazonaws_kms_CreateKeyResponse(native_input):
    return DafnyCreateKeyResponse(
        KeyMetadata=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyMetadata(native_input["KeyMetadata"])) if "KeyMetadata" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_KeyMetadata(native_input):
    return DafnyKeyMetadata(
        AWSAccountId=Option_Some(Seq(native_input["AWSAccountId"])) if "AWSAccountId" in native_input.keys() else Option_None(),
        KeyId=Seq(native_input["KeyId"]),
        Arn=Option_Some(Seq(native_input["Arn"])) if "Arn" in native_input.keys() else Option_None(),
        CreationDate=Option_Some(TypeError("TimestampShape not supported")) if "CreationDate" in native_input.keys() else Option_None(),
        Enabled=Option_Some(native_input["Enabled"]) if "Enabled" in native_input.keys() else Option_None(),
        Description=Option_Some(Seq(native_input["Description"])) if "Description" in native_input.keys() else Option_None(),
        KeyUsage=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyUsageType(native_input["KeyUsage"])) if "KeyUsage" in native_input.keys() else Option_None(),
        KeyState=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyState(native_input["KeyState"])) if "KeyState" in native_input.keys() else Option_None(),
        DeletionDate=Option_Some(TypeError("TimestampShape not supported")) if "DeletionDate" in native_input.keys() else Option_None(),
        ValidTo=Option_Some(TypeError("TimestampShape not supported")) if "ValidTo" in native_input.keys() else Option_None(),
        Origin=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_OriginType(native_input["Origin"])) if "Origin" in native_input.keys() else Option_None(),
        CustomKeyStoreId=Option_Some(Seq(native_input["CustomKeyStoreId"])) if "CustomKeyStoreId" in native_input.keys() else Option_None(),
        CloudHsmClusterId=Option_Some(Seq(native_input["CloudHsmClusterId"])) if "CloudHsmClusterId" in native_input.keys() else Option_None(),
        ExpirationModel=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_ExpirationModelType(native_input["ExpirationModel"])) if "ExpirationModel" in native_input.keys() else Option_None(),
        KeyManager=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyManagerType(native_input["KeyManager"])) if "KeyManager" in native_input.keys() else Option_None(),
        CustomerMasterKeySpec=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_CustomerMasterKeySpec(native_input["CustomerMasterKeySpec"])) if "CustomerMasterKeySpec" in native_input.keys() else Option_None(),
        KeySpec=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeySpec(native_input["KeySpec"])) if "KeySpec" in native_input.keys() else Option_None(),
        EncryptionAlgorithms=Option_Some(Seq([com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_EncryptionAlgorithmSpec(list_element) for list_element in native_input["EncryptionAlgorithms"]])) if "EncryptionAlgorithms" in native_input.keys() else Option_None(),
        SigningAlgorithms=Option_Some(Seq([com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_SigningAlgorithmSpec(list_element) for list_element in native_input["SigningAlgorithms"]])) if "SigningAlgorithms" in native_input.keys() else Option_None(),
        MultiRegion=Option_Some(native_input["MultiRegion"]) if "MultiRegion" in native_input.keys() else Option_None(),
        MultiRegionConfiguration=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_MultiRegionConfiguration(native_input["MultiRegionConfiguration"])) if "MultiRegionConfiguration" in native_input.keys() else Option_None(),
        PendingDeletionWindowInDays=Option_Some(native_input["PendingDeletionWindowInDays"]) if "PendingDeletionWindowInDays" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_KeyState(native_input):
    # Convert KeyState
    if native_input == "Creating":
        return KeyState_Creating()
    elif native_input == "Enabled":
        return KeyState_Enabled()
    elif native_input == "Disabled":
        return KeyState_Disabled()
    elif native_input == "PendingDeletion":
        return KeyState_PendingDeletion()
    elif native_input == "PendingImport":
        return KeyState_PendingImport()
    elif native_input == "PendingReplicaDeletion":
        return KeyState_PendingReplicaDeletion()
    elif native_input == "Unavailable":
        return KeyState_Unavailable()
    elif native_input == "Updating":
        return KeyState_Updating()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)

def com_amazonaws_kms_ExpirationModelType(native_input):
    # Convert ExpirationModelType
    if native_input == "KEY_MATERIAL_EXPIRES":
        return ExpirationModelType_KEY__MATERIAL__EXPIRES()
    elif native_input == "KEY_MATERIAL_DOES_NOT_EXPIRE":
        return ExpirationModelType_KEY__MATERIAL__DOES__NOT__EXPIRE()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)

def com_amazonaws_kms_KeyManagerType(native_input):
    # Convert KeyManagerType
    if native_input == "AWS":
        return KeyManagerType_AWS()
    elif native_input == "CUSTOMER":
        return KeyManagerType_CUSTOMER()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)

def com_amazonaws_kms_EncryptionAlgorithmSpec(native_input):
    # Convert EncryptionAlgorithmSpec
    if native_input == "SYMMETRIC_DEFAULT":
        return EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT()
    elif native_input == "RSAES_OAEP_SHA_1":
        return EncryptionAlgorithmSpec_RSAES__OAEP__SHA__1()
    elif native_input == "RSAES_OAEP_SHA_256":
        return EncryptionAlgorithmSpec_RSAES__OAEP__SHA__256()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)

def com_amazonaws_kms_SigningAlgorithmSpec(native_input):
    # Convert SigningAlgorithmSpec
    if native_input == "RSASSA_PSS_SHA_256":
        return SigningAlgorithmSpec_RSASSA__PSS__SHA__256()
    elif native_input == "RSASSA_PSS_SHA_384":
        return SigningAlgorithmSpec_RSASSA__PSS__SHA__384()
    elif native_input == "RSASSA_PSS_SHA_512":
        return SigningAlgorithmSpec_RSASSA__PSS__SHA__512()
    elif native_input == "RSASSA_PKCS1_V1_5_SHA_256":
        return SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__256()
    elif native_input == "RSASSA_PKCS1_V1_5_SHA_384":
        return SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__384()
    elif native_input == "RSASSA_PKCS1_V1_5_SHA_512":
        return SigningAlgorithmSpec_RSASSA__PKCS1__V1__5__SHA__512()
    elif native_input == "ECDSA_SHA_256":
        return SigningAlgorithmSpec_ECDSA__SHA__256()
    elif native_input == "ECDSA_SHA_384":
        return SigningAlgorithmSpec_ECDSA__SHA__384()
    elif native_input == "ECDSA_SHA_512":
        return SigningAlgorithmSpec_ECDSA__SHA__512()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)

def com_amazonaws_kms_MultiRegionConfiguration(native_input):
    return DafnyMultiRegionConfiguration(
        MultiRegionKeyType=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_MultiRegionKeyType(native_input["MultiRegionKeyType"])) if "MultiRegionKeyType" in native_input.keys() else Option_None(),
        PrimaryKey=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_MultiRegionKey(native_input["PrimaryKey"])) if "PrimaryKey" in native_input.keys() else Option_None(),
        ReplicaKeys=Option_Some(Seq([com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_MultiRegionKey(list_element) for list_element in native_input["ReplicaKeys"]])) if "ReplicaKeys" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_MultiRegionKeyType(native_input):
    # Convert MultiRegionKeyType
    if native_input == "PRIMARY":
        return MultiRegionKeyType_PRIMARY()
    elif native_input == "REPLICA":
        return MultiRegionKeyType_REPLICA()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)

def com_amazonaws_kms_MultiRegionKey(native_input):
    return DafnyMultiRegionKey(
        Arn=Option_Some(Seq(native_input["Arn"])) if "Arn" in native_input.keys() else Option_None(),
        Region=Option_Some(Seq(native_input["Region"])) if "Region" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_DecryptRequest(native_input):
    return DafnyDecryptRequest(
        CiphertextBlob=Seq(native_input["CiphertextBlob"]),
        EncryptionContext=Option_Some(Map({Seq(key): Seq(value) for (key, value) in native_input["EncryptionContext"].items() })) if "EncryptionContext" in native_input.keys() else Option_None(),
        GrantTokens=Option_Some(Seq([Seq(list_element) for list_element in native_input["GrantTokens"]])) if "GrantTokens" in native_input.keys() else Option_None(),
        KeyId=Option_Some(Seq(native_input["KeyId"])) if "KeyId" in native_input.keys() else Option_None(),
        EncryptionAlgorithm=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_EncryptionAlgorithmSpec(native_input["EncryptionAlgorithm"])) if "EncryptionAlgorithm" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_DecryptResponse(native_input):
    return DafnyDecryptResponse(
        KeyId=Option_Some(Seq(native_input["KeyId"])) if "KeyId" in native_input.keys() else Option_None(),
        Plaintext=Option_Some(Seq(native_input["Plaintext"])) if "Plaintext" in native_input.keys() else Option_None(),
        EncryptionAlgorithm=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_EncryptionAlgorithmSpec(native_input["EncryptionAlgorithm"])) if "EncryptionAlgorithm" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_DeleteAliasRequest(native_input):
    return DafnyDeleteAliasRequest(
        AliasName=Seq(native_input["AliasName"]),
    )

def com_amazonaws_kms_DeleteCustomKeyStoreRequest(native_input):
    return DafnyDeleteCustomKeyStoreRequest(
        CustomKeyStoreId=Seq(native_input["CustomKeyStoreId"]),
    )

def com_amazonaws_kms_DeleteCustomKeyStoreResponse(native_input):
    return DafnyDeleteCustomKeyStoreResponse(
    )

def com_amazonaws_kms_DeleteImportedKeyMaterialRequest(native_input):
    return DafnyDeleteImportedKeyMaterialRequest(
        KeyId=Seq(native_input["KeyId"]),
    )

def com_amazonaws_kms_DescribeCustomKeyStoresRequest(native_input):
    return DafnyDescribeCustomKeyStoresRequest(
        CustomKeyStoreId=Option_Some(Seq(native_input["CustomKeyStoreId"])) if "CustomKeyStoreId" in native_input.keys() else Option_None(),
        CustomKeyStoreName=Option_Some(Seq(native_input["CustomKeyStoreName"])) if "CustomKeyStoreName" in native_input.keys() else Option_None(),
        Limit=Option_Some(native_input["Limit"]) if "Limit" in native_input.keys() else Option_None(),
        Marker=Option_Some(Seq(native_input["Marker"])) if "Marker" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_DescribeCustomKeyStoresResponse(native_input):
    return DafnyDescribeCustomKeyStoresResponse(
        CustomKeyStores=Option_Some(Seq([com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_CustomKeyStoresListEntry(list_element) for list_element in native_input["CustomKeyStores"]])) if "CustomKeyStores" in native_input.keys() else Option_None(),
        NextMarker=Option_Some(Seq(native_input["NextMarker"])) if "NextMarker" in native_input.keys() else Option_None(),
        Truncated=Option_Some(native_input["Truncated"]) if "Truncated" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_CustomKeyStoresListEntry(native_input):
    return DafnyCustomKeyStoresListEntry(
        CustomKeyStoreId=Option_Some(Seq(native_input["CustomKeyStoreId"])) if "CustomKeyStoreId" in native_input.keys() else Option_None(),
        CustomKeyStoreName=Option_Some(Seq(native_input["CustomKeyStoreName"])) if "CustomKeyStoreName" in native_input.keys() else Option_None(),
        CloudHsmClusterId=Option_Some(Seq(native_input["CloudHsmClusterId"])) if "CloudHsmClusterId" in native_input.keys() else Option_None(),
        TrustAnchorCertificate=Option_Some(Seq(native_input["TrustAnchorCertificate"])) if "TrustAnchorCertificate" in native_input.keys() else Option_None(),
        ConnectionState=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_ConnectionStateType(native_input["ConnectionState"])) if "ConnectionState" in native_input.keys() else Option_None(),
        ConnectionErrorCode=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_ConnectionErrorCodeType(native_input["ConnectionErrorCode"])) if "ConnectionErrorCode" in native_input.keys() else Option_None(),
        CreationDate=Option_Some(TypeError("TimestampShape not supported")) if "CreationDate" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_ConnectionStateType(native_input):
    # Convert ConnectionStateType
    if native_input == "CONNECTED":
        return ConnectionStateType_CONNECTED()
    elif native_input == "CONNECTING":
        return ConnectionStateType_CONNECTING()
    elif native_input == "FAILED":
        return ConnectionStateType_FAILED()
    elif native_input == "DISCONNECTED":
        return ConnectionStateType_DISCONNECTED()
    elif native_input == "DISCONNECTING":
        return ConnectionStateType_DISCONNECTING()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)

def com_amazonaws_kms_ConnectionErrorCodeType(native_input):
    # Convert ConnectionErrorCodeType
    if native_input == "INVALID_CREDENTIALS":
        return ConnectionErrorCodeType_INVALID__CREDENTIALS()
    elif native_input == "CLUSTER_NOT_FOUND":
        return ConnectionErrorCodeType_CLUSTER__NOT__FOUND()
    elif native_input == "NETWORK_ERRORS":
        return ConnectionErrorCodeType_NETWORK__ERRORS()
    elif native_input == "INTERNAL_ERROR":
        return ConnectionErrorCodeType_INTERNAL__ERROR()
    elif native_input == "INSUFFICIENT_CLOUDHSM_HSMS":
        return ConnectionErrorCodeType_INSUFFICIENT__CLOUDHSM__HSMS()
    elif native_input == "USER_LOCKED_OUT":
        return ConnectionErrorCodeType_USER__LOCKED__OUT()
    elif native_input == "USER_NOT_FOUND":
        return ConnectionErrorCodeType_USER__NOT__FOUND()
    elif native_input == "USER_LOGGED_IN":
        return ConnectionErrorCodeType_USER__LOGGED__IN()
    elif native_input == "SUBNET_NOT_FOUND":
        return ConnectionErrorCodeType_SUBNET__NOT__FOUND()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)

def com_amazonaws_kms_DescribeKeyRequest(native_input):
    return DafnyDescribeKeyRequest(
        KeyId=Seq(native_input["KeyId"]),
        GrantTokens=Option_Some(Seq([Seq(list_element) for list_element in native_input["GrantTokens"]])) if "GrantTokens" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_DescribeKeyResponse(native_input):
    return DafnyDescribeKeyResponse(
        KeyMetadata=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyMetadata(native_input["KeyMetadata"])) if "KeyMetadata" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_DisableKeyRequest(native_input):
    return DafnyDisableKeyRequest(
        KeyId=Seq(native_input["KeyId"]),
    )

def com_amazonaws_kms_DisableKeyRotationRequest(native_input):
    return DafnyDisableKeyRotationRequest(
        KeyId=Seq(native_input["KeyId"]),
    )

def com_amazonaws_kms_DisconnectCustomKeyStoreRequest(native_input):
    return DafnyDisconnectCustomKeyStoreRequest(
        CustomKeyStoreId=Seq(native_input["CustomKeyStoreId"]),
    )

def com_amazonaws_kms_DisconnectCustomKeyStoreResponse(native_input):
    return DafnyDisconnectCustomKeyStoreResponse(
    )

def com_amazonaws_kms_EnableKeyRequest(native_input):
    return DafnyEnableKeyRequest(
        KeyId=Seq(native_input["KeyId"]),
    )

def com_amazonaws_kms_EnableKeyRotationRequest(native_input):
    return DafnyEnableKeyRotationRequest(
        KeyId=Seq(native_input["KeyId"]),
    )

def com_amazonaws_kms_EncryptRequest(native_input):
    return DafnyEncryptRequest(
        KeyId=Seq(native_input["KeyId"]),
        Plaintext=Seq(native_input["Plaintext"]),
        EncryptionContext=Option_Some(Map({Seq(key): Seq(value) for (key, value) in native_input["EncryptionContext"].items() })) if "EncryptionContext" in native_input.keys() else Option_None(),
        GrantTokens=Option_Some(Seq([Seq(list_element) for list_element in native_input["GrantTokens"]])) if "GrantTokens" in native_input.keys() else Option_None(),
        EncryptionAlgorithm=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_EncryptionAlgorithmSpec(native_input["EncryptionAlgorithm"])) if "EncryptionAlgorithm" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_EncryptResponse(native_input):
    return DafnyEncryptResponse(
        CiphertextBlob=Option_Some(Seq(native_input["CiphertextBlob"])) if "CiphertextBlob" in native_input.keys() else Option_None(),
        KeyId=Option_Some(Seq(native_input["KeyId"])) if "KeyId" in native_input.keys() else Option_None(),
        EncryptionAlgorithm=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_EncryptionAlgorithmSpec(native_input["EncryptionAlgorithm"])) if "EncryptionAlgorithm" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_GenerateDataKeyRequest(native_input):
    return DafnyGenerateDataKeyRequest(
        KeyId=Seq(native_input["KeyId"]),
        EncryptionContext=Option_Some(Map({Seq(key): Seq(value) for (key, value) in native_input["EncryptionContext"].items() })) if "EncryptionContext" in native_input.keys() else Option_None(),
        NumberOfBytes=Option_Some(native_input["NumberOfBytes"]) if "NumberOfBytes" in native_input.keys() else Option_None(),
        KeySpec=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_DataKeySpec(native_input["KeySpec"])) if "KeySpec" in native_input.keys() else Option_None(),
        GrantTokens=Option_Some(Seq([Seq(list_element) for list_element in native_input["GrantTokens"]])) if "GrantTokens" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_DataKeySpec(native_input):
    # Convert DataKeySpec
    if native_input == "AES_256":
        return DataKeySpec_AES__256()
    elif native_input == "AES_128":
        return DataKeySpec_AES__128()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)

def com_amazonaws_kms_GenerateDataKeyResponse(native_input):
    return DafnyGenerateDataKeyResponse(
        CiphertextBlob=Option_Some(Seq(native_input["CiphertextBlob"])) if "CiphertextBlob" in native_input.keys() else Option_None(),
        Plaintext=Option_Some(Seq(native_input["Plaintext"])) if "Plaintext" in native_input.keys() else Option_None(),
        KeyId=Option_Some(Seq(native_input["KeyId"])) if "KeyId" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_GenerateDataKeyPairRequest(native_input):
    return DafnyGenerateDataKeyPairRequest(
        EncryptionContext=Option_Some(Map({Seq(key): Seq(value) for (key, value) in native_input["EncryptionContext"].items() })) if "EncryptionContext" in native_input.keys() else Option_None(),
        KeyId=Seq(native_input["KeyId"]),
        KeyPairSpec=com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_DataKeyPairSpec(native_input["KeyPairSpec"]),
        GrantTokens=Option_Some(Seq([Seq(list_element) for list_element in native_input["GrantTokens"]])) if "GrantTokens" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_DataKeyPairSpec(native_input):
    # Convert DataKeyPairSpec
    if native_input == "RSA_2048":
        return DataKeyPairSpec_RSA__2048()
    elif native_input == "RSA_3072":
        return DataKeyPairSpec_RSA__3072()
    elif native_input == "RSA_4096":
        return DataKeyPairSpec_RSA__4096()
    elif native_input == "ECC_NIST_P256":
        return DataKeyPairSpec_ECC__NIST__P256()
    elif native_input == "ECC_NIST_P384":
        return DataKeyPairSpec_ECC__NIST__P384()
    elif native_input == "ECC_NIST_P521":
        return DataKeyPairSpec_ECC__NIST__P521()
    elif native_input == "ECC_SECG_P256K1":
        return DataKeyPairSpec_ECC__SECG__P256K1()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)

def com_amazonaws_kms_GenerateDataKeyPairResponse(native_input):
    return DafnyGenerateDataKeyPairResponse(
        PrivateKeyCiphertextBlob=Option_Some(Seq(native_input["PrivateKeyCiphertextBlob"])) if "PrivateKeyCiphertextBlob" in native_input.keys() else Option_None(),
        PrivateKeyPlaintext=Option_Some(Seq(native_input["PrivateKeyPlaintext"])) if "PrivateKeyPlaintext" in native_input.keys() else Option_None(),
        PublicKey=Option_Some(Seq(native_input["PublicKey"])) if "PublicKey" in native_input.keys() else Option_None(),
        KeyId=Option_Some(Seq(native_input["KeyId"])) if "KeyId" in native_input.keys() else Option_None(),
        KeyPairSpec=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_DataKeyPairSpec(native_input["KeyPairSpec"])) if "KeyPairSpec" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_GenerateDataKeyPairWithoutPlaintextRequest(native_input):
    return DafnyGenerateDataKeyPairWithoutPlaintextRequest(
        EncryptionContext=Option_Some(Map({Seq(key): Seq(value) for (key, value) in native_input["EncryptionContext"].items() })) if "EncryptionContext" in native_input.keys() else Option_None(),
        KeyId=Seq(native_input["KeyId"]),
        KeyPairSpec=com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_DataKeyPairSpec(native_input["KeyPairSpec"]),
        GrantTokens=Option_Some(Seq([Seq(list_element) for list_element in native_input["GrantTokens"]])) if "GrantTokens" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_GenerateDataKeyPairWithoutPlaintextResponse(native_input):
    return DafnyGenerateDataKeyPairWithoutPlaintextResponse(
        PrivateKeyCiphertextBlob=Option_Some(Seq(native_input["PrivateKeyCiphertextBlob"])) if "PrivateKeyCiphertextBlob" in native_input.keys() else Option_None(),
        PublicKey=Option_Some(Seq(native_input["PublicKey"])) if "PublicKey" in native_input.keys() else Option_None(),
        KeyId=Option_Some(Seq(native_input["KeyId"])) if "KeyId" in native_input.keys() else Option_None(),
        KeyPairSpec=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_DataKeyPairSpec(native_input["KeyPairSpec"])) if "KeyPairSpec" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_GenerateDataKeyWithoutPlaintextRequest(native_input):
    return DafnyGenerateDataKeyWithoutPlaintextRequest(
        KeyId=Seq(native_input["KeyId"]),
        EncryptionContext=Option_Some(Map({Seq(key): Seq(value) for (key, value) in native_input["EncryptionContext"].items() })) if "EncryptionContext" in native_input.keys() else Option_None(),
        KeySpec=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_DataKeySpec(native_input["KeySpec"])) if "KeySpec" in native_input.keys() else Option_None(),
        NumberOfBytes=Option_Some(native_input["NumberOfBytes"]) if "NumberOfBytes" in native_input.keys() else Option_None(),
        GrantTokens=Option_Some(Seq([Seq(list_element) for list_element in native_input["GrantTokens"]])) if "GrantTokens" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_GenerateDataKeyWithoutPlaintextResponse(native_input):
    return DafnyGenerateDataKeyWithoutPlaintextResponse(
        CiphertextBlob=Option_Some(Seq(native_input["CiphertextBlob"])) if "CiphertextBlob" in native_input.keys() else Option_None(),
        KeyId=Option_Some(Seq(native_input["KeyId"])) if "KeyId" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_GenerateRandomRequest(native_input):
    return DafnyGenerateRandomRequest(
        NumberOfBytes=Option_Some(native_input["NumberOfBytes"]) if "NumberOfBytes" in native_input.keys() else Option_None(),
        CustomKeyStoreId=Option_Some(Seq(native_input["CustomKeyStoreId"])) if "CustomKeyStoreId" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_GenerateRandomResponse(native_input):
    return DafnyGenerateRandomResponse(
        Plaintext=Option_Some(Seq(native_input["Plaintext"])) if "Plaintext" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_GetKeyPolicyRequest(native_input):
    return DafnyGetKeyPolicyRequest(
        KeyId=Seq(native_input["KeyId"]),
        PolicyName=Seq(native_input["PolicyName"]),
    )

def com_amazonaws_kms_GetKeyPolicyResponse(native_input):
    return DafnyGetKeyPolicyResponse(
        Policy=Option_Some(Seq(native_input["Policy"])) if "Policy" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_GetKeyRotationStatusRequest(native_input):
    return DafnyGetKeyRotationStatusRequest(
        KeyId=Seq(native_input["KeyId"]),
    )

def com_amazonaws_kms_GetKeyRotationStatusResponse(native_input):
    return DafnyGetKeyRotationStatusResponse(
        KeyRotationEnabled=Option_Some(native_input["KeyRotationEnabled"]) if "KeyRotationEnabled" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_GetParametersForImportRequest(native_input):
    return DafnyGetParametersForImportRequest(
        KeyId=Seq(native_input["KeyId"]),
        WrappingAlgorithm=com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_AlgorithmSpec(native_input["WrappingAlgorithm"]),
        WrappingKeySpec=com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_WrappingKeySpec(native_input["WrappingKeySpec"]),
    )

def com_amazonaws_kms_AlgorithmSpec(native_input):
    # Convert AlgorithmSpec
    if native_input == "RSAES_PKCS1_V1_5":
        return AlgorithmSpec_RSAES__PKCS1__V1__5()
    elif native_input == "RSAES_OAEP_SHA_1":
        return AlgorithmSpec_RSAES__OAEP__SHA__1()
    elif native_input == "RSAES_OAEP_SHA_256":
        return AlgorithmSpec_RSAES__OAEP__SHA__256()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)

def com_amazonaws_kms_WrappingKeySpec(native_input):
    # Convert WrappingKeySpec
    if native_input == "RSA_2048":
        return WrappingKeySpec_RSA__2048()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)

def com_amazonaws_kms_GetParametersForImportResponse(native_input):
    return DafnyGetParametersForImportResponse(
        KeyId=Option_Some(Seq(native_input["KeyId"])) if "KeyId" in native_input.keys() else Option_None(),
        ImportToken=Option_Some(Seq(native_input["ImportToken"])) if "ImportToken" in native_input.keys() else Option_None(),
        PublicKey=Option_Some(Seq(native_input["PublicKey"])) if "PublicKey" in native_input.keys() else Option_None(),
        ParametersValidTo=Option_Some(TypeError("TimestampShape not supported")) if "ParametersValidTo" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_GetPublicKeyRequest(native_input):
    return DafnyGetPublicKeyRequest(
        KeyId=Seq(native_input["KeyId"]),
        GrantTokens=Option_Some(Seq([Seq(list_element) for list_element in native_input["GrantTokens"]])) if "GrantTokens" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_GetPublicKeyResponse(native_input):
    return DafnyGetPublicKeyResponse(
        KeyId=Option_Some(Seq(native_input["KeyId"])) if "KeyId" in native_input.keys() else Option_None(),
        PublicKey=Option_Some(Seq(native_input["PublicKey"])) if "PublicKey" in native_input.keys() else Option_None(),
        CustomerMasterKeySpec=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_CustomerMasterKeySpec(native_input["CustomerMasterKeySpec"])) if "CustomerMasterKeySpec" in native_input.keys() else Option_None(),
        KeySpec=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeySpec(native_input["KeySpec"])) if "KeySpec" in native_input.keys() else Option_None(),
        KeyUsage=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyUsageType(native_input["KeyUsage"])) if "KeyUsage" in native_input.keys() else Option_None(),
        EncryptionAlgorithms=Option_Some(Seq([com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_EncryptionAlgorithmSpec(list_element) for list_element in native_input["EncryptionAlgorithms"]])) if "EncryptionAlgorithms" in native_input.keys() else Option_None(),
        SigningAlgorithms=Option_Some(Seq([com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_SigningAlgorithmSpec(list_element) for list_element in native_input["SigningAlgorithms"]])) if "SigningAlgorithms" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_ImportKeyMaterialRequest(native_input):
    return DafnyImportKeyMaterialRequest(
        KeyId=Seq(native_input["KeyId"]),
        ImportToken=Seq(native_input["ImportToken"]),
        EncryptedKeyMaterial=Seq(native_input["EncryptedKeyMaterial"]),
        ValidTo=Option_Some(TypeError("TimestampShape not supported")) if "ValidTo" in native_input.keys() else Option_None(),
        ExpirationModel=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_ExpirationModelType(native_input["ExpirationModel"])) if "ExpirationModel" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_ImportKeyMaterialResponse(native_input):
    return DafnyImportKeyMaterialResponse(
    )

def com_amazonaws_kms_ListAliasesRequest(native_input):
    return DafnyListAliasesRequest(
        KeyId=Option_Some(Seq(native_input["KeyId"])) if "KeyId" in native_input.keys() else Option_None(),
        Limit=Option_Some(native_input["Limit"]) if "Limit" in native_input.keys() else Option_None(),
        Marker=Option_Some(Seq(native_input["Marker"])) if "Marker" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_ListAliasesResponse(native_input):
    return DafnyListAliasesResponse(
        Aliases=Option_Some(Seq([com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_AliasListEntry(list_element) for list_element in native_input["Aliases"]])) if "Aliases" in native_input.keys() else Option_None(),
        NextMarker=Option_Some(Seq(native_input["NextMarker"])) if "NextMarker" in native_input.keys() else Option_None(),
        Truncated=Option_Some(native_input["Truncated"]) if "Truncated" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_AliasListEntry(native_input):
    return DafnyAliasListEntry(
        AliasName=Option_Some(Seq(native_input["AliasName"])) if "AliasName" in native_input.keys() else Option_None(),
        AliasArn=Option_Some(Seq(native_input["AliasArn"])) if "AliasArn" in native_input.keys() else Option_None(),
        TargetKeyId=Option_Some(Seq(native_input["TargetKeyId"])) if "TargetKeyId" in native_input.keys() else Option_None(),
        CreationDate=Option_Some(TypeError("TimestampShape not supported")) if "CreationDate" in native_input.keys() else Option_None(),
        LastUpdatedDate=Option_Some(TypeError("TimestampShape not supported")) if "LastUpdatedDate" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_ListGrantsRequest(native_input):
    return DafnyListGrantsRequest(
        Limit=Option_Some(native_input["Limit"]) if "Limit" in native_input.keys() else Option_None(),
        Marker=Option_Some(Seq(native_input["Marker"])) if "Marker" in native_input.keys() else Option_None(),
        KeyId=Seq(native_input["KeyId"]),
        GrantId=Option_Some(Seq(native_input["GrantId"])) if "GrantId" in native_input.keys() else Option_None(),
        GranteePrincipal=Option_Some(Seq(native_input["GranteePrincipal"])) if "GranteePrincipal" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_ListGrantsResponse(native_input):
    return DafnyListGrantsResponse(
        Grants=Option_Some(Seq([com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_GrantListEntry(list_element) for list_element in native_input["Grants"]])) if "Grants" in native_input.keys() else Option_None(),
        NextMarker=Option_Some(Seq(native_input["NextMarker"])) if "NextMarker" in native_input.keys() else Option_None(),
        Truncated=Option_Some(native_input["Truncated"]) if "Truncated" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_GrantListEntry(native_input):
    return DafnyGrantListEntry(
        KeyId=Option_Some(Seq(native_input["KeyId"])) if "KeyId" in native_input.keys() else Option_None(),
        GrantId=Option_Some(Seq(native_input["GrantId"])) if "GrantId" in native_input.keys() else Option_None(),
        Name=Option_Some(Seq(native_input["Name"])) if "Name" in native_input.keys() else Option_None(),
        CreationDate=Option_Some(TypeError("TimestampShape not supported")) if "CreationDate" in native_input.keys() else Option_None(),
        GranteePrincipal=Option_Some(Seq(native_input["GranteePrincipal"])) if "GranteePrincipal" in native_input.keys() else Option_None(),
        RetiringPrincipal=Option_Some(Seq(native_input["RetiringPrincipal"])) if "RetiringPrincipal" in native_input.keys() else Option_None(),
        IssuingAccount=Option_Some(Seq(native_input["IssuingAccount"])) if "IssuingAccount" in native_input.keys() else Option_None(),
        Operations=Option_Some(Seq([com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_GrantOperation(list_element) for list_element in native_input["Operations"]])) if "Operations" in native_input.keys() else Option_None(),
        Constraints=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_GrantConstraints(native_input["Constraints"])) if "Constraints" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_ListKeyPoliciesRequest(native_input):
    return DafnyListKeyPoliciesRequest(
        KeyId=Seq(native_input["KeyId"]),
        Limit=Option_Some(native_input["Limit"]) if "Limit" in native_input.keys() else Option_None(),
        Marker=Option_Some(Seq(native_input["Marker"])) if "Marker" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_ListKeyPoliciesResponse(native_input):
    return DafnyListKeyPoliciesResponse(
        PolicyNames=Option_Some(Seq([Seq(list_element) for list_element in native_input["PolicyNames"]])) if "PolicyNames" in native_input.keys() else Option_None(),
        NextMarker=Option_Some(Seq(native_input["NextMarker"])) if "NextMarker" in native_input.keys() else Option_None(),
        Truncated=Option_Some(native_input["Truncated"]) if "Truncated" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_ListResourceTagsRequest(native_input):
    return DafnyListResourceTagsRequest(
        KeyId=Seq(native_input["KeyId"]),
        Limit=Option_Some(native_input["Limit"]) if "Limit" in native_input.keys() else Option_None(),
        Marker=Option_Some(Seq(native_input["Marker"])) if "Marker" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_ListResourceTagsResponse(native_input):
    return DafnyListResourceTagsResponse(
        Tags=Option_Some(Seq([com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_Tag(list_element) for list_element in native_input["Tags"]])) if "Tags" in native_input.keys() else Option_None(),
        NextMarker=Option_Some(Seq(native_input["NextMarker"])) if "NextMarker" in native_input.keys() else Option_None(),
        Truncated=Option_Some(native_input["Truncated"]) if "Truncated" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_PutKeyPolicyRequest(native_input):
    return DafnyPutKeyPolicyRequest(
        KeyId=Seq(native_input["KeyId"]),
        PolicyName=Seq(native_input["PolicyName"]),
        Policy=Seq(native_input["Policy"]),
        BypassPolicyLockoutSafetyCheck=Option_Some(native_input["BypassPolicyLockoutSafetyCheck"]) if "BypassPolicyLockoutSafetyCheck" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_ReEncryptRequest(native_input):
    return DafnyReEncryptRequest(
        CiphertextBlob=Seq(native_input["CiphertextBlob"]),
        SourceEncryptionContext=Option_Some(Map({Seq(key): Seq(value) for (key, value) in native_input["SourceEncryptionContext"].items() })) if "SourceEncryptionContext" in native_input.keys() else Option_None(),
        SourceKeyId=Option_Some(Seq(native_input["SourceKeyId"])) if "SourceKeyId" in native_input.keys() else Option_None(),
        DestinationKeyId=Seq(native_input["DestinationKeyId"]),
        DestinationEncryptionContext=Option_Some(Map({Seq(key): Seq(value) for (key, value) in native_input["DestinationEncryptionContext"].items() })) if "DestinationEncryptionContext" in native_input.keys() else Option_None(),
        SourceEncryptionAlgorithm=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_EncryptionAlgorithmSpec(native_input["SourceEncryptionAlgorithm"])) if "SourceEncryptionAlgorithm" in native_input.keys() else Option_None(),
        DestinationEncryptionAlgorithm=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_EncryptionAlgorithmSpec(native_input["DestinationEncryptionAlgorithm"])) if "DestinationEncryptionAlgorithm" in native_input.keys() else Option_None(),
        GrantTokens=Option_Some(Seq([Seq(list_element) for list_element in native_input["GrantTokens"]])) if "GrantTokens" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_ReEncryptResponse(native_input):
    return DafnyReEncryptResponse(
        CiphertextBlob=Option_Some(Seq(native_input["CiphertextBlob"])) if "CiphertextBlob" in native_input.keys() else Option_None(),
        SourceKeyId=Option_Some(Seq(native_input["SourceKeyId"])) if "SourceKeyId" in native_input.keys() else Option_None(),
        KeyId=Option_Some(Seq(native_input["KeyId"])) if "KeyId" in native_input.keys() else Option_None(),
        SourceEncryptionAlgorithm=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_EncryptionAlgorithmSpec(native_input["SourceEncryptionAlgorithm"])) if "SourceEncryptionAlgorithm" in native_input.keys() else Option_None(),
        DestinationEncryptionAlgorithm=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_EncryptionAlgorithmSpec(native_input["DestinationEncryptionAlgorithm"])) if "DestinationEncryptionAlgorithm" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_ReplicateKeyRequest(native_input):
    return DafnyReplicateKeyRequest(
        KeyId=Seq(native_input["KeyId"]),
        ReplicaRegion=Seq(native_input["ReplicaRegion"]),
        Policy=Option_Some(Seq(native_input["Policy"])) if "Policy" in native_input.keys() else Option_None(),
        BypassPolicyLockoutSafetyCheck=Option_Some(native_input["BypassPolicyLockoutSafetyCheck"]) if "BypassPolicyLockoutSafetyCheck" in native_input.keys() else Option_None(),
        Description=Option_Some(Seq(native_input["Description"])) if "Description" in native_input.keys() else Option_None(),
        Tags=Option_Some(Seq([com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_Tag(list_element) for list_element in native_input["Tags"]])) if "Tags" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_ReplicateKeyResponse(native_input):
    return DafnyReplicateKeyResponse(
        ReplicaKeyMetadata=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyMetadata(native_input["ReplicaKeyMetadata"])) if "ReplicaKeyMetadata" in native_input.keys() else Option_None(),
        ReplicaPolicy=Option_Some(Seq(native_input["ReplicaPolicy"])) if "ReplicaPolicy" in native_input.keys() else Option_None(),
        ReplicaTags=Option_Some(Seq([com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_Tag(list_element) for list_element in native_input["ReplicaTags"]])) if "ReplicaTags" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_RetireGrantRequest(native_input):
    return DafnyRetireGrantRequest(
        GrantToken=Option_Some(Seq(native_input["GrantToken"])) if "GrantToken" in native_input.keys() else Option_None(),
        KeyId=Option_Some(Seq(native_input["KeyId"])) if "KeyId" in native_input.keys() else Option_None(),
        GrantId=Option_Some(Seq(native_input["GrantId"])) if "GrantId" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_RevokeGrantRequest(native_input):
    return DafnyRevokeGrantRequest(
        KeyId=Seq(native_input["KeyId"]),
        GrantId=Seq(native_input["GrantId"]),
    )

def com_amazonaws_kms_ScheduleKeyDeletionRequest(native_input):
    return DafnyScheduleKeyDeletionRequest(
        KeyId=Seq(native_input["KeyId"]),
        PendingWindowInDays=Option_Some(native_input["PendingWindowInDays"]) if "PendingWindowInDays" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_ScheduleKeyDeletionResponse(native_input):
    return DafnyScheduleKeyDeletionResponse(
        KeyId=Option_Some(Seq(native_input["KeyId"])) if "KeyId" in native_input.keys() else Option_None(),
        DeletionDate=Option_Some(TypeError("TimestampShape not supported")) if "DeletionDate" in native_input.keys() else Option_None(),
        KeyState=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_KeyState(native_input["KeyState"])) if "KeyState" in native_input.keys() else Option_None(),
        PendingWindowInDays=Option_Some(native_input["PendingWindowInDays"]) if "PendingWindowInDays" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_SignRequest(native_input):
    return DafnySignRequest(
        KeyId=Seq(native_input["KeyId"]),
        Message=Seq(native_input["Message"]),
        MessageType=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_MessageType(native_input["MessageType"])) if "MessageType" in native_input.keys() else Option_None(),
        GrantTokens=Option_Some(Seq([Seq(list_element) for list_element in native_input["GrantTokens"]])) if "GrantTokens" in native_input.keys() else Option_None(),
        SigningAlgorithm=com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_SigningAlgorithmSpec(native_input["SigningAlgorithm"]),
    )

def com_amazonaws_kms_MessageType(native_input):
    # Convert MessageType
    if native_input == "RAW":
        return MessageType_RAW()
    elif native_input == "DIGEST":
        return MessageType_DIGEST()
    else:
        raise ValueError("No recognized enum value in enum type: " + native_input)

def com_amazonaws_kms_SignResponse(native_input):
    return DafnySignResponse(
        KeyId=Option_Some(Seq(native_input["KeyId"])) if "KeyId" in native_input.keys() else Option_None(),
        Signature=Option_Some(Seq(native_input["Signature"])) if "Signature" in native_input.keys() else Option_None(),
        SigningAlgorithm=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_SigningAlgorithmSpec(native_input["SigningAlgorithm"])) if "SigningAlgorithm" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_TagResourceRequest(native_input):
    return DafnyTagResourceRequest(
        KeyId=Seq(native_input["KeyId"]),
        Tags=Seq([com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_Tag(list_element) for list_element in native_input["Tags"]]),
    )

def com_amazonaws_kms_UntagResourceRequest(native_input):
    return DafnyUntagResourceRequest(
        KeyId=Seq(native_input["KeyId"]),
        TagKeys=Seq([Seq(list_element) for list_element in native_input["TagKeys"]]),
    )

def com_amazonaws_kms_UpdateAliasRequest(native_input):
    return DafnyUpdateAliasRequest(
        AliasName=Seq(native_input["AliasName"]),
        TargetKeyId=Seq(native_input["TargetKeyId"]),
    )

def com_amazonaws_kms_UpdateCustomKeyStoreRequest(native_input):
    return DafnyUpdateCustomKeyStoreRequest(
        CustomKeyStoreId=Seq(native_input["CustomKeyStoreId"]),
        NewCustomKeyStoreName=Option_Some(Seq(native_input["NewCustomKeyStoreName"])) if "NewCustomKeyStoreName" in native_input.keys() else Option_None(),
        KeyStorePassword=Option_Some(Seq(native_input["KeyStorePassword"])) if "KeyStorePassword" in native_input.keys() else Option_None(),
        CloudHsmClusterId=Option_Some(Seq(native_input["CloudHsmClusterId"])) if "CloudHsmClusterId" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_UpdateCustomKeyStoreResponse(native_input):
    return DafnyUpdateCustomKeyStoreResponse(
    )

def com_amazonaws_kms_UpdateKeyDescriptionRequest(native_input):
    return DafnyUpdateKeyDescriptionRequest(
        KeyId=Seq(native_input["KeyId"]),
        Description=Seq(native_input["Description"]),
    )

def com_amazonaws_kms_UpdatePrimaryRegionRequest(native_input):
    return DafnyUpdatePrimaryRegionRequest(
        KeyId=Seq(native_input["KeyId"]),
        PrimaryRegion=Seq(native_input["PrimaryRegion"]),
    )

def com_amazonaws_kms_VerifyRequest(native_input):
    return DafnyVerifyRequest(
        KeyId=Seq(native_input["KeyId"]),
        Message=Seq(native_input["Message"]),
        MessageType=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_MessageType(native_input["MessageType"])) if "MessageType" in native_input.keys() else Option_None(),
        Signature=Seq(native_input["Signature"]),
        SigningAlgorithm=com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_SigningAlgorithmSpec(native_input["SigningAlgorithm"]),
        GrantTokens=Option_Some(Seq([Seq(list_element) for list_element in native_input["GrantTokens"]])) if "GrantTokens" in native_input.keys() else Option_None(),
    )

def com_amazonaws_kms_VerifyResponse(native_input):
    return DafnyVerifyResponse(
        KeyId=Option_Some(Seq(native_input["KeyId"])) if "KeyId" in native_input.keys() else Option_None(),
        SignatureValid=Option_Some(native_input["SignatureValid"]) if "SignatureValid" in native_input.keys() else Option_None(),
        SigningAlgorithm=Option_Some(com_amazonaws_kms.smithygenerated.com_amazonaws_kms.aws_sdk_to_dafny.com_amazonaws_kms_SigningAlgorithmSpec(native_input["SigningAlgorithm"])) if "SigningAlgorithm" in native_input.keys() else Option_None(),
    )
