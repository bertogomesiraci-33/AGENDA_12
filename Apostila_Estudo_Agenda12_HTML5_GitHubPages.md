# 📘 APOSTILA COMPLETA DE ESTUDOS: DESENVOLVIMENTO WEB I (HTML5) & GITHUB PAGES
**Componente Curricular:** Desenvolvimento de Sistemas I — Agenda 12  
**Instituição:** Centro Paula Souza (ETEC / CPS) — Curso Técnico em Desenvolvimento de Sistemas  
**Estudante:** Iraci Berto Gomes  
**Material de Base:** Apostila Oficial CETEC/GEEaD (*agenda_12_web_i_dsi_i_atualizada1_251.pdf*) e Guia Oficial (*como_hospedar_um_site_no_github_pages1.pdf*)  
**Projeto Prático Integrado:** *Meus Sites Favoritos* (`IraciBertoGomes_Ag12_DS_I.html` / `index.html`)

---

## 🎯 Apresentação e Objetivo deste Guia

Esta apostila foi elaborada especialmente para você, **Iraci**, consolidar com extrema clareza e profundidade **100% dos conceitos teóricos e práticos** ensinados na disciplina de Desenvolvimento de Sistemas I (Agenda 12) e no guia de publicação no GitHub Pages.

Aqui você encontrará:
1. Explicações detalhadas de cada conceito com linguagem simples e didática.
2. Todas as tags, atributos e regras oficiais ensinadas pelos professores Sandro Valérius e Paulo Eduardo Cardoso Andrade.
3. Como o seu projeto prático ("Meus Sites Favoritos") foi estruturado linha por linha.
4. Um **Simulado Preparatório com 15 Questões Comentadas** para você revisar e gabaritar a sua prova!

---

# MÓDULO 1: O Que É HTML e Como a Web Funciona?

### 1.1 O que significa a sigla HTML?
A sigla **HTML** significa **HyperText Markup Language** (em português: *Linguagem de Marcação de Hipertexto*).

- **HyperText (Hipertexto):** É o texto que contém conexões (links) para outros documentos, imagens ou recursos na web. É o que nos permite "navegar" de uma página para outra clicando com o mouse.
- **Markup (Marcação):** O HTML não é uma linguagem de programação (ele não possui variáveis matemáticas, cálculos lógicos ou laços de repetição). Ele é uma **linguagem de marcação**. Isso significa que ele usa marcadores especiais chamados **tags** para informar ao navegador o papel de cada pedaço de conteúdo (se é um título, parágrafo, imagem, link, etc.).
- **Language (Linguagem):** Conjunto padronizado de regras e termos compreendidos por todos os navegadores do mundo (Google Chrome, Edge, Firefox, Safari, etc.).

> 📌 **Pergunta clássica de prova:**  
> *O HTML é uma linguagem de programação?*  
> **Resposta:** **NÃO!** O HTML é uma **linguagem de marcação de texto**. Quem executa a lógica de programação na web é o JavaScript, e quem cuida do estilo visual é o CSS. O HTML é responsável apenas pela **estrutura e pelo conteúdo** da página.

### 1.2 O papel do Navegador Web (Browser)
O navegador (Chrome, Edge, Firefox) é um programa leitor e tradutor (interpretador). 
- Ele lê o arquivo de texto puro `.html`.
- Ele **não mostra as tags** para a pessoa que está usando a página.
- Ele **renderiza** o resultado visual na tela com base no que cada tag ordenou.

---

# MÓDULO 2: A Estrutura Básica Obrigatória do HTML5

Todo documento HTML5 profissional deve conter uma estrutura padrão. Se você abrir o Visual Studio Code em um arquivo vazio `.html` e digitar o atalho `html:5` pressionando Enter, ele criará exatamente esta base:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Título da Página</title>
</head>
<body>
    <!-- Aqui entra todo o conteúdo visível -->
