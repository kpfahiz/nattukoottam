import cv2
import os
from datetime import datetime
from django.conf import settings


def add_text_to_certificate(name, blood_group, date):
    template_path=os.path.join(settings.MEDIA_ROOT, 'certificate_template.jpg')
    # Load the certificate image
    template = cv2.imread(template_path)

    # Check if the template was loaded successfully
    if template is None:
        raise FileNotFoundError(f"Template file not found at {template_path}")

    # Define the font and the position for the text
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (0, 0, 0)  # Black color in BGR
    thickness = 2

    # Coordinates for the text (adjust based on your certificate layout)
    name_position = (590, 495)
    blood_group_position = (590, 910)
    date_position = (590, 950)

    # Add text to the image
    cv2.putText(template, name, name_position, font, font_scale, color, thickness, cv2.LINE_AA)
    cv2.putText(template, blood_group, blood_group_position, font, font_scale, color, thickness, cv2.LINE_AA)
    cv2.putText(template, date, date_position, font, font_scale, color, thickness, cv2.LINE_AA)

    # Define the output path
    output_filename = f"certificate_{name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
    output_path = os.path.join(settings.MEDIA_ROOT, output_filename)
    
    # Save the output image
    cv2.imwrite(output_path, template)
    return output_path

