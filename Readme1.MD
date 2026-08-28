
# AI, Generative AI & Agentic AI — Master Concept List

A structured map of the concepts across the three layers. Layers build on each other: classical AI/ML → deep learning → generative AI → agentic AI, with math and engineering as cross-cutting foundations.

---

## PART 0 — Math & CS Foundations

**Linear algebra**
Scalars, vectors, matrices, tensors · dot product · matrix multiplication · transpose · inverse · identity matrix · rank · determinant · eigenvalues & eigenvectors · singular value decomposition (SVD) · vector norms (L1, L2) · cosine similarity · vector spaces · projections

**Calculus**
Derivatives · partial derivatives · chain rule · gradients · Jacobian · Hessian · convexity · local vs global minima · saddle points

**Probability & statistics**
Random variables · probability distributions (normal, Bernoulli, binomial, Poisson, uniform, categorical) · joint/marginal/conditional probability · Bayes' theorem · expectation & variance · covariance & correlation · maximum likelihood estimation (MLE) · MAP estimation · sampling · central limit theorem · hypothesis testing · p-values · confidence intervals · law of large numbers

**Information theory**
Entropy · cross-entropy · KL divergence · JS divergence · mutual information · perplexity

**Optimization**
Objective/loss functions · convex optimization · gradient descent · constrained optimization · Lagrange multipliers

**Computer science**
Data structures & algorithms · time/space complexity (Big-O) · recursion · graphs & trees · hashing · matrix/array operations · parallelism & concurrency · distributed systems basics

---

## PART 1 — Core Artificial Intelligence

**Definitions & scope**
Artificial intelligence · narrow AI (ANI) · artificial general intelligence (AGI) · artificial superintelligence (ASI) · Turing test · Chinese room argument · AI winters · symbolic AI (GOFAI) vs connectionism

**Classical AI**
Search algorithms (BFS, DFS, uniform cost, A*, greedy best-first) · heuristics · adversarial search · minimax · alpha-beta pruning · Monte Carlo tree search (MCTS) · constraint satisfaction problems · logic & inference (propositional, first-order) · expert systems · rule engines · knowledge representation · ontologies · knowledge graphs · planning (STRIPS, PDDL) · fuzzy logic · genetic algorithms · swarm intelligence

**Machine learning paradigms**
Supervised learning · unsupervised learning · semi-supervised learning · self-supervised learning · reinforcement learning · online vs batch learning · transfer learning · multi-task learning · meta-learning · few-shot / zero-shot learning · active learning · federated learning · continual/lifelong learning

---

## PART 2 — Machine Learning

**Core vocabulary**
Features · labels/targets · training set · validation set · test set · hold-out · k-fold cross-validation · stratified sampling · hypothesis function · parameters vs hyperparameters · inductive bias · generalization

**Supervised algorithms**
Linear regression · polynomial regression · logistic regression · ridge (L2) & lasso (L1) & elastic net · k-nearest neighbours (kNN) · naive Bayes · support vector machines (SVM) · kernel trick · decision trees · entropy & Gini impurity · information gain · random forests · bagging · boosting · AdaBoost · gradient boosting · XGBoost · LightGBM · CatBoost · stacking & blending · ensembles

**Unsupervised algorithms**
k-means · k-means++ · elbow method · silhouette score · hierarchical clustering · dendrograms · DBSCAN · Gaussian mixture models · expectation-maximization · principal component analysis (PCA) · t-SNE · UMAP · independent component analysis · autoencoders · anomaly/outlier detection · isolation forest · association rule mining (Apriori, FP-growth) · collaborative filtering · matrix factorization

**Reinforcement learning**
Agent · environment · state · action · reward · policy · value function · Q-function · discount factor · Markov decision process (MDP) · partially observable MDP · Bellman equation · exploration vs exploitation · epsilon-greedy · Q-learning · SARSA · deep Q-networks (DQN) · policy gradient · REINFORCE · actor-critic · A2C/A3C · PPO · TRPO · DDPG · SAC · model-based vs model-free RL · reward shaping · reward hacking · credit assignment problem

**Data preparation**
Data cleaning · missing value imputation · outlier handling · feature engineering · feature selection · feature scaling (normalization, standardization, min-max) · encoding (one-hot, label, ordinal, target, embeddings) · binning/discretization · log transforms · dimensionality reduction · class imbalance · oversampling/undersampling · SMOTE · data augmentation · data leakage · train-serve skew

**Model behaviour & tuning**
Bias-variance tradeoff · underfitting · overfitting · regularization · dropout · early stopping · learning curves · grid search · random search · Bayesian optimization · Optuna/Hyperopt · pruning · ablation studies

**Evaluation metrics**
Confusion matrix · accuracy · precision · recall/sensitivity · specificity · F1 score · Fβ score · ROC curve · AUC-ROC · precision-recall curve · AUC-PR · log loss · Matthews correlation coefficient · Cohen's kappa · MSE · RMSE · MAE · MAPE · R² · adjusted R² · silhouette score · Davies-Bouldin index · NDCG · MRR · hit rate

---

## PART 3 — Deep Learning

**Neural network fundamentals**
Artificial neuron · perceptron · multilayer perceptron (MLP) · weights & biases · forward pass · backpropagation · computational graph · automatic differentiation · epochs · batches · mini-batch · iterations

**Activation functions**
Sigmoid · tanh · ReLU · Leaky ReLU · PReLU · ELU · GELU · SiLU/Swish · SwiGLU · softmax · softplus

**Loss functions**
Mean squared error · mean absolute error · Huber loss · binary cross-entropy · categorical cross-entropy · sparse cross-entropy · hinge loss · contrastive loss · triplet loss · focal loss · KL divergence loss · CTC loss

**Optimizers & training dynamics**
Batch/stochastic/mini-batch gradient descent · momentum · Nesterov momentum · AdaGrad · RMSprop · Adam · AdamW · learning rate · learning rate schedules · warmup · cosine decay · gradient clipping · vanishing gradients · exploding gradients · weight initialization (Xavier/Glorot, He) · normalization (batch norm, layer norm, RMSNorm, group norm) · residual/skip connections · gradient accumulation · mixed precision (FP16, BF16, FP8) · gradient checkpointing

**Architectures**
Feedforward networks · convolutional neural networks (CNN) · convolution · kernels/filters · stride · padding · pooling (max, average) · receptive field · LeNet/AlexNet/VGG/ResNet/Inception/EfficientNet/MobileNet · recurrent neural networks (RNN) · backpropagation through time · LSTM · GRU · bidirectional RNNs · sequence-to-sequence · encoder-decoder · attention mechanism · graph neural networks (GNN, GCN, GAT) · siamese networks · capsule networks · Vision Transformer (ViT) · U-Net

**Transformers**
Self-attention · scaled dot-product attention · query, key, value (QKV) · multi-head attention · cross-attention · causal/masked attention · positional encoding (sinusoidal, learned, RoPE, ALiBi) · feedforward/MLP block · residual stream · encoder-only (BERT) vs decoder-only (GPT) vs encoder-decoder (T5) · KV cache · grouped-query attention (GQA) · multi-query attention (MQA) · FlashAttention · sliding window attention · sparse attention · mixture of experts (MoE) · routing & expert load balancing · state space models (Mamba, S4) as alternatives

