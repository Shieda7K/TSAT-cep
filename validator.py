import re

FAIXAS_CEP = {
    "Aluminio": (18125000, 18129999),
    "Ipero": (18560000, 18569999),
    "Aracariguama": (18147000, 18149999),
    "Aracoiaba da Serra": (18190000, 18194999),
    "Itu": (13300000, 13314999),
    "Mairinque": (18120000, 18124999),
    "Cabreuva": (13315000, 13319999),
    "Capela do Alto": (18195000, 18199999),
    "Salto": (13320000, 13329999),
    "Salto de Pirapora": (18160000, 18169999),
    "São Roque": (18130000, 18146999), 
    "Sarapui": (18225000, 18229999),
    "Sorocaba": (18000000, 18109999),
    "Votorantim": (18110000, 18119999),
    "Porto Feliz": (18540000, 18549999)
}

def validar_cep(cidade, cep):
    cep_limpo = int(re.sub(r'\D', '', cep))

    if cidade in FAIXAS_CEP:
        min_cep, max_cep = FAIXAS_CEP[cidade]
        return min_cep <= cep_limpo <= max_cep
    return False

#fingindo