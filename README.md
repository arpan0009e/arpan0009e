<!-- ========================= HEADER ========================= -->
<div align="center">

<!-- <img width="100%" src="https://capsule-render.vercel.app/api?type=venom&color=0:0f0c29,50:302b63,100:24243e&height=240&section=header&text=Arpan%20Mondal&fontSize=62&fontColor=ffffff&fontAlignY=42&desc=AI%20%2F%20ML%20Engineer%20%E2%80%A2%20LLM%20%26%20RAG%20%E2%80%A2%20Backend%20Systems&descAlignY=64&descSize=18&animation=fadeIn" /> -->

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&pause=1100&color=A78BFA&center=true&vCenter=true&width=700&lines=Building+production-minded+AI+systems;RAG+%7C+LLM+Fine-Tuning+%7C+FastAPI;B.Tech+AI+%26+ML+%E2%80%A2+Class+of+2027;Open+to+AI%2FML+internships+%26+entry-level+roles)](https://git.io/typing-svg)

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/arpan0009e)
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/arpan0009e)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:arpanmondal708@gmail.com)
[![Resume](https://img.shields.io/badge/Resume-00897B?style=for-the-badge&logo=readthedocs&logoColor=white)](https://drive.google.com/file/d/1o5NIxA7jt3gwbkxdDijbH9VYNXVRJwmw/view?usp=sharing)
![Profile Views](https://komarev.com/ghpvc/?username=arpan0009e&style=for-the-badge&color=7c3aed&label=PROFILE+VIEWS)

<br/>


</div>

---

##  About

```python
class Arpan:
    name        = "Arpan Mondal"
    role        = "Aspiring AI / ML Engineer"
    education   = "B.Tech in AI & ML @ NIMS University, Jaipur (2023 – 2027)"
    based_in    = "Jaipur / Kolkata, India 🇮🇳"
    languages   = ["English", "Hindi", "Bengali"]

    focus = [
        "LLM apps with Retrieval-Augmented Generation (RAG)",
        "Parameter-efficient fine-tuning (LoRA / QLoRA)",
        "Production-ready APIs with FastAPI",
        "End-to-end ML pipelines: data -> model -> deploy",
    ]

    learning    = ["Transformers internals", "MLOps (Docker, DVC, AWS)", "Agentic systems"]
    status      = "🟢 Open to AI/ML internships & entry-level roles"
    goal        = "Become an AI Engineer who ships reliable, useful AI products"

    def say_hi(self):
        print("Thanks for stopping by. Let's build something great together!")
```

---

##  Tech Stack

<div align="center">

### Languages
<img src="https://skillicons.dev/icons?i=py,cpp,c,js&theme=dark" />

### ML / Deep Learning
<img src="https://skillicons.dev/icons?i=pytorch,tensorflow,sklearn,opencv,numpy,pandas&theme=dark" />

![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![spaCy](https://img.shields.io/badge/spaCy-09A3D5?style=for-the-badge&logo=spacy&logoColor=white)
![Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)

### GenAI & NLP
`RAG` · `Vector DBs (FAISS, ChromaDB)` · `Embeddings` · `LoRA / QLoRA / PEFT` · `Prompt Engineering` · `NLTK` · `Tokenization`

### Backend & Databases
<img src="https://skillicons.dev/icons?i=fastapi,nodejs,express,mongodb,mysql,postgres&theme=dark" />

### Frontend
<img src="https://skillicons.dev/icons?i=react,tailwind,streamlit&theme=dark" />

### Cloud, MLOps & Tools
<img src="https://skillicons.dev/icons?i=aws,docker,git,github,vercel,linux,vscode&theme=dark" />

![DVC](https://img.shields.io/badge/DVC-13ADC7?style=for-the-badge&logo=dvc&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=black)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

</div>

---

##  Featured Projects

###  [MedExplain](https://github.com/arpan0009e/MedExplain) — Medical Report Explanation Platform
> Turns complex medical reports into clear, patient-friendly explanations using an LLM + RAG pipeline.

- Built with **FastAPI + Pydantic**, with PDF/document processing, embeddings, and **vector-database retrieval** to ground answers in authoritative medical sources
- **MongoDB** persistence for context-aware, follow-up Q&A
- `Python` `FastAPI` `Pydantic` `RAG` `Vector DB` `MongoDB` `LLM`

```mermaid
flowchart LR
    A[📄 Medical Report PDF] --> B[Parse & Chunk]
    B --> C[Embeddings]
    C --> D[(Vector DB)]
    E[❓ User Question] --> F[Retriever]
    D --> F
    F --> G[LLM]
    G --> H[✅ Patient-friendly Answer]
    G --> I[(MongoDB)]
```

<br/>

###  Domain-Specific LLM Fine-Tuning (LoRA / QLoRA)
> Adapted an open-source LLM to a niche Q&A domain on limited GPU resources.

- Curated a custom instruction-style dataset of **400+ Q&A examples**
- Applied **LoRA + 4-bit QLoRA quantization** (PEFT) to fine-tune efficiently while preserving the base model's general language ability
- `Python` `PyTorch` `Hugging Face Transformers` `PEFT` `QLoRA`

```mermaid
flowchart LR
    A[📚 Custom Q&A Dataset<br/>400+ examples] --> B[Format as<br/>Instruction Prompts]
    B --> C[Tokenize]
    D[🤖 Base Open-Source LLM] --> E[4-bit QLoRA<br/>Quantization]
    E --> F[Attach LoRA Adapters<br/>PEFT]
    C --> G[Fine-Tune on<br/>Limited GPU]
    F --> G
    G --> H[Evaluate<br/>Domain Q&A]
    H --> I[✅ Domain-Adapted Model]
```

<br/>

###  AI Travel Planner
> Generates personalized, budget-aware, day-by-day travel itineraries.

- Powered by the **Google Gemini API**; recommendations are grounded in real places via the **Google Maps Places API**
- Deployed on **Streamlit Community Cloud**
- `Python` `Gemini API` `Streamlit` `Google Maps API`

```mermaid
flowchart LR
    A[🧳 User Input<br/>Destination, Days, Budget] --> B[Streamlit UI]
    B --> C[Prompt Builder]
    C --> D[Google Gemini API]
    D --> E[Draft Itinerary]
    E --> F[Google Maps<br/>Places API]
    F --> G[Ground Places &<br/>Optimize Routes]
    G --> H[✅ Day-by-Day Itinerary]
    H --> B
```

<br/>

###  More ML Projects

| Project | What it does | Stack |
|---|---|---|
| [**House Price Prediction**](https://github.com/arpan0009e/House_Price_Prediciton) | Regression model with preprocessing and visualization | `Scikit-learn` `Pandas` |
| [**Food Delivery Time Prediction**](https://github.com/arpan0009e/Food_Delivery_Time_Prediction) | Feature engineering on a real-world dataset to predict ETA | `NumPy` `Scikit-learn` |

<div align="center">

[![All repos](https://img.shields.io/badge/Browse%20all%20repositories-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/arpan0009e?tab=repositories)

</div>

---

##  Experience

<table>
<tr>
<td width="180"><b>Sept 2025 – Oct 2025</b><br/><sub>Remote</sub></td>
<td>

**AI & Cloud Technology Intern** — *Edunet Foundation*

- Built end-to-end **ML pipelines in Python**: preprocessing, training, evaluation, and deployment
- Collaborated with a cross-functional team on scalable AI solutions, improving **model inference time by 20%**

</td>
</tr>
</table>

---

##  Education 

**B.Tech — Artificial Intelligence & Machine Learning**, NIMS University, Jaipur · *Jul 2023 – May 2027*
<br/>
<sub>Coursework: Data Structures · AI · Machine Learning · Deep Learning · NLP · Cloud Computing</sub>

**All India Senior School Certificate Examination**, Jawahar Navodaya Vidyalaya, West Medinipur · *Jul 2022*
<br/>
<sub>Coursework: Computer Science · Physics · Chemistry ·Mathematics</sub>



---

##  Currently

| | |
|---|---|
|  **Working on** | Deployable, end-to-end LLM / RAG applications |
|  **Learning** | Transformers & NLP internals, MLOps with Docker, DVC and AWS |
|  **Open to** | AI/ML internships (including PPO), entry-level roles, and open-source collaboration |
|  **Ask me about** | RAG pipelines, QLoRA fine-tuning, FastAPI, ML pipelines |

---

##  GitHub Stats

<div align="center">

<img width="49%" src="https://github-readme-stats.vercel.app/api?username=arpan0009e&show_icons=true&theme=tokyonight&hide_border=true&cache_seconds=86400" />
<img width="49%" src="https://github-readme-streak-stats.herokuapp.com/?user=arpan0009e&theme=tokyonight&hide_border=true" />

<br/>

<img width="40%" src="https://github-readme-stats.vercel.app/api/top-langs/?username=arpan0009e&layout=compact&theme=tokyonight&hide_border=true&cache_seconds=86400" />

<br/><br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=arpan0009e&theme=tokyo-night&hide_border=true&area=true" width="95%" />

</div>

---

##  Let's Connect

<div align="center">

I'm actively looking for **AI/ML internship and entry-level opportunities**. If you're building something with LLMs, RAG, or applied ML, I'd love to chat.

[![LinkedIn](https://img.shields.io/badge/Connect%20on%20LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/arpan0009e)
[![Email](https://img.shields.io/badge/Send%20an%20Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:arpanmondal708@gmail.com)
[![Resume](https://img.shields.io/badge/View%20My%20Resume-00897B?style=for-the-badge&logo=readthedocs&logoColor=white)](https://drive.google.com/file/d/1o5NIxA7jt3gwbkxdDijbH9VYNXVRJwmw/view?usp=sharing)

<br/>

*"The best way to predict the future is to build it."*

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=110&section=footer" />

</div>
