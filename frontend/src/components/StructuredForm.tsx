import React from 'react';
import { Search, Plus, Mic } from 'lucide-react';

const StructuredForm: React.FC = () => {

  return (
    <div className="panel">
      <div className="panel-title form-title">
        Interaction Details
      </div>
      
      <div className="form-content">
        <div className="form-row">
          <div>
            <label>HCP Name</label>
            <input type="text" placeholder="Search or select HCP..." />
          </div>
          <div>
            <label>Interaction Type</label>
            <select defaultValue="Meeting">
              <option value="Meeting">Meeting</option>
              <option value="Call">Call</option>
              <option value="Email">Email</option>
            </select>
          </div>
        </div>

        <div className="form-row">
          <div>
            <label>Date</label>
            <input type="text" placeholder="19-04-2025" defaultValue="19-04-2025" />
          </div>
          <div>
            <label>Time</label>
            <input type="text" placeholder="19:36" defaultValue="19:36" />
          </div>
        </div>

        <div>
          <label>Attendees</label>
          <input type="text" placeholder="Enter names or search..." />
        </div>

        <div>
          <label>Topics Discussed</label>
          <textarea rows={3} placeholder="Enter key discussion points..."></textarea>
          <button type="button" className="btn" style={{ marginTop: '8px' }}>
            <Mic size={14} /> Summarize from Voice Note (Requires Consent)
          </button>
        </div>

        <div>
          <label style={{marginTop: '4px'}}>Materials Shared / Samples Distributed</label>
          
          <div className="box-section">
            <div className="box-section-info">
              <span>Materials Shared</span>
              <small>No materials added.</small>
            </div>
            <button className="btn">
              <Search size={14} /> Search/Add
            </button>
          </div>

          <div className="box-section">
            <div className="box-section-info">
              <span>Samples Distributed</span>
              <small>No samples added.</small>
            </div>
            <button className="btn">
               Add Sample
            </button>
          </div>
        </div>

        <div>
          <label>Observed/Inferred HCP Sentiment</label>
          <div className="sentiment-group">
            <label className="sentiment-option">
              <input type="radio" name="sentiment" value="positive" />
              <span>😊 Positive</span>
            </label>
            <label className="sentiment-option">
              <input type="radio" name="sentiment" value="neutral" defaultChecked />
              <span>😐 Neutral</span>
            </label>
            <label className="sentiment-option">
              <input type="radio" name="sentiment" value="negative" />
              <span>😞 Negative</span>
            </label>
          </div>
        </div>

        <div>
          <label>Outcomes</label>
          <textarea rows={2} placeholder="Key outcomes or agreements..."></textarea>
        </div>

        <div>
          <label>Follow-up Actions</label>
          <textarea rows={2} placeholder="Enter next steps or tasks..."></textarea>
        </div>

        <div>
          <label style={{textTransform: 'none', fontWeight: 600, color: 'var(--text-main)', marginTop: '8px'}}>
            AI Suggested Follow-ups:
          </label>
          <div className="ai-followup-links">
            <a href="#">+ Schedule follow-up meeting in 2 weeks</a>
            <a href="#">+ Send OncoBoost Phase III PDF</a>
            <a href="#">+ Add Dr. Sharma to advisory board invite list</a>
          </div>
        </div>

      </div>
    </div>
  );
};

export default StructuredForm;
