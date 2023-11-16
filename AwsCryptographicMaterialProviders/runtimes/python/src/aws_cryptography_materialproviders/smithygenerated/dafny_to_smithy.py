# Code generated by smithy-python-codegen DO NOT EDIT.

import aws_cryptography_materialproviders.smithygenerated.config
import aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy
import aws_cryptography_materialproviders.smithygenerated.models
from software_amazon_cryptography_materialproviders_internaldafny_types import (
    AlgorithmSuiteId_DBE,
    AlgorithmSuiteId_ESDK,
    CacheType_Default,
    CacheType_MultiThreaded,
    CacheType_No,
    CacheType_SingleThreaded,
    CacheType_StormTracking,
    CommitmentPolicy_DBE,
    CommitmentPolicy_ESDK,
    DerivationAlgorithm_HKDF,
    DerivationAlgorithm_IDENTITY,
    DerivationAlgorithm_None,
    EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING,
    EdkWrappingAlgorithm_IntermediateKeyWrapping,
    Encrypt_AES__GCM,
    Materials_BeaconKey,
    Materials_BranchKey,
    Materials_Decryption,
    Materials_Encryption,
    SignatureAlgorithm_ECDSA,
    SignatureAlgorithm_None,
    SymmetricSignatureAlgorithm_HMAC,
    SymmetricSignatureAlgorithm_None,
)


def DafnyToSmithy_aws_cryptography_materialproviders_GetBranchKeyIdInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.GetBranchKeyIdInput(
        encryption_context={bytes(key): bytes(value) for (key, value) in input.encryptionContext.items },
    )

def DafnyToSmithy_aws_cryptography_materialproviders_GetBranchKeyIdOutput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.GetBranchKeyIdOutput(
        branch_key_id=input.branchKeyId.VerbatimString(False),
    )

def DafnyToSmithy_aws_cryptography_materialproviders_GetClientInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.GetClientInput(
        region=input.region.VerbatimString(False),
    )

def DafnyToSmithy_aws_cryptography_materialproviders_KmsClientReference(input):
    return input.impl

def DafnyToSmithy_aws_cryptography_materialproviders_GetClientOutput(input):
    return aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_KmsClientReference(input)

def DafnyToSmithy_aws_cryptography_materialproviders_Materials(input):
    # Convert Materials
    if isinstance(input, Materials_Encryption):
        Materials_union_value = aws_cryptography_materialproviders.smithygenerated.models.MaterialsEncryption(input.encryption)
    elif isinstance(input, Materials_Decryption):
        Materials_union_value = aws_cryptography_materialproviders.smithygenerated.models.MaterialsDecryption(input.decryption)
    elif isinstance(input, Materials_BranchKey):
        Materials_union_value = aws_cryptography_materialproviders.smithygenerated.models.MaterialsBranchKey(input.branch_key)
    elif isinstance(input, Materials_BeaconKey):
        Materials_union_value = aws_cryptography_materialproviders.smithygenerated.models.MaterialsBeaconKey(input.beacon_key)
    else:
        raise ValueError("No recognized union value in union type: " + input)

    return Materials_union_value

def DafnyToSmithy_aws_cryptography_materialproviders_PutCacheEntryInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.PutCacheEntryInput(
        identifier=bytes(input.identifier),
        materials=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_Materials(input.materials),
        creation_time=input.creationTime,
        expiry_time=input.expiryTime,
        messages_used=(input.messagesUsed.value) if (input.messagesUsed.is_Some) else None,
        bytes_used=(input.bytesUsed.value) if (input.bytesUsed.is_Some) else None,
    )

def DafnyToSmithy_smithy_api_Unit():
    return aws_cryptography_materialproviders.smithygenerated.models.Unit(
    )

def DafnyToSmithy_aws_cryptography_materialproviders_GetCacheEntryInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.GetCacheEntryInput(
        identifier=bytes(input.identifier),
        bytes_used=(input.bytesUsed.value) if (input.bytesUsed.is_Some) else None,
    )

def DafnyToSmithy_aws_cryptography_materialproviders_GetCacheEntryOutput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.GetCacheEntryOutput(
        materials=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_Materials(input.materials),
        creation_time=input.creationTime,
        expiry_time=input.expiryTime,
        messages_used=input.messagesUsed,
        bytes_used=input.bytesUsed,
    )

