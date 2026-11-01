@echo off
chcp 65001 > nul
cd /d "%~dp0"

echo ====================================================================
echo   PUBLICADOR AUTOMATICO DO PROJETO AGENDA 12 NO GITHUB
echo   Estudante: Iraci Berto Gomes
echo   Repositorio: https://github.com/bertogomesiraci-33/AGENDA_12.git
echo ====================================================================
echo.
echo [1/3] Verificando arquivos para envio...
git status
echo.
echo [2/3] Enviando arquivos para a branch main no GitHub...
git push -u origin main
if %ERRORLEVEL% EQU 0 (
    echo.
    echo ====================================================================
    echo [SUCESSO] Repositorio enviado com sucesso para o GitHub!
    echo.
    echo Agora, para ativar o GitHub Pages:
    echo 1. Acesse: https://github.com/bertogomesiraci-33/AGENDA_12/settings/pages
    echo 2. Em 'Build and deployment', selecione Branch: main e pasta: / (root)
    echo 3. Clique em 'Save'.
    echo 4. Seu site estara online em:
    echo    https://bertogomesiraci-33.github.io/AGENDA_12/
    echo ====================================================================
) else (
    echo.
    echo ====================================================================
    echo [ATENCAO] O GitHub ainda nao encontrou o repositorio 'AGENDA_12'.
    echo.
    echo Para resolver isso em 1 minuto:
    echo 1. Abra o navegador e entre em: https://github.com/new
    echo 2. Em 'Repository name', digite: AGENDA_12
    echo 3. Marque a opcao 'Public'
    echo 4. Clique no botao verde 'Create repository'
    echo 5. Apos criar la no site, execute este arquivo novamente dando 2 cliques!
    echo ====================================================================
)
echo.
pause
