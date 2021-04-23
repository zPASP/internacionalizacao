# PADRÃO PARA GLOBALIZAÇÃO DO APLICATIVO UTILIZANDO "**GNU gettext**"


É uma biblioteca runtime que é implementada por um catálogos de mensagens e permite a análise e criação de arquivos com a mensagem traduzida.

Para começar por é necessário fazer o import da biblioteca.

    

    import gettext

Após é necessário criar um objeto passando como parâmetro o domínio(nome da aplicação), uma pasta para a localidade e a linguagem para a qual será traduzido as strings. Em seguida associar  a função gettext ao caractere sublinhado( **_** )

    t = gettext.translation('app', localedir='locale', languages=['pt_BR.UTF-8'])
    _ = t.gettext
    
|VARIAVEIS|SIGNIFICADOS  |
|--|--|
| **t** | Pode ser qualquer uma, porem o "t" é auto intuitiva para translation e/ou tradução |
| **'app'** | geralmente é o nome do aplicativo |
| **'localedir'**|Por padrão a biblioteca irá procurar em uma estrutura de pasta especifica os arquivos de tradução geralmente a pasta é chamada de 'locale' por padronização de tradução |
| **'languages'**|será a linguagem a ser selecionada a qual será executado o aplicativo, podendo ter até mesmo mais de uma versão para o mesmo idioma.<br> Ela tem que estar no padrão da estrutura esperada pela biblioteca |
|**PADRÃO DE PASTAS**|`<localdir>/<linguage_code>/LC_MESSAGES/<domain>.po`<br>Exemplo no caso do meu aplicativo:<br> `./locale/pt_BR.UTF-8/LC_MESSAGES/app.po`|

> EXEMPLO CODIGO COMPLETO

    #Python 3.8.5
    import gettext
    t = gettext.translation('app', localedir='locale', languages=['pt_BR.UTF-8'])
    _ = t.gettext
     
    print(_('Olá, Mundo'))


Com o código com as marcações nas strings que serão traduzidas é possível coleta-las utilizando a ferramenta pela linha de comando `xgettext` do pacote GNU gettext. Utilizando ela será gerado um arquivo **.PO** contendo as strings que foram marcadas.
|  GERANDO O ARQUIVO|COM AS MARCAÇÕES
|--|--|
| Comando para utilizar:|Comando no nosso exemplo|
|`xgettext -d <nomeDoArquivosQueSeraGerado> <Nomedoarquivo>`|`xgettext -d app app.py`|

> o arquivo PO que será gerado contem uma estrutura básica.

    "Project-Id-Version: PACKAGE VERSION\n" 
    "Report-Msgid-Bugs-To: \n"
    "POT-Creation-Date: 2019-05-03 13:23-0300\n" 
    "PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
    "Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
    "Language-Team: LANGUAGE <LL@li.org>\n"
    "Language: \n"
    "MIME-Version: 1.0\n"
    "Content-Type: text/plain; charset=UTF-8\n"
    "Content-Transfer-Encoding: 8bit\n"  
     
    #: app.py:6 
    msgid "Hello, world!"
    msgstr ""

Uma vez com o arquivo com as marcações gerado, basta copia-lo para a pasta do idioma o qual será traduzido e colocar a palavra no idioma a ser traduzido destro das ** `"" `** que vem após a palavra `msgtr` que no exemplo poderia ser para o inglês ficando<br> 

    #: app.py:6
    msgid "Olá, Mundo"
    msgstr "Hello, world!"

O arquivo .PO tem que ser copiado e colado dentro da pasta padrão onde ele será dos idiomas que foi criado e fazer as modificações no **mgstr** no arquivo de cada pasta.

> Arvore dos diretórios como ficará até o momento

    |-- app.py 
    |-- locale 
		    |-- en_US |
			|	    |-- LC_MESSAGES |
					|		|-- app.po 
			|-- pt_BR.UTF-8
			|		|-- LC_MESSAGES	
					|		|-- app.po

> Para a biblioteca funcionar e reconhecer os arquivos basta compilar o arquivo PO em um arquivo MO usando o comando `msgfmt`

    msgfmt -o app.mo app.po #dentro da pasta LC_MENSSAGES do idioma com a tradução.

 - **<h2>Possiveis Erros</h2>**
	 - `FileNotFoudError: [Errno2] No translation file found dor domain: 'app'`
		 - Para resolver basta verificar se o idioma colocado destro da variável ***languages*** realmente já foi criado dentro da pasta e feito a compilação do arquivo PO em MO
		 - Adicionar o tratamento para o erro caso não encontre o idioma exibir com o original, passando para o objeto ***translation*** junto dos outros paramentos o `fallback=True` que por padrão fica False.
	 - Não aparecer acentuação e não reconhecer caracteres especiais de algumas linguagens.
		 - Dentro da pasta da linguagem com problemas checar o arquivo .PO e procurar na linha que contem as referencias a `"Content-Type:"` e colocar o ***charset*** da linguagem.


|PROCESSO SEM EXPLICAÇÃO:> |
|--|--|
|

 - [ ] TER UM APP "EM PYTHON"
 - [ ] FAZER O IMPORT DA BIBLIOTECA E CRIAR UM OBJETO
 - [ ] FAZER AS MARCAÇÕES DAS STRINGS COM ***_***
 - [ ] CRIAR O ARQUIVO .PO
 - [ ] CRIAR AS PASTAS ***LOCATE/<LANGUAGE_CODE>/LC_MESSAGES***
 - [ ] COPIAR O ARQUIVO .PO E COLOCAR EM TODAS ***/LC_MESSAGES*** CRIADA
 - [ ] FAZER AS TRADUÇÃO DO ARQUIVO .PO EM CADA PASTA MUDANDO A `MSGTR ""`
 - [ ] ESCOLHER EM QUAL IDIOMA SERÁ EXECUTADO O PROGRAMA NO APP MODIFICANDO A ***LANGUAGES***

