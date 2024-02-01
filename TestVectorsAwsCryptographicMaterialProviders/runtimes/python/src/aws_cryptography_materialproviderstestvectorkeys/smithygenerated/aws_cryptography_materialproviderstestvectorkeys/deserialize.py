# Code generated by smithy-python-codegen DO NOT EDIT.

import _dafny
import aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy
import aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy
import module_
from software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types import (
    Error,
    Error_KeyVectorException,
    GetKeyDescriptionOutput_GetKeyDescriptionOutput as DafnyGetKeyDescriptionOutput,
    SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput as DafnySerializeKeyDescriptionOutput,
)
from typing import Any

from .dafny_protocol import DafnyResponse
from .errors import CollectionOfErrors, KeyVectorException, OpaqueError, ServiceError

from .config import Config


async def _deserialize_create_test_vector_keyring(input: DafnyResponse, config: Config):

  if input.IsFailure():
    return await _deserialize_error(input.error)
  return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateKeyringOutput(input.value)

async def _deserialize_create_wrapped_test_vector_keyring(input: DafnyResponse, config: Config):

  if input.IsFailure():
    return await _deserialize_error(input.error)
  return aws_cryptographic_materialproviders.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.aws_cryptography_materialproviders_CreateKeyringOutput(input.value)

async def _deserialize_create_wrapped_test_vector_cmm(input: DafnyResponse, config: Config):

  if input.IsFailure():
    return await _deserialize_error(input.error)
  return aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_CreateWrappedTestVectorCmmOutput(input.value)

async def _deserialize_get_key_description(input: DafnyResponse, config: Config):

  if input.IsFailure():
    return await _deserialize_error(input.error)
  return aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_GetKeyDescriptionOutput(input.value)

async def _deserialize_serialize_key_description(input: DafnyResponse, config: Config):

  if input.IsFailure():
    return await _deserialize_error(input.error)
  return aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviderstestvectorkeys.dafny_to_smithy.aws_cryptography_materialproviderstestvectorkeys_SerializeKeyDescriptionOutput(input.value)

async def _deserialize_error(error: Error) -> ServiceError:
    if error.is_Opaque:
      return OpaqueError(obj=error.obj)
    elif error.is_CollectionOfErrors:
      return CollectionOfErrors(message=error.message, list=error.list)
    elif error.is_KeyVectorException:
      return KeyVectorException(message=_dafny.string_of(error.message))
    else:
        return OpaqueError(obj=error)
