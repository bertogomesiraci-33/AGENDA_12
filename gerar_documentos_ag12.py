"""
Script de Geração de Documentos Oficiais - Agenda 12 (Desenvolvimento de Sistemas I)
Estudante: Iraci Berto Gomes
Instituição: ETEC / Centro Paula Souza (CPS)
Projeto: Meus Sites Favoritos (HTML5 & CSS3)

Gera automaticamente:
1. IraciBertoGomes_Ag12_DS_I.docx
2. IraciBertoGomes_Ag12_DS_I.pdf
3. IraciBertoGomes_Ag12_DS_I.zip
"""

import os
import sys
import zipfile
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, KeepTogether, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


# ====================================================================
# AUXILIARES PARA WORD (DOCX)
# ====================================================================

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)


def gerar_word(caminho_docx, base_dir):
    doc = docx.Document()

    # Configuração de Margens
    for section in doc.sections:
        section.top_margin = Inches(0.7)
        section.bottom_margin = Inches(0.7)
        section.left_margin = Inches(0.7)
        section.right_margin = Inches(0.7)

    navy = RGBColor(26, 54, 93)      # #1A365D
    slate = RGBColor(43, 108, 176)   # #2B6CB0
    dark = RGBColor(45, 55, 72)      # #2D3748

    # Título Principal do Relatório
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(2)
    run_title = p_title.add_run("RELATÓRIO TÉCNICO DE DESENVOLVIMENTO WEB")
    run_title.bold = True
    run_title.font.name = "Arial"
    run_title.font.size = Pt(16)
    run_title.font.color.rgb = navy

    # Subtítulo Acadêmico
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(12)
    run_sub = p_sub.add_run(
        "Curso Técnico em Desenvolvimento de Sistemas | ETEC / Centro Paula Souza\n"
        "Componente: Desenvolvimento de Sistemas I — Agenda 12 (HTML5, Semântica e GitHub Pages)\n"
        "Estudante: Iraci Berto Gomes  |  Arquivo de Entrega: IraciBertoGomes_Ag12_DS_I"
    )
    run_sub.font.name = "Arial"
    run_sub.font.size = Pt(9.5)
    run_sub.font.color.rgb = RGBColor(100, 116, 139)

    def add_section_header(title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(title)
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(12)
        run.font.color.rgb = navy
        return p

    def add_body(text, bold_prefix=None):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            rb = p.add_run(bold_prefix)
            rb.bold = True
            rb.font.name = "Arial"
            rb.font.size = Pt(9.5)
            rb.font.color.rgb = dark
        r = p.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(9.5)
        r.font.color.rgb = dark
        return p

    # Seção 1: Cenário e Objetivos da Atividade
    add_section_header("1. Cenário e Proposta da Atividade")
    add_body(
        "Na Sociedade da Informação e da Comunicação, os sistemas integrados à web representam a espinha dorsal da divulgação "
        "de serviços, produtos e conhecimento técnico. O objetivo desta atividade prática da Agenda 12 é consolidar os fundamentos "
        "de estruturação web com HTML5 e estilização CSS3, através do desenvolvimento de uma página personalizada denominada "
        "'Meus sites favoritos'."
    )
    add_body(
        "A página foi projetada para organizar cinco portais web de máxima relevância para a formação técnica em Desenvolvimento "
        "de Sistemas, cumprindo rigorosamente os padrões semânticos da W3C, acessibilidade e as orientações metodológicas da ETEC/CPS."
    )

    # Seção 2: Checklist de Atendimento aos Requisitos
    add_section_header("2. Matriz de Conformidade com os Requisitos do Enunciado")
    
    table_req = doc.add_table(rows=8, cols=3)
    table_req.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_req.autofit = False

    col_widths_req = [Inches(2.4), Inches(2.3), Inches(2.2)]
    headers_req = ["Requisito do Enunciado", "Implementação no Projeto", "Status de Conformidade"]

    for i, h in enumerate(headers_req):
        cell = table_req.cell(0, i)
        cell.width = col_widths_req[i]
        set_cell_background(cell, "1A365D")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    dados_req = [
        ("Título (aba) da página", "<title>Meus sites favoritos</title>", "Atendido com Exatidão"),
        ("Título do corpo da página", "Meus sites favoritos: Iraci Berto Gomes", "Atendido com Exatidão"),
        ("Nome de cada site acima da imagem", "Tag <h1> individual para cada site", "Atendido (Conforme Dica)"),
        ("5 Imagens locais dos sites", "Imagens salvas na mesma pasta do HTML", "Atendido com Arquivos Locais"),
        ("Link abaixo de cada imagem", "Tag <a href='...'> direcionando ao portal", "Atendido com Target Blank"),
        ("Link na própria imagem (Opcional)", "Tag <img> envolvida por tag <a> clicável", "Atendido (Diferencial)"),
        ("Código com comentários em linhas", "Comentários em todas as tags e seções", "Atendido Linha a Linha")
    ]

    for row_idx, row_data in enumerate(dados_req, start=1):
        bg = "F8FAFC" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, val in enumerate(row_data):
            cell = table_req.cell(row_idx, col_idx)
            cell.width = col_widths_req[col_idx]
            set_cell_background(cell, bg)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx == 2 else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(8.5)
            r.font.color.rgb = dark
            if col_idx == 2:
                r.bold = True
                r.font.color.rgb = RGBColor(22, 101, 52)  # Verde escuro

    # Seção 3: Seleção dos 5 Sites Favoritos
    add_section_header("3. Relação dos 5 Sites Favoritos Selecionados")
    add_body("Para a composição da página, foram selecionados cinco portais indispensáveis na rotina do estudante de T.I.:")

    table_sites = doc.add_table(rows=6, cols=4)
    table_sites.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_sites.autofit = False

    col_widths_sites = [Inches(1.2), Inches(1.5), Inches(2.2), Inches(2.0)]
    headers_sites = ["Site", "Categoria", "Justificativa Didática / Profissional", "URL Oficial"]

    for i, h in enumerate(headers_sites):
        cell = table_sites.cell(0, i)
        cell.width = col_widths_sites[i]
        set_cell_background(cell, "2B6CB0")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    dados_sites = [
        ("GitHub", "Controle de Versão", "Hospedagem de repositórios Git, colaboração open-source e portfólio.", "https://github.com"),
        ("MDN Web Docs", "Documentação Web", "Referência mundial da Mozilla sobre padrões oficiais HTML5, CSS3 e JS.", "https://developer.mozilla.org"),
        ("Stack Overflow", "Comunidade Técnica", "Maior fórum de suporte colaborativo para depuração e soluções de bugs.", "https://stackoverflow.com"),
        ("W3Schools", "Tutoriais Práticos", "Plataforma de aprendizado dinâmico com testes interativos 'Try it Yourself'.", "https://www.w3schools.com"),
        ("YouTube", "Vídeos & Educação", "Videoaulas do Centro Paula Souza, cursos técnicos e momentos de lazer.", "https://www.youtube.com")
    ]

    for row_idx, row_data in enumerate(dados_sites, start=1):
        bg = "F8FAFC" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, val in enumerate(row_data):
            cell = table_sites.cell(row_idx, col_idx)
            cell.width = col_widths_sites[col_idx]
            set_cell_background(cell, bg)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx == 0 else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(8.5)
            r.font.color.rgb = dark
            if col_idx == 0:
                r.bold = True

    # Seção 4: Evidências de Execução e Código
    add_section_header("4. Evidências de Execução no Navegador e Código Comentado")
    add_body("Conforme orientação da atividade, são apresentadas abaixo as capturas comprobatórias:")

    # Imagem 1: Execução no navegador
    img_nav = os.path.join(base_dir, "captura-execucao-navegador.png")
    if os.path.exists(img_nav):
        p_cap1_title = doc.add_paragraph()
        p_cap1_title.paragraph_format.space_before = Pt(6)
        r = p_cap1_title.add_run("Figura 1: Execução da página web renderizada no navegador (Desktop):")
        r.bold = True
        r.font.size = Pt(9)
        p_img1 = doc.add_paragraph()
        p_img1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img1.paragraph_format.space_after = Pt(8)
        p_img1.add_run().add_picture(img_nav, width=Inches(6.2))

    # Imagem 2: Código comentado
    img_code = os.path.join(base_dir, "captura-codigo-html-comentado.png")
    if os.path.exists(img_code):
        p_cap2_title = doc.add_paragraph()
        p_cap2_title.paragraph_format.space_before = Pt(6)
        r = p_cap2_title.add_run("Figura 2: Captura do código HTML5 com comentários didáticos no Visual Studio Code:")
        r.bold = True
        r.font.size = Pt(9)
        p_img2 = doc.add_paragraph()
        p_img2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img2.paragraph_format.space_after = Pt(8)
        p_img2.add_run().add_picture(img_code, width=Inches(6.2))

    # Seção 5: Código-Fonte Oficial Completo
    add_section_header("5. Código-Fonte Oficial Comentado (IraciBertoGomes_Ag12_DS_I.html)")
    html_file = os.path.join(base_dir, "IraciBertoGomes_Ag12_DS_I.html")
    with open(html_file, "r", encoding="utf-8") as f:
        codigo_fonte = f.read()

    p_code = doc.add_paragraph()
    p_code.paragraph_format.space_before = Pt(4)
    p_code.paragraph_format.space_after = Pt(6)
    p_code.paragraph_format.line_spacing = 1.0
    r_code = p_code.add_run(codigo_fonte)
    r_code.font.name = "Consolas"
    r_code.font.size = Pt(7)
    r_code.font.color.rgb = RGBColor(30, 41, 59)

    # Seção 6: Procedimento de Publicação no GitHub e GitHub Pages
    add_section_header("6. Procedimento de Hospedagem no GitHub Pages")
    add_body(
        "Em observância ao guia complementar 'Como hospedar um site no GitHub Pages' disponibilizado pelo Centro Paula Souza, "
        "o projeto foi estruturado com controle de versão Git e preparado para deploy estático gratuito:"
    )
    add_body(
        "1. Inicialização do repositório local com 'git init' e inclusão de todos os arquivos do site.\n"
        "2. Criação de arquivo index.html na raiz do projeto (cópia idêntica de IraciBertoGomes_Ag12_DS_I.html).\n"
        "3. Vinculação ao repositório remoto público no GitHub: https://github.com/bertogomesiraci-33/AGENDA_12.git\n"
        "4. Ativação do serviço GitHub Pages em Settings > Pages > Build and deployment (Branch: main / root).\n"
        "5. Disponibilização pública online através da URL: https://bertogomesiraci-33.github.io/AGENDA_12/"
    )

    # Seção 7: Conclusão e Competências
    add_section_header("7. Competências e Habilidades Consolidadas")
    add_body(
        "A realização prática da Agenda 12 permitiu consolidar com êxito os seguintes objetivos de formação:\n"
        "• Estruturação semântica em conformidade com os padrões modernos da Web (HTML5: header, main, article, figure, a, h1);\n"
        "• Manipulação precisa de caminhos relativos de arquivos para inclusão de imagens locais e folhas de estilos;\n"
        "• Aplicação de comentários no código-fonte como instrumento de legibilidade e documentação técnica;\n"
        "• Versionamento distribuído com Git e hospedagem em nuvem via GitHub Pages."
    )

    doc.save(caminho_docx)
    print(f"[OK] Documento DOCX gerado com sucesso: {caminho_docx}")


# ====================================================================
# GERADOR DE PDF (REPORTLAB)
# ====================================================================

def gerar_pdf(caminho_pdf, base_dir):
    doc = SimpleDocTemplate(
        caminho_pdf,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=26,
        bottomMargin=26
    )

    styles = getSampleStyleSheet()
    primary = colors.HexColor("#1A365D")
    secondary = colors.HexColor("#2B6CB0")
    dark = colors.HexColor("#2D3748")

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=primary,
        alignment=1,
        spaceAfter=3
    )

    subtitle_style = ParagraphStyle(
        'DocSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#4A5568"),
        alignment=1,
        spaceAfter=8
    )

    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=primary,
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.3,
        leading=11.5,
        textColor=dark,
        spaceAfter=4
    )

    table_body = ParagraphStyle(
        'TableBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=10,
        textColor=dark
    )

    table_header = ParagraphStyle(
        'TableHead',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=colors.white,
        alignment=1
    )

    code_style = ParagraphStyle(
        'Code',
        parent=styles['Code'],
        fontName='Courier',
        fontSize=6.2,
        leading=7.8,
        textColor=colors.HexColor("#1A202C")
    )

    story = []

    # Cabeçalho Principal
    story.append(Paragraph("RELATÓRIO TÉCNICO DE DESENVOLVIMENTO WEB", title_style))
    story.append(Paragraph(
        "Curso Técnico em Desenvolvimento de Sistemas | ETEC / Centro Paula Souza<br/>"
        "Componente: Desenvolvimento de Sistemas I — Agenda 12 (HTML5, Semântica e GitHub Pages)<br/>"
        "Estudante: <b>Iraci Berto Gomes</b>  |  Arquivo de Entrega: <b>IraciBertoGomes_Ag12_DS_I</b>",
        subtitle_style
    ))
    story.append(Spacer(1, 4))

    # Seção 1
    story.append(Paragraph("1. Cenário e Proposta da Atividade", h1_style))
    story.append(Paragraph(
        "Na Sociedade da Informação e da Comunicação, os sistemas integrados à web representam a base da comunicação contemporânea. "
        "A atividade da Agenda 12 teve como objetivo a implementação prática de uma página estruturada em <b>HTML5</b> intitulada "
        "<i>'Meus sites favoritos'</i>, integrando cinco portais essenciais para o aprendizado e prática em Desenvolvimento de Sistemas.",
        body_style
    ))

    # Seção 2: Matriz de Conformidade
    story.append(Paragraph("2. Matriz de Conformidade com os Requisitos do Enunciado", h1_style))
    t1_data = [
        [Paragraph("<b>Requisito do Enunciado</b>", table_header),
         Paragraph("<b>Implementação no Projeto</b>", table_header),
         Paragraph("<b>Status</b>", table_header)],
        [Paragraph("Título (aba) da página", table_body), Paragraph("&lt;title&gt;Meus sites favoritos&lt;/title&gt;", table_body), Paragraph("<font color='#166534'><b>Atendido</b></font>", table_body)],
        [Paragraph("Título do corpo da página", table_body), Paragraph("Meus sites favoritos: Iraci Berto Gomes", table_body), Paragraph("<font color='#166534'><b>Atendido</b></font>", table_body)],
        [Paragraph("Nome de cada site acima da imagem", table_body), Paragraph("Tag &lt;h1&gt; para o nome de cada site", table_body), Paragraph("<font color='#166534'><b>Atendido</b></font>", table_body)],
        [Paragraph("5 Imagens locais dos sites", table_body), Paragraph("Imagens armazenadas na pasta raiz do HTML", table_body), Paragraph("<font color='#166534'><b>Atendido</b></font>", table_body)],
        [Paragraph("Link abaixo de cada imagem", table_body), Paragraph("Tag &lt;a href='...' target='_blank'&gt;", table_body), Paragraph("<font color='#166534'><b>Atendido</b></font>", table_body)],
        [Paragraph("Link na imagem (Opcional)", table_body), Paragraph("Tag &lt;img&gt; envolvida pela tag &lt;a&gt;", table_body), Paragraph("<font color='#166534'><b>Atendido</b></font>", table_body)],
        [Paragraph("Código comentado em linhas", table_body), Paragraph("Comentários didáticos em todas as tags", table_body), Paragraph("<font color='#166534'><b>Atendido</b></font>", table_body)]
    ]
    t1 = Table(t1_data, colWidths=[180, 260, 100])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor("#F8FAFC"), colors.white]),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t1)
    story.append(Spacer(1, 6))

    # Seção 3: Relação dos Sites
    story.append(Paragraph("3. Relação dos 5 Sites Favoritos Selecionados", h1_style))
    t2_data = [
        [Paragraph("<b>Site</b>", table_header),
         Paragraph("<b>Categoria</b>", table_header),
         Paragraph("<b>Justificativa Didática / Profissional</b>", table_header),
         Paragraph("<b>URL Oficial</b>", table_header)],
        [Paragraph("<b>GitHub</b>", table_body), Paragraph("Controle de Versão", table_body), Paragraph("Hospedagem de repositórios Git, colaboração open-source e portfólio.", table_body), Paragraph("github.com", table_body)],
        [Paragraph("<b>MDN Web Docs</b>", table_body), Paragraph("Documentação Web", table_body), Paragraph("Guia oficial mundial da Mozilla para HTML5, CSS3 e JavaScript.", table_body), Paragraph("developer.mozilla.org", table_body)],
        [Paragraph("<b>Stack Overflow</b>", table_body), Paragraph("Comunidade Dev", table_body), Paragraph("Fórum colaborativo para esclarecimento de dúvidas e correção de erros.", table_body), Paragraph("stackoverflow.com", table_body)],
        [Paragraph("<b>W3Schools</b>", table_body), Paragraph("Tutoriais Práticos", table_body), Paragraph("Plataforma interativa com testes em tempo real (Try it Yourself).", table_body), Paragraph("w3schools.com", table_body)],
        [Paragraph("<b>YouTube</b>", table_body), Paragraph("Vídeos & Educação", table_body), Paragraph("Videoaulas da ETEC/CPS, tutoriais práticos e momentos de lazer.", table_body), Paragraph("youtube.com", table_body)]
    ]
    t2 = Table(t2_data, colWidths=[90, 100, 240, 110])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), secondary),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor("#F8FAFC"), colors.white]),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t2)
    story.append(Spacer(1, 6))

    # Seção 4: Evidências Visuais
    story.append(Paragraph("4. Evidências de Execução no Navegador e Código Comentado", h1_style))
    img_nav = os.path.join(base_dir, "captura-execucao-navegador.png")
    if os.path.exists(img_nav):
        story.append(Paragraph("<b>Figura 1: Execução da página web renderizada no navegador (Desktop):</b>", body_style))
        story.append(RLImage(img_nav, width=540, height=280))
        story.append(Spacer(1, 4))

    img_code = os.path.join(base_dir, "captura-codigo-html-comentado.png")
    if os.path.exists(img_code):
        story.append(Paragraph("<b>Figura 2: Captura do código HTML5 com comentários didáticos no Visual Studio Code:</b>", body_style))
        story.append(RLImage(img_code, width=540, height=310))
        story.append(Spacer(1, 4))

    # Seção 5: Código Fonte
    story.append(PageBreak())
    story.append(Paragraph("5. Código-Fonte Oficial Comentado (IraciBertoGomes_Ag12_DS_I.html)", h1_style))
    html_file = os.path.join(base_dir, "IraciBertoGomes_Ag12_DS_I.html")
    with open(html_file, "r", encoding="utf-8") as f:
        codigo_linhas = f.readlines()

    # Formatar em blocos legíveis
    codigo_formatado = "".join(codigo_linhas).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    story.append(Paragraph(f"<pre>{codigo_formatado}</pre>", code_style))
    story.append(Spacer(1, 6))

    # Seção 6: Procedimento GitHub Pages
    story.append(Paragraph("6. Procedimento de Hospedagem no GitHub Pages", h1_style))
    story.append(Paragraph(
        "Seguindo o guia didático oficial da ETEC (<i>como_hospedar_um_site_no_github_pages1.pdf</i>), o projeto foi versionado com Git:<br/>"
        "• <b>Repositório GitHub:</b> https://github.com/bertogomesiraci-33/AGENDA_12.git<br/>"
        "• <b>Deploy GitHub Pages:</b> https://bertogomesiraci-33.github.io/AGENDA_12/<br/>"
        "• <b>Arquivo Principal:</b> index.html e IraciBertoGomes_Ag12_DS_I.html mantidos na raiz do projeto.",
        body_style
    ))

    # Conclusão
    story.append(Spacer(1, 4))
    story.append(Paragraph("7. Conclusão e Competências Consolidadas", h1_style))
    story.append(Paragraph(
        "A atividade foi finalizada com 100% de conformidade técnica em relação aos requisitos da Agenda 12. "
        "Apresenta estrutura semântica HTML5 completa, estilização moderna, responsividade para dispositivos móveis, "
        "código integralmente comentado e deploy funcional no GitHub Pages.",
        body_style
    ))

    doc.build(story)
    print(f"[OK] Documento PDF gerado com sucesso: {caminho_pdf}")


