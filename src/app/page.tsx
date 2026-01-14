import React from 'react';
import { 
  ArrowUpRight, 
  Play, 
  Clock, 
  CheckCircle2, 
  Loader2, 
  MoreVertical 
} from 'lucide-react';

export default function Dashboard() {
  const activeProjects = [
    {
      id: '1',
      title: 'The Future of AI Hardware',
      type: 'Hero Video',
      status: 'Processing',
      progress: 65,
      agents: ['Ingestion', 'Analyst', 'Viral Scout'],
      timestamp: '2 mins ago'
    },
    {
      id: '2',
      title: 'React Server Components Explained',
      type: 'Technical Tutorial',
      status: 'Completed',
      progress: 100,
      agents: ['Ingestion', 'Analyst', 'Viral Scout', 'Distribution'],
      timestamp: '4 hours ago'
    }
  ];

  return (
    <div className="p-8 space-y-8">
      <header className="flex justify-between items-end">
        <div>
          <h1 className="text-3xl font-bold">Creator Dashboard</h1>
          <p className="text-slate-400 mt-1">Monitor your content pipeline and AI agent activity.</p>
        </div>
        <button className="bg-indigo-600 hover:bg-indigo-500 text-white px-6 py-2.5 rounded-xl font-semibold transition-all shadow-lg shadow-indigo-600/20">
          Upload Hero Content
        </button>
      </header>

      {/* Stats Overview */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {[
          { label: 'Weekly Adaptations', value: '142', trend: '+12%' },
          { label: 'Time Saved (AI)', value: '48.5 hrs', trend: '+5%' },
          { label: 'Active Agents', value: '12', trend: 'Optimal' },
        ].map((stat, i) => (
          <div key={i} className="bg-slate-900 border border-slate-800 p-6 rounded-2xl">
            <p className="text-slate-400 text-sm font-medium">{stat.label}</p>
            <div className="flex items-end justify-between mt-2">
              <h3 className="text-3xl font-bold">{stat.value}</h3>
              <span className="text-emerald-400 text-sm font-medium flex items-center gap-1">
                {stat.trend} <ArrowUpRight className="w-4 h-4" />
              </span>
            </div>
          </div>
        ))}
      </div>

      {/* Active Pipeline */}
      <section className="space-y-4">
        <h2 className="text-xl font-semibold flex items-center gap-2">
          Active Pipelines <span className="text-sm font-normal text-slate-500 bg-slate-800 px-2 py-0.5 rounded-full">2</span>
        </h2>
        
        <div className="grid gap-4">
          {activeProjects.map((project) => (
            <div key={project.id} className="bg-slate-900 border border-slate-800 p-5 rounded-2xl flex items-center gap-6">
              <div className="w-32 h-20 bg-slate-800 rounded-lg flex items-center justify-center relative overflow-hidden group">
                <Play className="w-8 h-8 text-slate-600 group-hover:text-indigo-400 transition-colors" />
                <div className="absolute bottom-0 left-0 h-1 bg-indigo-500 transition-all" style={{ width: `${project.progress}%` }} />
              </div>

              <div className="flex-1">
                <div className="flex justify-between items-start">
                  <div>
                    <h3 className="font-bold text-lg">{project.title}</h3>
                    <p className="text-slate-400 text-sm flex items-center gap-2">
                      <Clock className="w-3 h-3" /> {project.timestamp} • {project.type}
                    </p>
                  </div>
                  <button className="text-slate-500 hover:text-white">
                    <MoreVertical className="w-5 h-5" />
                  </button>
                </div>

                <div className="mt-4 flex items-center gap-4">
                   <div className="flex-1 bg-slate-800 h-2 rounded-full overflow-hidden">
                      <div 
                        className={`h-full transition-all duration-1000 ${project.status === 'Completed' ? 'bg-emerald-500' : 'bg-indigo-500 animate-pulse'}`}
                        style={{ width: `${project.progress}%` }}
                      />
                   </div>
                   <span className="text-sm font-medium text-slate-300 w-12">{project.progress}%</span>
                </div>
              </div>

              <div className="flex -space-x-2">
                {project.agents.map((agent, idx) => (
                  <div 
                    key={idx} 
                    title={agent}
                    className="w-8 h-8 rounded-full border-2 border-slate-900 bg-slate-700 flex items-center justify-center text-[10px] font-bold"
                  >
                    {agent[0]}
                  </div>
                ))}
              </div>

              <div className="min-w-[120px] flex flex-col items-end">
                {project.status === 'Processing' ? (
                  <span className="text-indigo-400 text-sm font-bold flex items-center gap-2 bg-indigo-400/10 px-3 py-1 rounded-full border border-indigo-400/20">
                    <Loader2 className="w-3 h-3 animate-spin" /> In Progress
                  </span>
                ) : (
                  <span className="text-emerald-400 text-sm font-bold flex items-center gap-2 bg-emerald-400/10 px-3 py-1 rounded-full border border-emerald-400/20">
                    <CheckCircle2 className="w-3 h-3" /> Ready
                  </span>
                )}
              </div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}