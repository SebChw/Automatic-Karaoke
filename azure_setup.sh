az group create --name automatic-karaoke --location westeurope
az identity create --name admin --resource-group automatic-karaoke
az appservice plan create --name automatic-karaoke-plan --resource-group automatic-karaoke --sku F1 --is-linux --location westeurope
az webapp create --name automatic-karaoke-frontend --resource-group automatic-karaoke --plan automatic-karaoke-plan --runtime "PYTHON:3.10"