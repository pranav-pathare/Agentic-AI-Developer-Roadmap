
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


