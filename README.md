# Módulo de Validação de Cadastros

Este repositório contém as funções de validação utilizadas no sistema de cadastros da empresa, implementadas utilizando a metodologia TDD (Test-Driven Development) e versionamento com Git Flow.

## Funcionalidade: Validador de CEP

A função `validar_cep(cidade, cep)` verifica se o CEP fornecido pelo usuário corresponde à faixa de CEPs registrada para a cidade informada. A validação lida automaticamente com máscaras de formatação (pontos e traços).

### Exemplos de Uso e Validação

[cite_start]Abaixo estão os cenários de teste documentados para homologação do sistema:

**CEPs Válidos (Retornam `True`):**

- [cite_start]CEP: 18.050-100 - Cidade: Sorocaba [cite: 569]
- [cite_start]CEP: 18.195-000 - Cidade: Capela do Alto [cite: 570]
- [cite_start]CEP: 18.130-020 - Cidade: São Roque [cite: 571]

**CEPs Inválidos (Retornam `False`):**

- [cite_start]CEP: 19.000-000 - Cidade: Votorantim (CEP fora da faixa da cidade) [cite: 572]

## Como rodar os testes

Os testes automatizados foram construídos utilizando a biblioteca `pytest`. Para executá-los, certifique-se de estar na raiz do projeto e rode o seguinte comando no terminal:

```bash
python -m pytest -v
```
