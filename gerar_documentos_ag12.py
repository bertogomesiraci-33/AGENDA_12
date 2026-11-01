"""
Script de Geração de Documentos Oficiais - Agenda 12 (Desenvolvimento de Sistemas I)
Estudante: Iraci Berto Gomes
Instituição: ETEC / Centro Paula Souza (CPS)
Projeto: Meus Sites Favoritos (HTML / Web I)

Gera automaticamente:
1. IraciBertoGomes_Ag12_DS_I.docx
2. IraciBertoGomes_Ag12_DS_I.pdf
3. IraciBertoGomes_Ag12_DS_I.zip
"""

import os
import sys
import zipfile
import shutil
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
    run_title = p_title.add_run("RELATÓRIO TÉCNICO DE DESENVOLVIMENTO DE SOFTWARE")
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
        "Componente: Desenvolvimento de Sistemas I — Agenda 12 (HTML / Web I)\n"
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
        "Na Sociedade da Informação e da Comunicação, é essencial que as empresas e profissionais divulguem seus serviços "
        "e conhecimentos por meio de sistemas web integrados. O objetivo desta atividade prática da Agenda 12 é consolidar os "
        "conceitos fundamentais da linguagem de marcação HTML estudados na apostila didática da ETEC (agenda_12_web_i_dsi_i_atualizada1_251.pdf)."
    )
    add_body(
        "A página foi desenvolvida para organizar 5 sites favoritos do cotidiano para compras online e rastreamento de encomendas: "
        "Shopee, Mercado Livre, Correios, Casas Bahia e Amazon, aplicando com fidelidade a estrutura de tags exigida pelo enunciado."
    )

    # Seção 2: Checklist de Atendimento aos Requisitos
    add_section_header("2. Matriz de Atendimento aos Requisitos do Enunciado")
    
    table_req = doc.add_table(rows=8, cols=3)
    table_req.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_req.autofit = False

    col_widths_req = [Inches(2.4), Inches(2.3), Inches(2.2)]
    headers_req = ["Requisito do Enunciado", "Implementação no Código HTML", "Status de Conformidade"]

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
        ("Nome de cada site acima da imagem", "Tag <h1> com o nome de cada site", "Atendido (Conforme Dica)"),
        ("5 Imagens locais dos sites", "Imagens salvas na mesma pasta do HTML", "Atendido com Arquivos Locais"),
        ("Link abaixo de cada imagem", "Tag <a href='...' target='_blank'>", "Atendido com Target Blank"),
        ("Link na própria imagem (Opcional)", "Tag <img> dentro da tag <a> clicável", "Atendido (Diferencial)"),
        ("Código com comentários em linhas", "Comentários didáticos <!-- --> nas tags", "Atendido Linha a Linha")
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
                r.font.color.rgb = RGBColor(22, 101, 52)

    # Seção 3: Seleção dos 5 Sites Favoritos
    add_section_header("3. Relação dos 5 Sites Selecionados e Tags Utilizadas")
    add_body("Conforme o material de estudo da Agenda 12, cada site foi estruturado com as tags <h1>, <figure>, <img>, <figcaption>, <p> e <a>:")

    table_sites = doc.add_table(rows=6, cols=4)
    table_sites.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_sites.autofit = False

    col_widths_sites = [Inches(1.2), Inches(1.5), Inches(2.2), Inches(2.0)]
    headers_sites = ["Site", "Categoria", "Descrição Didática", "Arquivo Local da Imagem"]

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
        ("Shopee", "E-commerce & Ofertas", "Ofertas diárias relâmpago, cupons e frete grátis em produtos diversos.", "site1_shopee.png"),
        ("Mercado Livre", "Marketplace", "Compras seguras com Mercado Pago e entregas rápidas na modalidade Full.", "site2_mercadolivre.png"),
        ("Correios", "Rastreio e Logística", "Acompanhamento em tempo real de encomendas, cálculo de prazos e Sedex.", "site3_correios.png"),
        ("Casas Bahia", "Varejo", "Móveis, eletrodomésticos, tecnologia e condições no carnê digital.", "site4_casasbahia.png"),
        ("Amazon", "E-commerce Global", "Entregas rápidas Prime, catálogo amplo de eletrônicos, livros e promoções.", "site5_amazon.png")
    ]

    for row_idx, row_data in enumerate(dados_sites, start=1):
        bg = "F8FAFC" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, val in enumerate(row_data):
            cell = table_sites.cell(row_idx, col_idx)
            cell.width = col_widths_sites[col_idx]
            set_cell_background(cell, bg)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx in (0, 3) else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(8.5)
            r.font.color.rgb = dark
            if col_idx == 0:
                r.bold = True

    # Seção 4: Evidências de Execução e Código
    add_section_header("4. Evidências de Execução no Navegador e Código Comentado")
    add_body("Conforme orientação da atividade, são apresentadas abaixo as capturas comprobatórias:")

    img_nav = os.path.join(base_dir, "captura-execucao-navegador.png")
    if os.path.exists(img_nav):
        p_cap1_title = doc.add_paragraph()
        p_cap1_title.paragraph_format.space_before = Pt(6)
        r = p_cap1_title.add_run("Figura 1: Execução da página web renderizada no navegador com as capturas dos sites:")
        r.bold = True
        r.font.size = Pt(9)
        p_img1 = doc.add_paragraph()
        p_img1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img1.paragraph_format.space_after = Pt(8)
        p_img1.add_run().add_picture(img_nav, width=Inches(6.2))

    img_code = os.path.join(base_dir, "captura-codigo-html-comentado.png")
    if os.path.exists(img_code):
        p_cap2_title = doc.add_paragraph()
        p_cap2_title.paragraph_format.space_before = Pt(6)
        r = p_cap2_title.add_run("Figura 2: Código HTML com comentários nas linhas no Visual Studio Code:")
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
    add_section_header("6. Hospedagem no GitHub e GitHub Pages")
    add_body(
        "Em observância ao guia 'Como hospedar um site no GitHub Pages' disponibilizado pelo Centro Paula Souza, "
        "o projeto foi enviado ao GitHub e publicado online:"
    )
    add_body(
        "• Repositório no GitHub: https://github.com/bertogomesiraci-33/AGENDA_12\n"
        "• Site no ar via GitHub Pages: https://bertogomesiraci-33.github.io/AGENDA_12/\n"
        "• Arquivo principal: index.html e IraciBertoGomes_Ag12_DS_I.html na raiz do repositório."
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
    story.append(Paragraph("RELATÓRIO TÉCNICO DE DESENVOLVIMENTO DE SOFTWARE", title_style))
    story.append(Paragraph(
        "Curso Técnico em Desenvolvimento de Sistemas | ETEC / Centro Paula Souza<br/>"
        "Componente: Desenvolvimento de Sistemas I — Agenda 12 (HTML / Web I)<br/>"
        "Estudante: <b>Iraci Berto Gomes</b>  |  Arquivo de Entrega: <b>IraciBertoGomes_Ag12_DS_I</b>",
        subtitle_style
    ))
    story.append(Spacer(1, 4))

    # Seção 1
    story.append(Paragraph("1. Cenário e Proposta da Atividade", h1_style))
    story.append(Paragraph(
        "A atividade prática da Agenda 12 teve como objetivo a implementação de uma página web aplicando estritamente "
        "as tags básicas de <b>HTML</b> estudadas no material didático (<i>agenda_12_web_i_dsi_i_atualizada1_251.pdf</i>), "
        "intitulada <i>'Meus sites favoritos'</i> com 5 plataformas do cotidiano: <b>Shopee, Mercado Livre, "
        "Correios, Casas Bahia e Amazon</b>.",
        body_style
    ))

    # Seção 2: Matriz de Conformidade
    story.append(Paragraph("2. Matriz de Atendimento aos Requisitos do Enunciado", h1_style))
    t1_data = [
        [Paragraph("<b>Requisito do Enunciado</b>", table_header),
         Paragraph("<b>Implementação no Código HTML</b>", table_header),
         Paragraph("<b>Status</b>", table_header)],
        [Paragraph("Título (aba) da página", table_body), Paragraph("&lt;title&gt;Meus sites favoritos&lt;/title&gt;", table_body), Paragraph("<font color='#166534'><b>Atendido</b></font>", table_body)],
        [Paragraph("Título do corpo da página", table_body), Paragraph("Meus sites favoritos: Iraci Berto Gomes", table_body), Paragraph("<font color='#166534'><b>Atendido</b></font>", table_body)],
        [Paragraph("Nome de cada site acima da imagem", table_body), Paragraph("Tag &lt;h1&gt; para o nome de cada site", table_body), Paragraph("<font color='#166534'><b>Atendido</b></font>", table_body)],
        [Paragraph("5 Imagens locais dos sites", table_body), Paragraph("Imagens salvas na pasta raiz do HTML", table_body), Paragraph("<font color='#166534'><b>Atendido</b></font>", table_body)],
        [Paragraph("Link abaixo de cada imagem", table_body), Paragraph("Tag &lt;a href='...' target='_blank'&gt;", table_body), Paragraph("<font color='#166534'><b>Atendido</b></font>", table_body)],
        [Paragraph("Link na imagem (Opcional)", table_body), Paragraph("Tag &lt;img&gt; dentro da tag &lt;a&gt;", table_body), Paragraph("<font color='#166534'><b>Atendido</b></font>", table_body)],
        [Paragraph("Código comentado em linhas", table_body), Paragraph("Comentários didáticos nas tags HTML", table_body), Paragraph("<font color='#166534'><b>Atendido</b></font>", table_body)]
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
    story.append(Paragraph("3. Relação dos 5 Sites Selecionados e Tags Utilizadas", h1_style))
    t2_data = [
        [Paragraph("<b>Site</b>", table_header),
         Paragraph("<b>Categoria</b>", table_header),
         Paragraph("<b>Descrição Didática</b>", table_header),
         Paragraph("<b>Arquivo da Imagem</b>", table_header)],
        [Paragraph("<b>Shopee</b>", table_body), Paragraph("E-commerce & Ofertas", table_body), Paragraph("Promoções diárias, cupons de desconto e frete grátis.", table_body), Paragraph("site1_shopee.png", table_body)],
        [Paragraph("<b>Mercado Livre</b>", table_body), Paragraph("Marketplace", table_body), Paragraph("Compras seguras com Mercado Pago e entregas rápidas Full.", table_body), Paragraph("site2_mercadolivre.png", table_body)],
        [Paragraph("<b>Correios</b>", table_body), Paragraph("Rastreio e Logística", table_body), Paragraph("Acompanhamento de encomendas em tempo real e cálculo de frete.", table_body), Paragraph("site3_correios.png", table_body)],
        [Paragraph("<b>Casas Bahia</b>", table_body), Paragraph("Varejo", table_body), Paragraph("Eletrodomésticos, móveis, tecnologia e carnê digital.", table_body), Paragraph("site4_casasbahia.png", table_body)],
        [Paragraph("<b>Amazon</b>", table_body), Paragraph("E-commerce Global", table_body), Paragraph("Entregas rápidas Prime, livros, tecnologia e promoções.", table_body), Paragraph("site5_amazon.png", table_body)]
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
        story.append(Paragraph("<b>Figura 1: Execução da página web renderizada no navegador:</b>", body_style))
        story.append(RLImage(img_nav, width=540, height=280))
        story.append(Spacer(1, 4))

    img_code = os.path.join(base_dir, "captura-codigo-html-comentado.png")
    if os.path.exists(img_code):
        story.append(Paragraph("<b>Figura 2: Código HTML com comentários nas linhas no Visual Studio Code:</b>", body_style))
        story.append(RLImage(img_code, width=540, height=310))
        story.append(Spacer(1, 4))

    # Seção 5: Código Fonte
    story.append(PageBreak())
    story.append(Paragraph("5. Código-Fonte Oficial Comentado (IraciBertoGomes_Ag12_DS_I.html)", h1_style))
    html_file = os.path.join(base_dir, "IraciBertoGomes_Ag12_DS_I.html")
    with open(html_file, "r", encoding="utf-8") as f:
        codigo_linhas = f.readlines()

    codigo_formatado = "".join(codigo_linhas).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    story.append(Paragraph(f"<pre>{codigo_formatado}</pre>", code_style))
    story.append(Spacer(1, 6))

    # Seção 6: Procedimento GitHub Pages
    story.append(Paragraph("6. Procedimento de Hospedagem no GitHub Pages", h1_style))
    story.append(Paragraph(
        "Em observância ao guia oficial da ETEC (<i>como_hospedar_um_site_no_github_pages1.pdf</i>):<br/>"
        "• <b>Repositório GitHub:</b> https://github.com/bertogomesiraci-33/AGENDA_12<br/>"
        "• <b>Deploy GitHub Pages:</b> https://bertogomesiraci-33.github.io/AGENDA_12/<br/>"
        "• <b>Arquivo Principal:</b> index.html e IraciBertoGomes_Ag12_DS_I.html na raiz do projeto.",
        body_style
    ))

    # Conclusão
    story.append(Spacer(1, 4))
    story.append(Paragraph("7. Conclusão", h1_style))
    story.append(Paragraph(
        "A atividade foi finalizada em total conformidade com o conteúdo didático da Agenda 12. "
        "Apresenta estrutura básica e fundamental de HTML conforme ensinado no material de apoio da ETEC, "
        "imagens locais autênticas de cada site, links funcionais com target='_blank' e hospedagem no GitHub Pages.",
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
        "site1_shopee.png",
        "site2_mercadolivre.png",
        "site3_correios.png",
        "site4_casasbahia.png",
        "site5_amazon.png",
        "captura-execucao-navegador.png",
        "captura-execucao-mobile.png",
        "captura-codigo-html-comentado.png",
        "README.md",
        "publicar_github.bat",
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

    caminho_docx_raiz = r"c:\Users\Iraci\Desktop\estudos\IraciBertoGomes_Ag12_DS_I.docx"
    caminho_pdf_raiz = r"c:\Users\Iraci\Desktop\estudos\IraciBertoGomes_Ag12_DS_I.pdf"
    caminho_zip_raiz = r"c:\Users\Iraci\Desktop\estudos\IraciBertoGomes_Ag12_DS_I.zip"

    gerar_word(caminho_docx, base_dir)
    gerar_pdf(caminho_pdf, base_dir)
    gerar_zip(caminho_zip, base_dir)

    # Copiar também para a raiz de estudos
    shutil.copyfile(caminho_docx, caminho_docx_raiz)
    shutil.copyfile(caminho_pdf, caminho_pdf_raiz)
    shutil.copyfile(caminho_zip, caminho_zip_raiz)
    print("[OK] Arquivos copiados também para c:\\Users\\Iraci\\Desktop\\estudos")