def DafnyToSmithy_aws_cryptography_materialproviders_UpdateUsageMetadataInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.UpdateUsageMetadataInput(
        identifier=bytes(input.identifier),
        bytes_used=input.bytesUsed,
    )

def DafnyToSmithy_aws_cryptography_materialproviders_DeleteCacheEntryInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.DeleteCacheEntryInput(
        identifier=bytes(input.identifier),
    )

def DafnyToSmithy_aws_cryptography_materialproviders_CommitmentPolicy(input):
    # Convert CommitmentPolicy
    if isinstance(input, CommitmentPolicy_ESDK):
        CommitmentPolicy_union_value = aws_cryptography_materialproviders.smithygenerated.models.CommitmentPolicyESDK(input.esdk)
    elif isinstance(input, CommitmentPolicy_DBE):
        CommitmentPolicy_union_value = aws_cryptography_materialproviders.smithygenerated.models.CommitmentPolicyDBE(input.dbe)
    else:
        raise ValueError("No recognized union value in union type: " + input)

    return CommitmentPolicy_union_value

def DafnyToSmithy_aws_cryptography_materialproviders_AlgorithmSuiteId(input):
    # Convert AlgorithmSuiteId
    if isinstance(input, AlgorithmSuiteId_ESDK):
        AlgorithmSuiteId_union_value = aws_cryptography_materialproviders.smithygenerated.models.AlgorithmSuiteIdESDK(input.esdk)
    elif isinstance(input, AlgorithmSuiteId_DBE):
        AlgorithmSuiteId_union_value = aws_cryptography_materialproviders.smithygenerated.models.AlgorithmSuiteIdDBE(input.dbe)
    else:
        raise ValueError("No recognized union value in union type: " + input)

    return AlgorithmSuiteId_union_value

def DafnyToSmithy_aws_cryptography_materialproviders_GetEncryptionMaterialsInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.GetEncryptionMaterialsInput(
        encryption_context={bytes(key): bytes(value) for (key, value) in input.encryptionContext.items },
        commitment_policy=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CommitmentPolicy(input.commitmentPolicy),
        algorithm_suite_id=(aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_AlgorithmSuiteId(input.algorithmSuiteId.value)) if (input.algorithmSuiteId.is_Some) else None,
        max_plaintext_length=(input.maxPlaintextLength.value) if (input.maxPlaintextLength.is_Some) else None,
        required_encryption_context_keys=([bytes(list_element) for list_element in input.requiredEncryptionContextKeys.value]) if (input.requiredEncryptionContextKeys.is_Some) else None,
    )

def DafnyToSmithy_aws_cryptography_materialproviders_EncryptionMaterials(input):
    return aws_cryptography_materialproviders.smithygenerated.models.EncryptionMaterials(
        algorithm_suite=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_AlgorithmSuiteInfo(input.algorithmSuite),
        encryption_context={bytes(key): bytes(value) for (key, value) in input.encryptionContext.items },
        encrypted_data_keys=[aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_EncryptedDataKey(list_element) for list_element in input.encryptedDataKeys],
        required_encryption_context_keys=[bytes(list_element) for list_element in input.requiredEncryptionContextKeys],
        plaintext_data_key=(bytes(input.plaintextDataKey.value)) if (input.plaintextDataKey.is_Some) else None,
        signing_key=(bytes(input.signingKey.value)) if (input.signingKey.is_Some) else None,
        symmetric_signing_keys=([bytes(list_element) for list_element in input.symmetricSigningKeys.value]) if (input.symmetricSigningKeys.is_Some) else None,
    )

def DafnyToSmithy_aws_cryptography_materialproviders_AlgorithmSuiteInfo(input):
    return aws_cryptography_materialproviders.smithygenerated.models.AlgorithmSuiteInfo(
        id=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_AlgorithmSuiteId(input.id),
        binary_id=bytes(input.binaryId),
        message_version=input.messageVersion,
        encrypt=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_Encrypt(input.encrypt),
        kdf=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_DerivationAlgorithm(input.kdf),
        commitment=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_DerivationAlgorithm(input.commitment),
        signature=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_SignatureAlgorithm(input.signature),
        symmetric_signature=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_SymmetricSignatureAlgorithm(input.symmetricSignature),
        edk_wrapping=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_EdkWrappingAlgorithm(input.edkWrapping),
    )

