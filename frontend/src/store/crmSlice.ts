import { createSlice, createAsyncThunk, PayloadAction } from '@reduxjs/toolkit';

export interface Message {
  id: string;
  sender: 'user' | 'agent';
  text: string;
}

export interface Interaction {
  id?: number;
  hcp_id: number | null;
  date: string;
  notes: string;
  products_discussed: string;
}

export interface HCP {
  id: number;
  name: string;
  specialty: string;
  location: string;
  tier: string;
}

interface CRMState {
  chatHistory: Message[];
  interactions: Interaction[];
  hcps: HCP[];
  draftInteraction: Interaction;
  isLoading: boolean;
  error: string | null;
}

const initialState: CRMState = {
  chatHistory: [{ id: '1', sender: 'agent', text: 'Hello! I am your AI assistant. You can chat with me to log an HCP interaction, edit a past interaction, or schedule a follow-up. How can I help you today?' }],
  interactions: [],
  hcps: [],
  draftInteraction: {
    hcp_id: null,
    date: new Date().toISOString().split('T')[0],
    notes: '',
    products_discussed: ''
  },
  isLoading: false,
  error: null
};

// Async thunks for API calls
// Use relative path on production, localhost on development
const getAPIBase = () => {
  if (typeof window !== 'undefined' && window.location.hostname === 'localhost') {
    return 'http://localhost:8000/api';
  }
  return '/api'; // Will use backend service from Render
};

const API_BASE = import.meta.env.VITE_API_BASE || getAPIBase();

export const fetchInteractions = createAsyncThunk('crm/fetchInteractions', async () => {
  const response = await fetch(`${API_BASE}/interactions`);
  return await response.json();
});

export const fetchHcps = createAsyncThunk('crm/fetchHcps', async () => {
  const response = await fetch(`${API_BASE}/hcps`);
  return await response.json();
});

export const sendChatMessage = createAsyncThunk(
  'crm/sendChatMessage',
  async (message: string, { dispatch }) => {
    // Add user msg early to state (handled in extraReducers or component directly, but doing it in component is easier for optimistic update. Let's just return the response here)
    const response = await fetch(`${API_BASE}/chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message, thread_id: 'local_session_1' })
    });
    
    const data = await response.json();
    
    if (!response.ok) {
      throw new Error(data.detail || 'Error communicating with AI');
    }
    
    dispatch(fetchInteractions()); // Refresh data after chat as it might have logged or edited
    return data.response || "No response generated.";
  }
);

export const crmSlice = createSlice({
  name: 'crm',
  initialState,
  reducers: {
    addMessage(state, action: PayloadAction<Message>) {
      state.chatHistory.push(action.payload);
    },
    updateDraftField(state, action: PayloadAction<{ field: keyof Interaction, value: any }>) {
      (state.draftInteraction as any)[action.payload.field] = action.payload.value;
    },
    clearDraft(state) {
        state.draftInteraction = initialState.draftInteraction;
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(sendChatMessage.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(sendChatMessage.fulfilled, (state, action) => {
        state.isLoading = false;
        state.chatHistory.push({
          id: Date.now().toString(),
          sender: 'agent',
          text: action.payload
        });
      })
      .addCase(sendChatMessage.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.error.message || 'Error communicating with AI';
        state.chatHistory.push({
          id: Date.now().toString(),
          sender: 'agent',
          text: 'Sorry, I encountered an error. Is the backend running?'
        });
      })
      .addCase(fetchInteractions.fulfilled, (state, action) => {
        state.interactions = action.payload;
      })
      .addCase(fetchHcps.fulfilled, (state, action) => {
        state.hcps = action.payload;
      });
  }
});

export const { addMessage, updateDraftField, clearDraft } = crmSlice.actions;
export default crmSlice.reducer;
