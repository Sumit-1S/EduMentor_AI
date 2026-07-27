import { useState } from "react";
import "./ChatInput.css";

export default function ChatInput({ onSend, loading }) {

    const [prompt, setPrompt] = useState("");

    const handleSend = () => {

        if (!prompt.trim()) return;

        onSend(prompt);

        setPrompt("");
    };

    const handleKeyDown = (e) => {

        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            handleSend();
        }

    };

    return (

        <div className="chat-input-container">

            <textarea
                placeholder="Message EduMentor AI..."
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
                onKeyDown={handleKeyDown}
                rows={1}
                disabled={loading}
            />

            <button
                onClick={handleSend}
                disabled={loading || !prompt.trim()}
            >
                {loading ? "..." : "➤"}
            </button>

        </div>

    );

}