def DafnyToSmithy_aws_cryptography_materialproviders_EncryptedDataKey(input):
    return aws_cryptography_materialproviders.smithygenerated.models.EncryptedDataKey(
        key_provider_id=bytes(input.keyProviderId),
        key_provider_info=bytes(input.keyProviderInfo),
        ciphertext=bytes(input.ciphertext),
    )

def DafnyToSmithy_aws_cryptography_materialproviders_Encrypt(input):
    # Convert Encrypt
    if isinstance(input, Encrypt_AES__GCM):
        Encrypt_union_value = aws_cryptography_materialproviders.smithygenerated.models.EncryptAES_GCM(input.aes_gcm)
    else:
        raise ValueError("No recognized union value in union type: " + input)

    return Encrypt_union_value

def DafnyToSmithy_aws_cryptography_materialproviders_DerivationAlgorithm(input):
    # Convert DerivationAlgorithm
    if isinstance(input, DerivationAlgorithm_HKDF):
        DerivationAlgorithm_union_value = aws_cryptography_materialproviders.smithygenerated.models.DerivationAlgorithmHKDF(input.hkdf)
    elif isinstance(input, DerivationAlgorithm_IDENTITY):
        DerivationAlgorithm_union_value = aws_cryptography_materialproviders.smithygenerated.models.DerivationAlgorithmIDENTITY(input.identity)
    elif isinstance(input, DerivationAlgorithm_None):
        DerivationAlgorithm_union_value = aws_cryptography_materialproviders.smithygenerated.models.DerivationAlgorithmNone(input.none_)
    else:
        raise ValueError("No recognized union value in union type: " + input)

    return DerivationAlgorithm_union_value

def DafnyToSmithy_aws_cryptography_materialproviders_SignatureAlgorithm(input):
    # Convert SignatureAlgorithm
    if isinstance(input, SignatureAlgorithm_ECDSA):
        SignatureAlgorithm_union_value = aws_cryptography_materialproviders.smithygenerated.models.SignatureAlgorithmECDSA(input.ecdsa)
    elif isinstance(input, SignatureAlgorithm_None):
        SignatureAlgorithm_union_value = aws_cryptography_materialproviders.smithygenerated.models.SignatureAlgorithmNone(input.none_)
    else:
        raise ValueError("No recognized union value in union type: " + input)

    return SignatureAlgorithm_union_value

def DafnyToSmithy_aws_cryptography_materialproviders_SymmetricSignatureAlgorithm(input):
    # Convert SymmetricSignatureAlgorithm
    if isinstance(input, SymmetricSignatureAlgorithm_HMAC):
        SymmetricSignatureAlgorithm_union_value = aws_cryptography_materialproviders.smithygenerated.models.SymmetricSignatureAlgorithmHMAC(input.hmac)
    elif isinstance(input, SymmetricSignatureAlgorithm_None):
        SymmetricSignatureAlgorithm_union_value = aws_cryptography_materialproviders.smithygenerated.models.SymmetricSignatureAlgorithmNone(input.none_)
    else:
        raise ValueError("No recognized union value in union type: " + input)

    return SymmetricSignatureAlgorithm_union_value

def DafnyToSmithy_aws_cryptography_materialproviders_EdkWrappingAlgorithm(input):
    # Convert EdkWrappingAlgorithm
    if isinstance(input, EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING):
        EdkWrappingAlgorithm_union_value = aws_cryptography_materialproviders.smithygenerated.models.EdkWrappingAlgorithmDIRECT_KEY_WRAPPING(input.direct_key_wrapping)
    elif isinstance(input, EdkWrappingAlgorithm_IntermediateKeyWrapping):
        EdkWrappingAlgorithm_union_value = aws_cryptography_materialproviders.smithygenerated.models.EdkWrappingAlgorithmIntermediateKeyWrapping(input.intermediate_key_wrapping)
    else:
        raise ValueError("No recognized union value in union type: " + input)

    return EdkWrappingAlgorithm_union_value

def DafnyToSmithy_aws_cryptography_materialproviders_GetEncryptionMaterialsOutput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.GetEncryptionMaterialsOutput(
        encryption_materials=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_EncryptionMaterials(input.encryptionMaterials),
    )