</body>
</html>
```

Vamos dissecar cada uma dessas linhas:

---

### 2.1 A Declaração `<!DOCTYPE html>`
- **O que é:** É uma **instrução** (declaração de tipo de documento) enviada ao navegador.
- **Atenção:** `<!DOCTYPE html>` **NÃO é uma tag HTML!** Não possui fechamento (`</...>`).
- **Função:** Informa ao navegador qual a versão do HTML deve ser utilizada para renderizar a página. Ao escrever apenas `<!DOCTYPE html>`, estamos dizendo: *"Navegador, use o padrão moderno **HTML5**"*.

> 📚 **Comparativo histórico cobrado em provas (Página 9 da apostila):**
> - **HTML5:** `<!DOCTYPE html>` *(simples, curto e universal)*
> - **HTML 4.01 Strict:** `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">`
> - **HTML 4.01 Transitional:** `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">`
> - **HTML 4.01 Frameset:** `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" "http://www.w3.org/TR/html4/frameset.dtd">`
>
> *Hoje a regra oficial do W3C é usar sempre a versão mais recente: HTML5.*

---

### 2.2 A Tag Raiz `<html>` e o Atributo `lang`
- A tag `<html>` é o elemento **raiz** (root) de todo o documento. Todas as outras tags da página ficam dentro dela.
- Fecha no final do arquivo: `</html>`.
- **Atributo `lang="pt-br"`:** Define o idioma predominante do texto como **Português do Brasil**.
  * Serve para que leitores de tela para pessoas com deficiência visual saibam a pronúncia correta das palavras.
  * Serve para que navegadores não fiquem perguntando se você quer traduzir a página.
  * Serve para que motores de busca (Google) entreguem a página a pessoas que buscam em português.

> 💡 **Conceito de Atributos:**
> Os atributos adicionam propriedades às tags. Ficam sempre dentro da tag de abertura `<tag atributo="valor">`.
> - **Atributos Globais:** Podem ser usados em qualquer tag HTML (ex.: `id`, `class`, `title`).
> - **Atributos Específicos:** Pertencem exclusivamente a certas tags (ex.: `src` e `alt` na tag `<img>`; `href` e `target` na tag `<a>`).

---

### 2.3 A Tag `<head>` (Cabeçalho Técnico / Metadados)
- Funciona como o cabeçalho técnico de um trabalho escolar.
- O que é colocado entre `<head>` e `</head>` **não aparece diretamente na janela branca do site**.
- Guarda **metadados** (dados sobre os dados da página), configurações técnicas e o título da aba.

Dentro do `<head>` encontramos as seguintes tags essenciais:

#### 1. `<meta charset="UTF-8">`
- Define a codificação universal de caracteres para a tabela **UTF-8** (Unicode).
- **Para que serve:** Garante que caracteres especiais do português, como acentos (`á`, `é`, `õ`, `ê`) e cedilha (`ç`), sejam exibidos perfeitamente sem virar símbolos estranhos ou corrompidos.
- *Outras tabelas mais antigas:* ASCII, ANSI, ISO-8859-1 (Latin-1). O UTF-8 é o padrão moderno da Web mundial.

#### 2. `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- Configuração de responsividade da área visível (*viewport*).
- `width=device-width`: Faz a largura do site se ajustar automaticamente à largura da tela do aparelho (seja um monitor grande, um notebook ou um celular pequeno).
- `initial-scale=1.0`: Define o nível de zoom inicial normal (100%) quando a página é aberta.
- Sem essa tag, no celular o site pareceria uma versão minúscula e distante de tela de computador.

#### 3. `<meta http-equiv="X-UA-Compatible" content="ie=edge">`
- Instrução de compatibilidade que força navegadores antigos da Microsoft (como Internet Explorer) a utilizarem seu motor de renderização mais recente.

#### 4. `<title>Título</title>`
- É **obrigatória** dentro do `<head>`.
- O texto colocado entre `<title>` e `</title>` aparece na **aba (guia) do navegador** e quando o usuário salva o site nos Favoritos.
- Na atividade da Agenda 12, a exigência oficial foi: `<title>Meus sites favoritos</title>`.

---

### 2.4 A Tag `<body>` (Corpo Visível da Página)
- Tudo o que o usuário enxerga, lê e clica na janela do navegador fica obrigatoriamente dentro de `<body>` e `</body>`.
- É o coração da nossa página web!

