# Análise dos programas de Pós-Graduação no Brasil em 2018.
## Trabalho para a disciplina de Laboratório de Banco de Dados
### Discentes: Bruno Carvalho Ferro & Leonardo Tamanhão
### Docente: Professor Fernando Masanori

# Requirements

## Utilizamos o Jupyter Notebook, Anaconda e Python 3.7 para construção do projeto com as seguintes bibliotecas:

```
conda install pandas
conda install folium
conda install json
conda install matplotlib
```

## Rodando
Para mostrar a região com mais cursos em uma determinada área, troca-se o ensino pela área
```python
area = "MEDICINA"
df.loc[df["NM_AREA_CONHECIMENTO"] == area]["SG_UF_PROGRAMA"].value_counts().head().plot(kind='barh')
```
# Referências:
https://dadosabertos.capes.gov.br/

# Jupyter Notebook:
```
https://github.com/BuiuFerro/pos-graduacao_regioes/blob/master/P%C3%B3s-Gradua%C3%A7%C3%A3o%20por%20Estado.ipynb
```
