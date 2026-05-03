Este projeto é um artefato técnico desenvolvido para a disciplina de Projeto Interdisciplinar para Sistemas de Informação 3 (PISI3) do 3° período do curso de Bacharelado em Sistemas de Informação (BSI) e do Programa de Pós-Graduação em Informática Aplicada da Universidade Federal Rural de Pernambuco (UFRPE).

por: Claudiany Martins (claudiany.martins@ufrpe.br)


##  VinBigData Chest X-ray Abnormalities Detection 
Duc Nguyen, DungNB, Ha Q. Nguyen, Julia Elliott, NguyenThanhNhan, and Phil Culliton. VinBigData Chest X-ray Abnormalities Detection. https://kaggle.com/competitions/vinbigdata-chest-xray-abnormalities-detection, 2020. Kaggle.

### Dataset information

O *dataset* **VinBigData** possui 18.000 exames de radiografia de tórax (CXR) em projeção posteroanterior (PA) no formato DICOM, os quais foram anonimizados para proteger a privacidade dos pacientes. Todas as imagens foram rotuladas por um painel de radiologistas experientes quanto à presença de 14 achados radiográficos críticos, listados abaixo:

- 0 - Aumento aórtico (*Aortic enlargement*)
- 1 - Atelectasia (*Atelectasis*)
- 2 - Calcificação (*Calcification*)
- 3 - Cardiomegalia (*Cardiomegaly*)
- 4 - Consolidação (*Consolidation*)
- 5 - Doença Pulmonar Intersticial (*ILD*)
- 6 - Infiltração (*Infiltration*)
- 7 - Opacidade Pulmonar (*Lung Opacity*)
- 8 - Nódulo/Massa (*Nodule/Mass*)
- 9 - Outra lesão (*Other lesion*)
- 10 - Derrame pleural (*Pleural effusion*)
- 11 - Espessamento pleural (*Pleural thickening*)
- 12 - Pneumotórax (*Pneumothorax*)
- 13 - Fibrose pulmonar (*Pulmonary fibrosis*)
- **14 - Sem achados** (*No finding*) - foi destinada a registrar a ausência de todos os achados listados acima. 

### Arquivos
* **train.csv**: Metadados do conjunto de treinamento, com uma linha para cada objeto detectado, incluindo a classe e a caixa delimitadora (*bounding box*). Algumas imagens, tanto no conjunto de teste quanto no de treinamento, possuem múltiplos objetos.


### Colunas
* **image_id**: Identificador único da imagem.
* **class_name**: Nome da classe do objeto detectado (ou "No finding").
* **class_id**: ID da classe do objeto detectado.
* **rad_id**: ID do radiologista que realizou a observação.
* **x_min**: Coordenada X mínima da caixa delimitadora do objeto.
* **y_min**: Coordenada Y mínima da caixa delimitadora do objeto.
* **x_max**: Coordenada X máxima da caixa delimitadora do objeto.
* **y_max**: Coordenada Y máxima da caixa delimitadora do objeto.


### Instalação

1. Instalar as dependencias

   ```
   $ pip install -r requirements.txt
   ```

2. Executar o app

   ```
   $ streamlit run streamlit_app.py
   ```

