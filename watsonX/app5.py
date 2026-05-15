import gradio as gr
# pillow ==> 밝기 변경
from PIL import ImageEnhance

def process_image(editor_value):
    
    '''
    composite : 원본 그리미 위에 레이어 반영한 최종 이미지
    '''

    image = editor_value['composite']
    enhancer = ImageEnhance.Brightness(image)
    result = enhancer.enhance(1.5)

    return result

# interface = gr.Interface(fn=process_image, inputs=gr.ImageEditor(type="pil"), outputs=gr.Textbox())
interface = gr.Interface(fn=process_image, inputs=gr.ImageEditor(type="pil"), outputs=gr.Image())
interface.launch()