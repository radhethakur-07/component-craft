import React, { useState } from 'react';
import { Sandpack } from "@codesandbox/sandpack-react";

function App() {
  const [prompt, setPrompt] = useState("");
  const [generatedCode, setGeneratedCode] = useState("");
  const [isGenerating, setIsGenerating] = useState(false);

  const handleGenerate = async () => {
    if (!prompt.trim()) return;
    
    setIsGenerating(true);
    try {
      // ✅ FIX: Dynamic URL logic added for Production (Vercel) & Local development
      const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";
      
      const response = await fetch(`${API_BASE_URL}/api/v1/generate`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: prompt }),
      });
      
      const data = await response.json();
      
      if (data.success) {
        setGeneratedCode(data.code);
      } else {
        alert("Generation Error: " + data.message);
      }
    } catch (error) {
      console.error("API Error:", error);
      alert("Failed to connect to the backend server.");
    } finally {
      setIsGenerating(false);
    }
  };

  return (
    <div className="flex h-screen bg-gray-900 text-white font-sans p-4 gap-4">
      {/* Left Panel - Input Area */}
      <div className="w-1/3 flex flex-col gap-4 bg-gray-800 p-6 rounded-xl shadow-lg border border-gray-700">
        <h1 className="text-3xl font-bold bg-gradient-to-r from-blue-400 to-purple-500 bg-clip-text text-transparent">
          Component Craft ✨
        </h1>
        <p className="text-gray-400 text-sm">Describe the UI component you want to build using Tailwind CSS.</p>
        
        <textarea
          className="flex-1 bg-gray-900 border border-gray-700 rounded-lg p-4 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none"
          placeholder="E.g., A pricing card with three tiers..."
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
        />
        
        <button
          onClick={handleGenerate}
          disabled={isGenerating || !prompt.trim()}
          className={`py-3 px-4 rounded-lg font-bold transition-all ${
            isGenerating ? "bg-gray-600 cursor-not-allowed" : "bg-blue-600 hover:bg-blue-500 shadow-md"
          }`}
        >
          {isGenerating ? "Generating Magic..." : "Generate UI"}
        </button>
      </div>

      {/* Right Panel - Sandpack Live Preview (Decorated & Movable) */}
      <div className="w-2/3 bg-gray-800 rounded-xl shadow-lg border border-gray-700 overflow-hidden flex flex-col">
        {generatedCode ? (
          <Sandpack
            template="react"
            theme="dark"
            customSetup={{
              dependencies: {
                "lucide-react": "^0.292.0",
                "tailwindcss": "^3.3.0"
              }
            }}
            options={{
              showNavigator: false,      
              showTabs: true,
              resizablePanels: true,     
              editorWidthPercentage: 35, 
              editorHeight: "calc(100vh - 4rem)", 
            }}
            files={{
            "/App.js": generatedCode,
            
            "/index.css": `
              /* Yahan se @tailwind hata diya kyunki CDN khud sab handle karega */
              body { background-color: #111827; color: white; margin: 0; font-family: system-ui, sans-serif; }
            `,
            
            "/index.js": `
              import React, { StrictMode } from "react";
              import { createRoot } from "react-dom/client";
              import "./index.css";
              import App from "./App";
              
              // 🔥 BRAHMASTRA: Forcefully inject Tailwind CSS via JavaScript
              const script = document.createElement("script");
              script.src = "https://cdn.tailwindcss.com";
              document.head.appendChild(script);
              
              const root = createRoot(document.getElementById("root"));
              root.render(
                <StrictMode>
                  <App />
                </StrictMode>
              );
            `
          }}
          />
        ) : (
          <div className="h-full flex flex-col items-center justify-center text-gray-500 gap-3">
            <svg className="w-16 h-16 opacity-20" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
            </svg>
            <p>Your generated React component will appear here.</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;