AI-Powered Question Paper Augmenter

The AI-Powered Question Paper Augmenter is an innovative application developed using Streamlit and integrated with Ollama, a local large language model (LLM) platform. This tool is designed to help educators, students, and academic professionals by generating a fresh set of similar questions and answers from any uploaded question paper in PDF format.

The application features a clean, web-based interface built using Streamlit, making it easy to use and deploy. Users can upload any question paper in PDF form, and the app automatically extracts the text using PyMuPDF (fitz). It then selects the first 10 questions and sends them to an AI model running locally via Ollama. The model processes the input and generates 20 new questions along with detailed answers, following a clear format.

![image](https://github.com/user-attachments/assets/ebb73ff7-d974-4cdd-9e85-a9a4a8f1b892)

One of the standout aspects of this project is its offline capability. By using Ollama, the app doesn't rely on external cloud APIs or internet connectivity. All AI responses are generated locally on the user’s system, ensuring faster response times, data privacy, and usability in low-connectivity environments such as classrooms or remote institutions.

Key Features:

->  PDF upload and parsing to extract original questions.

->  Integration with Ollama’s LLMs (e.g., LLaMA 3) for AI-generated question-answer pairs.

->  Streamlit-based UI for real-time interaction and simplicity.

->  Completely offline AI functionality, enhancing security and privacy.

->  Easy deployment and minimal setup for educators and institutions.

->  This tool can be particularly useful for:

->  Teachers creating practice papers or mock exams.

->  Students seeking additional practice questions.

![image](https://github.com/user-attachments/assets/4f33c07f-764e-4170-b04e-0dd318fb7334)

->  Educational platforms looking to automate content generation.

In essence, this project combines the power of local AI processing with the accessibility of web-based tools. It represents a practical, impactful use of modern LLMs to improve educational workflows. Future improvements could include support for multiple question formats, language translation, or integration with learning management systems (LMS).


![image](https://github.com/user-attachments/assets/0a104a80-a382-4598-8b3b-657281e94d50)

![image](https://github.com/user-attachments/assets/3ea690c4-734c-47d9-bbe2-175ba95e05b5)







