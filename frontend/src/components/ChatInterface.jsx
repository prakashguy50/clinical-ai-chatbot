import React, { useState } from "react";
import axios from "axios";

const ChatInterface = () => {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    try {
      const response = await axios.post("https://clinical-ai-chatbot-934733378968.us-central1.run.app/ask", {
        question,
      });
      
      setAnswer(response.data.answer);
    } catch (error) {
      setAnswer("Something went wrong. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-xl mx-auto">
      <textarea
        className="w-full p-2 border rounded mb-4"
        rows="4"
        placeholder="Enter your medical question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      ></textarea>
      <button
        className="bg-blue-600 text-white px-4 py-2 rounded"
        onClick={handleSubmit}
        disabled={loading}
      >
        {loading ? "Asking..." : "Ask"}
      </button>
      {answer && (
        <div className="mt-4 p-3 bg-white shadow rounded">
          <strong>Response:</strong>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
};

export default ChatInterface;
