from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient

# Authenticate using your Azure CLI session
credential = AzureCliCredential()

# Replace with your subscription ID
subscription_id = "<your-subscription-id>"

# Initialize the client
client = ResourceManagementClient(credential, subscription_id)

# List all resource groups
print("Listing Azure resource groups:\n")
for rg in client.resource_groups.list():
    print(f"- {rg.name} (Location: {rg.location})")

