import gradio as gr

def cheer(name, level):
    return name + "🧨" * int(level)

def review(name, grade):
    return name + "⭐" * int(grade)

def bmi_calculator(height, weight):

    #몸무게 / (키 / 100 **2 )
    bmi = weight / ((float(height) / 100) ** 2)
    if bmi < 18.5:
        result = "저체중"
    elif bmi < 22.9:
        result = "정상체중"
    elif bmi < 24.9:
        result = "과체중"
    else:
        result = "비만"

    print(result + str(bmi))
    return f"당신의 몸무게는 {weight}이며, 현재 {result}입니다."

with gr.Blocks() as demo:
    with gr.Tab("응원"):
        name = gr.Text(label="이름")
        cheer_strength = gr.Slider(1,5,label="응원강도")
        msg = gr.Textbox(label="응원 메시지")
        cheer_btn = gr.Button("응원!")
        cheer_btn.click(fn=cheer, inputs=[name, cheer_strength], outputs=[msg])
    with gr.Tab("별점"):
        name = gr.Text(label="음식명")
        level = gr.Slider(1,5,label="별점")
        msg = gr.Textbox(label="만족도 확인")
        review_btn = gr.Button("별점 등록")
        review_btn.click(fn=review, inputs=[name, level], outputs=[msg])
    with gr.Tab("bmi"):
        height = gr.Number(label="키")
        weight = gr.Number(label="몸무게")
        result = gr.Text(label="BMI 판정")
        bmi_btn = gr.Button("BMI 판정")
        bmi_btn.click(fn=bmi_calculator, inputs=[height,weight], outputs=[result])

demo.launch()