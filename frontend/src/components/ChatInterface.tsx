import React, { useState, useRef, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { RootState, AppDispatch } from '../store';
import { sendChatMessage, addMessage } from '../store/crmSlice';
import { Send, Bot, User } from 'lucide-react';

const ChatInterface: React.FC = () => {
  const [input, setInput] = useState('');
  const dispatch = useDispatch<AppDispatch>();
  const { chatHistory, isLoading } = useSelector((state: RootState) => state.crm);
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [chatHistory, isLoading]);

  const handleSend = () => {
    if (!input.trim() || isLoading) return;
    
    dispatch(addMessage({
      id: Date.now().toString(),
      sender: 'user',
      text: input
    }));

    dispatch(sendChatMessage(input));
    setInput('');
  };

  return (
    <div className="glass-panel" style={{ height: '100%' }}>
      <div className="panel-header">
        <Bot size={20} color="var(--primary)" /> AI Co-Pilot
      </div>
      
      <div className="panel-content chat-container">
        <div className="messages-area" ref={scrollRef}>
          {chatHistory.map((msg) => (
            <div key={msg.id} className={`message ${msg.sender}`}>
              {msg.text}
            </div>
          ))}
          {isLoading && (
            <div className="typing-indicator">
              <span></span><span></span><span></span>
            </div>
          )}
        </div>

        <div className="chat-input-area">
          <input 
            type="text" 
            placeholder="Log an interaction, e.g. 'Met with Dr. Smith...'" 
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleSend()}
            disabled={isLoading}
          />
          <button className="send-btn" onClick={handleSend} disabled={isLoading || !input.trim()}>
            <Send size={16} />
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatInterface;
