import asyncio
import os
from azure.keyvault.secrets.aio import SecretClient
from azure.identity.aio import DefaultAzureCredential
from azure.core.exceptions import HttpResponseError

# ----------------------------------------------------------------------------------------------------------
# Prerequistes -
#
# 1. An Azure Key Vault-
#    https://docs.microsoft.com/en-us/azure/key-vault/quick-create-cli
#
# 2. Microsoft Azure Key Vault PyPI package -
#    https://pypi.python.org/pypi/azure-keyvault-secrets/
#
# 3. Microsoft Azure Identity package -
#    https://pypi.python.org/pypi/azure-identity/
#
# 4. Set Environment variables AZURE_CLIENT_ID, AZURE_TENANT_ID, AZURE_CLIENT_SECRET, VAULT_URL.
# How to do this - https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault-secrets#createget-credentials)
#
# ----------------------------------------------------------------------------------------------------------
# Sample - demonstrates the basic recover and purge operations on a vault(secret) resource for Azure Key Vault. The vault has to be soft-delete enabled to perform the following operations. [Azure Key Vault soft delete](https://docs.microsoft.com/en-us/azure/key-vault/key-vault-ovw-soft-delete)
#
# 1. Create a secret (set_secret)
#
# 2. Delete a secret (delete_secret)
#
# 3. Recover a deleted secret (recover_deleted_secret)
#
# 4. Purge a deleted secret (purge_deleted_secret)
# ----------------------------------------------------------------------------------------------------------
async def run_sample():
    # Instantiate a secret client that will be used to call the service.
    # Notice that the client is using default Azure credentials.
    # To make default credentials work, ensure that environment variables 'AZURE_CLIENT_ID',
    # 'AZURE_CLIENT_SECRET' and 'AZURE_TENANT_ID' are set with the service principal credentials.
    VAULT_URL = os.environ["VAULT_URL"]
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=VAULT_URL, credential=credential)
    try:
        # Let's create secrets holding storage and bank accounts credentials. If the secret
        # already exists in the Key Vault, then a new version of the secret is created.
        print("\n1. Create Secret")
        bank_secret = await client.set_secret("recoverPurgeBankSecretName", "recoverPurgeSecretValue1")
        storage_secret = await client.set_secret("recoverPurgeStorageSecretName", "recoverPurgeSecretValue2")
        print("Secret with name '{0}' was created.".format(bank_secret.name))
        print("Secret with name '{0}' was created.".format(storage_secret.name))

        # The storage account was closed, need to delete its credentials from the Key Vault.
        print("\n2. Delete a Secret")
        secret = await client.delete_secret(bank_secret.name)
        await asyncio.sleep(20)
        print("Secret with name '{0}' was deleted on date {1}.".format(secret.name, secret.deleted_date))

        # We accidentally deleted the bank account secret. Let's recover it.
        # A deleted secret can only be recovered if the Key Vault is soft-delete enabled.
        print("\n3. Recover Deleted  Secret")
        recovered_secret = await client.recover_deleted_secret(bank_secret.name)
        print("Recovered Secret with name '{0}'.".format(recovered_secret.name))

        # Let's delete storage account now.
        # If the keyvault is soft-delete enabled, then for permanent deletion deleted secret needs to be purged.
        await client.delete_secret(storage_secret.name)

        # To ensure secret is deleted on the server side.
        print("\nDeleting Storage Secret...")
        await asyncio.sleep(20)

        # To ensure permanent deletion, we might need to purge the secret.
        print("\n4. Purge Deleted Secret")
        await client.purge_deleted_secret(storage_secret.name)
        print("Secret has been permanently deleted.")

    except HttpResponseError as e:
        if "(NotSupported)" in e.message:
            print("\n{0} Please enable soft delete on Key Vault to perform this operation.".format(e.message))
        else:
            print("\nrun_sample has caught an error. {0}".format(e.message))

    finally:
        print("\nrun_sample done")


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run_sample())
        loop.close()

    except Exception as e:
        print("Top level Error: {0}".format(str(e)))
