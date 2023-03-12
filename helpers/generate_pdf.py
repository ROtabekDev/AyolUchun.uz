from fpdf import FPDF
 

def generate_certificate(course_name, user_name, completed_course_id):

    pdf = FPDF()
     
    pdf.add_page()
     
    pdf.set_font("Arial", size = 15)
     
    pdf.cell(200, 10, txt = user_name,
            ln = 1, align = 'C')
     
    pdf.cell(200, 10, txt = course_name,
            ln = 2, align = 'C')
     
    pdf.output(f"media/main/certificate/file/{user_name}_{course_name}_{completed_course_id}.pdf")  


# generate_certificate(course_name='Python backend developer', user_name='Rahmonov Otabek', completed_course_id=1)
