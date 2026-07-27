import "./MessageBubble.css";

export default function MessageBubble({ role, content }) {

    const isUser = role === "user";

    return (
        <div className={`message ${isUser ? "user" : "assistant"}`}>

            <div className="avatar">
                {isUser ? "🧑" : "🎓"}
            </div>

            <div className="bubble">
                {content}
            </div>

        </div>
    );
}