import { useState } from "react";
import { askQuestion } from "./services/api";

function App() {
  const [query, setQuery] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
  if (!query.trim()) return;

  setLoading(true);

  const data = await askQuestion(query);

  setMessages((prev) => [
    ...prev,
    { type: "user", text: query },
    {
      type: "bot",
      text: data.response,
      route: data.route,
    },
  ]);

  setQuery("");
  setLoading(false);
};

  return (
    <div>
      <h1>AI Finance Copilot</h1>

      <input
  value={query}
  onChange={(e) => setQuery(e.target.value)}
  onKeyDown={(e) => {
    if (e.key === "Enter") {
      handleSubmit();
    }
  }}
  placeholder="Ask a finance question..."
/>

      <button
  className="clear-btn"
  onClick={() => setMessages([])}
>
  Clear Chat
</button>

<div>
  <button onClick={() => setQuery("What is NVDA stock price?")}>
    NVDA Price
  </button>

  <button onClick={() => setQuery("Compare NVDA and AMD")}>
    Compare Stocks
  </button>

  <button onClick={() => setQuery("What are the company risks?")}>
    Risk Analysis
  </button>
</div>


      <div className="chat-container">
  {messages.map((msg, index) => (
    <div
      key={index}
      className={
        msg.type === "user"
          ? "user-msg"
          : "bot-msg"
      }
    >
      <strong>
        {msg.type === "user"
          ? "You"
          : msg.route?.toUpperCase()}
      </strong>

      <p>{msg.text}</p>
    </div>
  ))}

  {loading && <p>🤖 Analyzing...</p>}
</div>

  {loading && <p>Thinking...</p>}
</div>
    
  );
}

export default App;