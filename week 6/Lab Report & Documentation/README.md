# CA1601400 Artificial Intelligence Lab 6: NLP Fundamentals

**Author:** Saad Javaid  
**Course Code:** CA1601400  
**Curriculum Mapping:** CLO3 (C3: Apply)  

---

## 1. Project Overview
This repository contains a reproducible, traceable Natural Language Processing (NLP) information retrieval pipeline. It compares whitespace, regex-based Unicode word-like, and pretrained subword tokenization, investigates the survivability of policy exceptions across fixed-window and sentence-aware chunking boundaries, and evaluates retrieval accuracy using TF-IDF and dense sentence embeddings (`all-MiniLM-L6-v2`) on CPU.

---

## 2. Directory Structure
```text
.
├── requirements.txt         # Pinned virtual environment dependencies
├── README.md                # System documentation and reproduction guide
├── corpus.json              # 5 synthetic documents (150-250 words each)
├── queries.json             # 8 labeled queries (4 dev, 4 test) + 2 unanswerable
├── retrieval_log.csv        # Comprehensive top-3 retrieval log across all runs
├── lab6_search.py           # Core Retriever module (TF-IDF & Dense Embeddings)
├── scenario1_handbook.py    # University late policy scenario
├── scenario2_support.py     # Damage report & regional filtering
├── scenario3_docs.py        # Case-sensitive API documentation retrieval
├── scenario4_workplace.py   # Contractor vs staff telecommuting rules
├── scenario5_equipment.py   # Step-by-step diagnostic troubleshooting
├── guided_tokens.py         # Guided tokenization inspection
├── guided_embeddings.py     # Dense vector similarity walkthrough
├── guided_chunks.py         # Chunk boundary inspection
├── guided_limits.py         # Token length and model budget audit
├── guided_metrics.py        # Hit@3 and MRR@3 metric sanity checks
├── guided_chatbot.py        # Canonical FAQ assistant script
├── guided_suggestions.py    # Partial query lexical suggestion script
├── task1_tokens.py          # Task 1 tokenization comparison on 6 inputs
├── task1_chatbot_check.py   # Task 1 FAQ assistant validation checks
├── task2_chunks.py          # Task 2 chunking engine & boundary unit tests
├── task2_semantic_check.py  # Task 2 lexical vs semantic paraphrase check
├── task3_retrieval.py       # Task 3 full evaluation pipeline across 6 configs
├── document_chatbot.py      # Interactive evidence retrieval chatbot
└── Lab6_Report.docx         # Formal academic report
```

---

## 3. Installation & Virtual Environment Setup

### On Linux / macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### On Windows PowerShell:
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## 4. Execution & Verification Instructions

### Step 1: Run Tokenization Tests (Task 1)
```bash
python task1_tokens.py
python task1_chatbot_check.py
```

### Step 2: Run Chunking Unit Tests & Semantic Checks (Task 2)
```bash
python task2_chunks.py
python task2_semantic_check.py
```

### Step 3: Run Full Retrieval Benchmark & Metric Logging (Task 3)
```bash
python task3_retrieval.py
```

### Step 4: Run the Interactive Document Chatbot
```bash
python document_chatbot.py
```

---

## 5. External References & Models
- Pretrained Dense Sentence Encoder: `sentence-transformers/all-MiniLM-L6-v2`
- Sparse Lexical Baseline: `scikit-learn` `TfidfVectorizer`
