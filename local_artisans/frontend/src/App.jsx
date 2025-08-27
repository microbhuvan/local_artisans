import React, { useState } from "react";

const API_BASE = import.meta.env.VITE_API_URL || "http://localhost:8000";

export const App = () => {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [category, setCategory] = useState("");
  const [priceRange, setPriceRange] = useState("");
  const [region, setRegion] = useState("");
  const [imageFile, setImageFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [result, setResult] = useState(null);

  async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const payload = { title, description, category, priceRange, region };
      const form = new FormData();
      form.append("payload", JSON.stringify(payload));
      if (imageFile) form.append("image", imageFile);

      const resp = await fetch(`${API_BASE}/api/analyze-product`, {
        method: "POST",
        body: form,
      });
      if (!resp.ok) throw new Error(`${resp.status} ${resp.statusText}`);
      const data = await resp.json();
      setResult(data);
    } catch (err) {
      setError(err.message || "Request failed");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="container">
      <div className="grid-2">
        <div className="card">
          <h1>Local Artisans: Marketing Planner</h1>
          <p className="muted" style={{ marginTop: -8, marginBottom: 20 }}>
            Upload a product and get a marketing plan. Press{" "}
            <span className="kbd">Enter</span> to submit.
          </p>
          <form onSubmit={handleSubmit} className="grid">
            <div>
              <label>Title</label>
              <input
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                required
                placeholder="Handmade clay pot"
              />
            </div>
            <div>
              <label>Description</label>
              <textarea
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                required
                placeholder="Describe materials, style, size, story"
              />
            </div>

            <div className="row">
              <div>
                <label>Category</label>
                <input
                  value={category}
                  onChange={(e) => setCategory(e.target.value)}
                  placeholder="Home decor"
                />
              </div>
              <div>
                <label>Price Range</label>
                <input
                  value={priceRange}
                  onChange={(e) => setPriceRange(e.target.value)}
                  placeholder="$20 - $30"
                />
              </div>
            </div>

            <div className="row">
              <div>
                <label>Region</label>
                <input
                  value={region}
                  onChange={(e) => setRegion(e.target.value)}
                  placeholder="Bengaluru, India"
                />
              </div>
              <div>
                <label>Image</label>
                <input
                  type="file"
                  accept="image/*"
                  onChange={(e) => setImageFile(e.target.files?.[0] || null)}
                />
              </div>
            </div>

            <div className="actions">
              <button disabled={loading} type="submit">
                {loading ? "Analyzing…" : "Generate Plan"}
              </button>
              {error && <span style={{ color: "#ef4444" }}>{error}</span>}
            </div>
          </form>
        </div>

        <div className="card result">
          <h2>Result</h2>
          {!result && (
            <p className="muted">No plan yet. Submit the form to generate.</p>
          )}
          {result && (
            <>
              <p className="muted">Provider: {result.provider}</p>
              <pre>{JSON.stringify(result.plan, null, 2)}</pre>
            </>
          )}
        </div>
      </div>
    </div>
  );
};