**Distributed training**
Data parallelism · model parallelism · tensor parallelism · pipeline parallelism · sequence parallelism · ZeRO / FSDP · DeepSpeed · Megatron · all-reduce · parameter servers

---

## PART 4 — Natural Language Processing

Text preprocessing · tokenization · word/subword/character tokens · byte-pair encoding (BPE) · WordPiece · SentencePiece · Unigram · vocabulary · stop words · stemming · lemmatization · n-grams · bag of words · TF-IDF · word embeddings · word2vec (CBOW, skip-gram) · GloVe · fastText · contextual embeddings · sentence embeddings · language modeling · causal LM vs masked LM · next-token prediction · named entity recognition (NER) · part-of-speech tagging · dependency parsing · coreference resolution · sentiment analysis · text classification · topic modeling (LDA) · summarization (extractive, abstractive) · machine translation · question answering · semantic similarity · BLEU · ROUGE · METEOR · BERTScore · perplexity

---

## PART 5 — Generative AI

**Foundations**
Generative vs discriminative models · latent space · latent variables · sampling · likelihood-based vs implicit models · mode collapse · manifold hypothesis

**Generative model families**
- **Autoencoders / VAEs** — encoder, decoder, bottleneck, reconstruction loss, variational autoencoder, ELBO, reparameterization trick, KL regularization, disentanglement
- **GANs** — generator, discriminator, adversarial loss, minimax game, DCGAN, StyleGAN, CycleGAN, conditional GAN, Wasserstein GAN, mode collapse, training instability
- **Diffusion models** — forward (noising) process, reverse (denoising) process, DDPM, DDIM, noise schedule, score-based models, U-Net backbone, latent diffusion, classifier-free guidance (CFG), guidance scale, samplers/schedulers, inpainting, ControlNet, LoRA for images, img2img, flow matching, rectified flow, consistency models
- **Autoregressive models** — next-token generation, teacher forcing, exposure bias
- **Normalizing flows** · **energy-based models** · **NeRF** · **3D Gaussian splatting**

**Large language models**
Foundation model · pretraining corpus · scaling laws (Chinchilla) · compute-optimal training · emergent abilities · parameter count · context window / context length · long-context techniques · base model vs instruct/chat model · reasoning models · test-time compute · chain-of-thought as computation · model families (GPT, Claude, Gemini, Llama, Mistral, Qwen, DeepSeek) · open-weight vs closed models · model cards

**Adapting models**
Continued pretraining · domain adaptation · supervised fine-tuning (SFT) · instruction tuning · parameter-efficient fine-tuning (PEFT) · LoRA · QLoRA · DoRA · adapters · prefix tuning · prompt tuning / soft prompts · p-tuning · full fine-tuning vs PEFT tradeoffs · catastrophic forgetting · knowledge distillation · teacher-student models · model merging · quantization (INT8, INT4, GPTQ, AWQ, GGUF, bitsandbytes) · pruning · sparsity

**Alignment & preference learning**
Human preference data · reward model · RLHF · PPO for RLHF · direct preference optimization (DPO) · IPO · KTO · ORPO · GRPO · RLAIF · Constitutional AI · rejection sampling / best-of-n · alignment tax · helpfulness-harmlessness tradeoff · red teaming · refusal behaviour · sycophancy · specification gaming

**Inference & decoding**
Greedy decoding · beam search · sampling · temperature · top-k sampling · top-p (nucleus) sampling · min-p · typical sampling · repetition penalty · frequency & presence penalty · stop sequences · logit bias · constrained/structured decoding · JSON mode · grammar-constrained generation · speculative decoding · draft models · streaming · time to first token (TTFT) · tokens per second · continuous batching · paged attention · prompt caching

**Prompt engineering**
System prompt · user/assistant roles · zero-shot prompting · few-shot prompting · in-context learning · chain-of-thought (CoT) · zero-shot CoT · self-consistency · least-to-most prompting · tree of thoughts · graph of thoughts · ReAct prompting · role/persona prompting · delimiters & structure · output format specification · prompt templates · prompt chaining · decomposition · self-critique / self-refine · reflection · meta-prompting · automatic prompt optimization (DSPy, APE) · negative prompting (images) · prompt versioning

**Retrieval-Augmented Generation (RAG)**
Knowledge cutoff problem · grounding · document ingestion · parsing & extraction · chunking strategies (fixed, recursive, semantic, document-aware) · chunk overlap · embedding models · vector store / vector database (FAISS, Pinecone, Weaviate, Qdrant, Chroma, pgvector, Milvus) · indexing · approximate nearest neighbour (HNSW, IVF, ScaNN, LSH) · similarity metrics (cosine, dot product, Euclidean) · dense retrieval vs sparse retrieval (BM25, TF-IDF) · hybrid search · reciprocal rank fusion · metadata filtering · query rewriting · query expansion · multi-query retrieval · HyDE · step-back prompting · reranking · cross-encoders · ColBERT / late interaction · contextual retrieval · parent-document retrieval · small-to-big · sentence-window retrieval · GraphRAG · knowledge graph RAG · multimodal RAG · agentic RAG · self-RAG · corrective RAG · context stuffing vs retrieval · lost in the middle · RAG evaluation (faithfulness, answer relevance, context precision/recall, RAGAS)

**Multimodal & other generative domains**
Multimodal models · vision-language models (VLM) · CLIP · contrastive pretraining · image captioning · visual question answering · OCR · text-to-image · text-to-video · image-to-video · text-to-3D · text-to-speech (TTS) · voice cloning · automatic speech recognition (ASR, Whisper) · speech-to-speech · audio & music generation · code generation · text-to-SQL · embeddings for images/audio

**Failure modes & risks**
Hallucination (intrinsic, extrinsic) · confabulation · knowledge cutoff · outdated information · bias & fairness · toxicity · jailbreaking · prompt injection (direct, indirect) · data exfiltration · training data extraction / memorization · copyright & attribution · deepfakes · watermarking · model collapse from synthetic data · overconfidence & calibration · nondeterminism

---

## PART 6 — Agentic AI

**Core idea**
Agent · agency · autonomy spectrum · goal-directed behaviour · workflow vs agent · agent loop (perceive → reason → act → observe) · environment · affordances · harness / scaffolding · determinism vs autonomy tradeoff

**Agent components**
LLM as reasoning engine · instructions/system prompt · tools · memory · planner · executor · critic/evaluator · state · context management

**Tool use**
Function calling · tool schemas (JSON Schema) · tool descriptions · tool selection · parallel tool calls · tool result handling · error handling & retries · code execution / code interpreter · sandboxing · shell/bash access · file system access · web search · web browsing / browser automation · computer use (screenshot + mouse/keyboard) · API integrations · database queries · Model Context Protocol (MCP) · MCP servers, tools, resources, prompts · tool overloading · permissioning & approval gates

