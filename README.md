# AI Compliance Orchestrator

This project is an advanced AI-powered compliance workflow orchestrator. It integrates Retrieval-Augmented Generation (RAG), OCR, code/config scanning, risk scoring, red team critic, human-in-the-loop (HITL), multimodal input handling, workflow control, reliability, and caching/state management.

## Directory Structure

```
ai_compliance_orchestrator/
    agents.py
    main.py
    models.py
    utils.py
    __pycache__/
    test_main.py
    .env
```

## Features

- **RAG for Policy Retrieval & Evidence Collection**: Uses LLMs and vector DBs for document retrieval and Q&A.
- **Vision/OCR Agent**: Extracts text from images using OCR.
- **Code/Config Scanner**: Scans code/config for secrets and vulnerabilities.
- **Risk Scorer & Red Team Critic**: Assesses risk and generates adversarial questions.
- **Final Aggregator**: Aggregates results and applies business logic.
- **Retries & Circuit Breakers**: Ensures reliability and fault tolerance.
- **State, Memory, Caching**: Uses Redis and MongoDB for session and result storage.
- **Multimodal Inputs**: Handles text, image, and code inputs.
- **Workflow Control & Reliability**: Orchestrates tasks with error handling and fallback logic.

## Setup

1.  **Clone the repository**
2.  **Install dependencies**:

    ```bash
    pip install fastapi uvicorn redis pymongo websockets openai pillow pytesseract
    ```

3.  **Configure environment variables**:

    -   Create a `.env` file in `ai_compliance_orchestrator/` with your MongoDB Atlas URI and database name:

        ```
        MONGODB_URI=your_mongodb_atlas_uri
        MONGODB_DATABASE=your_db_name
        OPENAI_API_KEY=your_openai_api_key
        ```

4.  **Start the server**:

    ```bash
    python ai_compliance_orchestrator/main.py
    ```

5.  **Run tests**:

    ```bash
    python -m pytest ai_compliance_orchestrator/test_main.py
    ```

## Usage

-   Access API endpoints via FastAPI (see `main.py`).
-   WebSocket endpoint for HITL: `ws://localhost:8000/connect?session_id=your_session_id`
-   REST endpoints for workflow, results, history, and HITL.

## Notes

-   Ensure MongoDB Atlas and Redis are running and accessible.
-   For OCR, Tesseract must be installed on your system.
-   Set your OpenAI API key in `.env` for LLM features.

