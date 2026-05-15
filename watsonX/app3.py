import gradio as gr

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
    return "당신은 " + result + "입니다."

demo = gr.Interface(
    fn=bmi_calculator, # function
    inputs=[gr.Number(label="키"), gr.Number(label="몸무게")],
    outputs=[gr.Text(label="BMI 판정")],
    api_name="BMI 판정기"
)

demo.launch()