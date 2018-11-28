---
layout: default
---

# Projetos Dados Relativos A Projetos Api

All URIs are relative to *http://68.183.107.229:8000* or 0.0.0.0:8000

|Método | HTTP request | Descrição
------------- | ------------- | -------------
[**projeto_list**](https://fga-eps-mds.github.io/2018.2-NaturalSearch/docs/Documentacao_API/DadosRelativosAProjetosApi.html#projeto_list) | **GET** /projeto/{projeto_id} | Busca projetos e todos seus atributos dado um id|


### **projeto_list**
> list[Projeto] projeto_list(projeto_id, format=format)

Busca projetos e todos seus atributos dado um id.

### Exemplo
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjetosDadosRelativosAProjetosApi()
projeto_id = 'projeto_id_example' # str | id do projeto
format = 'format_example' # str | Formato de retorno (optional)

try:
    # Busca projetos e todos seus atributos dado um id
    api_response = api_instance.projeto_list(projeto_id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjetosDadosRelativosAProjetosApi->projeto_list: %s\n" % e)
```

### Parâmetros

|Nome | Tipo | Descrição  | Notas
------------- | ------------- | ------------- | -------------
 **projeto_id** | **str**| id do projeto | 
 **format** | **str**| Formato de retorno | JSON e curl |

### Return type

[** Classe Projeto**](https://fga-eps-mds.github.io/2018.2-NaturalSearch/docs/Documentacao_API/Projeto.html)

### Autorização

Não é necessária autorização para executar consultas ao banco da API, entretanto para adicionar, deletar e modificar dados é preciso efetuar login com poderes de administrador.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#)