---

# MÓDULO 3: Dicionário das Tags Ensinadas na Agenda 12

A apostila da Agenda 12 ensina um conjunto específico de tags essenciais. Veja cada uma delas:

---

### 3.1 Títulos e Subtítulos: `<h1>` até `<h6>`
- A letra **H** vem da palavra inglesa **Heading** (cabeçalho / título).
- Existem 6 níveis hierárquicos:
  * `<h1>`: Título de maior nível, maior destaque visual e maior importância semântica.
  * `<h2>`: Subtítulo principal.
  * `<h3>` até `<h6>`: Subdivisões menores sucessivas.
- **Importância para os Motores de Busca (Google/Bing):** O Google usa o conteúdo das tags `<h1>` para saber qual é o assunto principal da página.
- **Na sua atividade:** O enunciado pediu para usar `<h1>` para o título principal e para o nome de cada um dos 5 sites favoritos.

---

### 3.2 Parágrafos: `<p>`
- Usado para delimitar blocos de texto comuns.
- Abertura `<p>` e fechamento `</p>`.
- O navegador adiciona automaticamente um espaçamento antes e depois de cada parágrafo para organizar a leitura.

---

### 3.3 Quebra de Linha: `<br>`
- Abreviação de *Break* (quebra).
- **Característica essencial:** É uma **tag vazia** (*void element*). Ela **NÃO possui fechamento** (não existe `</br>`).
- Força o texto seguinte a pular para a linha de baixo sem criar o espaço duplo de um novo parágrafo.

---

### 3.4 Inserção de Imagens: `<img>`
- Abreviação de *Image*.
- Também é uma **tag vazia** que **não possui fechamento**.
- **Atributos essenciais:**
  1. `src` (*source* / origem): Caminho ou link onde a foto está salva.
     * Se a imagem estiver na mesma pasta do arquivo HTML: basta colocar o nome do arquivo com a extensão: `src="site1_shopee.png"`.
     * Se estiver na web: coloca-se o endereço completo (URL): `src="https://exemplo.com/foto.jpg"`.
  2. `alt` (*alternative text* / texto alternativo):
     * Descreve a imagem para pessoas cegas que utilizam leitores de tela (acessibilidade).
     * Se a imagem falhar ao carregar ou a internet cair, o navegador exibe o texto do `alt` no lugar da foto.
  3. `width` e `height`: Largura e altura da imagem em pixels (ex.: `width="700"`).

---

### 3.5 Imagens Semânticas: `<figure>` e `<figcaption>`
Introduzidas no **HTML5** (Páginas 25 e 26 da apostila):
- `<figure>`: Tag semântica que encapsula uma unidade visual autônoma (imagem, gráfico, diagrama).
- `<figcaption>`: Tag semântica que define a **legenda explicativa** da imagem contida na `<figure>`.
- **Por que são importantes:** Mecanismos de busca e leitores de tela entendem que aquela imagem e aquela legenda estão diretamente conectadas.

Exemplo da apostila:
```html
<figure>
    <img src="site1_shopee.png" alt="Página inicial da Shopee">
    <figcaption>Figura 1: Página inicial da Shopee Brasil</figcaption>
</figure>
```

---

### 3.6 Links e Hiperligações: `<a>`
- A letra **a** significa **Anchor** (âncora).
- É a tag que cria os links clicáveis que nos levam para outras páginas.
- **Atributos essenciais:**
  1. `href` (*Hypertext Reference*): Endereço de destino para onde o usuário será levado ao clicar.
     * Exemplo: `href="https://www.mercadolivre.com.br/"`.
  2. `target`: Onde a página de destino será aberta:
     * `target="_blank"`: **Abre o link em uma nova aba/guia** do navegador (muito útil para não fazer o usuário perder a sua página).
     * `target="_self"`: Abre o link na **mesma aba** (é o comportamento padrão).

#### Como transformar uma imagem em link clicável?
Basta envolver a tag `<img>` dentro da tag `<a>`:
```html
<a href="https://www.mercadolivre.com.br/" target="_blank">
    <img src="site2_mercadolivre.png" alt="Mercado Livre">
</a>
```

