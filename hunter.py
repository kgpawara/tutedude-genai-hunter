# A1 - Data Structures for RAG - By [Tuz Naav]
# TuteDude - Assignment 1

# Use Case 1: RAG Chunks are always List
rag_chunks = ["MPSC PYQ 2019", "MPSC PYQ 2020", "MPSC PYQ 2021"]
print(f"Total Chunks: {len(rag_chunks)}")

# Use Case 2: LLM API needs Dict
llm_message = {"role": "user", "content": "MPSC साठी RAG कसा बनवायचा?","model": "gpt-4o"}
print(llm_message)

# Use Case 3: Tuple for Fixed Config - तू आत्ताच शिकलास
RAG_CONFIG = (500, 50)
print(f"Config: {RAG_CONFIG}")

# Use Case 4: Set for Removing Duplicate PDFs
pdf_files = ["pyq.pdf", "pyq.pdf", "syllabus.pdf"]
unique_pdfs = set(pdf_files)
print(f"Unique PDFs: {unique_pdfs}")