# ====================================================================
# GERADOR DE PACOTE ZIP PARA SUBMISSÃO NO FICHÁRIO
# ====================================================================

def gerar_zip(caminho_zip, base_dir):
    arquivos_incluir = [
        "IraciBertoGomes_Ag12_DS_I.html",
        "index.html",
        "style.css",
        "site1_github.png",
        "site2_mdn.png",
        "site3_stackoverflow.png",
        "site4_w3schools.png",
        "site5_youtube.png",
        "captura-execucao-navegador.png",
        "captura-execucao-mobile.png",
        "captura-codigo-html-comentado.png",
        "README.md",
        "IraciBertoGomes_Ag12_DS_I.docx",
        "IraciBertoGomes_Ag12_DS_I.pdf"
    ]

    with zipfile.ZipFile(caminho_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for arq in arquivos_incluir:
            caminho_completo = os.path.join(base_dir, arq)
            if os.path.exists(caminho_completo):
                zipf.write(caminho_completo, arcname=arq)
                print(f"  + Adicionado ao ZIP: {arq}")

    print(f"[OK] Pacote ZIP gerado com sucesso: {caminho_zip}")


if __name__ == "__main__":
    base_dir = r"c:\Users\Iraci\Desktop\estudos\AGENDA_12"
    caminho_docx = os.path.join(base_dir, "IraciBertoGomes_Ag12_DS_I.docx")
    caminho_pdf = os.path.join(base_dir, "IraciBertoGomes_Ag12_DS_I.pdf")
    caminho_zip = os.path.join(base_dir, "IraciBertoGomes_Ag12_DS_I.zip")

    # Também copia para a raiz de estudos caso o aluno queira acessar direto da pasta principal
    caminho_docx_raiz = r"c:\Users\Iraci\Desktop\estudos\IraciBertoGomes_Ag12_DS_I.docx"
    caminho_pdf_raiz = r"c:\Users\Iraci\Desktop\estudos\IraciBertoGomes_Ag12_DS_I.pdf"
    caminho_zip_raiz = r"c:\Users\Iraci\Desktop\estudos\IraciBertoGomes_Ag12_DS_I.zip"

    gerar_word(caminho_docx, base_dir)
    gerar_pdf(caminho_pdf, base_dir)
    gerar_zip(caminho_zip, base_dir)

    # Copiar para a raiz de estudos
    import shutil
    shutil.copyfile(caminho_docx, caminho_docx_raiz)
    shutil.copyfile(caminho_pdf, caminho_pdf_raiz)
    shutil.copyfile(caminho_zip, caminho_zip_raiz)
    print("[OK] Arquivos copiados também para c:\\Users\\Iraci\\Desktop\\estudos")