---

### 3.7 Multimídia no HTML5: `<video>`, `<audio>` e `<source>`
Apostila, páginas 28 a 30:
- Antes do HTML5, para rodar vídeos na web era obrigatório instalar plug-ins externos (como o Adobe Flash Player).
- O HTML5 criou suporte nativo direto pelo navegador com a tag `<video>` e a tag `<audio>`.
- **Atributo `controls`:** Não precisa de valor. Faz o navegador exibir a barra com botão play, pause, volume, barra de progresso e botão de tela cheia.
- **Tag `<source>`:** Indica o caminho do vídeo/áudio (`src`) e o formato (`type="video/mp4"`).

Exemplo:
```html
<video controls>
    <source src="geeadIntro.mp4" type="video/mp4">
</video>
```

---

### 3.8 Comentários no Código: `<!-- ... -->`
Apostila, páginas 30 e 31:
- **Sintaxe:** Inicia com `<!--` e termina com `-->`.
- **Regra:** O ponto de exclamação `!` fica apenas no início.
- **Funções dos comentários:**
  1. **Documentação:** Explicar o que uma parte do código faz para outros desenvolvedores ou para você mesma lembrar no futuro.
  2. **Depuração / Testes:** Desativar temporariamente uma tag sem apagá-la, para verificar se ela é a causa de algum erro na página.
- **Visualização:** Os comentários **NUNCA são renderizados na tela do site** para o visitante. No Visual Studio Code, eles aparecem destacados na cor **verde**.

---

### 3.9 🌟 A REGRA DE OURO: Como Salvar Arquivos no Visual Studio Code e a Extensão `.html`
Apostila, páginas 14 a 20:

#### 1. Qual é a extensão obrigatória?
Ao digitar seu código no Visual Studio Code (ou Sublime Text), você deve salvar o arquivo obrigatoriamente com a extensão:
# 👉 **`.html`**

#### 2. Por que a extensão `.html` é indispensável?
- **Para o Navegador:** Se você esquecer de colocar o `.html` (ou deixar como `.txt`), o navegador não entenderá que se trata de uma página web e exibirá as tags de texto puro na tela em vez de desenhar a página visual.
- **Para o Visual Studio Code:** Enquanto o arquivo for um documento sem nome ou `.txt`, o VS Code não sabe qual linguagem você está escrevendo. No instante em que você salva como `.html`, ele ativa:
  * O destaque colorido da sintaxe (*Syntax Highlighting*).
  * O fechamento automático das tags (você digita `<p>` e ele fecha `</p>`).
  * O **IntelliSense** (você digita `html:5` e aperta Enter, e ele cria a estrutura completa em 1 segundo!).

#### 3. Como salvar no teclado (Passo a Passo):
1. Pressione o atalho: **`Ctrl + S`** (ou menu **File** > **Save As...**).
2. Na caixa *Nome do arquivo*, digite o nome seguido de `.html` (exemplo: `index.html`).
3. Clique no botão **Salvar**.

#### 4. As Proibições da Regra de Ouro nos Nomes de Arquivos (Página 20):
- ❌ **NUNCA use espaços em branco:** Na internet, servidores Linux transformam espaços no código estranho `%20`, que quebra links.
- ❌ **NUNCA use acentuação (`á`, `é`, `õ`) ou cedilha (`ç`):** Podem corromper a URL dependendo do servidor.
- ❌ **NUNCA use caracteres especiais (`@`, `#`, `$`, `!`, `&`):** Esses símbolos têm funções reservadas nos navegadores.
- ✅ **SEMPRE USE:** Letras minúsculas ou formato *camelCase*, separadas por sublinhado `_` ou traço `-`.
  * *Correto:* `index.html`, `IraciBertoGomes_Ag12_DS_I.html`, `site1_shopee.png`.
  * *Incorreto:* `minha página!.html`, `meu site favorito 1.html`.

---

### 3.10 Comparativo de Ferramentas: Bloco de Notas vs Sublime Text vs VS Code
Apostila, páginas 14 a 16:

