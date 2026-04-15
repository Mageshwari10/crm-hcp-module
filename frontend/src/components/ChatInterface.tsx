import React, { useState, useRef, useEffect } from 'react';
import { Bot, Send } from 'lucide-react';
import { useDispatch, useSelector } from 'react-redux';
import { RootState, AppDispatch } from '../store';
import { addMessage, sendChatMessage } from '../store/crmSlice';

const ChatInterface: React.FC = () => {
  const [input, setInput] = useState('');
  const dispatch = useDispatch<AppDispatch>();
  const { chatHistory, isLoading, error } = useSelector((state: RootState) => state.crm);
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
    <div className="panel" style={{ height: '100%', maxHeight: 'calc(100vh - 100px)' }}>
      <div className="panel-title" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: '2px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <Bot size={18} />
          <span>AI Assistant</span>
        </div>
        <span className="panel-subtitle">Log interaction via chat</span>
      </div>
      
      <div className="chat-body" ref={scrollRef}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
          {chatHistory.map(msg => (
             <div 
               key={msg.id} 
               className="agent-msg" 
               style={msg.sender === 'user' ? { alignSelf: 'flex-end', background: 'var(--bg-body)', borderColor: 'var(--border-color)' } : { alignSelf: 'flex-start' }}
             >
               {msg.text}
             </div>
          ))}
          {isLoading && (
            <div className="agent-msg" style={{ alignSelf: 'flex-start', display: 'flex', gap: '4px' }}>
               <span style={{ fontSize: '1.2rem'}}>...</span>
            </div>
          )}
          {error && (
            <div className="agent-msg" style={{ alignSelf: 'flex-start', color: 'red' }}>
               {error}
            </div>
          )}
        </div>
      </div>

      <div className="chat-footer">
        <input 
          className="chat-input"
          type="text" 
          placeholder="Describe interaction..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleSend()}
        />
        <button className="chat-log-btn" onClick={handleSend} disabled={isLoading}>
           <Send size={14} style={{ transform: 'rotate(-45deg)', marginTop: '-2px' }} />
           Log
        </button>
      </div>
    </div>
  );
};

export default ChatInterface;
