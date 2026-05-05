# Medication Counter

## 📌 Descrição do Projeto

O **Medication Counter** é um projeto que utiliza técnicas de visão computacional para detectar e contar automaticamente medicamentos (como comprimidos) em uma imagem.

A aplicação processa uma imagem de entrada, identifica objetos relevantes com base em suas características visuais e exibe o total detectado, além de destacar cada item encontrado com elementos gráficos.

O objetivo principal do projeto é demonstrar o uso prático de técnicas de processamento de imagem e análise visual aplicadas a um problema do mundo real.

---

## ⚠️ Requisitos da Imagem (Importante)

Para que o sistema funcione corretamente, algumas condições devem ser respeitadas:

* **Alto contraste entre fundo e objetos**: O fundo deve ser visualmente distinto dos medicamentos (ex: comprimidos claros em fundo escuro ou vice-versa).

* **Objetos não sobrepostos ou agrupados**: Os medicamentos devem estar separados uns dos outros, sem contato direto. Agrupamentos dificultam a segmentação e podem gerar contagens incorretas.

* **Iluminação uniforme**: Evitar sombras fortes ou reflexos intensos que possam interferir na detecção.

* **Imagem nítida**: Baixo nível de ruído e boa qualidade visual ajudam na precisão do algoritmo.

---

## 🧠 Técnicas clássicas de Visão Computacional Utilizadas

### 1. Pré-processamento de imagem

* **Conversão para escala de cinza**: simplifica a análise removendo informações de cor.
* **CLAHE (Contrast Limited Adaptive Histogram Equalization)**: melhora o contraste local da imagem, facilitando a detecção de objetos mesmo com iluminação irregular.
* **Gaussian Blur**: reduz ruídos e suaviza a imagem.

### 2. Segmentação

* **Thresholding com método de Otsu**: separa automaticamente os objetos do fundo, criando uma imagem binária.
* **Inversão binária**: garante que os objetos de interesse sejam destacados corretamente.

### 3. Operações morfológicas

* **Abertura (Morphological Opening)**: remove pequenos ruídos.
* **Erosão**: ajuda a separar objetos que estão muito próximos ou agrupados.

### 4. Detecção de objetos

* **Detecção de contornos (Contours)**: identifica regiões que representam possíveis medicamentos.
* **Filtro por área**: elimina detecções irrelevantes (ruídos pequenos).

### 5. Análise geométrica

* **Minimum Area Rectangle**: cria caixas delimitadoras rotacionadas ao redor dos objetos detectados.

### 6. Visualização

* Desenho de contornos suavizados (anti-aliasing)
* Marcação do centro dos objetos
* Interface visual com contagem total exibida na imagem

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **OpenCV (cv2)** – processamento de imagem
* **NumPy** – manipulação de arrays

---

## ⚙️ Instalação e Dependências

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/medication-counter.git
cd medication-counter
```

### 2. Criar ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instalar dependências

```bash
pip install opencv-python numpy
```

---

## ▶️ Como Executar

1. Coloque a imagem que deseja analisar no diretório do projeto (ex: `remedio.png`)
2. Execute o script:

```bash
python main.py
```

3. O programa irá:

* Exibir a máscara binária processada
* Mostrar a imagem final com os objetos detectados
* Informar no terminal o número total de medicamentos encontrados

---

## 📷 Resultado Esperado

* Cada medicamento será destacado com uma caixa delimitadora
* Um marcador central será exibido
* Um contador individual aparecerá sobre cada item
* Um painel superior exibirá o total detectado