- **Bloco de Notas (Windows):** Editor de texto simples. Dá para fazer um site inteiro nele? **SIM!** Porém é tudo em preto e branco, não avisa erros de digitação e não possui numeração de linhas.
- **Sublime Text:** Editor de código-fonte profissional, famoso por ser extremamente rápido e leve. Deixa o código colorido, numera as linhas e tem fechamento inteligente de tags.
- **Visual Studio Code (VS Code):** Editor moderno e completo adotado oficialmente pelo Centro Paula Souza / ETEC. Possui IntelliSense avançado, controle de versão (Git integrado) e atalhos de alta produtividade (como `html:5`).

---

# MÓDULO 4: Guia Passo a Passo do GitHub e GitHub Pages

O guia oficial do Centro Paula Souza (*como_hospedar_um_site_no_github_pages1.pdf*) ensina a colocar um site estático no ar gratuitamente. Veja o resumo completo:

### 4.1 O que é o GitHub?
O **GitHub** é uma plataforma mundial em nuvem para hospedar projetos de software, controlar versões de código e compartilhar trabalhos em equipe.

### 4.2 O que é o GitHub Pages?
É um serviço gratuito oferecido pelo GitHub que transforma o código HTML, imagens e estilos do seu repositório em um **site de verdade acessível na internet** por qualquer pessoa, no celular ou computador.

### 4.3 A Regra do `index.html`
- Quando alguém digita um endereço web (exemplo: `https://seunome.github.io/projeto/`), o servidor web procura automaticamente na raiz da pasta um arquivo com o nome exato: **`index.html`**.
- O arquivo `index.html` é, por padrão universal, a **página principal de entrada de qualquer site na internet**.
- Por isso, no projeto da Agenda 12, nós mantemos tanto o arquivo com o nome exigido no enunciado (`IraciBertoGomes_Ag12_DS_I.html`) quanto a cópia idêntica chamada `index.html` na raiz do repositório.

### 4.4 Os 4 Passos Oficiais para Publicar no GitHub Pages:
1. **Preparar os arquivos:** Garantir que o `index.html` e todas as fotos estejam na mesma pasta raiz.
2. **Criar o Repositório no GitHub:**
   - Acessar `github.com` e entrar na sua conta.
   - Clicar no botão `+` (canto superior direito) > `New repository`.
   - Dar um nome (ex.: `AGENDA_12`).
   - Marcar obrigatoriamente a opção **Public** (Público), pois o GitHub Pages gratuito exige que seja público.
   - Clicar em `Create repository`.
3. **Enviar os arquivos:** Fazer o upload dos arquivos (arrastando e soltando ou via comandos `git push`).
4. **Ativar o GitHub Pages:**
   - Entrar na aba **Settings** (Configurações) do repositório.
   - No menu lateral esquerdo, clicar em **Pages**.
   - Em *Build and deployment*, no campo **Branch**, mudar de `None` para **`main`** e manter a pasta **/ (root)**.
   - Clicar em **Save**.
   - O site estará no ar no endereço: `https://seu-usuario.github.io/nome-do-repositorio/`.

---

# MÓDULO 5: Como o Seu Projeto "Meus Sites Favoritos" Foi Construído

Vamos analisar exatamente como o seu código `IraciBertoGomes_Ag12_DS_I.html` atendeu a **todas as exigências do professor**:

### Tabela de Correspondência entre Requisitos e Código

