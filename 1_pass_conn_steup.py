#Importing Client API
from onepasswordconnectsdk.client import (
    Client,
    new_client_from_environment,
    new_client
)
OP_CONNECT_TOKEN = "YOUR_ONEPASSWORD_API_TOKEN" #Inserting Credential
OP_CONNECT_HOST = "http://IP ADDRESS:8080" #Inserting your connection server port

Client = new_client(OP_CONNECT_HOST,OP_CONNECT_TOKEN) # Generating instances
# Client.get_items(vault_id ='jjyl5ipeewpt7jaglvxu7vqw6q')

#Now we are going to get list of our Vault, So that we can confirm that our Instances is succesfully generated
#or we can say we can able to connect our 1Password
print(Client.get_vaults())

