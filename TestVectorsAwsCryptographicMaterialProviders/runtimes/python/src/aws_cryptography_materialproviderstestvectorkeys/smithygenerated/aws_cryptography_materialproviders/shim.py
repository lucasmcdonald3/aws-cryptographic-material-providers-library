# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Do not modify this file. This file is machine generated, and any changes to it will be overwritten.

from aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes import (
    AlgorithmSuiteInfo_AlgorithmSuiteInfo as DafnyAlgorithmSuiteInfo,
    CreateAwsKmsDiscoveryKeyringInput_CreateAwsKmsDiscoveryKeyringInput as DafnyCreateAwsKmsDiscoveryKeyringInput,
    CreateAwsKmsDiscoveryMultiKeyringInput_CreateAwsKmsDiscoveryMultiKeyringInput as DafnyCreateAwsKmsDiscoveryMultiKeyringInput,
    CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput as DafnyCreateAwsKmsHierarchicalKeyringInput,
    CreateAwsKmsKeyringInput_CreateAwsKmsKeyringInput as DafnyCreateAwsKmsKeyringInput,
    CreateAwsKmsMrkDiscoveryKeyringInput_CreateAwsKmsMrkDiscoveryKeyringInput as DafnyCreateAwsKmsMrkDiscoveryKeyringInput,
    CreateAwsKmsMrkDiscoveryMultiKeyringInput_CreateAwsKmsMrkDiscoveryMultiKeyringInput as DafnyCreateAwsKmsMrkDiscoveryMultiKeyringInput,
    CreateAwsKmsMrkKeyringInput_CreateAwsKmsMrkKeyringInput as DafnyCreateAwsKmsMrkKeyringInput,
    CreateAwsKmsMrkMultiKeyringInput_CreateAwsKmsMrkMultiKeyringInput as DafnyCreateAwsKmsMrkMultiKeyringInput,
    CreateAwsKmsMultiKeyringInput_CreateAwsKmsMultiKeyringInput as DafnyCreateAwsKmsMultiKeyringInput,
    CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput as DafnyCreateAwsKmsRsaKeyringInput,
    CreateCryptographicMaterialsCacheInput_CreateCryptographicMaterialsCacheInput as DafnyCreateCryptographicMaterialsCacheInput,
    CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput as DafnyCreateDefaultClientSupplierInput,
    CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput as DafnyCreateDefaultCryptographicMaterialsManagerInput,
    CreateMultiKeyringInput_CreateMultiKeyringInput as DafnyCreateMultiKeyringInput,
    CreateRawAesKeyringInput_CreateRawAesKeyringInput as DafnyCreateRawAesKeyringInput,
    CreateRawRsaKeyringInput_CreateRawRsaKeyringInput as DafnyCreateRawRsaKeyringInput,
    CreateRequiredEncryptionContextCMMInput_CreateRequiredEncryptionContextCMMInput as DafnyCreateRequiredEncryptionContextCMMInput,
    DecryptionMaterials_DecryptionMaterials as DafnyDecryptionMaterials,
    EncryptionMaterials_EncryptionMaterials as DafnyEncryptionMaterials,
    InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput as DafnyInitializeDecryptionMaterialsInput,
    InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput as DafnyInitializeEncryptionMaterialsInput,
    ValidDecryptionMaterialsTransitionInput_ValidDecryptionMaterialsTransitionInput as DafnyValidDecryptionMaterialsTransitionInput,
    ValidEncryptionMaterialsTransitionInput_ValidEncryptionMaterialsTransitionInput as DafnyValidEncryptionMaterialsTransitionInput,
    ValidateCommitmentPolicyOnDecryptInput_ValidateCommitmentPolicyOnDecryptInput as DafnyValidateCommitmentPolicyOnDecryptInput,
    ValidateCommitmentPolicyOnEncryptInput_ValidateCommitmentPolicyOnEncryptInput as DafnyValidateCommitmentPolicyOnEncryptInput,
)
import aws_cryptographic_materialproviders.internaldafny.generated.module_
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.errors
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny
from typing import Any

from aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.errors import (
    CollectionOfErrors,
    OpaqueError,
    ServiceError,
    _smithy_error_to_dafny_error,
)


import standard_library.internaldafny.generated.Wrappers as Wrappers
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.client as client_impl

