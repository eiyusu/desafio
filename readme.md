# 1.1.Descrição do JSON
O JSON pode ser descrito pelas seguinte chaves. 
Linhas 31-37 em <main.py>
<details><summary>Chaves JSON</summary>

> - curUTC
> - locRef
> - guestChecks
> - guestChecks[0]
> - guestChecks[0].guestCheckId
> - guestChecks[0].chkNum
> - guestChecks[0].opnBusDt
> - guestChecks[0].opnUTC
> - guestChecks[0].opnLcl
> - guestChecks[0].clsdBusDt
> - guestChecks[0].clsdUTC
> - guestChecks[0].clsdLcl
> - guestChecks[0].lastTransUTC
> - guestChecks[0].lastTransLcl
> - guestChecks[0].lastUpdatedUTC
> - guestChecks[0].lastUpdatedLcl
> - guestChecks[0].clsdFlag
> - guestChecks[0].gstCnt
> - guestChecks[0].subTtl
> - guestChecks[0].nonTxblSlsTtl
> - guestChecks[0].chkTtl
> - guestChecks[0].dscTtl
> - guestChecks[0].payTtl
> - guestChecks[0].balDueTtl
> - guestChecks[0].rvcNum
> - guestChecks[0].otNum
> - guestChecks[0].ocNum
> - guestChecks[0].tblNum
> - guestChecks[0].tblName
> - guestChecks[0].empNum
> - guestChecks[0].numSrvcRd
> - guestChecks[0].numChkPrntd
> - guestChecks[0].taxes
> - guestChecks[0].taxes[0]
> - guestChecks[0].taxes[0].taxNum
> - guestChecks[0].taxes[0].txblSlsTtl
> - guestChecks[0].taxes[0].taxCollTtl
> - guestChecks[0].taxes[0].taxRate
> - guestChecks[0].taxes[0].type
> - guestChecks[0].detailLines
> - guestChecks[0].detailLines[0]
> - guestChecks[0].detailLines[0].guestCheckLineItemId
> - guestChecks[0].detailLines[0].rvcNum
> - guestChecks[0].detailLines[0].dtlOtNum
> - guestChecks[0].detailLines[0].dtlOcNum
> - guestChecks[0].detailLines[0].lineNum
> - guestChecks[0].detailLines[0].dtlId
> - guestChecks[0].detailLines[0].detailUTC
> - guestChecks[0].detailLines[0].detailLcl
> - guestChecks[0].detailLines[0].lastUpdateUTC
> - guestChecks[0].detailLines[0].lastUpdateLcl
> - guestChecks[0].detailLines[0].busDt
> - guestChecks[0].detailLines[0].wsNum
> - guestChecks[0].detailLines[0].dspTtl
> - guestChecks[0].detailLines[0].dspQty
> - guestChecks[0].detailLines[0].aggTtl
> - guestChecks[0].detailLines[0].aggQty
> - guestChecks[0].detailLines[0].chkEmpId
> - guestChecks[0].detailLines[0].chkEmpNum
> - guestChecks[0].detailLines[0].svcRndNum
> - guestChecks[0].detailLines[0].seatNum
> - guestChecks[0].detailLines[0].menuItem
> - guestChecks[0].detailLines[0].menuItem.miNum
> - guestChecks[0].detailLines[0].menuItem.modFlag
> - guestChecks[0].detailLines[0].menuItem.inclTax
> - guestChecks[0].detailLines[0].menuItem.activeTaxes
> - guestChecks[0].detailLines[0].menuItem.prcLvl

</details>

# 1.2. Transcrição
> Arquivo <db_data.csv>

# 1.3. Abordagem escolhida
> A abordagem escolhida organiza os dados em um tipo de data lake simples com as chaves e valores, utilizando dois campos ('guestCheckId','guestCheckLineItemId') como chaves primárias.
> Esse tipo de organização facilita a busca, tratamento e categorização dos dados. É possível buscar informações detalhadas retornando apenas valores ou grupo de valores com aplicação de filtros sem, necessariamente, utilizar um arquivo JSON.


# 2.1. Por que armazenar os dados das APIs?
> O armazenamento dos dados das APIs aumenta a disponibilidade do dado e também o preparo prévio para consumo. Nem sempre o padrão retornado por uma API é ideal para utilização em todos os contextos. Quando estes dados são salvos, a atualização do formato nos permite ter mais agilidade nas buscas e facilidade no uso.

# 2.2. Como armazenar os arquivos
> O modelo apresentado para a API '/res/getGuestChecks' pode ser reproduzido para todas as APIs em novas tabelas para reduzir o tamanho geral de linhas em uma única tabela. Ainda assim, é possível reaproveitar a mesma tabela com a adição de uma nova coluna - que representa a API de origem do dado.

# 2.3. Alteração para guestChecks.taxation
> No algoritmo atual não haveria alteração, contudo, é necessário observar questões importante na recuperação desses dados para consumo.
> Duas abordagens podem ser adotadas e ambas com seus benefícios e malefícios.
> A primeira abordagem seria apenas documentar a alteração para que novas buscas utilizem tanto a chave 'guestChecks/taxation' quanto 'guestChecks/taxes', evitando que os dados recuperados venham incompletos. Essa abordagem é simples e adiciona etapas a mais para o desenvolvedor que trabalhará com o os dados, fazendo necessário o conhecimento prévio da alteração mediante consulta em documentações.
> A segunda abordagem considera a atualização das chaves no banco para o novo nome. A vantagem é a não necessidade de utilizar mais de uma chave nas buscas, porém a desvantagem que esse tratamento apresenta é muito maior do que o outro pois pode afetar códigos já em produção - seria necessária uma revisão em todos os sistemas que utilizam esses dados para atualização.