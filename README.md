# Automação de Presença - UNINTER

Este script Python foi desenvolvido para automatizar o processo de marcação de presença em disciplinas do curso de graduação EAD da UNINTER, utilizando a biblioteca Selenium.

## Pré-requisitos

Antes de executar o script, certifique-se de ter instalado os seguintes componentes:

- Python 3.12: [Download Python](https://www.python.org/downloads/)
- Certifique-se de ter o google chrome instalado.


## Como Usar

1. Clone este repositório:

   ```bash
   git clone https://github.com/AndreffSantos/Presenca-Uninter.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd Presenca-Uninter
   ```

3. Instale as dependências: 
   ```bash
   pip install -r requirements.txt
   ```

4. Modifique as credenciais no script:

   Modifique o nome do arquivo .env.exemple para .env e altere o RU e senha seguindo o que esta escrito no arquivo.


5. Execute o script:

   ```bash
   python main.py
   ```

6. Acompanhe a execução:

   O script abrirá um navegador automaticamente, fará login na plataforma AVA da UNINTER, navegará até a disciplina desejada e marcará sua presença.

Lembre-se de executar este script de maneira ética e em conformidade com as políticas da instituição. O uso inadequado pode resultar em penalidades.

Este projeto é fornecido como está, sem garantias de seu funcionamento contínuo, uma vez que as interfaces web podem ser alteradas. Certifique-se de ajustar o script conforme necessário.

**Aviso:** Este script foi desenvolvido para fins educacionais e não incentiva a prática de atividades proibidas ou antiéticas. Use-o de forma responsável.