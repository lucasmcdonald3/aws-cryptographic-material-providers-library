import module_
from Wrappers import Option_None, Option_Some
from com_amazonaws_dynamodb.smithygenerated.shim import DynamoDB_20120810Shim
from com_amazonaws_dynamodb.internaldafny.generated.software_amazon_cryptography_services_dynamodb_internaldafny import *
import com_amazonaws_dynamodb.internaldafny.generated.software_amazon_cryptography_services_dynamodb_internaldafny

import boto3
from botocore.config import Config

class default__(com_amazonaws_dynamodb.internaldafny.generated.software_amazon_cryptography_services_dynamodb_internaldafny.default__):
    @staticmethod
    def DynamoDBClient(region=None):
        if region is not None:
            boto_config = Config(
                region_name=region
            )
            impl = boto3.client("dynamodb", config=boto_config)
        else:
            impl = boto3.client("dynamodb")
            region = boto3.session.Session().region_name
        wrapped_client = DynamoDB_20120810Shim(impl, region)
        return Wrappers.Result_Success(wrapped_client)

    @staticmethod
    def RegionMatch(client, region):
        # We should never be passing anything other than Shim as the 'client'.
        # If this assertion fails, that indicates that there is something wrong with
        # our code generation.
        try:
            assert isinstance(client, DynamoDB_20120810Shim)
        except assertionError:
            raise TypeError("Client provided to RegionMatch is not a DynamoDB_20120810Shim: " + client)

        # Since client is a DynamoDB_20120810Shim, we can reach into its _impl, which is a boto3 client
        client_region_name = client._impl.meta.region_name
        return Option_Some(region.VerbatimString(False) == client_region_name)

import software_amazon_cryptography_services_dynamodb_internaldafny
software_amazon_cryptography_services_dynamodb_internaldafny.default__ = default__
com_amazonaws_dynamodb.internaldafny.generated.software_amazon_cryptography_services_dynamodb_internaldafny.default__ = default__
com_amazonaws_dynamodb.internaldafny.generated.software_amazon_cryptography_services_dynamodb_internaldafny.DynamoDBClient = default__.DynamoDBClient