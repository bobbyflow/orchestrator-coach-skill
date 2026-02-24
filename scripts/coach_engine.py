import json
import sys
import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class CoachPDF(FPDF):
    def header(self):
        self.set_fill_color(30, 58, 138)
        self.rect(0, 0, 210, 28, 'F')
        self.set_font('helvetica', 'B', 18)
        self.set_text_color(255, 255, 255)
        self.set_y(9)
        self.cell(0, 10, self.custom_title, align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(10)

    def footer(self):
        self.set_y(-12)
        self.set_font('helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, 'Orchestrator Coach Skill | High-Signal AI Mentorship', align='C')

    def chapter_title(self, title):
        self.ln(2)
        self.set_font('helvetica', 'B', 14)
        self.set_text_color(30, 58, 138)
        self.cell(0, 10, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(30, 58, 138)
        self.set_line_width(0.4)
        self.line(self.get_x(), self.get_y(), self.get_x() + 190, self.get_y())
        self.ln(4)

    def section_header(self, title):
        self.set_font('helvetica', 'B', 11.5)
        self.set_text_color(50, 50, 50)
        self.cell(0, 8, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def body_text(self, text, style=''):
        self.set_font('helvetica', style, 10.5)
        self.set_text_color(60, 60, 60)
        self.multi_cell(0, 6.5, text)
        self.ln(2)

    def prompt_box(self, text):
        self.set_fill_color(242, 247, 255)
        self.set_font('helvetica', 'I', 9.5)
        self.set_text_color(30, 58, 138)
        self.multi_cell(0, 6, text, fill=True, border='L')
        self.ln(4)

def generate_lesson(data):
    pdf = CoachPDF()
    pdf.custom_title = data.get('title', 'ORCHESTRATOR LESSON')
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)

    for section in data.get('sections', []):
        if section['type'] == 'chapter':
            pdf.chapter_title(section['content'])
        elif section['type'] == 'header':
            pdf.section_header(section['content'])
        elif section['type'] == 'body':
            pdf.body_text(section['content'])
        elif section['type'] == 'prompt':
            pdf.prompt_box(section['content'])
        elif section['type'] == 'emphasis':
            pdf.body_text(section['content'], 'B')

    output_path = data.get('output_path', 'lesson.pdf')
    pdf.output(output_path)
    print(f"SUCCESS: PDF generated at {output_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            generate_lesson(json.load(f))
