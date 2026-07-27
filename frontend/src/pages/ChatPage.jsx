import { useEffect, useRef, useState } from "react";

import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import ChatInput from "../components/ChatInput";

import { sendMessage, createSession, getHistory } from "../services/api";

import "./ChatPage.css";

export default function ChatPage() {

    const [messages, setMessages] = useState([]);

    const [loading, setLoading] = useState(false);

    const [sessions, setSessions] = useState([]);

    const [selectedSession, setSelectedSession] = useState(null);

    // Temporary session id
    // Later this will come from backend
    const sessionId = selectedSession;

    const bottomRef = useRef(null);

    useEffect(() => {
        bottomRef.current?.scrollIntoView({
            behavior: "smooth"
        });
    }, [messages]);

    const handleSend = async (prompt) => {

        if (!prompt.trim()) return;

        // Show user message instantly
        setMessages(prev => [
            ...prev,
            {
                role: "user",
                content: prompt
            }
        ]);

        setLoading(true);

        try {

            const data = await sendMessage(
                sessionId,
                prompt
            );

            setMessages(prev => [
                ...prev,
                {
                    role: "assistant",
                    content: data.response
                }
            ]);

        } catch (error) {

            console.error(error);

            setMessages(prev => [
                ...prev,
                {
                    role: "assistant",
                    content: "Something went wrong."
                }
            ]);

        } finally {

            setLoading(false);

        }

    };

    const handleSessionClick = (id) => {

        console.log("Selected Session:", id);

        // Later:
        // fetch previous history from backend

    };

    const handleNewChat = async() => {
        try{
            const session = await createSession("New CHat");

            setSessions(prev =>[
                session,
                ...prev
            ])
            setSelectedSession(session.id);
            setMessages([]);
        }catch(err){
            console.log(err);
        }
    };

    const handleSelectSession = async(id) => {
        setSelectedSession(id);

        try{
            const history = await getHistory(id);
            setMessages(history);
        }catch(err){
            console.log(err);
        }
    }

    return (

        <div className="chat-page">

            <Sidebar
                sessions={sessions}
                selectedSession={selectedSession}
                onSelect={handleSessionClick}
                onNewChat={handleNewChat}
            />

            <div className="chat-container">

                <div className="chat-header">

                    <h2>EduMentor AI</h2>

                </div>

                <div className="chat-body">

                    <ChatWindow
                        messages={messages}
                    />

                    {
                        loading &&
                        <div className="typing">
                            EduMentor AI is typing...
                        </div>
                    }

                    <div ref={bottomRef}></div>

                </div>

                <ChatInput
                    onSend={handleSend}
                    loadinig={loading}
                    disabled = {!selectedSession}
                >
                    <textarea disabled={loading}/>
                </ChatInput>

            </div>

        </div>

    );

}