**Memory**
Context window as working memory · short-term vs long-term memory · episodic memory · semantic memory · procedural memory · scratchpad · conversation history · summarization & compaction · vector memory · entity memory · memory retrieval · memory writing policies · forgetting/decay · state persistence · checkpointing

**Reasoning & planning patterns**
ReAct (reason + act) · Plan-and-Execute · ReWOO · Reflexion · self-refine · self-critique · task decomposition · subgoal generation · hierarchical planning · dynamic replanning · Tree of Thoughts search · MCTS with LLMs · LLM Compiler · chain of tools · verification & self-checking · scratchpad reasoning · budget/step limits

**Workflow patterns**
Prompt chaining · routing / classification · parallelization (sectioning, voting) · orchestrator-worker · evaluator-optimizer loop · map-reduce over documents · human-in-the-loop · escalation · guardrail wrappers · retry with feedback

**Multi-agent systems**
Multi-agent orchestration · supervisor/manager agent · hierarchical agent teams · peer-to-peer agents · role-based agents · agent handoffs · delegation · shared blackboard / shared state · message passing · agent communication protocols · Agent-to-Agent (A2A) · debate & self-play · consensus & voting · swarm patterns · specialization vs generalization · context isolation between subagents · coordination overhead · cost multiplication

**Frameworks & tooling**
LangChain · LangGraph · LlamaIndex · CrewAI · AutoGen · Semantic Kernel · OpenAI Agents SDK · Claude Agent SDK · Pydantic AI · smolagents · Haystack · DSPy · n8n / Zapier-style orchestration · agent state machines & graphs · nodes, edges, conditional edges · interrupts & resumption

**Agent evaluation**
Task success rate · trajectory evaluation · step-level vs outcome-level eval · tool-call accuracy · efficiency (steps, tokens, cost, latency) · robustness · benchmarks (SWE-bench, WebArena, GAIA, τ-bench, AgentBench, OSWorld) · LLM-as-judge for trajectories · regression suites · sandboxed replay

**Agent-specific risks**
Runaway loops · infinite retry · cost explosion · error compounding across steps · indirect prompt injection through tool outputs · over-permissioned tools · destructive actions · irreversibility · confused deputy problem · goal drift · deceptive alignment · insufficient observability · lack of audit trail · human oversight design · kill switches

---

## PART 7 — AI Engineering, MLOps & LLMOps

**Lifecycle**
Problem framing · data collection · labeling & annotation · data versioning (DVC, LakeFS) · experiment tracking (MLflow, Weights & Biases) · model registry · reproducibility · feature stores · CI/CD for ML · model packaging · containerization (Docker) · orchestration (Kubernetes, Airflow, Dagster, Prefect)

**Serving & infrastructure**
Model serving (vLLM, TGI, TorchServe, Triton, Ollama, llama.cpp) · REST/gRPC APIs · batch vs real-time inference · autoscaling · GPUs, TPUs, VRAM, HBM · CUDA · quantized inference · edge & on-device inference · model gateways / routers · fallback models · rate limiting · load balancing · multi-tenancy

**Observability**
Logging · tracing & spans · LLM observability (LangSmith, Langfuse, Arize, Helicone) · token accounting · cost per request · latency percentiles (p50/p95/p99) · error rates · data drift · concept drift · model decay · alerting · dashboards · feedback capture (thumbs up/down) · user analytics

**Evaluation & quality**
Benchmarks (MMLU, GPQA, HumanEval, MBPP, MATH, HellaSwag, ARC, BBH, MT-Bench, LMSYS Arena) · golden/eval datasets · unit tests for prompts · assertion-based eval · LLM-as-judge · pairwise comparison · rubric grading · inter-annotator agreement · human evaluation · A/B testing · shadow deployment · canary release · regression testing · eval-driven development

**Cost & performance optimization**
Token optimization · prompt compression · context pruning · prompt caching · semantic caching · model cascading / routing (small model first) · distillation to smaller models · batching · quantization · early stopping of agent loops · caching embeddings

**Safety, security & governance**
Guardrails (input & output) · content moderation APIs · PII detection & redaction · toxicity filters · topical restrictions · jailbreak detection · prompt injection defenses · output validation & schema enforcement · sandboxing · least privilege · secrets management · audit logs · data residency · GDPR/DPDP compliance · EU AI Act · NIST AI Risk Management Framework · ISO 42001 · model cards & datasheets · responsible AI principles · explainability (SHAP, LIME, attention visualization) · mechanistic interpretability (features, circuits, sparse autoencoders, probing) · AI safety (alignment, corrigibility, scalable oversight, evals for dangerous capabilities)

**Product & application layer**
Use case selection · build vs buy · human-AI interaction design · latency budgets · streaming UX · citations & source attribution · confidence display · fallback & graceful degradation · feedback loops · data flywheel · synthetic data generation · continuous improvement

---

## How to use this list

- **Breadth-first, then depth.** Skim every section once so you recognize the vocabulary, then go deep only where your roadmap phase requires it.
- **Layered dependency.** Parts 0–3 are prerequisites for Part 5; Part 5 is a prerequisite for Part 6. Part 7 runs alongside everything from the point you start deploying anything.
- **For an AI engineering track specifically**, the highest-leverage clusters are: Transformers (Part 3), LLM adaptation + prompting + RAG + inference (Part 5), the full of Part 6, and evaluation + observability + guardrails (Part 7). Classical ML (Part 2) matters for interviews and for knowing when *not* to reach for an LLM.

# AI Fundamentals + Agentic AI — Deep Dive

A working reference covering the fundamentals list and the NVIDIA agentic AI course outline. Read Part A before Part B — the course modules assume most of Part A.

---

# PART A — FOUNDATIONS

## 1. The four "types" of AI

These four terms get listed as if they're siblings. They aren't. Two describe *what the model does*, one describes *how it's wrapped*, and one describes *what it's for*. Getting this hierarchy right is the single most useful clarification in this whole document.

### 1.1 Decision AI (also: predictive AI, analytical AI)

The oldest and still the largest category by deployed volume. A model takes structured input and produces a **decision or a number**, not content.

- **Classification** — is this transaction fraud? will this user click?
- **Regression** — what will this campaign's CPA be next week?
- **Ranking / recommendation** — which offer goes in slot 1?
- **Optimization** — given a budget and pacing constraints, how do I allocate spend?

Characteristics: narrow scope, structured input/output, deterministic given the same input, evaluated with hard metrics (precision, recall, AUC, RMSE), cheap to run, easy to audit.

You already work with decision AI daily. Bid optimization, pacing algorithms, audience propensity scoring, fraud filters on offer redemption — all decision AI. It doesn't generate anything; it picks.

### 1.2 Generative AI

A model that produces **new content** sampled from a learned probability distribution — text, code, images, audio, video.

The mechanism for LLMs: given a sequence of tokens, predict a probability distribution over the next token, sample from it, append, repeat. That's it. Everything else — reasoning, style, tool use — is emergent behavior on top of that loop.

Key properties that matter downstream:

- **Stateless.** Each API call knows only what you send it. There is no server-side memory of the last call unless you build one. This is the single most important fact for agent design.
- **Probabilistic.** Same input can give different output. `temperature` controls how much.
- **Bounded by a context window.** A fixed token budget for system prompt + history + input + output.
- **No ground truth check.** It produces plausible continuations, not verified facts. Hence retrieval and tool use.

### 1.3 Conversational AI

An **interface pattern**, not a model class. It's the design of a multi-turn natural-language exchange.

- **Pre-LLM (2015–2022):** a pipeline. ASR/text in → intent classifier → entity/slot extraction → dialogue state manager → response template. Dialogflow, Rasa, Lex, IVR trees. Rigid, but predictable and cheap. Every intent had to be enumerated in advance.
- **Post-LLM:** the LLM absorbs intent recognition, slot filling, and response generation into one component. You get open-domain flexibility and lose the guarantee that the bot can only say approved things — which is why guardrails became an engineering discipline.

Important: conversational is orthogonal to agentic. You can have a conversational non-agent (a chatbot that only answers from a document) and an agentic non-conversational system (a batch pipeline that plans and executes with no human in the loop).

### 1.4 Agentic AI

A system where a model is given a **goal**, and it decides the sequence of actions to reach it — calling tools, observing results, and adjusting — rather than producing one output and stopping.

The minimum viable definition needs all four:

1. A **goal** stated at a higher level than the actions required.
2. **Tools** — the ability to affect or read the world outside its own text output.
3. A **loop** — act, observe the result, decide the next action.
4. **Termination logic** — a way to know it's done, or to stop trying.

Remove the loop and you have a chatbot with function calling. Remove tools and you have a chain-of-thought prompt.

### 1.5 How they stack

```
                    ┌─────────────────────────────┐
                    │        AGENTIC AI           │  goal → plan → act → observe → loop
                    │  (architecture / system)    │
                    └──────────────┬──────────────┘
                                   │ built on
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
┌───────▼────────┐        ┌────────▼────────┐        ┌────────▼────────┐
│ GENERATIVE AI  │        │  DECISION AI    │        │     TOOLS       │
│  reasoning,    │        │  classifiers,   │        │  APIs, DBs,     │
│  planning,     │        │  rankers,       │        │  browsers,      │
│  synthesis     │        │  routers        │        │  code exec      │
└────────────────┘        └─────────────────┘        └─────────────────┘

CONVERSATIONAL AI = an interface layer that can sit on top of any of the above.
```

A real production system uses all of them. A support agent might use decision AI to classify urgency, generative AI to plan and draft, agentic architecture to actually resolve the ticket, and a conversational interface to talk to the customer.

---

## 2. APIs

Everything an agent can do, it does through an API. Two things to understand: APIs in general, and LLM APIs specifically.

### 2.1 General API mechanics

**REST** is the dominant style. A request has:

- **Method** — `GET` (read, safe, idempotent), `POST` (create/act, not idempotent), `PUT` (replace, idempotent), `PATCH` (partial update), `DELETE`.
- **URL + path/query params** — `/campaigns/1558/offers?status=live&limit=50`
- **Headers** — auth, content type, request ID, idempotency key.
- **Body** — usually JSON, for POST/PUT/PATCH.

A response has a **status code** and a body:

| Range | Meaning | Common ones |
|---|---|---|
| 2xx | Success | 200 OK, 201 Created, 204 No Content |
| 3xx | Redirect | 301, 302, 304 Not Modified |
| 4xx | *You* did something wrong | 400 Bad Request, 401 Unauthorized (not authenticated), 403 Forbidden (authenticated, not permitted), 404, 409 Conflict, 422 Unprocessable, 429 Rate Limited |
| 5xx | *Server* broke | 500, 502, 503, 504 Timeout |

The 4xx/5xx distinction drives retry logic: retry 429 and 5xx with exponential backoff; never blindly retry a 4xx, because the same request will fail the same way.

**Auth patterns**, roughly in order of how you'll meet them:

- **API key** — a static secret in a header. Simple, no user context, all-or-nothing scope.
- **Bearer token / JWT** — a signed, expiring token carrying claims (who, what scopes, until when). Verified without a DB lookup.
- **OAuth 2.0** — a delegation protocol. Lets your app act *on behalf of a user* without seeing their password. The flow: redirect user to provider → user consents → you get an authorization code → exchange code + client secret for an access token (short-lived) and refresh token (long-lived). This is what you hit when wiring Microsoft Graph.
- **mTLS / service accounts** — machine-to-machine, common inside enterprises.

**Things that bite you in production:**

- **Rate limits.** Usually requests/min and tokens/min separately. Respect `Retry-After`. Design for backoff + jitter, not tight loops.
- **Pagination.** Offset-based (`?page=3`) is simple but breaks when data shifts under you. Cursor-based (`?after=abc123`) is stable. Always paginate; never assume one page is everything.
- **Idempotency.** For anything that creates or charges, send an idempotency key so a retry after a timeout doesn't double-create.
- **Webhooks vs polling.** Polling asks repeatedly; webhooks push to you. Webhooks are cheaper and lower-latency but need a public endpoint, signature verification, and duplicate handling (they can fire twice).
- **Versioning.** `/v1/` in the path or a version header. Never depend on an unversioned endpoint.

### 2.2 LLM APIs specifically

The shape is nearly identical across providers:

```json
POST /v1/messages
{
  "model": "...",
  "max_tokens": 1024,
  "system": "You are a campaign QA assistant.",
  "messages": [
    {"role": "user", "content": "Check offer 1558 for presentment errors."},
    {"role": "assistant", "content": "..."},
    {"role": "user", "content": "Now compare to 1559."}
  ],
  "tools": [ ... ],
  "temperature": 0.2
}
```

What to internalize:

- **You resend the entire history every call.** The `messages` array *is* the conversation. Nothing is remembered server-side. Short-term memory is literally this array, and managing it is a core engineering task.
- **Tokens are the unit of everything** — cost, latency, and the context limit. Roughly 3–4 characters per token in English. Input and output are usually priced differently.
- **`temperature`** — 0 is near-deterministic (still not guaranteed), higher is more varied. Use low values for extraction, classification, and tool selection; higher for drafting.
- **Streaming** — server-sent events, token by token. Only affects perceived latency, not total cost.
- **Tool / function calling** — you declare tools as JSON Schema. The model doesn't execute anything; it *returns a structured request* to call a tool. **Your code executes it** and sends the result back as a new message. That round trip is the agent loop, and the fact that you control execution is where all your safety leverage lives.
- **Structured output** — forcing valid JSON against a schema, so downstream code can parse reliably.

---

## 3. Learning algorithms

### 3.1 Supervised learning

**Labeled data.** You have inputs `X` and known correct outputs `y`, and you learn the mapping.

- **Classification** — discrete output. Spam/not-spam, offer category, churn risk bucket. Metrics: accuracy (misleading on imbalanced data), precision (of what I flagged, how much was right), recall (of what was actually positive, how much did I catch), F1 (harmonic mean), AUC-ROC.
- **Regression** — continuous output. Predicted CPA, LTV, days to conversion. Metrics: MAE, RMSE, R².

