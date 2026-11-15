from pathlib import Path
import re, json
p=Path(__file__).with_name('Loja_Drica_PIX.html')
s=p.read_text(encoding='utf-8')
print('LOJA DRICA - CONFIGURAR PIX')
print('Use o nome e a cidade oficiais do titular da chave no aplicativo do banco.')
nome=input('Nome real do recebedor: ').strip()
cidade=input('Cidade do recebedor (sem UF): ').strip()
if not (2<=len(nome)<=25 and 2<=len(cidade)<=15):
 raise SystemExit('Erro: nome 2-25 caracteres; cidade 2-15 caracteres.')
print('\nIMPORTANTE: os preços atuais do catálogo eram ILUSTRATIVOS.')
print('Antes de habilitar qualquer pagamento, você DEVE alterar os preços no cadastro PRODUCTS do HTML.')
confirma=input('Você já conferiu e atualizou TODOS os preços com os valores reais? (digite CONFIRMO): ').strip()
if confirma!='CONFIRMO':raise SystemExit('Nenhuma cobrança habilitada: preços não confirmados.')
def js(v):return json.dumps(v,ensure_ascii=True)
for prop,value in [('titular',nome),('cidade',cidade)]:
 pattern=r"("+prop+r"\s*:\s*)'[^']*'"
 s,n=re.subn(pattern,lambda m:m.group(1)+js(value),s,count=1)
 if n!=1:raise SystemExit('Falha ao atualizar '+prop)
s,n=re.subn(r'(catalogoConferido\s*:\s*)false',r'\g<1>true',s,count=1)
if n!=1:raise SystemExit('Falha ao confirmar catálogo')
p.with_name('Loja_Drica_PIX_Configurada.html').write_text(s,encoding='utf-8')
print('Criado: Loja_Drica_PIX_Configurada.html')
print('Revise os preços e teste a leitura Pix em app bancário antes de publicar.')