def DafnyToSmithy_aws_cryptography_materialproviders_DecryptMaterialsInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.DecryptMaterialsInput(
        algorithm_suite_id=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_AlgorithmSuiteId(input.algorithmSuiteId),
        commitment_policy=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CommitmentPolicy(input.commitmentPolicy),
        encrypted_data_keys=[aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_EncryptedDataKey(list_element) for list_element in input.encryptedDataKeys],
        encryption_context={bytes(key): bytes(value) for (key, value) in input.encryptionContext.items },
        reproduced_encryption_context=({bytes(key): bytes(value) for (key, value) in input.reproducedEncryptionContext.value.items }) if (input.reproducedEncryptionContext.is_Some) else None,
    )

def DafnyToSmithy_aws_cryptography_materialproviders_DecryptionMaterials(input):
    return aws_cryptography_materialproviders.smithygenerated.models.DecryptionMaterials(
        algorithm_suite=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_AlgorithmSuiteInfo(input.algorithmSuite),
        encryption_context={bytes(key): bytes(value) for (key, value) in input.encryptionContext.items },
        required_encryption_context_keys=[bytes(list_element) for list_element in input.requiredEncryptionContextKeys],
        plaintext_data_key=(bytes(input.plaintextDataKey.value)) if (input.plaintextDataKey.is_Some) else None,
        verification_key=(bytes(input.verificationKey.value)) if (input.verificationKey.is_Some) else None,
        symmetric_signing_key=(bytes(input.symmetricSigningKey.value)) if (input.symmetricSigningKey.is_Some) else None,
    )

def DafnyToSmithy_aws_cryptography_materialproviders_DecryptMaterialsOutput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.DecryptMaterialsOutput(
        decryption_materials=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_DecryptionMaterials(input.decryptionMaterials),
    )

def DafnyToSmithy_aws_cryptography_materialproviders_OnEncryptInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.OnEncryptInput(
        materials=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_EncryptionMaterials(input.materials),
    )

def DafnyToSmithy_aws_cryptography_materialproviders_OnEncryptOutput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.OnEncryptOutput(
        materials=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_EncryptionMaterials(input.materials),
    )

def DafnyToSmithy_aws_cryptography_materialproviders_OnDecryptInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.OnDecryptInput(
        materials=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_DecryptionMaterials(input.materials),
        encrypted_data_keys=[aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_EncryptedDataKey(list_element) for list_element in input.encryptedDataKeys],
    )

def DafnyToSmithy_aws_cryptography_materialproviders_OnDecryptOutput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.OnDecryptOutput(
        materials=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_DecryptionMaterials(input.materials),
    )

def DafnyToSmithy_aws_cryptography_materialproviders_DiscoveryFilter(input):
    return aws_cryptography_materialproviders.smithygenerated.models.DiscoveryFilter(
        account_ids=[list_element.VerbatimString(False) for list_element in input.accountIds],
        partition=input.partition.VerbatimString(False),
    )

def DafnyToSmithy_aws_cryptography_materialproviders_CreateAwsKmsDiscoveryKeyringInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.CreateAwsKmsDiscoveryKeyringInput(
        kms_client=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_KmsClientReference(input.kmsClient),
        discovery_filter=(aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_DiscoveryFilter(input.discoveryFilter.value)) if (input.discoveryFilter.is_Some) else None,
        grant_tokens=([list_element.VerbatimString(False) for list_element in input.grantTokens.value]) if (input.grantTokens.is_Some) else None,
    )

def DafnyToSmithy_aws_cryptography_materialproviders_KeyringReference(input):
    from aws_cryptography_materialproviders.smithygenerated.references import Keyring
    return Keyring(_impl=input)

def DafnyToSmithy_aws_cryptography_materialproviders_CreateMultiKeyringInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.CreateMultiKeyringInput(
        generator=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_KeyringReference(input.generator.UnwrapOr(None)),
        child_keyrings=[aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_KeyringReference(list_element) for list_element in input.childKeyrings],
    )

def DafnyToSmithy_aws_cryptography_materialproviders_ValidEncryptionMaterialsTransitionInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.ValidEncryptionMaterialsTransitionInput(
        start=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_EncryptionMaterials(input.start),
        stop=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_EncryptionMaterials(input.stop),
    )

def DafnyToSmithy_aws_cryptography_materialproviders_CreateDefaultCryptographicMaterialsManagerInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.CreateDefaultCryptographicMaterialsManagerInput(
        keyring=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_KeyringReference(input.keyring),
    )

