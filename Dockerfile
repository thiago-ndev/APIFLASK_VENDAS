# Use a imagem base do Ubuntu
FROM ubuntu:latest

# Evita prompts interativos durante a instalação
ENV DEBIAN_FRONTEND=noninteractive

# Atualiza os pacotes e instala as dependências necessárias
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    default-mysql-client \
    libmysqlclient-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Cria e ativa um ambiente virtual
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copia os arquivos do seu projeto para o container
COPY . /app
WORKDIR /app

# Instala as dependências do Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Define o comando padrão para executar quando o container iniciar
# Substitua `your_application.py` pelo script de entrada da sua aplicação
CMD ["python3", "app.py"]
