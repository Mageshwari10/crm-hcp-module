import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { RootState, AppDispatch } from '../store';
import { fetchInteractions, fetchHcps } from '../store/crmSlice';
import { History, Activity } from 'lucide-react';

const InteractionHistory: React.FC = () => {
  const dispatch = useDispatch<AppDispatch>();
  const { interactions, hcps } = useSelector((state: RootState) => state.crm);

  useEffect(() => {
    dispatch(fetchInteractions());
    dispatch(fetchHcps());
  }, [dispatch]);

  const getHcpName = (id: number | null) => {
    if (!id) return "Unknown HCP";
    const hcp = hcps.find(h => h.id === id);
    return hcp ? hcp.name : `HCP #${id}`;
  };

  return (
    <div className="glass-panel" style={{ height: '100%' }}>
      <div className="panel-header">
        <History size={20} color="var(--primary)" /> Timeline Logs
      </div>
      
      <div className="panel-content">
        {interactions.length === 0 ? (
          <div style={{ textAlign: 'center', marginTop: '40px', color: 'var(--text-muted)' }}>
            <Activity size={48} opacity={0.3} style={{ marginBottom: '16px' }} />
            <p>No interactions logged yet.</p>
          </div>
        ) : (
          interactions.map((interaction) => (
            <div key={interaction.id} className="history-card">
              <div className="hc-header">
                <strong>{getHcpName(interaction.hcp_id)}</strong>
                <span className="hc-date">{interaction.date}</span>
              </div>
              <div className="hc-products">
                 Products: {interaction.products_discussed}
              </div>
              <p style={{ fontSize: '0.9rem', color: '#d1d5db' }}>{interaction.notes}</p>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default InteractionHistory;
