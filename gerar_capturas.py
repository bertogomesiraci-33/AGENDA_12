import os
import html
from playwright.sync_api import sync_playwright

def gerar_captura_codigo():
    html_file = r'c:\Users\Iraci\Desktop\estudos\AGENDA_12\IraciBertoGomes_Ag12_DS_I.html'
    with open(html_file, 'r', encoding='utf-8') as f:
        code_text = f.read()

    # Prepara visualizador estilo VS Code
    code_viewer_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/line-numbers/prism-line-numbers.min.css">
<style>
  body {
    margin: 0;
    padding: 30px;
    background: #0d1117;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    display: flex;
    justify-content: center;
  }
  .vscode-window {
    width: 1050px;
    background: #1e1e1e;
    border-radius: 12px;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
    overflow: hidden;
    border: 1px solid #333333;
  }
  .vscode-titlebar {
    background: #323233;
    padding: 10px 18px;
    display: flex;
    align-items: center;
    color: #cccccc;
    font-size: 13px;
    font-weight: 500;
  }
  .traffic-lights {
    display: flex;
    gap: 8px;
    margin-right: 20px;
  }
  .light {
    width: 12px;
    height: 12px;
    border-radius: 50%;
  }
  .light-red { background: #ff5f56; }
  .light-yellow { background: #ffbd2e; }
  .light-green { background: #27c93f; }
  .tabs {
    display: flex;
    background: #252526;
    border-bottom: 1px solid #1e1e1e;
  }
  .tab {
    background: #1e1e1e;
    color: #ffffff;
    padding: 10px 22px;
    font-size: 13px;
    border-top: 2px solid #007acc;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .tab-inactive {
    background: #2d2d2d;
    color: #969696;
    border-top: none;
  }
  pre[class*="language-"] {
    margin: 0;
    padding: 24px 16px 24px 0;
    background: #1e1e1e !important;
    font-size: 13px;
    line-height: 1.55;
    font-family: 'Consolas', 'Courier New', monospace;
  }
  .token.comment {
    color: #6a9955 !important;
    font-style: italic;
    font-weight: normal;
  }
  .token.tag {
    color: #569cd6 !important;
  }
  .token.attr-name {
    color: #9cdcfe !important;
  }
  .token.attr-value {
    color: #ce9178 !important;
  }
</style>
</head>
<body>
  <div class="vscode-window">
    <div class="vscode-titlebar">
      <div class="traffic-lights">
        <div class="light light-red"></div>
        <div class="light light-yellow"></div>
        <div class="light light-green"></div>
      </div>
      <div>IraciBertoGomes_Ag12_DS_I.html — Visual Studio Code (Desenvolvimento de Sistemas I - Agenda 12)</div>
    </div>
    <div class="tabs">
      <div class="tab">📄 IraciBertoGomes_Ag12_DS_I.html</div>
      <div class="tab tab-inactive">🎨 style.css</div>
    </div>
    <pre class="line-numbers"><code class="language-html">""" + html.escape(code_text) + """</code></pre>
  </div>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-markup.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/line-numbers/prism-line-numbers.min.js"></script>
</body>
</html>"""

    temp_file = r'c:\Users\Iraci\Desktop\estudos\AGENDA_12\temp_code_preview.html'
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(code_viewer_html)

    out_capture = r'c:\Users\Iraci\Desktop\estudos\AGENDA_12\captura-codigo-html-comentado.png'

    with sync_playwright() as p:
        browser = p.chromium.launch()
        # Viewport amplo para capturar bem o bloco de código
        page = browser.new_page(viewport={'width': 1150, 'height': 1500})
        page.goto(f'file:///{os.path.abspath(temp_file)}')
        page.wait_for_timeout(2500)
        
        # Tirar print do elemento da janela do VS Code
        vscode_elem = page.locator('.vscode-window')
        vscode_elem.screenshot(path=out_capture)
        print('Saved code capture:', out_capture)
        browser.close()

    if os.path.exists(temp_file):
        os.remove(temp_file)

if __name__ == '__main__':
    gerar_captura_codigo()
