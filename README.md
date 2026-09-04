<<<<<<< HEAD
# Agentic-AI-Developer-Roadmap
=======
# Agentic-AI-Developer-Roadmap

# AI & ML Fundamentals — Video Notes
*Source: "AI Complete Crash Course for Beginners" (Apna College)*

---

## 1. What is AI?

AI = building systems that can perform tasks requiring human-like intelligence.

**Examples of human intelligence tasks AI replicates:**
- **Speech recognition** — Siri, Alexa, voice mode in ChatGPT/Gemini
- **Image analysis** — object detection, e.g. number-plate recognition systems used by traffic departments to auto-generate challans

---

## 2. The AI Hierarchy

```
Artificial Intelligence (AI)
   └── Machine Learning (ML)
          └── Deep Learning (DL)
                 └── Generative AI (Gen AI)
```

- **All ML is AI, but not all AI is ML.**
- Non-ML parts of AI: rule-based systems, classical robotics, A* search algorithm, fuzzy logic systems (e.g., in fridges/ACs) — these use hardcoded logic, not data-driven learning.
- Most AI we interact with today (LLMs, Google Maps, Uber, Amazon, Blinkit) **is** ML.

---

## 3. Machine Learning (ML)

**Definition:** Algorithms that learn patterns from data rather than being explicitly programmed.

**Why ML grew explosively (last 1–2 decades):** Internet → massive data generation → companies have huge datasets → ML became practical at scale.

### Two Core Steps of Any ML Model
| Step | Meaning |
|---|---|
| **Training** | Model learns patterns/logic from historical (past) data |
| **Inference** | Trained model makes predictions on new/unseen data |

**Example — Bank Loan Approval:**
1. Look at past applicants' data (credit score, salary, education, collateral)
2. Find patterns → common characteristics of approved vs. rejected loans (Training)
3. Apply this learned logic to new applicants (Inference)

**Other real examples:** cancer detection from X-rays, Gmail spam detection, credit card fraud detection, Swiggy/Zomato delivery-time estimation.

### ML vs. Traditional CS Algorithms
| Traditional Programming | Machine Learning |
|---|---|
| Input → Logic (hardcoded) → Output | Input **+ Output** (historical data) → **Model produces the logic (function)** |
| Programmer writes the rules | Algorithm derives the rules from data |

The "model" = the function/logic derived after training. New input → same function → predicted output.

---

## 4. Three Types of Machine Learning

### A) Supervised Learning
Learns from **labeled data** (input X + known output Y).
- Formula: **Y = f(X)** — model learns the function f
- "Features" = input columns/attributes

**Two sub-types:**

**1. Classification** — output falls into fixed/finite categories
- *Binary classification* (2 classes): spam/not spam, loan approved/rejected, cat/dog
- *Multi-class classification* (>2 classes): sentiment analysis (positive/negative/neutral), handwritten digit recognition (0–9, 10 classes)
- Algorithms: Logistic Regression, KNN (K-Nearest Neighbors), SVM (Support Vector Machine), Relevance Vector Machine, Random Forest, XGBoost

**2. Regression** — output is a **numerical value** (not a category)
- Examples: delivery time prediction, stock price forecasting, property price forecasting
- Input variable = **independent variable**; Output = **dependent variable**
- Simplest relationship: a straight line → **Y = aX + b**
  - a = slope, b = intercept
- Algorithms: Linear Regression, Lasso Regression, Multivariate Regression

### B) Unsupervised Learning
Learns from **unlabeled (raw) data** — no predefined categories; the model finds patterns itself.

**Two sub-types:**

**1. Clustering** — grouping similar data points together
- *Partitional clustering* — each data point belongs to only **one** cluster (e.g., a news article is either Sports OR Finance)
- *Hierarchical clustering* — a data point can belong to **multiple** clusters (e.g., an article on "Bitcoin taxation in India" fits Politics + Finance + Tech)
- Algorithms: K-Means, Hierarchical Clustering, PCA (Principal Component Analysis), DBSCAN

