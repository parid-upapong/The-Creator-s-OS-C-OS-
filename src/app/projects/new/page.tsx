"use client";
import React, { useState } from 'react';
import { Upload, Link as LinkIcon, Youtube, Globe, ArrowRight } from 'lucide-react';

export default function NewProject() {
  const [method, setMethod] = useState<'upload' | 'link'>('upload');

  return (
    <div className="p-8 max-w-4xl mx-auto w-full">
      <header className="mb-10 text-center">
        <h1 className="text-4xl font-extrabold tracking-tight">Ingest Hero Content</h1>
        <p className="text-slate-400 mt-2 text-lg">One source to rule them all. Upload or paste a link to start the AI transformation.</p>
      </header>

      <div className="grid grid-cols-2 gap-4 mb-8">
        <button 
          onClick={() => setMethod('upload')}
          className={`p-4 rounded-2xl border-2 transition-all flex flex-col items-center gap-3 ${
            method === 'upload' ? 'border-indigo-600 bg-indigo-600/5' : 'border-slate-800 hover:border-slate-700'
          }`}
        >
          <Upload className={method === 'upload' ? 'text-indigo-400' : 'text-slate-500'} />
          <span className="font-bold">File Upload</span>
        </button>
        <button 
          onClick={() => setMethod('link')}
          className={`p-4 rounded-2xl border-2 transition-all flex flex-col items-center gap-3 ${
            method === 'link' ? 'border-indigo-600 bg-indigo-600/5' : 'border-slate-800 hover:border-slate-700'
          }`}
        >
          <LinkIcon className={method === 'link' ? 'text-indigo-400' : 'text-slate-500'} />
          <span className="font-bold">Paste URL</span>
        </button>
      </div>

      <div className="bg-slate-900 border border-slate-800 rounded-3xl p-10 shadow-2xl">
        {method === 'upload' ? (
          <div className="border-2 border-dashed border-slate-700 rounded-2xl p-12 flex flex-col items-center justify-center text-center cursor-pointer hover:bg-slate-800/50 transition-colors">
            <div className="w-16 h-16 bg-slate-800 rounded-full flex items-center justify-center mb-4">
              <Upload className="text-slate-400 w-8 h-8" />
            </div>
            <h3 className="text-xl font-bold">Drop your video here</h3>
            <p className="text-slate-500 mt-1">MP4, MOV up to 2GB. 4K supported.</p>
            <button className="mt-6 bg-white text-black px-6 py-2 rounded-full font-bold hover:bg-slate-200 transition-colors">
              Browse Files
            </button>
          </div>
        ) : (
          <div className="space-y-6">
            <div className="relative">
              <Youtube className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-500" />
              <input 
                type="text" 
                placeholder="https://youtube.com/watch?v=..." 
                className="w-full bg-slate-950 border border-slate-800 rounded-xl py-4 pl-12 pr-4 focus:ring-2 focus:ring-indigo-500 outline-none transition-all"
              />
            </div>
            <div className="flex items-center gap-4 text-slate-500 px-2">
              <div className="h-px flex-1 bg-slate-800"></div>
              <span className="text-xs font-bold uppercase tracking-widest">Or other platforms</span>
              <div className="h-px flex-1 bg-slate-800"></div>
            </div>
            <div className="grid grid-cols-3 gap-3">
              {['Twitch', 'Vimeo', 'Google Drive'].map(p => (
                <button key={p} className="flex items-center justify-center gap-2 py-3 bg-slate-800 rounded-xl hover:bg-slate-700 transition-colors text-sm font-medium">
                  <Globe className="w-4 h-4 text-slate-400" /> {p}
                </button>
              ))}
            </div>
          </div>
        )}

        <div className="mt-10 border-t border-slate-800 pt-8">
          <div className="flex justify-between items-center">
            <div>
              <h4 className="font-bold text-lg">Auto-Processing Preset</h4>
              <p className="text-slate-400 text-sm">The "Viral Scout" will automatically create 10 vertical clips.</p>
            </div>
            <select className="bg-slate-800 border-none rounded-lg px-4 py-2 font-medium">
              <option>Standard Viral Mix</option>
              <option>Educational/Long-form</option>
              <option>Podcast Highlights</option>
            </select>
          </div>
          
          <button className="w-full mt-8 bg-indigo-600 hover:bg-indigo-500 py-4 rounded-xl font-bold flex items-center justify-center gap-2 text-lg shadow-xl shadow-indigo-600/10">
            Initialize Adaptation <ArrowRight className="w-5 h-5" />
          </button>
        </div>
      </div>
    </div>
  );
}