| Requisito do Enunciado | Como foi implementado no seu código | Linha / Exemplo |
| :--- | :--- | :--- |
| **Nome do arquivo** | Salvo como `IraciBertoGomes_Ag12_DS_I.html` | Na pasta `AGENDA_12` |
| **Título da aba** | `<title>Meus sites favoritos</title>` | Dentro da tag `<head>` |
| **Título do corpo** | `<h1>Meus sites favoritos: Iraci Berto Gomes</h1>` | Logo no início do `<body>` |
| **5 Sites favoritos** | Shopee, Mercado Livre, Correios, Casas Bahia, Amazon | 5 seções bem estruturadas |
| **Nome acima da foto** | `<h1>Nome do Site</h1>` | Acima de cada bloco |
| **Foto local** | `<img src="site1_shopee.png" alt="..." width="700">` | Imagens na mesma pasta |
| **Legenda da foto** | `<figure>` e `<figcaption>` | Tags semânticas do HTML5 |
| **Link abaixo da foto** | `<p><a href="..." target="_blank">Clique aqui...</a></p>` | Abre o site oficial em nova aba |
| **Opcional da atividade** | Imagem clicável: `<a href="..."><img ...></a>` | Clicar na foto abre o site |
| **Comentários nas linhas** | `<!-- Tag semântica ... -->` | Explicando a função de cada tag |
| **Linha divisória** | `<hr>` | Separa visualmente cada um dos 5 sites |

### Exemplo de um Bloco Completo do seu Código:
```html
<!-- Nome do site usando a tag <h1> conforme a dica da atividade -->
<h1>Shopee</h1>

<!-- Tag semântica do HTML5 <figure> estudada na página 25 da apostila -->
<figure>
    <!-- Opcional da atividade: link clicável também na imagem através da tag <a> -->
    <a href="https://shopee.com.br/" target="_blank">
        <!-- Tag <img> com atributos src e alt para inserção da imagem local -->
        <img src="site1_shopee.png" alt="Página inicial da Shopee Brasil" width="700">
    </a>
    <!-- Tag semântica do HTML5 <figcaption> para legenda da imagem conforme a apostila -->
    <figcaption>Figura 1: Página inicial da Shopee Brasil (shopee.com.br)</figcaption>
</figure>

<!-- Parágrafo explicativo da importância do site -->
<p>
    A <strong>Shopee</strong> é uma das maiores plataformas de comércio eletrônico...
</p>

<!-- Link para o site abaixo da imagem usando a tag <a> com o atributo target="_blank" -->
<p>
    <a href="https://shopee.com.br/" target="_blank">
        Clique aqui para acessar o site da Shopee
    </a>
</p>

<!-- Linha divisória horizontal entre os sites -->
<hr>
```

---

# MÓDULO 6: Simulado com 15 Questões Comentadas para a Prova

Treine respondendo a estas 15 questões que cobrem todo o conteúdo cobrado na Agenda 12 e nas provas do Centro Paula Souza:

---

#### Questão 1
**O que significa a sigla HTML e qual a sua classificação no desenvolvimento web?**  
- **Resposta:** Significa *HyperText Markup Language* (Linguagem de Marcação de Hipertexto). Ela é classificada como uma **linguagem de marcação de texto e estrutura**, e **não** uma linguagem de programação.

---

#### Questão 2
**A instrução `<!DOCTYPE html>` é uma tag HTML? Qual a sua finalidade?**  
- **Resposta:** **Não é uma tag!** É uma declaração de instrução especial para o navegador web saber qual especificação seguir. Ao declarar `<!DOCTYPE html>`, indicamos que a página deve ser interpretada de acordo com os padrões do **HTML5**.

---

#### Questão 3
**Qual a diferença entre o conteúdo colocado dentro da tag `<head>` e o conteúdo colocado dentro da tag `<body>`?**  
- **Resposta:** O `<head>` guarda o cabeçalho técnico e metadados da página (como charset, viewport, título da aba), que não aparecem no corpo visual do site. Já o `<body>` guarda todo o conteúdo visível que o usuário enxerga e interage na janela do navegador (textos, títulos, imagens, links).

---

#### Questão 4
**Para que serve a tag `<meta charset="UTF-8">` inserida dentro do `<head>`?**  
- **Resposta:** Define o conjunto universal de caracteres (Unicode) para que o navegador exiba corretamente acentos (`á`, `é`, `õ`) e cedilha (`ç`) em português, evitando caracteres ilegíveis e erros de codificação.

---

