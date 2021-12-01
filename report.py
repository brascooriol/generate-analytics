#Python libraries
from fpdf import FPDF
import sys

#Local imports
sys.path.append('resources')
sys.path.append('tmp')
from resources import utils
from resources import github_req
from utils import plot_daily_new_cases_country,plot_daily_total_cases_country

WIDTH=210
HEIGHT=297

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial','B',16)
pdf.cell(40,10,'Hello World!')

filename=plot_daily_new_cases_country(country='Spain',mode='Deaths')
pdf.image(filename,5,30, WIDTH/2-5)

filename=plot_daily_total_cases_country(country='Spain',mode='Confirmed')
pdf.image(filename,WIDTH/2+5,30, WIDTH/2-5)

pdf.output('tuto1.pdf','F')