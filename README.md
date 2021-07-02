# Canvas Explorer

<h4 align="center"> 
	🚧  🚀 Em construção...  🚧
</h4>

### Este é um projeto independente, criado com o intuito de prover formas de rastrear fóruns aos quais um determinado perfil do Canvas Instructure tem acesso. O funcionamento é simples: o módulo canvas acessa a API do Instructure de forma iterativa e capta todas as interações - posts de alunos com a regra de não ter sido respondido por ninguém do corpo técnico da instituição e com data de postagem recente (30 dias por exemplo) e cria cards em um board do Trello especificado na configuração.
### Para o funcionamento da ferramenta, o arquivo credentials.yml deve ser criado no diretório src, com a seguinte estrutura:

- bearer_token
- base_url
- mentor_list
- coordinators
- tutors
- mentors
- trello_key
- trello_token
- trello_list
- mentor_list *Apenas para essa versão do módulo
- topics_list *Apenas para essa versão do módulo

### Features

- [x] Scan dos posts no Canvas
- [x] Criação do card no Trello
- [ ] Criação de uma base de conhecimento

### Como executar via Docker?

docker build -t canvas . 
docker run canvas:latest
