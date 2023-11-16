# Code generated by smithy-python-codegen DO NOT EDIT.

import aws_cryptography_keystore.smithygenerated.config
import aws_cryptography_keystore.smithygenerated.dafny_to_smithy
import aws_cryptography_keystore.smithygenerated.models
from software_amazon_cryptography_keystore_internaldafny_types import (
    KMSConfiguration_kmsKeyArn,
)


def DafnyToSmithy_smithy_api_Unit():
    return aws_cryptography_keystore.smithygenerated.models.Unit(
    )

def DafnyToSmithy_aws_cryptography_keystore_GetBeaconKeyInput(input):
    return aws_cryptography_keystore.smithygenerated.models.GetBeaconKeyInput(
        branch_key_identifier=input.branchKeyIdentifier.VerbatimString(False),
    )

def DafnyToSmithy_aws_cryptography_keystore_CreateKeyStoreInput(input):
    return aws_cryptography_keystore.smithygenerated.models.CreateKeyStoreInput(
    )

def DafnyToSmithy_aws_cryptography_keystore_GetBranchKeyVersionInput(input):
    return aws_cryptography_keystore.smithygenerated.models.GetBranchKeyVersionInput(
        branch_key_identifier=input.branchKeyIdentifier.VerbatimString(False),
        branch_key_version=input.branchKeyVersion.VerbatimString(False),
    )

def DafnyToSmithy_aws_cryptography_keystore_GetActiveBranchKeyInput(input):
    return aws_cryptography_keystore.smithygenerated.models.GetActiveBranchKeyInput(
        branch_key_identifier=input.branchKeyIdentifier.VerbatimString(False),
    )

def DafnyToSmithy_aws_cryptography_keystore_CreateKeyInput(input):
    return aws_cryptography_keystore.smithygenerated.models.CreateKeyInput(
        branch_key_identifier=(input.branchKeyIdentifier.value.VerbatimString(False)) if (input.branchKeyIdentifier.is_Some) else None,
        encryption_context=({bytes(key): bytes(value) for (key, value) in input.encryptionContext.value.items }) if (input.encryptionContext.is_Some) else None,
    )

def DafnyToSmithy_aws_cryptography_keystore_VersionKeyInput(input):
    return aws_cryptography_keystore.smithygenerated.models.VersionKeyInput(
        branch_key_identifier=input.branchKeyIdentifier.VerbatimString(False),
    )

def DafnyToSmithy_aws_cryptography_keystore_KMSConfiguration(input):
    # Convert KMSConfiguration
    if isinstance(input, KMSConfiguration_kmsKeyArn):
        KMSConfiguration_union_value = aws_cryptography_keystore.smithygenerated.models.KMSConfigurationkmsKeyArn(input.kms_key_arn)
    else:
        raise ValueError("No recognized union value in union type: " + input)

    return KMSConfiguration_union_value

def DafnyToSmithy_aws_cryptography_keystore_GetKeyStoreInfoOutput(input):
    return aws_cryptography_keystore.smithygenerated.models.GetKeyStoreInfoOutput(
        key_store_id=input.keyStoreId.VerbatimString(False),
        key_store_name=input.keyStoreName.VerbatimString(False),
        logical_key_store_name=input.logicalKeyStoreName.VerbatimString(False),
        grant_tokens=[list_element.VerbatimString(False) for list_element in input.grantTokens],
        kms_configuration=aws_cryptography_keystore.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_keystore_KMSConfiguration(input.kmsConfiguration),
    )

def DafnyToSmithy_aws_cryptography_keystore_BeaconKeyMaterials(input):
    return aws_cryptography_keystore.smithygenerated.models.BeaconKeyMaterials(
        beacon_key_identifier=input.beaconKeyIdentifier.VerbatimString(False),
        encryption_context={bytes(key): bytes(value) for (key, value) in input.encryptionContext.items },
        beacon_key=(bytes(input.beaconKey.value)) if (input.beaconKey.is_Some) else None,
        hmac_keys=({key.VerbatimString(False): bytes(value) for (key, value) in input.hmacKeys.value.items }) if (input.hmacKeys.is_Some) else None,
    )

def DafnyToSmithy_aws_cryptography_keystore_GetBeaconKeyOutput(input):
    return aws_cryptography_keystore.smithygenerated.models.GetBeaconKeyOutput(
        beacon_key_materials=aws_cryptography_keystore.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_keystore_BeaconKeyMaterials(input.beaconKeyMaterials),
    )

def DafnyToSmithy_aws_cryptography_keystore_CreateKeyStoreOutput(input):
    return aws_cryptography_keystore.smithygenerated.models.CreateKeyStoreOutput(
        table_arn=input.tableArn.VerbatimString(False),
    )

def DafnyToSmithy_aws_cryptography_keystore_BranchKeyMaterials(input):
    return aws_cryptography_keystore.smithygenerated.models.BranchKeyMaterials(
        branch_key_identifier=input.branchKeyIdentifier.VerbatimString(False),
        branch_key_version=bytes(input.branchKeyVersion),
        encryption_context={bytes(key): bytes(value) for (key, value) in input.encryptionContext.items },
        branch_key=bytes(input.branchKey),
    )

def DafnyToSmithy_aws_cryptography_keystore_GetBranchKeyVersionOutput(input):
    return aws_cryptography_keystore.smithygenerated.models.GetBranchKeyVersionOutput(
        branch_key_materials=aws_cryptography_keystore.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_keystore_BranchKeyMaterials(input.branchKeyMaterials),
    )

def DafnyToSmithy_aws_cryptography_keystore_GetActiveBranchKeyOutput(input):
    return aws_cryptography_keystore.smithygenerated.models.GetActiveBranchKeyOutput(
        branch_key_materials=aws_cryptography_keystore.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_keystore_BranchKeyMaterials(input.branchKeyMaterials),
    )

def DafnyToSmithy_aws_cryptography_keystore_CreateKeyOutput(input):
    return aws_cryptography_keystore.smithygenerated.models.CreateKeyOutput(
        branch_key_identifier=input.branchKeyIdentifier.VerbatimString(False),
    )

def DafnyToSmithy_aws_cryptography_keystore_VersionKeyOutput(input):
    return aws_cryptography_keystore.smithygenerated.models.VersionKeyOutput(
    )

def DafnyToSmithy_aws_cryptography_keystore_DdbClientReference(input):
    return input.impl

def DafnyToSmithy_aws_cryptography_keystore_KmsClientReference(input):
    return input.impl

def DafnyToSmithy_aws_cryptography_keystore_KeyStoreConfig(input):
    return aws_cryptography_keystore.smithygenerated.config.KeyStoreConfig(
        ddb_table_name=input.ddbTableName.VerbatimString(False),
        kms_configuration=aws_cryptography_keystore.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_keystore_KMSConfiguration(input.kmsConfiguration),
        logical_key_store_name=input.logicalKeyStoreName.VerbatimString(False),
        id=(input.id.value.VerbatimString(False)) if (input.id.is_Some) else None,
        grant_tokens=([list_element.VerbatimString(False) for list_element in input.grantTokens.value]) if (input.grantTokens.is_Some) else None,
        ddb_client=aws_cryptography_keystore.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_keystore_DdbClientReference(input.ddbClient.UnwrapOr(None)),
        kms_client=aws_cryptography_keystore.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_keystore_KmsClientReference(input.kmsClient.UnwrapOr(None)),
    )
