import React from 'react';
import ChatInterface from './components/ChatInterface';
import StructuredForm from './components/StructuredForm';

const App: React.FC = () => {
  return (
    <>
      <div className="header-title">Log HCP Interaction</div>
      <div className="main-layout">
        <StructuredForm />
        <ChatInterface />
      </div>
    </>
  );
};

export default App;
