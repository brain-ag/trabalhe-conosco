
# Teste - Brain Agriculture

O teste tem como objetivo acurar as habilidades do candidato em resolver alguns problemas relacionados à lógica de programação, regra de negócio e orientação à objetos.

O mesmo consiste em um cadastro de produtor rural com os seguintes dados: 

 1. CPF ou CNPJ
 2. Nome
 3. Nome da Fazenda
 4. Cidade
 5. Estado
 6. Área total em hectares da fazenda
 7. Área agricultável em hectares
 8. Área de vegetação em hectares
 7. Culturas plantadas (Soja, Milho, Algodão, Café, Cana de Açucar) 


# Requisitos de negócio

 - O usuário deverá ter a possibilidade de cadastrar, editar, e excluir produtores rurais.
 - O sistema deverá validar CPF e CNPJ digitados incorretamente.
 - A soma de área agrícultável e vegetação, não deverá ser maior que a Área Total da Fazenda
 - Cada produtor pode plantar mais de uma cultura em sua Fazenda.
 - A plataforma deverá ter um Dashboard que exiba:
	 - Total de fazendas em quantidade
   - Total de fazendas em hectares (área total)
   - Gráfico de pizza por estado.
   - Gráfico de pizza por cultura. 
	 - Gráfico de pizza por uso de solo (Área agricultável e vegetação)
     

# Requisitos técnicos

 - O front-end deverá ser escrito em [ReactJS](http://reactjs.org) usando o [Redux](https://redux.js.org/) para controlar o estado da aplicação.
 - Os dados inputados pelo usuário deverão ser salvos em um banco de dados Postgres usando o NodeJS como layer de Backend.
 - Não envie a solução como anexo, suba os fontes para seu Github (ou outro repositório) e envie o link para *guilherme@brain.agr.br*. 
