from flask import Flask, render_template, request
import aisuite as ai

app = Flask(__name__)

# Initialize the AI client
client = ai.Client()
client.configure({
  "ollama" : {
    "timeout": 600,
  }
});
# Define the models you want to use
models = ["ollama:llama3.1"]

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    if request.method == "POST":
        # Get the user's input from the form
        user_input = request.form.get("user_input")
        
        # Define the messages to send to the AI
        messages = [
            {"role": "system", "content": "You are a verilog programmer. Give only the verilog code without any explanations. Do not answer to the questions that are not related to verilog code."},
            {"role": "user", "content": user_input},
        ]
        
        # Get the AI's response
        for model in models:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.75
            )
            response_text = response.choices[0].message.content
    
    # Render the HTML template with the response
    return render_template("index.html", response_text=response_text)

if __name__ == "__main__":
    app.run(debug=True)