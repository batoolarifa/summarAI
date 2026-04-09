# SummarAI Professional Text Summarization Application

**SummarAI** is an AI-powered text summarization tool built with a **fine-tuned T5 Transformer model**. It transforms long-form content articles, research papers, reports, meeting notes into concise, accurate summaries while preserving key insights and context.

This application is ideal for **business intelligence, content management, research efficiency, and customer engagement**.


## 🚀 Key Features

* **Automatic Summarization**: Reduce long-form text to concise summaries while retaining critical information.
  
* **Smart Capitalization**: First letters of sentences and abbreviations (e.g., NLP, AI, ML) are automatically capitalized for professional readability.
  
* **Abbreviation Handling**: Maintains consistent uppercase formatting for industry terms like NLP, AI, API, BERT, GPT.
  
* **Text Cleaning**: Removes HTML tags, extra spaces, invisible Unicode characters, and non-standard line breaks.
  
* **Web Interface**: Simple, responsive UI with copy-to-clipboard functionality for easy workflow integration.
  
* **Adaptable for Industry**: Ideal for content analysts, business intelligence teams, researchers, and developers.

##  Impact and Use Cases

* **Enterprise Efficiency**: Automates review of large volumes of unstructured data such as emails, reports, and customer feedback.
  
* **Research Optimization**: Speeds up reading and knowledge extraction from academic papers and technical documents.

* **Customer Insights**: Helps marketing and product teams understand social media sentiment, survey results, and reviews quickly.

* **Content Management**: Streamlines summarization for blogs, news articles, or internal documentation.


##  Application UI

Here’s a preview of **SummarAI** in action:

![Home Screen](https://github.com/user-attachments/assets/a762f755-6034-4a19-a79e-4318e5ee139a)  

The interface where users can paste or type their text for summarization.

![Generating Summary](https://github.com/user-attachments/assets/fa43e8f3-2482-4a50-b79e-263bcffb88c9)  

The application processes the input text to generate a concise summary.

![Formatted Summary Output](https://github.com/user-attachments/assets/28a0eea5-9015-4df4-acdb-099ade51a6bd)  

Final summarized text with proper capitalization, punctuation, and abbreviation handling.



## 📂 Folder Structure

```text
summarAI/
│
├─ app/
│  ├─ __init__.py
│  ├─ app.py                 # Flask web 
│  ├─ model.py               # T5 
│  ├─ utils/
│  │   ├─ __init__.py
│  │   └─ abbreviations.py   # Common abbreviations dictionary
│  ├─ static/
│  │   ├─ css/style.css
│  │   └─ js/script.js
│  └─ templates/
│      └─ index.html         # Web UI template
│
├─ notebook/
│  └─ fine_tune_t5.ipynb     # Notebook used to fine-tune the T5 model
│
├─ summary_model/
│  ├─ model/                 # Fine-tuned T5 model files
│  └─ tokenizer/             # Tokenizer files
│
├─ requirements.txt
├─ Dockerfile           
└─ README.md                  
```


## ⚡ Installation

1. **Clone the repository**:

```bash
git clone https://github.com/batoolarifa/summarAI.git
cd summarAI 
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

```bash
python -m app.app
```


## 📝 Usage

1. Paste or type your text into the input box.
2. Click **Generate Summary**.
3. Copy the summary using the **Copy Summary** button.

**Output formatting includes**:

* Capitalized first letters and proper spacing after punctuation.
* Uppercase industry abbreviations defined in `utils/abbreviations.py`.
* Proper sentence-ending punctuation.


## Industry Relevance

* **Content Automation**: Reduces manual summarization workload
  
* **Business Intelligence**: Quickly extracts insights from unstructured text
* **Customer Experience**: Enhances response and analysis speed
  
* **Scalable**: Deployable to Hugging Face, internal servers, or cloud-based solutions
  
* **Customizable**: Model fine-tuning allows domain-specific summarization




## 👤 Author

**Syeda Arifa Batool**  
SE @ Karachi University | AI & ML Practitioner | Applying technology to create real-world value 📈



## 🔗 Connect with Me

- **LinkedIn:** [Syeda Arifa Batool](https://www.linkedin.com/in/arifa-batool/)  
- **Kaggle:** [Syeda Arifa Batool](https://www.kaggle.com/arifa-batool/)  
- **Email:** [thearifabatool@gmail.com](mailto:thearifabatool@gmail.com)

⭐ If you find this project useful, feel free to star the repository!

