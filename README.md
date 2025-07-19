## 🧩 Key Features

- ** Multi-Agent Data Generation: **  
  Parallel agents extract and rephrase actuarial concepts, ensuring diversity and coverage of the SOA syllabus.

- ** Exam-Style Q&A Creation: **  
  Focuses on long-answer, scenario-based questions that require reasoning, calculation, and explanation—just like the real exams.

- ** Data Cleaning & Validation: **  
  Includes scripts to deduplicate, validate, and format data as JSONL, ready for LLM fine-tuning.

- ** Unicode & Formatting Robustness: **  
  Handles mathematical symbols, formulas, and actuarial notation with care, ensuring model-ready data.

- ** Extensible & Modular: **  
  Easily add new agents or data sources to expand coverage or adapt to new exam syllabi.


## 🛠️ Usage

### 1. **Scrape & Extract Data**

Run the main orchestration script to generate raw Q&A pairs:

```bash
python agents/main.py
```

### 2. **Clean & Validate Data**

Remove duplicates and non-JSON lines, ensuring every line is a valid Q&A pair:

```bash
python agents/clean.py
```

### 3. **Fine-Tune Your Model**

Use the cleaned `training_data.jsonl` as input for your favorite LLM fine-tuning framework (e.g., HuggingFace, OpenAI, Llama).

---

## 📚 Example Q&A Pair

```json
{
  "Question": "An insurer is required to calculate the policyholder benefit liability under VM-20. What assumptions must be considered, and how do they impact the calculation?",
  "Answer": "The calculation of policyholder benefit liability under VM-20 requires assumptions about mortality, interest rates, policyholder behavior, and expenses. Each assumption impacts the reserve calculation by affecting projected cash flows and the present value of future benefits."
}
```

---

## 🎯 Why Use This Project?

- **Save time**: Automate the tedious process of creating high-quality actuarial exam questions and answers.
- **Boost model performance**: Train LLMs that truly understand actuarial reasoning, not just rote memorization.
- **Stay syllabus-aligned**: Ensure your data and models are always up-to-date with the latest SOA exam requirements.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for new agents, data sources, or features.

---

## 📄 License

MIT License

---

## ✨ Get Started

Clone the repo, run the agents, clean your data, and start fine-tuning your actuarial expert LLM today!

---

**Empower your actuarial exam prep with AI.**  
_From raw commentary to expert-level Q&A—automated, accurate, and aligned with your goals._