def DafnyToSmithy_aws_cryptography_materialproviders_CreateRawRsaKeyringInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.CreateRawRsaKeyringInput(
        key_namespace=input.keyNamespace.VerbatimString(False),
        key_name=input.keyName.VerbatimString(False),
        padding_scheme=input.paddingScheme,
        public_key=(bytes(input.publicKey.value)) if (input.publicKey.is_Some) else None,
        private_key=(bytes(input.privateKey.value)) if (input.privateKey.is_Some) else None,
    )

def DafnyToSmithy_aws_cryptography_materialproviders_InitializeEncryptionMaterialsInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.InitializeEncryptionMaterialsInput(
        algorithm_suite_id=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_AlgorithmSuiteId(input.algorithmSuiteId),
        encryption_context={bytes(key): bytes(value) for (key, value) in input.encryptionContext.items },
        required_encryption_context_keys=[bytes(list_element) for list_element in input.requiredEncryptionContextKeys],
        signing_key=(bytes(input.signingKey.value)) if (input.signingKey.is_Some) else None,
        verification_key=(bytes(input.verificationKey.value)) if (input.verificationKey.is_Some) else None,
    )

def DafnyToSmithy_aws_cryptography_materialproviders_ClientSupplierReference(input):
    from aws_cryptography_materialproviders.smithygenerated.references import ClientSupplier
    return ClientSupplier(_impl=input)

def DafnyToSmithy_aws_cryptography_materialproviders_CreateAwsKmsMultiKeyringInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.CreateAwsKmsMultiKeyringInput(
        generator=(input.generator.value.VerbatimString(False)) if (input.generator.is_Some) else None,
        kms_key_ids=([list_element.VerbatimString(False) for list_element in input.kmsKeyIds.value]) if (input.kmsKeyIds.is_Some) else None,
        client_supplier=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_ClientSupplierReference(input.clientSupplier.UnwrapOr(None)),
        grant_tokens=([list_element.VerbatimString(False) for list_element in input.grantTokens.value]) if (input.grantTokens.is_Some) else None,
    )

def DafnyToSmithy_aws_cryptography_materialproviders_CreateAwsKmsMrkDiscoveryKeyringInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.CreateAwsKmsMrkDiscoveryKeyringInput(
        kms_client=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_KmsClientReference(input.kmsClient),
        discovery_filter=(aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_DiscoveryFilter(input.discoveryFilter.value)) if (input.discoveryFilter.is_Some) else None,
        grant_tokens=([list_element.VerbatimString(False) for list_element in input.grantTokens.value]) if (input.grantTokens.is_Some) else None,
        region=input.region.VerbatimString(False),
    )

def DafnyToSmithy_aws_cryptography_materialproviders_BranchKeyIdSupplierReference(input):
    from aws_cryptography_materialproviders.smithygenerated.references import BranchKeyIdSupplier
    return BranchKeyIdSupplier(_impl=input)

def DafnyToSmithy_aws_cryptography_materialproviders_KeyStoreReference(input):
    from aws_cryptography_keystore.smithygenerated.client import KeyStore
    return KeyStore(input)

def DafnyToSmithy_aws_cryptography_materialproviders_CacheType(input):
    # Convert CacheType
    if isinstance(input, CacheType_Default):
        CacheType_union_value = aws_cryptography_materialproviders.smithygenerated.models.CacheTypeDefault(input.default)
    elif isinstance(input, CacheType_No):
        CacheType_union_value = aws_cryptography_materialproviders.smithygenerated.models.CacheTypeNo(input.no)
    elif isinstance(input, CacheType_SingleThreaded):
        CacheType_union_value = aws_cryptography_materialproviders.smithygenerated.models.CacheTypeSingleThreaded(input.single_threaded)
    elif isinstance(input, CacheType_MultiThreaded):
        CacheType_union_value = aws_cryptography_materialproviders.smithygenerated.models.CacheTypeMultiThreaded(input.multi_threaded)
    elif isinstance(input, CacheType_StormTracking):
        CacheType_union_value = aws_cryptography_materialproviders.smithygenerated.models.CacheTypeStormTracking(input.storm_tracking)
    else:
        raise ValueError("No recognized union value in union type: " + input)

    return CacheType_union_value