Core workflow: split data into **train / validation / test**. Fit on train, tune hyperparameters against validation, report once on test. The test set is touched last and rarely — every time you look at it and adjust, you leak information into your model and your estimate becomes optimistic.

**The central tension: bias vs variance.**
- High bias = underfitting. Model too simple, wrong on both train and test.
- High variance = overfitting. Model memorized the training set, great on train, bad on test.
- Fixes for overfitting: more data, fewer features, regularization (L1/L2), dropout, early stopping, cross-validation.

Algorithms worth knowing: linear/logistic regression, decision trees, random forests, gradient boosting (XGBoost / LightGBM — still the best default on tabular data), SVMs, neural networks.

### 3.2 Unsupervised learning

**No labels.** You're finding structure.

- **Clustering** — K-means (fast, assumes spherical clusters, you pick k), DBSCAN (density-based, finds arbitrary shapes, handles noise), hierarchical.
- **Dimensionality reduction** — PCA (linear, preserves variance), t-SNE and UMAP (nonlinear, for visualization only — distances between clusters aren't meaningful).
- **Anomaly detection** — isolation forests, autoencoders.
- **Association rules** — market basket analysis. Directly relevant to offer/merchant work.

**Embeddings** are the bridge to modern AI. An embedding model maps text (or images) into a dense vector where semantic similarity becomes geometric proximity. Cosine similarity between vectors ≈ similarity of meaning. This is the entire basis of vector search and RAG, and therefore of agent long-term memory.

### 3.3 Reinforcement learning

**No labeled answers — only a reward signal.** An **agent** in an **environment** observes a **state**, takes an **action**, receives a **reward**, and lands in a new state. It learns a **policy** (state → action) that maximizes cumulative discounted reward.

Key concepts:
- **Exploration vs exploitation** — try new things vs use what's known to work. Epsilon-greedy, UCB, Thompson sampling.
- **Credit assignment** — when reward arrives late, which earlier action deserves credit? This is the hard part.
- **Discount factor γ** — how much you value future reward vs immediate.
- **On-policy vs off-policy** — learning from your own current behavior vs from stored/other behavior.

Where it touches your world: multi-armed bandits for creative/offer selection are RL. And **RLHF** (reinforcement learning from human feedback) is how base LLMs get turned into helpful assistants — humans rank outputs, a reward model learns those preferences, and policy optimization tunes the LLM against it.

**Important caveat:** agentic AI borrows RL's vocabulary (agent, environment, state, action, reward) but almost no production agent is trained with RL. The loop is orchestrated in code by a prompted LLM. Don't conflate the two — many people do.

### 3.4 The fourth one nobody lists: self-supervised learning

LLM pretraining is neither supervised nor unsupervised in the classic sense. It's **self-supervised**: the labels are generated from the data itself (predict the next token, predict the masked token). You get the scale advantage of unlabeled data with the training signal of supervised learning. This is *the* reason LLMs exist. Worth knowing when someone asks "is GPT supervised or unsupervised" — the honest answer is "self-supervised pretraining, then supervised fine-tuning, then RLHF."

---

## 4. Databases and SQL

### 4.1 Logical execution sequence

SQL is written in one order and **executed in another**. Nearly every confusing SQL error traces back to this.

**Written order:**
```
SELECT → FROM → JOIN → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT
```

**Logical execution order:**
```
1. FROM          pick the base table
2. JOIN / ON     combine tables, build the working row set
3. WHERE         filter individual rows      (no aggregates available yet)
4. GROUP BY      collapse rows into groups
5. HAVING        filter groups               (aggregates available here)
6. SELECT        compute output columns, evaluate aggregates, assign aliases
7. DISTINCT      remove duplicate output rows
8. ORDER BY      sort                        (aliases from SELECT are available)
9. LIMIT/OFFSET  slice the result
```

**What this order explains:**

- *Why can't I use a SELECT alias in WHERE?* Because WHERE (3) runs before SELECT (6). The alias doesn't exist yet.
- *Why can I use it in ORDER BY?* Because ORDER BY (8) runs after SELECT (6).
- *Why do I need HAVING instead of WHERE for `COUNT(*) > 5`?* Because aggregates only exist after GROUP BY (4), and WHERE runs at (3).
- *Why does filtering in `WHERE` vs in the `ON` clause of a LEFT JOIN give different results?* `ON` filters during the join (step 2), so unmatched left rows survive as NULLs. `WHERE` filters after (step 3), and `WHERE right.col = 'x'` throws away those NULL rows, silently turning your LEFT JOIN into an INNER JOIN. This is the most common real bug in reporting queries.
- Put the most selective filters in `WHERE`, not `HAVING` — filtering rows before grouping is dramatically cheaper than grouping everything and then discarding.

Note: this is the *logical* order the standard guarantees. The query optimizer physically executes it however it likes, as long as the result is identical.

### 4.2 Keys

| Key | What it is |
|---|---|
| **Super key** | Any set of columns that uniquely identifies a row. Can include redundant columns. |
| **Candidate key** | A *minimal* super key — remove any column and uniqueness breaks. A table can have several. |
| **Primary key** | The candidate key you chose as the row's official identity. Exactly one per table. `NOT NULL` + `UNIQUE`. Usually clustered, which physically orders the table. |
| **Alternate key** | The candidate keys you didn't pick as primary. Enforce them with `UNIQUE`. |
| **Composite key** | A key made of two or more columns. Common in junction tables: `(campaign_id, merchant_id)`. |
| **Foreign key** | A column referencing another table's primary key. This is what enforces **referential integrity** — you can't insert an offer for a merchant that doesn't exist, and `ON DELETE CASCADE`/`RESTRICT`/`SET NULL` defines what happens when the parent goes. |
| **Surrogate key** | A meaningless system-generated ID (auto-increment, UUID). Stable forever. |
| **Natural key** | A key with real-world meaning (email, ISBN, merchant code). Readable, but real-world values change and then your foreign keys everywhere are wrong. **Default to surrogate primary keys with a unique constraint on the natural key.** |

**Keys vs indexes** — commonly confused. A *key* is a logical constraint about uniqueness and integrity. An *index* is a physical structure (usually a B-tree) that speeds up lookups. Primary and unique keys are usually *backed* by an index automatically, but you can index a non-key column, and an index doesn't enforce anything unless declared unique.

### 4.3 Normalization, briefly

- **1NF** — atomic values, no repeating groups. One value per cell.
- **2NF** — 1NF + no partial dependency on part of a composite key.
- **3NF** — 2NF + no transitive dependency (non-key columns depend only on the key).

Rule of thumb: **normalize for transactional systems** (writes must be consistent, no update anomalies), **denormalize for analytics** (reads must be fast, joins are expensive). Star schemas in a warehouse are deliberately denormalized. This is also why `dbt` exists — it's the layer that transforms normalized source data into denormalized analytical models.

### 4.4 Why an AI engineer cares

- **RAG and agent tools** query databases. Bad schema = bad retrieval.
- **Text-to-SQL** is one of the highest-value and highest-risk agent tools. The agent writes SQL; you must sandbox it (read-only role, row limits, statement timeouts, no DDL).
- **Vector databases** (pgvector, Pinecone, Qdrant, Weaviate, Chroma) are where long-term memory lives. They're still databases: they have keys, indexes (HNSW/IVF instead of B-tree), and filtering.
- **Feature stores and training data** are SQL problems before they're ML problems. Most of the work in an ML project is data preparation.

---

## 5. Memory: short-term vs long-term

This is the concept that most directly separates a chatbot from an agent, and it's worth being precise because the terms are used loosely.

### 5.1 Short-term memory (working memory / context)

**What it is:** everything currently inside the model's context window for this call — system prompt, tool definitions, conversation history, retrieved documents, tool results, scratchpad reasoning.

**Properties:**
- Fast — no retrieval step, it's already there.
- Perfectly recalled — within the window, the model can see all of it.
- **Volatile and finite.** When the conversation ends or the window fills, it's gone.
- Expensive — every token in context is paid for on *every* subsequent call.

**Management strategies, roughly in order of sophistication:**
1. **Full buffer** — send everything. Works until it doesn't.
2. **Sliding window** — keep the last N turns. Simple, loses early context (often the most important context: the original goal).
3. **Summarization / compaction** — when approaching the limit, have the model summarize older turns into a compact block and replace them. Lossy but goal-preserving. This is what long-running agents actually do.
4. **Structured state** — don't keep the transcript at all. Maintain an explicit state object (goal, completed steps, open questions, artifacts) and rebuild a minimal context from it each turn. This is the LangGraph model and it scales best.

**"Lost in the middle"** — even with a large window, models attend most reliably to the beginning and end of the context. Put the goal and the current instruction at the edges, not buried in turn 40.

### 5.2 Long-term memory (persistent memory)

**What it is:** anything stored *outside* the context and pulled in when relevant. Four useful types:

| Type | Contents | Typical store | Example |
|---|---|---|---|
| **Semantic** | Facts and knowledge | Vector DB / KV store | "Pranav works in IST", "merchant X uses presentment type B" |
| **Episodic** | Records of past events and runs | Log / event store | "Last Tuesday the 1558 rollout failed on the locking check" |
| **Procedural** | How to do things | Prompts, skills, playbooks | "The EOD summary pulls from these four sources in this order" |
| **Entity / profile** | Structured records about people and objects | Relational DB | A user preferences row, a merchant config record |

**How retrieval usually works:**
1. Chunk the source content sensibly (respect semantic boundaries, not fixed character counts).
2. Embed each chunk into a vector.
3. On a new query, embed the query and find nearest neighbours by cosine similarity.
4. Optionally **rerank** the top ~50 with a cross-encoder down to the top ~5. This single step usually improves quality more than any other RAG tweak.
5. Inject the winners into short-term memory.

**Hybrid search** — combining dense vector search with keyword/BM25 search — beats either alone in most real systems, because vectors are bad at exact identifiers (offer IDs, SKUs, error codes) and keywords are bad at paraphrase.

### 5.3 The write path is the hard part

Retrieval gets all the attention; **deciding what to store is harder.** Store everything and retrieval degrades into noise. Store too little and the agent is amnesiac. Real systems need:

- A **durability test** — is this still true and useful next month?
- **Conflict resolution** — new fact contradicts old fact; which wins, and do you keep the history?
- **Scoping** — is this about the user, the project, or just this session?
- **Privacy boundaries** — some things must never be persisted regardless of usefulness.
- **Decay or review** — stale memory is worse than no memory.

### 5.4 The clean mental model

```
SHORT-TERM = RAM.  Fast, finite, wiped on restart, costs you on every cycle.
LONG-TERM  = DISK. Slow-ish, effectively unbounded, survives restarts,
                   useless without a good index and a retrieval strategy.
```

---

## 6. Git and GitHub

**Git** is a distributed version control system that runs locally. **GitHub** is a hosting platform with collaboration features (pull requests, issues, Actions, reviews) layered on top. You can use Git with no GitHub at all.

### 6.1 The four areas

```
  working directory  ──git add──▶  staging area (index)
                                        │
                                     git commit
                                        ▼
                                   local repository  ──git push──▶  remote (GitHub)
                                        ▲
                                   git fetch / pull
```

Understanding these four areas explains most Git confusion. `git status` tells you where everything currently sits.

### 6.2 Commands that actually matter

| Command | What it does |
|---|---|
| `git init` / `git clone` | Start a repo / copy an existing one |
| `git status` | Where is everything right now — run it constantly |
| `git add -p` | Stage changes *hunk by hunk*. Underrated; forces you to review your own diff |
| `git commit -m` | Snapshot the staging area |
| `git log --oneline --graph --all` | See the actual branch structure |
| `git diff` / `git diff --staged` | Unstaged vs staged changes |
| `git branch` / `git switch -c` | List / create + move to a branch |
| `git merge` | Join branches, creating a merge commit |
| `git rebase` | Replay your commits on top of another branch — linear history, **rewrites hashes** |
| `git stash` | Park uncommitted work temporarily |
| `git restore` / `git revert` / `git reset` | Undo, at three different levels of violence |

**Merge vs rebase:** merge preserves the true history including the fork; rebase produces a clean linear history by rewriting commits. **Never rebase a branch that others have pulled** — you rewrite hashes, and their history no longer matches yours.

**Revert vs reset:** `revert` creates a *new* commit that undoes an old one — safe on shared branches. `reset` moves the branch pointer backwards — fine locally, destructive if already pushed.

### 6.3 The collaboration flow

```
main
 └── feature/offer-validation
       commit → commit → push → open PR → review → CI passes → merge → delete branch
```

Rules worth adopting even when working solo: never commit directly to `main`, one logical change per commit, write commit messages that say *why* not *what* (the diff already says what), keep PRs small enough to actually review.

### 6.4 Practical notes

- **SSH vs HTTPS.** SSH keys avoid repeated credential prompts. If corporate network blocks port 22, SSH over port 443 via `ssh.github.com` is the standard workaround (`~/.ssh/config`).
- **`.gitignore`.** Never commit secrets, `.env` files, virtualenvs, `node_modules`, large data files, or model weights. If a secret does get committed, rotate it — removing it from history isn't enough, it's already in every clone.
- **Notebooks.** `.ipynb` files diff terribly because outputs and metadata are embedded JSON. Strip outputs before committing (`nbstripout`) or convert logic to `.py` modules.
- **Data and models** don't belong in Git. Use DVC, Git LFS, or an artifact registry.

### 6.5 Why it matters more for AI than for regular software

AI systems are non-deterministic, which makes reproducibility a discipline rather than a default. To reproduce a result you need the code version, the prompt version, the model version, the data version, and the config. Git handles the first two and the fifth. Prompts should be version-controlled files, not strings pasted into a notebook.

---

# PART B — THE NVIDIA AGENTIC AI MODULES

Below, each module heading is followed by the substance you should be able to explain in your own words afterwards.

## 1. Introduction

Framing: why now. Three things converged — models that can reason well enough to plan multi-step, a standardized way to give them tools, and cheap enough inference to run 10–20 calls per task. None of the ideas are new (multi-agent systems and BDI architectures date to the 1980s); the capable reasoning core is what's new.

## 2. What is Agentic AI?

The distinction to hold onto is **workflow vs agent**:

- A **workflow** has a path defined in code. The LLM fills in steps; you decide the sequence.
- An **agent** decides its own sequence at runtime based on what it observes.

Workflows are more reliable, cheaper, easier to debug, and easier to audit. Agents are more flexible. **Choose the workflow unless the task genuinely requires runtime path decisions.** Most production "agents" are mostly workflow with a small agentic core, and that's the right design, not a compromise.

Useful autonomy ladder:
```
L0  Fixed script, no model
L1  Model in a fixed pipeline           (LLM as a step)
L2  Model routes between fixed paths    (LLM as a router)
L3  Model plans its own steps, human approves actions
L4  Model plans and executes, human reviews outcomes
L5  Fully autonomous, long-horizon
```
Almost everything valuable in production today is L2–L4.

## 3. How Agentic and Generative AI Work Together

Generative AI is the **reasoning engine**; agentic AI is the **control system around it**. The generative model contributes: understanding the goal, decomposing it, choosing tools, interpreting results, and synthesizing output. The agentic layer contributes everything the model can't do: persistence, execution, retries, state, guardrails, and termination.

Concretely: the LLM never actually calls anything. It emits a structured intent — "call `get_campaign(1558)`" — and your orchestration code decides whether to run it, runs it, and feeds the result back. Every safety and reliability control lives in that gap.

## 4. The Core Traits of an Agent

Six traits, each with an engineering implication:

| Trait | Meaning | What you must build |
|---|---|---|
| **Autonomy** | Decides next action without step-by-step instruction | Permission model, action limits |
| **Goal-orientation** | Works toward an outcome, not a single output | Explicit success criteria, termination conditions |
| **Reasoning / planning** | Decomposes a goal into steps | Planning prompt or explicit planner node |
| **Tool use** | Acts on the world | Tool schemas, execution sandbox, error contracts |
| **Memory** | Carries state across steps and sessions | Context management + persistent store (Part A §5) |
| **Reflection** | Evaluates its own output and retries | Critic step, evaluation rubric, retry budget |

If a system has fewer than four of these, calling it an agent is marketing.

## 5. Agentic Architecture

The canonical loop:

```
        ┌──────────────────────────────────────────────┐
        │                                              │
        ▼                                              │
   PERCEIVE  ──▶  REASON / PLAN  ──▶  ACT  ──▶  OBSERVE ┘
   (goal +        (decide next        (call     (read result,
    context)       action)             tool)     update state)
                                                        │
                                             ┌──────────┴──────────┐
                                             │  done?  →  RESPOND  │
                                             └─────────────────────┘
```

The components you'll actually write:

- **Orchestrator / runtime** — owns the loop, the state, and the stopping conditions. The most important and least glamorous piece.
- **Reasoning core** — the LLM, with the system prompt that defines role, constraints, and tool policy.
- **Planner** — either implicit (the model reasons step by step) or explicit (a separate call produces a plan, then execution follows it). Explicit plans are auditable and interruptible; implicit is cheaper and adapts faster.
- **Tool layer** — schemas, execution, and crucially the **error contract**: a failing tool should return a structured, informative error the model can act on, not throw.
- **Memory layer** — short-term context management plus long-term store.
- **Guardrails** — input validation, output validation, permission checks, cost/step caps. These belong in code, not in the prompt. A prompt is a request; code is a guarantee.
- **Observability** — traces, spans, token counts, latency per step.

## 6. Engineering Principles

The principles that separate a demo from a system:

1. **Least privilege.** Every tool gets the narrowest possible scope. Read-only unless it has to write. The blast radius of a confused agent equals the permissions you gave it.
2. **Human-in-the-loop at the right seams.** Not on everything (defeats the purpose) — on irreversible actions: sends, payments, deletions, publishes, config changes.
3. **Bound everything.** Max steps, max tokens, max wall-clock, max cost per run. Unbounded loops are the default failure mode.
4. **Fail loudly and structurally.** Return errors the model can reason about: `{"error": "rate_limited", "retry_after": 30}` beats a stack trace.
5. **Observability from day one.** You cannot debug a non-deterministic multi-step system from the final output. You need the full trace of every prompt, tool call, and result.
6. **Evaluate, don't vibe-check.** Build a set of test cases with expected outcomes before you tune. Measure task success rate, not output "quality."
7. **Determinism where you can afford it.** Every step you move from the model into code is a step that can't hallucinate.
8. **Idempotency.** Agents retry. Make sure a retried action doesn't double-fire.
9. **Treat tool output as untrusted data.** Content returned by a tool can contain text that looks like instructions. **Prompt injection** is the defining security problem of agentic systems: an agent that reads a web page or an email can be instructed by it. Data from tools must never be treated as commands from the user.

## 7. Agentic Design Patterns

The named patterns, from simplest to most complex. Reach for them in this order.

**Building blocks (workflow-level):**
- **Prompt chaining** — output of step 1 feeds step 2. Fixed sequence, each step simpler.
- **Routing** — a classifier sends the input down one of several specialized paths. Cheap, high value, very common.
- **Parallelization** — run independent subtasks concurrently and merge. Two flavors: *sectioning* (split the work) and *voting* (run the same task N times and take consensus).

**Agentic patterns:**
- **Tool use** — the foundational one. Model requests, code executes, result returns.
- **ReAct (Reason + Act)** — interleave `Thought → Action → Observation` until done. The default agent pattern. Reasoning traces are visible, which makes it debuggable.
- **Reflection / self-critique** — generate, then evaluate against criteria, then revise. Works best when the evaluation signal is real (compiler output, test results, schema validation). Self-critique with no external signal produces confident revisions that aren't better.
- **Plan-and-execute** — produce a full plan first, then execute steps. Better for long tasks (the plan anchors the goal against context drift), worse at adapting mid-flight. Usually paired with re-planning on failure.
- **Orchestrator–worker** — a lead agent decomposes and delegates to workers, then synthesizes. Handles genuinely parallel decomposable work.
- **Evaluator–optimizer** — one component generates, a separate one scores against a rubric, loop until threshold or budget. Reflection with the critic split out.

**Selection rule:** start with the simplest pattern that could work, add complexity only where you measure a failure. Each added agent multiplies cost, latency, and failure surface.

## 8. Agent Roles and Collaboration

Multi-agent topologies:

- **Sequential / pipeline** — researcher → writer → editor. Predictable, easy to debug, no coordination overhead.
- **Hierarchical (supervisor)** — a manager routes to specialists and owns the final answer. The most common production multi-agent shape.
- **Handoff** — control transfers fully from one agent to another, each with its own tools and prompt. Common in support routing.
- **Blackboard / shared state** — agents read and write a shared state object rather than messaging each other. This is the LangGraph model.
- **Debate / consensus** — multiple agents argue or vote. Improves accuracy on reasoning-heavy tasks, expensive.

**Why role separation helps at all:** it's context engineering, not personality. Each agent gets a smaller, focused instruction set and only the tools it needs — which reduces tool-selection errors and keeps each context window clean. That's the real mechanism. "You are an expert marketing strategist" contributes far less than people assume.

**When multi-agent is wrong:** when the subtasks aren't genuinely independent, when the coordination overhead exceeds the benefit, or when a single agent with good tools would do. Multi-agent systems fail in ways single agents don't — deadlock, infinite delegation, context loss at handoffs, and cost blowup.

## 9. Real-World Applications

Patterns that are actually working in production, with the reason they work:

- **Coding agents** — strongest case, because verification is free. Tests pass or they don't.
- **Deep research** — parallel search, source triage, synthesis with citations. Works because the output is reviewable.
- **Customer support** — triage, retrieval, resolution of well-scoped issues, escalation of the rest.
- **Data / analytics agents** — natural language → SQL → chart → narrative. High value, needs strict sandboxing.
- **Ops and QA automation** — checking configurations against rules, validating campaign setups, reconciling records across systems, generating status summaries from multiple tools. This is the closest to your day job: multi-source, rule-checkable, high-toil, low-ambiguity.
- **Document processing** — extraction, classification, routing, compliance checking.

The pattern across all of them: **high toil, clear success criteria, verifiable output, bounded blast radius.** Where verification is impossible or the cost of error is unbounded, agents underperform.

## 10. Building and Scaling

**The development sequence that works:**
1. Do the task manually and write down every step and decision.
2. Build the simplest possible version — single prompt, no tools.
3. Add tools one at a time, measuring after each.
4. Build an eval set (20–50 real cases with expected outcomes) *before* optimizing.
5. Add memory only when statelessness demonstrably fails.
6. Add more agents only when a single agent demonstrably fails.

**Failure modes to design against:**
- **Compounding error.** 95% reliability per step is 60% over 10 steps. Reliability must be engineered per-step, and long chains need checkpoints.
- **Infinite loops.** The agent retries the same failing action forever. Fix: step budgets and loop detection.
- **Tool hallucination.** Calling a tool that doesn't exist or with invented arguments. Fix: strict schema validation, and return a helpful error listing valid options.
- **Context drift.** By step 30 the agent has forgotten the original goal. Fix: re-inject the goal every turn, keep structured state.
- **Silent success.** Reports "done" without having done it. Fix: verify outcomes with a separate check, don't trust the agent's self-report.
- **Cost blowup.** Agentic loops generate many calls per task; inference cost dominates total cost of ownership far more than people plan for.

**Scaling levers:** prompt caching for stable prefixes, model tiering (small fast model for routing and classification, large model only for hard reasoning), batching for offline work, aggressive context compaction, and caching tool results.

## 11. Frameworks and Tools

**What frameworks give you:** loop management, state persistence and checkpointing, retries, streaming, tracing, and pre-built integrations. **What they cost you:** abstraction you have to debug through, and opinions that may not match your problem.

**Honest advice for learning:** build one agent from scratch with raw API calls first — a while loop, a tool dispatcher, a message list. Maybe 150 lines. Once you've done that, every framework's docs become obvious, because you'll recognize what each abstraction is hiding.

Rough map of the landscape:

| Framework | Orchestration model | Best for |
|---|---|---|
| **LangGraph** | Directed graph, explicit nodes and conditional edges, checkpointed state | Stateful production workflows needing auditability and human-in-the-loop |
| **CrewAI** | Role-based crews with process types | Fast role-based multi-agent prototypes |
| **Claude Agent SDK** | Minimal agent loop, tools first, sub-agents as tools | Anthropic-native production agents |
| **OpenAI Agents SDK** | Explicit handoffs | Simplest path within the OpenAI ecosystem |
| **Microsoft Agent Framework** | Merged Semantic Kernel + AutoGen | Enterprise .NET / Microsoft stacks |
| **LlamaIndex Workflows** | Event-driven, retrieval-first | RAG-grounded agents |
| **Pydantic AI** | Type-safe, schema-first | Python teams who want static guarantees |
| **Google ADK** | Hierarchical agent tree | Google Cloud–native teams |

A common production split: prototype in a fast role-based framework, deploy in a graph-based one.

**The protocol layer matters more than the framework choice.** MCP (Model Context Protocol) standardizes how agents connect to tools and data — write a tool server once and any MCP-capable framework can use it. A2A covers agent-to-agent communication. Because your tool definitions become portable, framework lock-in is much weaker than it looks.

**Supporting infrastructure you'll also need:** a vector store (pgvector, Qdrant, Pinecone, Weaviate), an observability/eval layer (LangSmith, Langfuse, Braintrust, Arize, or OpenTelemetry-based tracing), and a prompt/config versioning approach.

## 12. Current Trends and Conclusion

Where the field is moving:

- **Protocol standardization.** MCP is settling into the tool-connection standard across frameworks; A2A is the emerging equivalent for agent-to-agent. The practical effect is that tool integrations become portable assets rather than framework-specific code.
- **Evaluation as a first-class discipline.** Agent evals — task success rate, trajectory quality, cost per task — are maturing from an afterthought into the thing that decides whether a system ships. Expect this to be the highest-leverage skill in the space.
- **Longer horizons.** Agents that run for hours or days, with durable state, checkpointing, and resumption. This is why graph/state-machine frameworks won the production tier.
- **Computer use and browser agents.** Operating existing software through its UI, which unlocks systems with no API — at the cost of much harder reliability and much bigger security exposure.
- **Model tiering and small models.** Routing, classification, and extraction moving to small fast models; large models reserved for genuine reasoning. Driven by the fact that inference is the dominant ongoing cost.
- **Security maturing.** Prompt injection, tool poisoning, and excessive agency are now recognized as the core risk class. Expect permission models, sandboxing, and injection defenses to become standard architecture rather than optional hardening.
- **Cost discipline.** Early development is a small fraction of total cost of ownership; inference dominates. Teams are getting serious about caching, compaction, and step budgets.

**The thing to take away from the whole course:** an agent is not a smarter model. It's a *control system* — a loop, a state store, a permission model, and a set of tools — with a language model in the reasoning seat. The model quality sets your ceiling. Your engineering sets whether you get anywhere near it.

---

# APPENDIX — SELF-CHECK

If you can answer these without looking, you've got the material:

1. Why is "conversational AI" not the same kind of category as "generative AI"?
2. Where does the LLM actually execute a tool call? (Trick question.)
3. Why can't you reference a SELECT alias in a WHERE clause?
4. What silently turns a LEFT JOIN into an INNER JOIN?
5. Why is a surrogate primary key usually better than a natural one?
6. Is LLM pretraining supervised or unsupervised?
7. What's the difference between a candidate key and a super key?
8. Why does a 95%-reliable step make a 10-step agent unreliable?
9. When should you use a workflow instead of an agent?
10. Why is prompt injection a fundamentally harder problem for agents than for chatbots?
11. What's the difference between short-term memory management by summarization vs by structured state?
12. Why does reflection work well for code but poorly for essays?
