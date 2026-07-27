import MessageBubble from "./MessageBubble";
import "./ChatWindow.css";

export default function ChatWindow({ messages }) {
    return (
        <div className="chat-window">

            {messages.length === 0 ? (
                <div className="empty-chat">
                    <h2>Welcome to EduMentor AI 👋</h2>
                    <p>Ask me anything about your studies.</p>
                </div>
            ) : (
                messages.map((message, index) => (
                    <MessageBubble
                        key={index}
                        role={message.role}
                        content={message.content}
                    />
                ))
            )}

        </div>
    );
}