def DafnyToSmithy_aws_cryptography_materialproviders_CreateAwsKmsHierarchicalKeyringInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.CreateAwsKmsHierarchicalKeyringInput(
        branch_key_id=(input.branchKeyId.value.VerbatimString(False)) if (input.branchKeyId.is_Some) else None,
        branch_key_id_supplier=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_BranchKeyIdSupplierReference(input.branchKeyIdSupplier.UnwrapOr(None)),
        key_store=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_KeyStoreReference(input.keyStore),
        ttl_seconds=input.ttlSeconds,
        cache=(aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CacheType(input.cache.value)) if (input.cache.is_Some) else None,
    )

def DafnyToSmithy_aws_cryptography_materialproviders_ValidateCommitmentPolicyOnDecryptInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.ValidateCommitmentPolicyOnDecryptInput(
        algorithm=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_AlgorithmSuiteId(input.algorithm),
        commitment_policy=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CommitmentPolicy(input.commitmentPolicy),
    )

def DafnyToSmithy_aws_cryptography_materialproviders_ValidDecryptionMaterialsTransitionInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.ValidDecryptionMaterialsTransitionInput(
        start=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_DecryptionMaterials(input.start),
        stop=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_DecryptionMaterials(input.stop),
    )

def DafnyToSmithy_aws_cryptography_materialproviders_CreateAwsKmsMrkDiscoveryMultiKeyringInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.CreateAwsKmsMrkDiscoveryMultiKeyringInput(
        regions=[list_element.VerbatimString(False) for list_element in input.regions],
        discovery_filter=(aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_DiscoveryFilter(input.discoveryFilter.value)) if (input.discoveryFilter.is_Some) else None,
        client_supplier=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_ClientSupplierReference(input.clientSupplier.UnwrapOr(None)),
        grant_tokens=([list_element.VerbatimString(False) for list_element in input.grantTokens.value]) if (input.grantTokens.is_Some) else None,
    )

def DafnyToSmithy_aws_cryptography_materialproviders_CreateAwsKmsKeyringInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.CreateAwsKmsKeyringInput(
        kms_key_id=input.kmsKeyId.VerbatimString(False),
        kms_client=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_KmsClientReference(input.kmsClient),
        grant_tokens=([list_element.VerbatimString(False) for list_element in input.grantTokens.value]) if (input.grantTokens.is_Some) else None,
    )

def DafnyToSmithy_aws_cryptography_materialproviders_CreateRawAesKeyringInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.CreateRawAesKeyringInput(
        key_namespace=input.keyNamespace.VerbatimString(False),
        key_name=input.keyName.VerbatimString(False),
        wrapping_key=bytes(input.wrappingKey),
        wrapping_alg=input.wrappingAlg,
    )

def DafnyToSmithy_aws_cryptography_materialproviders_CryptographicMaterialsManagerReference(input):
    from aws_cryptography_materialproviders.smithygenerated.references import CryptographicMaterialsManager
    return CryptographicMaterialsManager(_impl=input)

def DafnyToSmithy_aws_cryptography_materialproviders_CreateRequiredEncryptionContextCMMInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.CreateRequiredEncryptionContextCMMInput(
        underlying_cmm=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CryptographicMaterialsManagerReference(input.underlyingCMM.UnwrapOr(None)),
        keyring=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_KeyringReference(input.keyring.UnwrapOr(None)),
        required_encryption_context_keys=[bytes(list_element) for list_element in input.requiredEncryptionContextKeys],
    )

def DafnyToSmithy_aws_cryptography_materialproviders_CreateAwsKmsRsaKeyringInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.CreateAwsKmsRsaKeyringInput(
        public_key=(bytes(input.publicKey.value)) if (input.publicKey.is_Some) else None,
        kms_key_id=input.kmsKeyId.VerbatimString(False),
        encryption_algorithm=input.encryptionAlgorithm.VerbatimString(False),
        kms_client=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_KmsClientReference(input.kmsClient.UnwrapOr(None)),
        grant_tokens=([list_element.VerbatimString(False) for list_element in input.grantTokens.value]) if (input.grantTokens.is_Some) else None,
    )

def DafnyToSmithy_aws_cryptography_materialproviders_CreateCryptographicMaterialsCacheInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.CreateCryptographicMaterialsCacheInput(
        cache=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CacheType(input.cache),
    )

