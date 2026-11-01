@echo off
chcp 65001 > nul
echo ====================================================================
echo   PUBLICADOR AUTOMÁTICO DO PROJETO AGENDA 12 NO GITHUB
echo   Estudante: Iraci Berto Gomes
echo   Repositório: https://github.com/bertogomesiraci-33/AGENDA_12.git
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
    echo [SUCESSO] Repositório enviado com sucesso para o GitHub!
    echo.
    echo Agora, para ativar o GitHub Pages:
    echo 1. Acesse: https://github.com/bertogomesiraci-33/AGENDA_12/settings/pages
    echo 2. Em 'Build and deployment', selecione Branch: main e pasta: / (root)
    echo 3. Clique em 'Save'.
    echo 4. Seu site estará online em:
    echo    https://bertogomesiraci-33.github.io/AGENDA_12/
    echo ====================================================================
) else (
    echo.
    echo [ATENÇÃO] Ocorreu um aviso ou erro no envio.
    echo Certifique-se de que o repositório 'AGENDA_12' foi criado no seu GitHub:
    echo 1. Acesse: https://github.com/new
    echo 2. Repository name: AGENDA_12
    echo 3. Marque como 'Public'
    echo 4. Clique em 'Create repository'
    echo 5. Execute este arquivo novamente!
)
echo.
pause
