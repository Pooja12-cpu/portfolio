# api/chat.py
from flask import Flask, render_template, request, jsonify
import os
import json
import requests
app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():    
    return render_template("index.html")

@app.route("/get_response", methods=['POST'])
def get_response():
    user_message = request.json['message']
    response = requests.post(
      url="https://openrouter.ai/api/v1/chat/completions",
      headers={
        "Authorization": "Bearer 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",
      },
      data=json.dumps({
        "model": "arcee-ai/trinity-large-preview:free", # Optional
        "messages": [
          {
            "role": "user",
            "content": """Context: Pooja currently works as a Research Associate at Michigan Medicine and is working on an LLM-based model for gene expression prediction from pathology images for furthering research in cancer prognosis. At her position in Michigan Medicine, she engineered a large language model (LLM) based gene expression prediction system using Hugging Face and PyTorch Lightning, achieving a 20% MSE improvement over existing ML baselines. She also designed and implemented a cross-modal attention transformer to fuse multimodal biological datasets, significantly enhancing predictive accuracy and model generalization. She developed a scalable gene expression analysis pipeline in Python using Seaborn and Pandas to automate visualization tasks (e.g., heatmaps, UMAPs) for model evaluation and data exploration. This role demonstrated her skills in LLM development, data processing and research acumen.
    
    Pooja also worked as a Software Engineer Intern at Xfinion Inc for 8 months from May 2024 to December 2024. Here she developed a full-stack Gen AI website for using an LLM that can take in multiple documents at a time and answer user questions pertaining to the contents of the document. For building this, she leveraged libraries including HuggingFace, TensorFlow and PyTorch to extract more than 10 high-end LLMs and fine-tune them for the specific use case. She also developed a website frontend using H2O-wave tools and best-performing models chosen after testing in the backend for document parsing and question-answering. She deployed this web application using the CI/CD pipeline available on GitHub actions. In addition to this, at the same position Pooja also worked on a backend engineering and data science project where she developed an embedded Java application for a Linux environment for operating an RFID Reader as an edge-device to collect RFID data at specific intervals of time and store collected data into an MS SQL database on the cloud via Kafka. She performed tag data visualization using Tableau to determine patterns in RFID tag readings over a period of a month and contributed to finding most optimum locations for tag reader installations. This role demonstrates her multitasking abilities and her skills in developing production ready LLMs and ML models.
    
    Pooja also has a lot of experience working with CNNs and computer vision projects. As a Research Assistant at the University of Michigan she developed a Python-based program to measure vitals of drivers, such as heart rate and respiratory rate, as a safety precaution to prevent car accidents. She also built an ML-based framework to detect facial landmarks and apply pose estimation to calculate heart rate and respiratory rate from image and depth data from a 3D iToF camera. She was able to improve accuracy of the heart rate measurement from 75% to 90% throughout the development process. She worked at this position for 10 months starting in November 2023 till September 2024. This position demonstrates her ability in working with 3D image data and developing computer vision models.
    
    In addition to this, at Unilactic Enterprises she also designed a CNN using PyTorch for detecting cars, pedestrians, and vehicles through drone cameras with an additional tracking system for any selected objects on screen - also demonstrating her skills in working with image data. At the same position she also contributed to a 10% power consumption reduction in a drone motor through an application to process Dyson motor power input and output data to visualize peak times and trends of power usage using PyQt and Pandas on Python.
    
    Pooja also has some published work. For instance she developed a novel hybrid GAN (Generative Adversarial Network) Algorithm with autoencoder for reducing intensity inhomogeneity in brain MR-images using TensorFlow on Python. She was able to improve the SSIM, MSSSIM and PSNR values of resulting images by about 80-90% as compared to traditional methods and previously suggested intensity inhomogeneity correction methods. Her published work can be viewed at https://www.nature.com/articles/s41598-025-08552-8.
    She also published another paper in the ML field in which she developed a full-stack machine learning algorithm using KNN classifier on Python to design a system to predict elevator emergencies and send alerts and shortest path map to elevator to the maintenance crew through an Android application. The written research paper for this work was accepted for publication by the IEEE Xplore library in July 2022 at https://ieeexplore.ieee.org/document/9915909.
    
    In her spare time, Pooja loves reading, watching anime and just fangirling over superheroes. She is also an ardent space and astronomy fanatic and occasionally leaves her home (albeit forcefully) for some star-gazing.\n\nQuestion:""" + user_message + "\nAnswer:"
          }
        ]
      })
    )
    temp = json.loads(response.content.decode('utf-8'))
    r_response = temp['choices'][0]['message']['content']
    return jsonify({'response': r_response})

if __name__ == "__main__":
    app.run(debug=True)