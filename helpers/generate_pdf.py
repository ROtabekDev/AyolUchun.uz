from fpdf import FPDF
 

def generate_certificate(course_name, user_name, completed_course_id):
    # save FPDF() class into a
    # variable pdf
    pdf = FPDF()
    
    # Add a page
    pdf.add_page()
    
    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size = 15)
    
    # create a cell
    pdf.cell(200, 10, txt = user_name,
            ln = 1, align = 'C')
    
    # add another cell
    pdf.cell(200, 10, txt = course_name,
            ln = 2, align = 'C')
    
    # save the pdf with name .pdf
    pdf.output(f"media/main/certificate/file/{user_name}_{course_name}_{completed_course_id}.pdf")  


# generate_certificate(course_name='Python backend developer', user_name='Rahmonov Otabek', completed_course_id=1)
