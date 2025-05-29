from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.mgmt.resource import ResourceManagementClient
from constants import Constants


# Build Key Vault URI
kv_uri = f"https://{Constants.KEY_VAULT_NAME}.vault.azure.net"

# Authenticate 
credential = DefaultAzureCredential()

# Get Subscription Id 
print(Constants.MESSAGE_RETRIEVING_SECRET)
secret_client = SecretClient(vault_url=kv_uri, credential=credential)
subscription_id = secret_client.get_secret(Constants.SUBSCRIPTION_ID_SECRET).value

# Initialize the client
client = ResourceManagementClient(credential, subscription_id)

# List all resource groups
print("Listing Azure resource groups:\n")
for rg in client.resource_groups.list():
    print(f"- {rg.name} (Location: {rg.location})")