#### Questão 5
**Explique a função da meta tag de viewport: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`.**  
- **Resposta:** Ela configura a responsividade da página para dispositivos móveis. O parâmetro `width=device-width` ajusta a largura da página à tela do aparelho (celular, tablet ou computador), e `initial-scale=1.0` define o zoom inicial padrão (100%).

---

#### Questão 6
**Qual a diferença fundamental entre as tags de título `<h1>` e `<h6>`?**  
- **Resposta:** Hierarquia e tamanho. `<h1>` é o título de nível 1, de maior destaque visual e de maior relevância semântica para motores de busca (como o Google). `<h6>` é o título de menor nível e menor destaque.

---

#### Questão 7
**A tag `<br>` necessita de tag de fechamento (`</br>`)? Qual a sua função?**  
- **Resposta:** **Não necessita de fechamento.** Ela é uma tag vazia (*void element*). Sua única função é realizar uma quebra de linha no texto, fazendo o conteúdo seguinte descer para a próxima linha.

---

#### Questão 8
**Na tag `<img src="foto.jpg" alt="Logo da empresa">`, quais são as funções dos atributos `src` e `alt`?**  
- **Resposta:** 
  - `src` (*source*): Indica o caminho ou URL onde a imagem está localizada.
  - `alt` (*alternative*): Fornece um texto alternativo para leitores de tela de pessoas com deficiência visual e é exibido na tela caso a imagem não carregue.

---

#### Questão 9
**Por que o HTML5 introduziu as tags `<figure>` e `<figcaption>` em vez de usar apenas a tag `<img>`?**  
- **Resposta:** Para dar significado semântico à relação entre uma imagem e a sua respectiva legenda explicativa. Isso ajuda a estruturar melhor o documento para motores de busca e ferramentas de acessibilidade.

---

#### Questão 10
**Qual a diferença de comportamento entre os atributos `target="_blank"` e `target="_self"` na tag `<a>`?**  
- **Resposta:** 
  - `target="_blank"` abre a página de destino em uma **nova aba (guia)** do navegador.
  - `target="_self"` abre a página de destino na **mesma aba** em que o usuário já se encontra (comportamento padrão).

---

#### Questão 11
**Como podemos transformar uma imagem em um link clicável no HTML?**  
- **Resposta:** Envolvendo a tag `<img>` dentro da tag de link `<a>`, como em: `<a href="https://site.com"><img src="foto.png" alt="Descrição"></a>`.

---

#### Questão 12
**Qual é a sintaxe correta para inserir um comentário no código HTML? O comentário aparece na tela para o usuário?**  
- **Resposta:** A sintaxe é `<!-- seu comentário aqui -->`. O ponto de exclamação fica somente no início. Os comentários **não aparecem na tela para o usuário**, servindo apenas para anotações do programador e testes no código.

---

#### Questão 13
**Quais as principais vantagens de usar o Visual Studio Code em vez do Bloco de Notas para programar em HTML?**  
- **Resposta:** O Visual Studio Code oferece destaque colorido da sintaxe (*syntax highlighting*), auxílio inteligente de código (*IntelliSense* para autocompletar tags), atalhos rápidos como `html:5` e ferramentas integradas de produtividade.

---

#### Questão 14
**Por que, no serviço GitHub Pages, o arquivo principal do site deve obrigatoriamente se chamar `index.html`?**  
- **Resposta:** Porque `index.html` é o nome universalmente padronizado que os servidores web procuram automaticamente como página inicial de entrada de qualquer site quando a raiz do domínio é acessada.

---

#### Questão 15
**No GitHub Pages, para ativar a publicação de um site, quais opções devem ser selecionadas no menu Settings > Pages?**  
- **Resposta:** Em *Build and deployment* (origem), deve-se selecionar a **Branch: `main`** e a pasta **/ (root)**, e em seguida clicar no botão **Save**.

---

### 🎓 Dica Final de Estudos da Antigravity para a Dona Iraci:
> *"Revise este material com calma. Preste atenção no par de abertura e fechamento das tags (ex: `<h1>` e `</h1>`), nos atributos (`src`, `href`, `alt`, `target`) e na estrutura padrão (`<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`). Com esses conceitos bem fixados na mente, você terá total segurança e confiança para tirar nota máxima na sua avaliação técnica!"*
