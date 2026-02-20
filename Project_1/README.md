# 📝 Todo List em Python

Aplicação de lista de tarefas no terminal desenvolvida em **Python**, com persistência de dados utilizando **JSON**.

Este projeto foi criado com o objetivo de praticar lógica de programação, manipulação de arquivos, tratamento de exceções e organização de código.

---

## 📌 Estrutura de Dados

Cada tarefa é representada como um dicionário:

```python
{"descricao": "estudar python", "status": "pendente"}
```

Todas as tarefas são armazenadas em uma lista:

```python
tarefas = []
```

Os dados são persistidos no arquivo:

```
tarefas.json
```

---

## ⚙️ O programa possui:

1. 🔁 Um loop principal que roda até o usuário escolher sair  
2. 📋 Um menu interativo com opções numeradas  
3. 🛠 5 funcionalidades principais:
   - ➕ Adicionar tarefa
   - 📋 Listar tarefas
   - ✅ Concluir tarefa
   - ❌ Remover tarefa
   - 🚪 Sair do programa
4. 💾 Persistência de dados utilizando arquivo JSON  
5. ⚠️ Tratamento de erros:
   - Número inválido
   - Entrada não numérica
   - Arquivo inexistente
   - JSON inválido ou corrompido
6. 💬 Mensagens claras de confirmação, erro e aviso ao usuário

---

## 🧠 Fluxo do Programa

```
Mostra menu → Usuário escolhe opção → Executa ação → Retorna ao menu
```

Ao listar tarefas, o status é exibido com emojis:

```
0 - estudar python ⏳
1 - treinar lógica ✅
```

- ⏳ = Pendente  
- ✅ = Concluída  

---

## 💾 Persistência com JSON

Ao iniciar o programa:

- Se `tarefas.json` existir → os dados são carregados
- Se não existir → uma lista vazia é criada automaticamente
- Ao adicionar, concluir ou remover tarefas → o arquivo é atualizado

Isso garante que as tarefas permaneçam salvas mesmo após fechar o programa.

---

## 🚀 Como Executar

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
```

2. Entre na pasta do projeto:

```bash
cd todo-python
```

3. Execute o programa:

```bash
python todo.py
```

---

## 📚 Tecnologias Utilizadas

- Python 3
- Biblioteca padrão `json`

---

## 🎯 Objetivo do Projeto

Consolidar fundamentos de:

- Estruturas de dados (listas e dicionários)
- Manipulação de arquivos
- Tratamento de exceções
- Organização básica de código
- Persistência de dados com JSON

---

## 📈 Possíveis Melhorias Futuras

- Refatoração completa para funções independentes
- Versão orientada a objetos
- Uso de SQLite no lugar de JSON
- Interface gráfica ou versão web (Flask ou FastAPI)
- Filtro de tarefas por status (pendente/concluída)
- Sistema de prioridade ou datas