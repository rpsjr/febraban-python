#!/usr/bin/python
# -*- coding: latin-1 -*-

errors03 = {
    "03": "AG. COBRADORA: NÃO FOI POSSÍVEL ATRIBUIR A AGÊNCIA PELO CEP OU CEP INVÁLIDO",
    "04": "ESTADO: SIGLA DO ESTADO INVÁLIDA",
    "05": "DATA VENCIMENTO: PRAZO DA OPERAÇÃO MENOR QUE PRAZO MÍNIMO OU MAIOR QUE O MÁXIMO",
    "08": "NOME DO PAGADOR: NÃO INFORMADO OU DESLOCADO",
    "09": "AGÊNCIA/CONTA: AGÊNCIA ENCERRADA",
    "10": "LOGRADOURO: NÃO INFORMADO OU DESLOCADO",
    "11": "CEP: CEP NÃO NUMÉRICO",
    "12": "SACADOR AVALISTA: NOME NÃO INFORMADO OU DESLOCADO",
    "13": "ESTADO/CEP: CEP INCOMPATÍVEL COM A SIGLA DO ESTADO",
    "14": "NOSSO NÚMERO: NOSSO NÚMERO JÁ REGISTRADO NO CADASTRO DO BANCO OU FORA DA FAIXA",
    "15": "NOSSO NÚMERO: NOSSO NÚMERO EM DUPLICIDADE NO MESMO MOVIMENTO",
    "18": "DATA DE ENTRADA: DATA DE ENTRADA INVÁLIDA PARA OPERAR COM ESTA CARTEIRA",
    "19": "OCORRÊNCIA: OCORRÊNCIA INVÁLIDA",
    "21": "AG. COBRADORA: CARTEIRA NÃO ACEITA DEPOSITÁRIA CORRESPONDENTE/ ESTADO DA AGÊNCIA DIFERENTE DO ESTADO DO PAGADOR/ AG. COBRADORA NÃO CONSTA NO CADASTRO OU ENCERRANDO",
    "22": "CARTEIRA: CARTEIRA NÃO PERMITIDA (NECESSÁRIO CADASTRAR FAIXA LIVRE)",
    "27": "CNPJ INAPTO: CNPJ DO BENEFICIÁRIO INAPTO DEVOLUÇÃO DE TÍTULO EM GARANTIA",
    "29": "CÓDIGO EMPRESA: CATEGORIA DA CONTA INVÁLIDA",
    "31": "AGÊNCIA/CONTA: CONTA NÃO TEM PERMISSÃO PARA PROTESTAR (CONTATE SEU GERENTE)",
    "35": "VALOR DO IOF: IOF MAIOR QUE 5%",
    "36": "QTDADE DE MOEDA: QUANTIDADE DE MOEDA INCOMPATÍVEL COM VALOR DO TÍTULO",
    "37": "CNPJ/CPF DO PAGADOR: NÃO NUMÉRICO OU IGUAL A ZEROS",
    "42": "NOSSO NÚMERO: NOSSO NÚMERO FORA DA FAIXA",
    "52": "AG. COBRADORA: EMPRESA NÃO ACEITA BANCO CORRESPONDENTE",
    "53": "AG. COBRADORA: EMPRESA NÃO ACEITA BANCO CORRESPONDENTE - COBRANÇA MENSAGEM",
    "54": "DATA DE VENCTO: BANCO CORRESPONDENTE – TÍTULO COM VENCIMENTO INFERIOR A 15 DIAS",
    "55": "DEP./BCO. CORRESP.: CEP NÃO PERTENCE A DEPOSITÁRIA INFORMADA",
    "56": "DT. VCTO./BCO. CORESP.: VENCTO. SUPERIOR A 180 DIAS DA DATA DE ENTRADA",
    "57": "DATA DE VENCIMENTO: CEP SÓ DEPOSITÁRIA BCO. DO BRASIL COM VENCTO. INFERIOR A 8 DIAS",
    "60": "ABATIMENTO: VALOR DO ABATIMENTO INVÁLIDO",
    "61": "JUROS DE MORA: JUROS DE MORA MAIOR QUE O PERMITIDO",
    "62": "DESCONTO: VALOR DO DESCONTO MAIOR QUE O VALOR DO TÍTULO",
    "63": "DESCONTO DE ANTECIPAÇÃO: VALOR DA IMPORTÂNCIA POR DIA DE DESCONTO (IDD) NÃO PERMITIDO",
    "64": "EMISSÃO DO TÍTULO: DATA DE EMISSÃO DO TÍTULO INVÁLIDA (VENDOR)",
    "65": "TAXA FINANCTO.: TAXA INVÁLIDA (VENDOR)",
    "66": "DATA DE VENCTO.: INVALIDA/FORA DE PRAZO DE OPERAÇÃO (MÍNIMO OU MÁXIMO)",
    "67": "VALOR/QTIDADE.: VALOR DO TÍTULO/QUANTIDADE DE MOEDA INVÁLIDO",
    "68": "CARTEIRA: CARTEIRA INVÁLIDA OU NÃO CADASTRADA NO INTERCÂMBIO DA COBRANÇA",
    "98": "FLASH INVÁLIDO: REGISTRO MENSAGEM SEM FLASH CADASTRADO OU FLASH INFORMADO DIFERENTE DO CADASTRADO",
    "99": "FLASH INVÁLIDO: CONTA DE COBRANÇA COM FLASH CADASTRADO E SEM REGISTRO DE MENSAGEM CORRESPONDENTE",
}

