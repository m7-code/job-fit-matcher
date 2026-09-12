import { useState } from "react";
import axios from "axios";
import "./App.css";

const API_URL = "http://127.0.0.1:8000";

function App() {
  const [resumeFile, setResumeFile] = useState(null);
  const [jobTitle, setJobTitle] = useState("");
  const [jdText, setJdText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!resumeFile || !jdText.trim()) {
      setError("Resume aur Job Description dono zaroori hain.");
      return;
    }

    setError("");
    setLoading(true);
    setResult(null);

    const formData = new FormData();
    formData.append("resume", resumeFile);
    formData.append("job_title", jobTitle);
    formData.append("jd_text", jdText);

    try {
      const response = await axios.post(`${API_URL}/analyze`, formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setResult(response.data);
    } catch (err) {
      console.error(err);
      setError("Kuch ghalat ho gaya. Backend chal raha hai check kar lein.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Job-Fit Matcher</h1>

      <form onSubmit={handleSubmit} className="form">
        <label>
          Resume (PDF)
          <input
            type="file"
            accept="application/pdf"
            onChange={(e) => setResumeFile(e.target.files[0])}
          />
        </label>

        <label>
          Job Title (optional)
          <input
            type="text"
            placeholder="e.g. Python Developer"
            value={jobTitle}
            onChange={(e) => setJobTitle(e.target.value)}
          />
        </label>

        <label>
          Job Description / Context
          <textarea
            rows={8}
            placeholder="Poora job post yahan paste karein (LinkedIn se copy bhi kar sakte hain)"
            value={jdText}
            onChange={(e) => setJdText(e.target.value)}
          />
        </label>

        <button type="submit" disabled={loading}>
          {loading ? "Analyzing..." : "Analyze"}
        </button>
      </form>

      {error && <p className="error">{error}</p>}

      {result && <ResultCard result={result} />}
    </div>
  );
}

function ResultCard({ result }) {
  const hasMatched = result.matched_skills && result.matched_skills.length > 0;
  const hasMissingQuick =
    result.missing_skills_quick && result.missing_skills_quick.length > 0;

  return (
    <div className="result">
      <h2>Overall Fit Score: {result.overall_fit_score}/100</h2>
      <p className="sub-score">Semantic Score: {result.semantic_score}%</p>

      {hasMatched && (
        <Section title="✅ Matched Skills" items={result.matched_skills} />
      )}

      {hasMissingQuick && (
        <Section
          title="⚠️ Missing Skills (quick check)"
          items={result.missing_skills_quick}
        />
      )}

      <Section title="💪 Strengths" items={result.strengths} />
      <Section title="❌ Missing Skills / Gaps" items={result.missing_skills} />
      <Section title="💡 Suggestions" items={result.suggestions} />
    </div>
  );
}

function Section({ title, items }) {
  if (!items || items.length === 0) return null;

  return (
    <div className="section">
      <h3>{title}</h3>
      <ul>
        {items.map((item, i) => (
          <li key={i}>{item}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;