**2. Association** — finding relationships between entities
- Example: **Market Basket Analysis** (Amazon's "frequently bought together") — e.g., bread + milk purchased together

**Outlier/Anomaly Detection** is also a byproduct of unsupervised learning — useful in finance, medical, and cybersecurity (e.g., detecting a user logging in from 5 cities within 1 minute).

### C) Reinforcement Learning (RL)
Analogy: training a dog — reward good behavior, no reward for bad.

- **Agent** = the model that makes decisions by interacting with an **environment**
- Agent takes **actions** → gets **rewards** (positive) or **penalties** (negative)
- Goal of the agent: **maximize cumulative reward**, not just get one prediction right
- Example: Snakes & Ladders — penalty for hitting a snake, reward for climbing a ladder; goal = win the game
- Real applications: **self-driving cars, robotics** (movement, object picking), game-playing AI (Chess, Go)
- Algorithms: Q-Learning, Deep Q-Networks (DQN), Policy Gradient Methods, PPO (Proximal Policy Optimization)

---

## 5. Tools for Classical ML
- **Language:** Python (most popular), R
- **Environment:** Jupyter Notebook
- **Libraries:**
  - NumPy, Pandas → data preprocessing
  - Seaborn, Matplotlib → data visualization
  - Scikit-learn, XGBoost → model training

---

## 6. Deep Learning (DL)

**Subset of ML focused on Neural Networks.**

| Structured Data | Unstructured Data |
|---|---|
| Tabular data (rows/columns) | Images, video, audio, raw chat text |
| **Statistical ML** performs well | **Deep Learning** performs much better |

Why? For unstructured data (e.g., recognizing a face), it's very hard to manually define features ("what exactly is an eye?"). Deep learning models **automatically extract relevant features** from raw data.

### Neural Networks — Structure
Inspired by the human brain's neurons.
- **Input Layer** → **Hidden Layer(s)** → **Output Layer**
- Each connection between neurons has a **weight**
- Each neuron (except input layer) has a **bias** value

### How a Neuron Computes
For a neuron receiving inputs x1, x2, x3 with weights w1, w2, w3 and bias b:

```
Weighted Sum = (x1×w1 + x2×w2 + x3×w3) + b
Output = ActivationFunction(Weighted Sum)
```

**Common activation functions:**
- Sigmoid: `1 / (1 + e^-z)`
- ReLU (Rectified Linear Unit)

### Training a Neural Network — Two Steps
1. **Forward Propagation** — input flows forward through the network → produces a prediction/output
2. **Backward Propagation** — compare prediction with the expected value → calculate error using a **Loss Function** → adjust weights & biases backward through the network (learning from mistakes)

This forward+backward cycle repeats for every data entry, gradually minimizing the loss → more accurate predictions. (Analogy used: a college adjusting exam-weightage formulas based on results — same iterative adjustment idea.)

### Tools for Deep Learning
- **PyTorch** (by Meta) — more beginner-friendly/academic; **recommended starting point**
- **TensorFlow** (by Google) — more industry-oriented
- **Kaggle** — platform for datasets (used for both classical ML and DL)
- DL requires heavy compute → GPUs (local or cloud) needed due to large data/parameter volumes

---

## 7. Neural Network Architectures

| Architecture | Best For | Key Trait |
|---|---|---|
| **FNN** (Feed Forward Neural Network) | Simple predictions (medical diagnosis, loan approval) | Info flows one direction only, no loops; not good for sequential/time-based data |
| **RNN** (Recurrent Neural Network) | Sequential data — language translation, speech recognition, stock prediction | Has "memory" — loops back to reuse info from previous steps; context matters. **Weak at long-term memory** |
| **LSTM** (Long Short-Term Memory) | Same as RNN but better | Advanced RNN variant — handles long-term memory better |
| **CNN** (Convolutional Neural Network) | Images & video | Processes small patches of an image (via **kernels**) to detect edges/corners/shapes, drastically reducing computation vs. feeding every pixel individually. Layers: Convolution, Pooling, Fully Connected |
| **Transformer** | Sequential data, esp. text — powers GPT | Analyzes the *entire* sequence at once (not step-by-step) using an **Attention mechanism** — decides which parts of input are most relevant. Text is broken into **tokens**, and **attention scores** are computed between tokens to capture context/meaning |

**CNN pixel-computation example given:** A 1000×1000 black-and-white image = 10⁶ inputs per neuron computation; a colored image (RGB) = 3×10⁶ — this explosion in computation is why CNNs (patch-based processing) are essential instead of plain neural nets.

---

## 8. Generative AI (Gen AI)

Subset/application of Deep Learning focused on **generating new content** (text, audio, video, images) — as opposed to just classifying/predicting from existing data.

### Popular Gen AI Tools by Category
| Category | Tools |
|---|---|
| Text | GPT (OpenAI, funded by Microsoft), Claude (Anthropic, funded by Amazon), Gemini (Google), LLaMA (Meta) |
| Images | Midjourney, DALL-E, Stable Diffusion (open source; others closed source) |
| Audio | ElevenLabs, Bark, MusicGen |
| Video | Sora, Runway, Veo |
| Code | GitHub Copilot, Code Llama, Amazon CodeWhisperer (AWS-focused) |

### NLP (Natural Language Processing)
Field of ML focused on machines understanding, interpreting, and generating human language (English, Hindi, French, etc.)

### LLMs (Large Language Models)
- A type of model used to solve NLP tasks (not the only type, but the most popular today)
- GPT, Claude, LLaMA are all examples of LLMs
- Called "large" because:
  - Trained on **massive datasets** (internet text, books, articles)
  - Contain **billions to trillions of parameters** (weights + biases)
- **RLHF** (Reinforcement Learning with Human Feedback) — technique used (e.g., by OpenAI for ChatGPT) to refine raw LLM output using human review, ensuring responses are relevant, non-toxic, and appropriate.

### Computer Vision
Field of AI/ML enabling computers to "see" and interpret images/video — heavily relies on **CNNs**.
- Applications: face recognition, self-driving cars (detecting roads, pedestrians, objects)

---

## Quick Recap Map

```
AI
├── Non-ML AI: rule-based systems, A*, fuzzy logic
└── Machine Learning
     ├── Supervised Learning → Classification (binary/multi-class), Regression
     ├── Unsupervised Learning → Clustering (partitional/hierarchical), Association
     ├── Reinforcement Learning → Agent, Environment, Reward/Penalty
     └── Deep Learning (Neural Networks)
          ├── FNN, RNN, LSTM, CNN, Transformer
          └── Generative AI
               ├── NLP → LLMs (GPT, Claude, Gemini, LLaMA)
               └── Computer Vision (CNNs)
```

>>>>>>> origin/main