errors17 = {
    "02": "AGÊNCIA COBRADORA INVÁLIDA OU COM O MESMO CONTEÚDO",
    "04": "SIGLA DO ESTADO INVÁLIDA",
    "05": "DATA DE VENCIMENTO INVÁLIDA OU COM O MESMO CONTEÚDO",
    "06": "VALOR DO TÍTULO COM OUTRA ALTERAÇÃO SIMULTÂNEA",
    "08": "NOME DO PAGADOR COM O MESMO CONTEÚDO",
    "11": "CEP INVÁLIDO",
    "12": "NÚMERO INSCRIÇÃO INVÁLIDO DO SACADOR AVALISTA",
    "13": "SEU NÚMERO COM O MESMO CONTEÚDO",
    "21": "AGÊNCIA COBRADORA NÃO CONSTA NO CADASTRO DE DEPOSITÁRIA OU EM ENCERRAMENTO",
    "42": "ALTERAÇÃO INVÁLIDA PARA TÍTULO VENCIDO",
    "43": "ALTERAÇÃO BLOQUEADA – VENCIMENTO JÁ ALTERADO",
    "53": "INSTRUÇÃO COM O MESMO CONTEÚDO",
    "54": "DATA VENCIMENTO PARA BANCOS CORRESPONDENTES INFERIOR AO ACEITO PELO BANCO",
    "55": "ALTERAÇÕES IGUAIS PARA O MESMO CONTROLE (AGÊNCIA/CONTA/CARTEIRA/NOSSO NÚMERO)",
    "60": "VALOR DE IOF – ALTERAÇÃO NÃO PERMITIDA PARA CARTEIRAS DE N.S. – MOEDA VARIÁVEL",
    "61": "TÍTULO JÁ BAIXADO OU LIQUIDADO OU NÃO EXISTE TÍTULO CORRESPONDENTE NO SISTEMA",
    "66": "ALTERAÇÃO NÃO PERMITIDA PARA CARTEIRAS DE NOTAS DE SEGUROS – MOEDA VARIÁVEL",
    "67": "NOME INVÁLIDO DO SACADOR AVALISTA",
    "72": "ENDEREÇO INVÁLIDO – SACADOR AVALISTA",
    "73": "BAIRRO INVÁLIDO – SACADOR AVALISTA",
    "74": "CIDADE INVÁLIDA – SACADOR AVALISTA",
    "75": "SIGLA ESTADO INVÁLIDO – SACADOR AVALISTA",
    "76": "CEP INVÁLIDO – SACADOR AVALISTA",
    "81": "ALTERAÇÃO BLOQUEADA - TÍTULO COM NEGATIVAÇÃO EXPRESSA OU PROTESTO",
}

