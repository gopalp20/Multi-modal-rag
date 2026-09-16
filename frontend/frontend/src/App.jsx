import { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [uploadMessage, setUploadMessage] = useState("");
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
    setUploadMessage("");
  };

  const handleUpload = async () => {
    if (!file) {
      setUploadMessage("Please select a PDF first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setUploadMessage("Ingesting PDF...");

      const response = await fetch("http://localhost:8000/upload", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Upload failed");
      }

      setUploadMessage(data.message);
    } catch (error) {
      setUploadMessage(error.message);
    }
  };

  const handleQuery = async () => {
    if (!question.trim()) {
      return;
    }

    try {
      setLoading(true);
      setAnswer("");

      const response = await fetch("http://localhost:8000/query", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: question,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Query failed");
      }

      setAnswer(data.answer);
    } catch (error) {
      setAnswer(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">

      <header className="header">
        <h1>PDF RAG Assistant</h1>
        <p>Upload a PDF and ask questions about its contents</p>
      </header>

      <main className="container">

        {/* Upload Card */}

        <section className="card">
          <h2>Upload your PDF</h2>

          <p className="card-description">
            Select a PDF document and ingest it into the knowledge base.
          </p>

          <input
            className="file-input"
            type="file"
            accept=".pdf"
            onChange={handleFileChange}
          />

          <button
            className="ingest-button"
            onClick={handleUpload}
          >
            Ingest PDF
          </button>

          {uploadMessage && (
            <p className="status">
              {uploadMessage}
            </p>
          )}
        </section>


        {/* Query Card */}

        <section className="card">
          <h2>Ask a Question</h2>

          <p className="card-description">
            Ask anything related to the uploaded document.
          </p>

          <div className="question-container">

            <input
              className="question-input"
              type="text"
              placeholder="What is this document about?"
              value={question}
              onChange={(event) => setQuestion(event.target.value)}
              onKeyDown={(event) => {
                if (event.key === "Enter") {
                  handleQuery();
                }
              }}
            />

            <button
              className="ask-button"
              onClick={handleQuery}
              disabled={loading}
            >
              {loading ? "Thinking..." : "Ask"}
            </button>

          </div>

          {loading && (
            <p className="loading">
              Searching the document and generating an answer...
            </p>
          )}

          {answer && (
            <div className="answer-box">
              <h3>Answer</h3>
              <p>{answer}</p>
            </div>
          )}

        </section>

      </main>

    </div>
  );
}

export default App;