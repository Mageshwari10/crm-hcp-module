import React from 'react';
import ChatInterface from './components/ChatInterface';
import StructuredForm from './components/StructuredForm';
import InteractionHistory from './components/InteractionHistory';

const App: React.FC = () => {
  return (
    <div className="app-container">
      {/* Left Column: Timeline / History */}
      <div className="layout-col">
        <InteractionHistory />
      </div>

      {/* Middle Column: Chat AI */}
      <div className="layout-col">
        <ChatInterface />
      </div>

      {/* Right Column: Structured Form */}
      <div className="layout-col">
        <StructuredForm />
      </div>
    </div>
  );
};

export default App;
