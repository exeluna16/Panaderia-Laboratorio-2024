from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from datetime import datetime
import io
from django.http import FileResponse

def generar_reporte_tabla(datos,titulo, nombre_archivo="reporte.pdf"):
    # Crear un buffer para el archivo PDF
    buffer = io.BytesIO()
    
    # Crear el documento PDF
    pdf = SimpleDocTemplate(buffer, pagesize=A4)
    
    # Estilos para el título y el contenido
    estilos = getSampleStyleSheet()
    titulo_reporte = Paragraph(titulo, estilos['Title'])
    fecha = Paragraph(f"Fecha: {datetime.now().strftime('%d/%m/%Y')}", estilos['Normal'])
    
    # Crear la tabla con los datos
    tabla = Table(datos)
    
    # Configurar el estilo de la tabla
    estilo_tabla = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    
    # Aplicar el estilo a la tabla
    tabla.setStyle(estilo_tabla)
    
    # Generar el contenido del PDF
    contenido = [titulo_reporte, Spacer(1, 12), fecha, Spacer(1, 12), tabla]
    
    # Construir el PDF
    pdf.build(contenido)
    
    # Posicionar el puntero al inicio del buffer
    buffer.seek(0)
    
    # Retornar el PDF como respuesta
    return FileResponse(buffer, as_attachment=True, filename=nombre_archivo)


def fecha_actual_strig():
    fecha = datetime.now()
    return fecha.strftime('%d/%m/%Y')
