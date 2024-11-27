# Pacotes usados
import json

# Função para extração de chaves do JSON
def extract_keys(obj, parent_key=''):
    keys = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            full_key = f"{parent_key}.{k}" if parent_key else k
            keys.append(full_key)
            if isinstance(v, (dict, list)):
                keys.extend(extract_keys(v, full_key))
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            full_key = f"{parent_key}[{i}]"
            keys.append(full_key)
            if isinstance(item, (dict, list)):
                keys.extend(extract_keys(item, full_key))
    return keys

# Função auxiliar para recuperar dado do json dado um caminho
def get_data(path,json):
    data = json
    for item in path:
        if item.endswith('[0]'):
            data = data[item.replace('[0]','')][0]
        else:
            data = data[item]
    return data

# Carregamento dos dados
with open('ERP.json', 'r') as f:
    erp_data = json.load(f)

# Descrição do JSOn
erp_keys = extract_keys(erp_data)
print("\n".join(erp_keys))

# Tratamento dos dados para apresentação em tabela/data lake
database_keys = []
primary_keys = []
desired_primary_keys = ['guestCheckId','guestCheckLineItemId']
for key in erp_keys:
    if not any(text in key for text in desired_primary_keys):
        database_keys.append(key)
    else:
        primary_keys.append(key)
        
# Algumas chaves precisam ser eliminadas porque retornam outra estrutura com mais de um par chave-valor
# Interessa apenas caminhos que retornam único par chave-valor   
keys_to_remove = []
for item in database_keys:
    aux = []
    for key in database_keys:
        if any(text in key for text in [item]):
            aux.append(key)
    if len(aux)>1:
        keys_to_remove.append(item)        

database_keys = [item for item in database_keys if not item.endswith('[0]') and not item in keys_to_remove]

# Tratamento simples dos dados para criar um arquivo csv que representa a tabela no banco
db_data = 'guestCheckId,guestCheckLineItemId,key,data\n'
for key in database_keys:
    db_line = ''
    for p_key in primary_keys:
        path = p_key.split('.')
        if ('guestCheckId' in path):
            db_line = db_line + str(get_data(path,erp_data)) + ','
        else:
            db_line = db_line + str(get_data(path,erp_data)) + ','
    db_line = db_line + (key.replace('.','/').replace('[0]','')) + ','
    path = key.split('.')
    db_line = db_line + str(get_data(path,erp_data)) + '\n'
    db_data=db_data+db_line
    
with open('db_data.csv', 'w') as outfile:
    outfile.write(db_data)
    
# APIs - para cada uma, um ID e um tratameno diferente
# No caso da /res/getGuestChecks, usar o tratamento acima