class MaterialProvidersShim(aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient):
    def __init__(self, _impl: client_impl) :
        self._impl = _impl

    def CreateAwsKmsKeyring(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsKeyringInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateAwsKmsKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_aws_kms_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateAwsKmsDiscoveryKeyring(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsDiscoveryKeyringInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateAwsKmsDiscoveryKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_aws_kms_discovery_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateAwsKmsMultiKeyring(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsMultiKeyringInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateAwsKmsMultiKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_aws_kms_multi_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateAwsKmsDiscoveryMultiKeyring(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsDiscoveryMultiKeyringInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateAwsKmsDiscoveryMultiKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_aws_kms_discovery_multi_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateAwsKmsMrkKeyring(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsMrkKeyringInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateAwsKmsMrkKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_aws_kms_mrk_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateAwsKmsMrkMultiKeyring(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsMrkMultiKeyringInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateAwsKmsMrkMultiKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_aws_kms_mrk_multi_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateAwsKmsMrkDiscoveryKeyring(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsMrkDiscoveryKeyringInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateAwsKmsMrkDiscoveryKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_aws_kms_mrk_discovery_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateAwsKmsMrkDiscoveryMultiKeyring(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsMrkDiscoveryMultiKeyringInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateAwsKmsMrkDiscoveryMultiKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_aws_kms_mrk_discovery_multi_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateAwsKmsHierarchicalKeyring(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsHierarchicalKeyringInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateAwsKmsHierarchicalKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_aws_kms_hierarchical_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateMultiKeyring(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.CreateMultiKeyringInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateMultiKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_multi_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateRawAesKeyring(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.CreateRawAesKeyringInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateRawAesKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_raw_aes_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateRawRsaKeyring(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.CreateRawRsaKeyringInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateRawRsaKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_raw_rsa_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateAwsKmsRsaKeyring(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.CreateAwsKmsRsaKeyringInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateAwsKmsRsaKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_aws_kms_rsa_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateDefaultCryptographicMaterialsManager(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.CreateDefaultCryptographicMaterialsManagerInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateDefaultCryptographicMaterialsManagerInput(input)
        try:
            smithy_client_response = self._impl.create_default_cryptographic_materials_manager(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateCryptographicMaterialsManagerOutput(smithy_client_response))

    def CreateRequiredEncryptionContextCMM(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.CreateRequiredEncryptionContextCMMInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateRequiredEncryptionContextCMMInput(input)
        try:
            smithy_client_response = self._impl.create_required_encryption_context_cmm(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateRequiredEncryptionContextCMMOutput(smithy_client_response))

    def CreateCryptographicMaterialsCache(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.CreateCryptographicMaterialsCacheInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateCryptographicMaterialsCacheInput(input)
        try:
            smithy_client_response = self._impl.create_cryptographic_materials_cache(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateCryptographicMaterialsCacheOutput(smithy_client_response))

    def CreateDefaultClientSupplier(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.CreateDefaultClientSupplierInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateDefaultClientSupplierInput(input)
        try:
            smithy_client_response = self._impl.create_default_client_supplier(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_CreateDefaultClientSupplierOutput(smithy_client_response))

    def InitializeEncryptionMaterials(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.InitializeEncryptionMaterialsInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_InitializeEncryptionMaterialsInput(input)
        try:
            smithy_client_response = self._impl.initialize_encryption_materials(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_EncryptionMaterials(smithy_client_response))

    def InitializeDecryptionMaterials(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.InitializeDecryptionMaterialsInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_InitializeDecryptionMaterialsInput(input)
        try:
            smithy_client_response = self._impl.initialize_decryption_materials(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_DecryptionMaterials(smithy_client_response))

    def ValidEncryptionMaterialsTransition(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.ValidEncryptionMaterialsTransitionInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_ValidEncryptionMaterialsTransitionInput(input)
        try:
            smithy_client_response = self._impl.valid_encryption_materials_transition(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def ValidDecryptionMaterialsTransition(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.ValidDecryptionMaterialsTransitionInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_ValidDecryptionMaterialsTransitionInput(input)
        try:
            smithy_client_response = self._impl.valid_decryption_materials_transition(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def EncryptionMaterialsHasPlaintextDataKey(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.EncryptionMaterials = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_EncryptionMaterials(input)
        try:
            smithy_client_response = self._impl.encryption_materials_has_plaintext_data_key(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def DecryptionMaterialsWithPlaintextDataKey(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.DecryptionMaterials = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_DecryptionMaterials(input)
        try:
            smithy_client_response = self._impl.decryption_materials_with_plaintext_data_key(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def GetAlgorithmSuiteInfo(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.GetAlgorithmSuiteInfoInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_GetAlgorithmSuiteInfoInput(input)
        try:
            smithy_client_response = self._impl.get_algorithm_suite_info(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.aws_cryptography_materialproviders_AlgorithmSuiteInfo(smithy_client_response))

    def ValidAlgorithmSuiteInfo(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.AlgorithmSuiteInfo = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_AlgorithmSuiteInfo(input)
        try:
            smithy_client_response = self._impl.valid_algorithm_suite_info(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def ValidateCommitmentPolicyOnEncrypt(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.ValidateCommitmentPolicyOnEncryptInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_ValidateCommitmentPolicyOnEncryptInput(input)
        try:
            smithy_client_response = self._impl.validate_commitment_policy_on_encrypt(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def ValidateCommitmentPolicyOnDecrypt(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.models.ValidateCommitmentPolicyOnDecryptInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_ValidateCommitmentPolicyOnDecryptInput(input)
        try:
            smithy_client_response = self._impl.validate_commitment_policy_on_decrypt(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)
