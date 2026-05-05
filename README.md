Este projeto é um artefato técnico desenvolvido para a disciplina de Projeto Interdisciplinar para Sistemas de Informação 3 (PISI3) do 3° período do curso de Bacharelado em Sistemas de Informação (BSI) e do Programa de Pós-Graduação em Informática Aplicada da Universidade Federal Rural de Pernambuco (UFRPE).

por: Claudiany Martins (claudiany.martins@ufrpe.br)


##  Dataset para Classificação de Câncer de Mama (1M de Amostras, 40 Atributos) 

### Dataset information
[kaggle - Breast Cancer Dataset ](https://www.kaggle.com/datasets/sharmajicoder/breast-cancer-dataset?select=breast_cancer_40_features_1M.csv)
 
O câncer de mama é um dos tipos de câncer mais comuns que afetam mulheres em todo o mundo. A detecção precoce aumenta significativamente as chances de sucesso no tratamento. Modelos de **Machine Learning** são cada vez mais utilizados para auxiliar médicos na identificação de tumores malignos com base em características clínicas e celulares.

Este dataset foi criado para apoiar a pesquisa e a experimentação em aprendizado de máquina para diagnóstico médico, especificamente para a classificação do câncer de mama.

O dataset contém **1.000.000 de amostras de pacientes** com **40 atributos numéricos** que descrevem características do tumor, como geometria, textura, densidade celular e propriedades nucleares.

### Características do Conjunto de Dados

| Propriedade | Valor |
| :--- | :--- |
| Total de Amostras | 1.000.000 |
| Total de Atributos (Features) | 40 |
| Variável Alvo (Target) | `diagnosis` |
| Classes | Binária (Benigno / Maligno) |
| Formato do Arquivo | CSV |
| Tipo de Tarefa | Classificação Binária |

### Variável Alvo
**`diagnosis`**

| Valor | Significado |
| :--- | :--- |
| 0 | Tumor Benigno |
| 1 | Tumor Maligno |

O rótulo alvo foi gerado usando uma pontuação de risco derivada de múltiplos indicadores tumorais, simulando padrões de diagnóstico do mundo real.

**Distribuição aproximada das classes:**
* Benigno: ~65%
* Maligno: ~35%

---

### Descrição dos Atributos (Features)
Os atributos representam múltiplas características biológicas e morfológicas dos tumores.

#### Geometria do Tumor
Descrevem o tamanho e a estrutura do tumor.

| Atributo | Descrição |
| :--- | :--- |
| `radius_mean` | Raio médio do tumor |
| `perimeter_mean` | Perímetro médio das células tumorais |
| `area_mean` | Área média do tumor |
| `radius_worst` | Maior raio medido |
| `area_worst` | Maior área tumoral observada |

#### Textura e Forma
Capturam irregularidades na estrutura do tumor.

| Atributo | Descrição |
| :--- | :--- |
| `texture_mean` | Variações médias de textura |
| `smoothness_mean` | Suavidade da borda do tumor |
| `compactness_mean` | Compacidade da forma do tumor |
| `concavity_mean` | Grau de porções côncavas |
| `concave_points_mean` | Número de pontos côncavos |
| `symmetry_mean` | Simetria da estrutura tumoral |
| `fractal_dimension_mean` | Complexidade da borda do tumor |

#### Medições de Erro Padrão (SE)
Representam a variação nas medições.
*(Inclui `_se` para todos os atributos acima: raio, textura, perímetro, área, suavidade, compacidade, concavidade, pontos côncavos, simetria e dimensão fractal).*

#### Medições do Pior Caso (Worst)
Representam os valores mais extremos registrados (geralmente a média dos três maiores valores).
*(Inclui `_worst` para todos os atributos de geometria e forma citados anteriormente).*

#### Atributos Celulares e Biológicos
Simulam propriedades celulares microscópicas.

| Atributo | Descrição |
| :--- | :--- |
| `cell_density` | Densidade de células no tecido tumoral |
| `nucleus_size` | Tamanho médio dos núcleos celulares |
| `nucleus_texture` | Variação na textura do núcleo |
| `mitosis_rate` | Taxa de divisão celular |
| `tumor_border_irregularity` | Irregularidade das bordas do tumor |
| `chromatin_density` | Concentração de cromatina no núcleo |
| `cell_variation` | Variação nos tamanhos das células |
| `nuclear_variation` | Variação nas formas dos núcleos |
| `cytoplasm_ratio` | Razão entre citoplasma e núcleo |
| `cell_clump_thickness` | Espessura dos aglomerados celulares |

---

### Instalação

1. Instalar as dependencias

   ```
   $ pip install -r requirements.txt
   ```

2. Executar o app

   ```
   $ streamlit run streamlit_app.py
   ```

