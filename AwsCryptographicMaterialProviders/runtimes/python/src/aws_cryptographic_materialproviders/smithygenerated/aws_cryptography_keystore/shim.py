# Code generated by smithy-python-codegen DO NOT EDIT.

import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.errors
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny
from com_amazonaws_dynamodb.smithygenerated.com_amazonaws_dynamodb.shim import (
    _sdk_error_to_dafny_error as com_amazonaws_dynamodb_sdk_error_to_dafny_error,
)
from com_amazonaws_kms.smithygenerated.com_amazonaws_kms.shim import (
    _sdk_error_to_dafny_error as com_amazonaws_kms_sdk_error_to_dafny_error,
)
import module_
import software_amazon_cryptography_keystore_internaldafny_types
from software_amazon_cryptography_keystore_internaldafny_types import (
    CreateKeyInput_CreateKeyInput as DafnyCreateKeyInput,
    CreateKeyOutput_CreateKeyOutput as DafnyCreateKeyOutput,
    CreateKeyStoreInput_CreateKeyStoreInput as DafnyCreateKeyStoreInput,
    CreateKeyStoreOutput_CreateKeyStoreOutput as DafnyCreateKeyStoreOutput,
    GetActiveBranchKeyInput_GetActiveBranchKeyInput as DafnyGetActiveBranchKeyInput,
    GetActiveBranchKeyOutput_GetActiveBranchKeyOutput as DafnyGetActiveBranchKeyOutput,
    GetBeaconKeyInput_GetBeaconKeyInput as DafnyGetBeaconKeyInput,
    GetBeaconKeyOutput_GetBeaconKeyOutput as DafnyGetBeaconKeyOutput,
    GetBranchKeyVersionInput_GetBranchKeyVersionInput as DafnyGetBranchKeyVersionInput,
    GetBranchKeyVersionOutput_GetBranchKeyVersionOutput as DafnyGetBranchKeyVersionOutput,
    GetKeyStoreInfoOutput_GetKeyStoreInfoOutput as DafnyGetKeyStoreInfoOutput,
    VersionKeyInput_VersionKeyInput as DafnyVersionKeyInput,
    VersionKeyOutput_VersionKeyOutput as DafnyVersionKeyOutput,
)
from typing import Any

from .errors import (
    CollectionOfErrors,
    ComAmazonawsDynamodb,
    ComAmazonawsKms,
    OpaqueError,
    ServiceError,
)


import Wrappers
import software_amazon_cryptography_keystore_internaldafny_types
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.client as client_impl

def _smithy_error_to_dafny_error(e: ServiceError):
       '''
       Converts the provided native Smithy-modelled error
       into the corresponding Dafny error.
       '''
       if isinstance(e, aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.errors.KeyStoreException):
           return software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(message=e.message)

       if isinstance(e, ComAmazonawsDynamodb):
           return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsDynamodb(com_amazonaws_dynamodb_sdk_error_to_dafny_error(e.message))

       if isinstance(e, ComAmazonawsKms):
           return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsKms(com_amazonaws_kms_sdk_error_to_dafny_error(e.message))

       if isinstance(e, CollectionOfErrors):
           return software_amazon_cryptography_keystore_internaldafny_types.Error_CollectionOfErrors(message=e.message, list=e.list)

       if isinstance(e, OpaqueError):
           return software_amazon_cryptography_keystore_internaldafny_types.Error_Opaque(obj=e.obj)

class KeyStoreShim(software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient):
    def __init__(self, _impl: client_impl) :
        self._impl = _impl

    def GetKeyStoreInfo(self, ):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.Unit = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.smithy_api_Unit()
        try:
            smithy_client_response = self._impl.get_key_store_info(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_GetKeyStoreInfoOutput(smithy_client_response))

    def CreateKeyStore(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.CreateKeyStoreInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_CreateKeyStoreInput(input)
        try:
            smithy_client_response = self._impl.create_key_store(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_CreateKeyStoreOutput(smithy_client_response))

    def CreateKey(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.CreateKeyInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_CreateKeyInput(input)
        try:
            smithy_client_response = self._impl.create_key(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_CreateKeyOutput(smithy_client_response))

    def VersionKey(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.VersionKeyInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_VersionKeyInput(input)
        try:
            smithy_client_response = self._impl.version_key(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_VersionKeyOutput(smithy_client_response))

    def GetActiveBranchKey(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.GetActiveBranchKeyInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_GetActiveBranchKeyInput(input)
        try:
            smithy_client_response = self._impl.get_active_branch_key(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_GetActiveBranchKeyOutput(smithy_client_response))

    def GetBranchKeyVersion(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.GetBranchKeyVersionInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_GetBranchKeyVersionInput(input)
        try:
            smithy_client_response = self._impl.get_branch_key_version(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_GetBranchKeyVersionOutput(smithy_client_response))

    def GetBeaconKey(self, input):
        smithy_client_request: aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.models.GetBeaconKeyInput = aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.aws_cryptography_keystore_GetBeaconKeyInput(input)
        try:
            smithy_client_response = self._impl.get_beacon_key(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(_smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.aws_cryptography_keystore_GetBeaconKeyOutput(smithy_client_response))
