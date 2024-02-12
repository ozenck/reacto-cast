import React, { useState, useEffect } from 'react';

const WebSocketComponent = () => {
    const [messages, setMessages] = useState([]);

    useEffect(() => {
        const ws = new WebSocket('ws://localhost:8000/ws/task-status/');

        ws.onopen = () => {
            console.log('WebSocket Connected');
        };

        ws.onmessage = (e) => {
            console.log(e)
            const data = JSON.parse(e.data);
            const statusMessage = data.message;
            setMessages(prevMessages => [...prevMessages, statusMessage]); // Update state with the status message
        };

        ws.onclose = () => {
            console.log('WebSocket Disconnected');
        };

        // Clean up function to close websocket connection when component unmounts
        return () => {
            ws.close();
        };
    }, []); // Empty dependency array means this effect runs only once when the component mounts

    return (
        <div>
            <h2>Messages</h2>
            <ul>
                {messages.map((message, index) => (
                    <li key={index}>{message.status}</li> // Adjust according to the message format
                ))}
            </ul>
        </div>
    );
};

export default WebSocketComponent;
