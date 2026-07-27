import "./Sidebar.css";

export default function Sidebar({
    sessions,
    selectedSession,
    onSelect,
    onNewChat
}) {

    return (

        <div className="sidebar">

            <div className="sidebar-header">

                <h2>🎓 EduMentor AI</h2>

                <button
                    className="new-chat-btn"
                    onClick={onNewChat}
                >
                    + New Chat
                </button>

            </div>

            <div className="chat-list">

                {
                    sessions.length === 0 ? (

                        <p className="empty-chat">
                            No conversations yet
                        </p>

                    ) : (

                        sessions.map((session) => (

                            <div
                                key={session.id}
                                className={`chat-item ${
                                    selectedSession === session.id
                                        ? "active"
                                        : ""
                                }`}
                                onClick={() => onSelect(session.id)}
                            >
                                <span>💬</span>

                                <span className="title">
                                    {session.title}
                                </span>

                            </div>

                        ))

                    )
                }

            </div>

            <div className="sidebar-footer">

                <p>Powered by Gemini</p>

            </div>

        </div>

    );

}