errors16 = {
    "01": "INSTRUÇÃO/OCORRÊNCIA NÃO EXISTENTE",
    "03": "CONTA NÃO TEM PERMISSÃO PARA PROTESTAR (CONTATE SEU GERENTE) 06 NOSSO NÚMERO IGUAL A ZEROS",
    "09": "CNPJ/CPF DO SACADOR/AVALISTA INVÁLIDO",
    "14": "REGISTRO EM DUPLICIDADE",
    "15": "CNPJ/CPF INFORMADO SEM NOME DO SACADOR/AVALISTA",
    "19": "VALOR DO ABATIMENTO MAIOR QUE 90% DO VALOR DO TÍTULO",
    "20": "EXISTE SUSTACAO DE PROTESTO PENDENTE PARA O TITULO",
    "21": "TÍTULO NÃO REGISTRADO NO SISTEMA",
    "22": "TÍTULO BAIXADO OU LIQUIDADO",
    "23": "INSTRUÇÃO NÃO ACEITA",
    "24": "INSTRUÇÃO INCOMPATÍVEL - EXISTE INSTRUÇÃO DE PROTESTO PARA O TÍTULO",
    "25": "INSTRUÇÃO INCOMPATÍVEL - NÃO EXISTE INSTRUÇÃO DE PROTESTO PARA O TÍTULO",
    "26": "INSTRUÇÃO NÃO ACEITA POR JÁ TER SIDO EMITIDA A ORDEM DE PROTESTO AO CARTÓRIO",
    "27": "INSTRUÇÃO NÃO ACEITA POR NÃO TER SIDO EMITIDA A ORDEM DE PROTESTO AO CARTÓRIO",
    "28": "JÁ EXISTE UMA MESMA INSTRUÇÃO CADASTRADA ANTERIORMENTE PARA O TÍTULO",
    "29": "VALOR LÍQUIDO + VALOR DO ABATIMENTO DIFERENTE DO VALOR DO TÍTULO REGISTRADO",
    "30": "EXISTE UMA INSTRUÇÃO DE NÃO PROTESTAR ATIVA PARA O TÍTULO",
    "31": "EXISTE UMA OCORRÊNCIA DO PAGADOR QUE BLOQUEIA A INSTRUÇÃO",
    "32": "DEPOSITÁRIA DO TÍTULO = 9999 OU CARTEIRA NÃO ACEITA PROTESTO",
    "33": "ALTERAÇÃO DE VENCIMENTO IGUAL À REGISTRADA NO SISTEMA OU QUE TORNA O TÍTULO VENCIDO",
    "34": "INSTRUÇÃO DE EMISSÃO DE AVISO DE COBRANÇA PARA TÍTULO VENCIDO ANTES DO VENCIMENTO",
    "35": "SOLICITAÇÃO DE CANCELAMENTO DE INSTRUÇÃO INEXISTENTE",
    "36": "TÍTULO SOFRENDO ALTERAÇÃO DE CONTROLE (AGÊNCIA/CONTA/CARTEIRA/NOSSO NÚMERO)",
    "37": "INSTRUÇÃO NÃO PERMITIDA PARA A CARTEIRA",
    "40": "INSTRUÇÃO INCOMPATÍVEL – NÃO EXISTE INSTRUÇÃO DE NEGATIVAÇÃO EXPRESSA PARA O TÍTULO",
    "41": "INSTRUÇÃO NÃO PERMITIDA – TÍTULO JÁ ENVIADO PARA NEGATIVAÇÃO EXPRESSA",
    "42": "INSTRUÇÃO NÃO PERMITIDA – TÍTULO COM NEGATIVAÇÃO EXPRESSA CONCLUÍDA",
    "43": "PRAZO INVÁLIDO PARA NEGATIVAÇÃO – MÍNIMO: 02 DIAS CORRIDOS APÓS O VENCIMENTO",
    "45": "INSTRUÇÃO INCOMPATÍVEL PARA O MESMO TÍTULO NESTA DATA",
    "47": "INSTRUÇÃO NÃO PERMITIDA – ESPÉCIE INVÁLIDA",
    "48": "DADOS DO PAGADOR INVÁLIDOS (CPF / CNPJ / NOME)",
    "49": "DADOS DO ENDEREÇO DO PAGADOR INVÁLIDOS",
    "50": "DATA DE EMISSÃO DO TÍTULO INVÁLIDA",
    "51": "INSTRUÇÃO NÃO PERMITIDA – TÍTULO COM NEGATIVAÇÃO EXPRESSA AGENDADA",
}

errors15 = {
    "04": "NOSSO NÚMERO EM DUPLICIDADE NUM MESMO MOVIMENTO",
    "05": "SOLICITAÇÃO DE BAIXA PARA TÍTULO JÁ BAIXADO OU LIQUIDADO",
    "06": "SOLICITAÇÃO DE BAIXA PARA TÍTULO NÃO REGISTRADO NO SISTEMA",
    "07": "COBRANÇA PRAZO CURTO - SOLICITAÇÃO DE BAIXA P/ TÍTULO NÃO REGISTRADO NO SISTEMA",
    "08": "SOLICITAÇÃO DE BAIXA PARA TÍTULO EM FLOATING",
}

errors18 = {
    "16": "ABATIMENTO/ALTERAÇÃO DO VALOR DO TÍTULO OU SOLICITAÇÃO DE BAIXA BLOQUEADOS",
    "40": "NÃO APROVADA DEVIDO AO IMPACTO NA ELEGIBILIDADE DE GARANTIAS",
    "41": "AUTOMATICAMENTE REJEITADA",
    "42": "CONFIRMA RECEBIMENTO DE INSTRUÇÃO – PENDENTE DE ANÁLISE",
}
