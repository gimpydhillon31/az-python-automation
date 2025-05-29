# Azure Resource Group Lister from Key Vault

This Python script retrieves an Azure subscription ID stored in **Azure Key Vault**, then uses that ID to list all resource groups in the subscription using the Azure SDK.

## 🔧 Technologies
- Python
- Azure Key Vault
- Azure SDKs (`azure-identity`, `azure-mgmt-resource`, `azure-keyvault-secrets`)
- Managed Identity for authentication

## 🔐 Prerequisites

- Subscription ID saved in Key Vault:
  ```bash
  az keyvault secret set --vault-name <KeyVaultName> --name "SubscriptionId" --value "<your-subscription-id>"
