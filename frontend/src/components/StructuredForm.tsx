import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { RootState, AppDispatch } from '../store';
import { updateDraftField, clearDraft, fetchInteractions } from '../store/crmSlice';
import { FileText, Save } from 'lucide-react';

const StructuredForm: React.FC = () => {
  const dispatch = useDispatch<AppDispatch>();
  const { draftInteraction, hcps } = useSelector((state: RootState) => state.crm);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const dbHcpId = draftInteraction.hcp_id || 1; // Default fallback for MVP

      await fetch('http://localhost:8000/api/interactions', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
           ...draftInteraction,
           hcp_id: dbHcpId
        })
      });
      dispatch(clearDraft());
      dispatch(fetchInteractions());
    } catch(err) {
      console.error(err);
    }
  };

  const handleChange = (field: string, value: any) => {
    dispatch(updateDraftField({ field: field as any, value }));
  };

  return (
    <div className="glass-panel" style={{ height: '100%' }}>
      <div className="panel-header">
        <FileText size={20} color="var(--primary)" /> Manual Logger
      </div>
      
      <div className="panel-content">
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Provider (HCP)</label>
            <select 
              value={draftInteraction.hcp_id || ''} 
              onChange={(e) => handleChange('hcp_id', parseInt(e.target.value))}
            >
              <option value="">Select an HCP...</option>
              {hcps.map(hcp => (
                <option key={hcp.id} value={hcp.id}>{hcp.name} - {hcp.specialty}</option>
              ))}
              {hcps.length === 0 && <option value="1">Dr. Demo Generic</option>}
            </select>
          </div>

          <div className="form-group">
            <label>Interaction Date</label>
            <input 
              type="date" 
              value={draftInteraction.date}
              onChange={(e) => handleChange('date', e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label>Products Discussed</label>
            <input 
              type="text" 
              placeholder="e.g. CardioPlus, NeuroMax"
              value={draftInteraction.products_discussed}
              onChange={(e) => handleChange('products_discussed', e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label>Interaction Notes</label>
            <textarea 
              rows={6}
              placeholder="Detailed summary of the conversation..."
              value={draftInteraction.notes}
              onChange={(e) => handleChange('notes', e.target.value)}
              required
            />
          </div>

          <button type="submit" style={{ width: '100%', marginTop: '10px' }}>
            <Save size={18} /> Save Interaction
          </button>
        </form>
      </div>
    </div>
  );
};

export default StructuredForm;