def DafnyToSmithy_aws_cryptography_materialproviders_InitializeDecryptionMaterialsInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.InitializeDecryptionMaterialsInput(
        algorithm_suite_id=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_AlgorithmSuiteId(input.algorithmSuiteId),
        encryption_context={bytes(key): bytes(value) for (key, value) in input.encryptionContext.items },
        required_encryption_context_keys=[bytes(list_element) for list_element in input.requiredEncryptionContextKeys],
    )

def DafnyToSmithy_aws_cryptography_materialproviders_GetAlgorithmSuiteInfoInput(input):
    return bytes(input)

def DafnyToSmithy_aws_cryptography_materialproviders_CreateAwsKmsDiscoveryMultiKeyringInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.CreateAwsKmsDiscoveryMultiKeyringInput(
        regions=[list_element.VerbatimString(False) for list_element in input.regions],
        discovery_filter=(aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_DiscoveryFilter(input.discoveryFilter.value)) if (input.discoveryFilter.is_Some) else None,
        client_supplier=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_ClientSupplierReference(input.clientSupplier.UnwrapOr(None)),
        grant_tokens=([list_element.VerbatimString(False) for list_element in input.grantTokens.value]) if (input.grantTokens.is_Some) else None,
    )

def DafnyToSmithy_aws_cryptography_materialproviders_CreateAwsKmsMrkKeyringInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.CreateAwsKmsMrkKeyringInput(
        kms_key_id=input.kmsKeyId.VerbatimString(False),
        kms_client=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_KmsClientReference(input.kmsClient),
        grant_tokens=([list_element.VerbatimString(False) for list_element in input.grantTokens.value]) if (input.grantTokens.is_Some) else None,
    )

def DafnyToSmithy_aws_cryptography_materialproviders_ValidateCommitmentPolicyOnEncryptInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.ValidateCommitmentPolicyOnEncryptInput(
        algorithm=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_AlgorithmSuiteId(input.algorithm),
        commitment_policy=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CommitmentPolicy(input.commitmentPolicy),
    )

def DafnyToSmithy_aws_cryptography_materialproviders_CreateAwsKmsMrkMultiKeyringInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.CreateAwsKmsMrkMultiKeyringInput(
        generator=(input.generator.value.VerbatimString(False)) if (input.generator.is_Some) else None,
        kms_key_ids=([list_element.VerbatimString(False) for list_element in input.kmsKeyIds.value]) if (input.kmsKeyIds.is_Some) else None,
        client_supplier=aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_ClientSupplierReference(input.clientSupplier.UnwrapOr(None)),
        grant_tokens=([list_element.VerbatimString(False) for list_element in input.grantTokens.value]) if (input.grantTokens.is_Some) else None,
    )

def DafnyToSmithy_aws_cryptography_materialproviders_CreateDefaultClientSupplierInput(input):
    return aws_cryptography_materialproviders.smithygenerated.models.CreateDefaultClientSupplierInput(
    )

def DafnyToSmithy_aws_cryptography_materialproviders_CreateKeyringOutput(input):
    return aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_KeyringReference(input)

def DafnyToSmithy_aws_cryptography_materialproviders_CreateCryptographicMaterialsManagerOutput(input):
    return aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CryptographicMaterialsManagerReference(input)

def DafnyToSmithy_aws_cryptography_materialproviders_CreateRequiredEncryptionContextCMMOutput(input):
    return aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CryptographicMaterialsManagerReference(input)

def DafnyToSmithy_aws_cryptography_materialproviders_CryptographicMaterialsCacheReference(input):
    from aws_cryptography_materialproviders.smithygenerated.references import CryptographicMaterialsCache
    return CryptographicMaterialsCache(_impl=input)

def DafnyToSmithy_aws_cryptography_materialproviders_CreateCryptographicMaterialsCacheOutput(input):
    return aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CryptographicMaterialsCacheReference(input)

def DafnyToSmithy_aws_cryptography_materialproviders_CreateDefaultClientSupplierOutput(input):
    return aws_cryptography_materialproviders.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_ClientSupplierReference(input)

def DafnyToSmithy_aws_cryptography_materialproviders_MaterialProvidersConfig(input):
    return aws_cryptography_materialproviders.smithygenerated.config.MaterialProvidersConfig(
    )
