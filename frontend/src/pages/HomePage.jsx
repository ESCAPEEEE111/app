import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { ArrowRight, Zap, Rocket, Globe, BarChart3, Shield, Brain } from 'lucide-react';
import { stats, partnerBrands } from '../data/mock';
import MobileMatrixOptimizer from '../components/MobileMatrixOptimizer';
import TerminalWindow from '../components/TerminalWindow';
import { Button } from '../components/ui/button';
import { Badge } from '../components/ui/badge';

const HomePage = () => {
  const [terminalText, setTerminalText] = useState('');

  // Terminal typing effect
  useEffect(() => {
    const text = "INITIALIZING DIGITAL DOMINANCE...";
    let index = 0;
    const timer = setInterval(() => {
      setTerminalText(text.slice(0, index));
      index++;
      if (index > text.length) {
        clearInterval(timer);
      }
    }, 100);
    return () => clearInterval(timer);
  }, []);

  return (
    <MobileMatrixOptimizer className="min-h-screen bg-black text-matrix-green relative overflow-hidden">
      {/* Clean background without animations */}
      <div className="fixed inset-0 z-0 bg-black" />
      
      {/* Hero Section */}
      <section className="min-h-screen flex items-center justify-center relative z-10 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div className="space-y-8">
            <div className="space-y-4">
              <Badge className="bg-gradient-to-r from-matrix-green/20 to-matrix-cyan/20 text-matrix-green border-matrix-green/40 font-mono">
                🚀 #1 Digital Marketing Agency in Dubai
              </Badge>
              
              <h1 className="text-5xl lg:text-7xl font-bold font-mono leading-tight">
                <span className="text-transparent bg-clip-text bg-gradient-to-r from-matrix-cyan to-matrix-bright-cyan matrix-text-glow">
                  DIGITAL
                </span>
                <br />
                <span className="text-white">
                  SUPREMACY
                </span>
              </h1>
            </div>

            <p className="text-xl lg:text-2xl text-matrix-green/80 font-mono leading-relaxed">
              Transform your business with AI-powered digital marketing solutions. 
              <span className="text-matrix-bright-cyan"> 500+ successful projects</span> in Dubai & UAE.
            </p>

            <div className="flex flex-col sm:flex-row gap-4">
              <Link to="/ai-solver">
                <Button className="bg-gradient-to-r from-matrix-cyan to-matrix-bright-cyan text-black hover:from-matrix-bright-cyan hover:to-matrix-cyan font-mono font-bold px-8 py-4 text-lg transition-all duration-300 transform hover:scale-105">
                  🧠 START YOUR PROJECT
                  <ArrowRight className="ml-2 w-5 h-5" />
                </Button>
              </Link>
              
              <Link to="/platform">
                <Button variant="outline" className="border-matrix-green text-matrix-green hover:bg-matrix-green/10 font-mono font-bold px-8 py-4 text-lg">
                  📊 VIEW PORTFOLIO
                </Button>
              </Link>
            </div>

            <div className="flex items-center space-x-8 text-sm font-mono">
              <div className="flex items-center space-x-2">
                <div className="w-2 h-2 bg-matrix-green rounded-full animate-pulse"></div>
                <span className="text-matrix-green/80">Free Consultation</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-2 h-2 bg-matrix-green rounded-full animate-pulse"></div>
                <span className="text-matrix-green/80">24/7 Support</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-2 h-2 bg-matrix-green rounded-full animate-pulse"></div>
                <span className="text-matrix-green/80">UAE Specialists</span>
              </div>
            </div>
          </div>

          <div className="space-y-6">
            <TerminalWindow title="MISSION_BRIEFING.txt">
              <p className="text-matrix-green/80 leading-relaxed font-mono text-sm">
                &gt; Loading Digital Marketing Agency in Dubai, UAE
                <br />
                &gt; Custom Web & App Development Solutions
                <br />
                &gt; AI Agents Integration & Lead Generation  
                <br />
                &gt; UAE market domination protocols active
                <br />
                &gt; <span className="text-matrix-bright-cyan">STATUS: READY_FOR_DEPLOYMENT</span>
              </p>
            </TerminalWindow>

            <TerminalWindow title="SYSTEM_CAPABILITIES.exe">
              <div className="grid grid-cols-3 gap-4 p-4">
                {[
                  { icon: Globe, label: "WEB_DEV" },
                  { icon: Brain, label: "MOBILE" },
                  { icon: Rocket, label: "AI_POWERED" },
                  { icon: BarChart3, label: "ANALYTICS" },
                  { icon: Shield, label: "SECURITY" },
                  { icon: Zap, label: "PERFORMANCE" }
                ].map((item, index) => {
                  const IconComponent = item.icon;
                  return (
                    <div key={index} className="text-center">
                      <IconComponent className="w-8 h-8 text-matrix-cyan mx-auto mb-2" />
                      <span className="text-xs text-matrix-green/80 font-mono">{item.label}</span>
                    </div>
                  );
                })}
              </div>
              <div className="mt-4 text-center font-mono text-matrix-bright-cyan text-sm">
                AI_POWERED_SOLUTIONS
                <br />
                <span className="text-matrix-green/60">CUTTING_EDGE_TECHNOLOGY_MEETS_CREATIVE_EXCELLENCE</span>
              </div>
            </TerminalWindow>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="py-20 relative z-10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl lg:text-5xl font-bold mb-6 font-mono">
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-matrix-cyan to-matrix-bright-cyan matrix-text-glow">
                PROVEN_RESULTS
              </span>
            </h2>
            <p className="text-xl text-matrix-green/80 max-w-3xl mx-auto font-mono">
              DATA_DRIVEN_SUCCESS | UAE_MARKET_LEADERS | CLIENT_SATISFACTION_GUARANTEED
            </p>
          </div>

          <div className="grid grid-cols-2 lg:grid-cols-4 gap-8">
            {stats.map((stat, index) => (
              <div key={index} className="text-center group">
                <div className="text-4xl lg:text-6xl font-bold text-matrix-bright-cyan mb-2 font-mono group-hover:text-white transition-colors duration-300">
                  {stat.number}
                </div>
                <div className="text-sm lg:text-base text-matrix-green/80 font-mono">
                  {stat.label}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Quick Services Preview */}
      <section className="py-20 relative z-10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl lg:text-5xl font-bold mb-6 font-mono">
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-matrix-cyan to-matrix-bright-cyan matrix-text-glow">
                CORE_SERVICES
              </span>
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
            <div className="bg-black/60 border border-matrix-green/30 rounded-lg p-6 hover:border-matrix-cyan/60 transition-all duration-300 group">
              <Brain className="w-12 h-12 text-matrix-cyan mb-4 group-hover:text-white transition-colors" />
              <h3 className="text-xl font-bold text-matrix-green mb-2 font-mono group-hover:text-white transition-colors">AI_AUTOMATION</h3>
              <p className="text-matrix-green/70 font-mono text-sm">Intelligent business automation and AI-powered solutions</p>
            </div>

            <div className="bg-black/60 border border-matrix-green/30 rounded-lg p-6 hover:border-matrix-cyan/60 transition-all duration-300 group">
              <Globe className="w-12 h-12 text-matrix-cyan mb-4 group-hover:text-white transition-colors" />
              <h3 className="text-xl font-bold text-matrix-green mb-2 font-mono group-hover:text-white transition-colors">DIGITAL_ECOSYSTEM</h3>
              <p className="text-matrix-green/70 font-mono text-sm">Complete digital transformation and web solutions</p>
            </div>

            <div className="bg-black/60 border border-matrix-green/30 rounded-lg p-6 hover:border-matrix-cyan/60 transition-all duration-300 group">
              <BarChart3 className="w-12 h-12 text-matrix-cyan mb-4 group-hover:text-white transition-colors" />
              <h3 className="text-xl font-bold text-matrix-green mb-2 font-mono group-hover:text-white transition-colors">MARKETING_INTELLIGENCE</h3>
              <p className="text-matrix-green/70 font-mono text-sm">Data-driven marketing and advanced analytics</p>
            </div>
          </div>

          <div className="text-center">
            <Link to="/services">
              <Button className="bg-gradient-to-r from-matrix-green to-matrix-cyan text-black hover:from-matrix-cyan hover:to-matrix-bright-cyan font-mono font-bold px-8 py-4 text-lg">
                EXPLORE_ALL_SERVICES
                <ArrowRight className="ml-2 w-5 h-5" />
              </Button>
            </Link>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 relative z-10">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="bg-gradient-to-r from-matrix-green/10 to-matrix-cyan/10 border border-matrix-green/30 rounded-lg p-12 backdrop-blur-sm">
            <h2 className="text-3xl lg:text-4xl font-bold mb-6 font-mono">
              <span className="text-matrix-green">READY_TO_DOMINATE</span>
              <br />
              <span className="text-white">THE_DIGITAL_SPACE?</span>
            </h2>
            
            <p className="text-xl text-matrix-green/80 mb-8 font-mono">
              Let our AI analyze your business challenges and create a custom solution
            </p>

            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link to="/ai-solver">
                <Button className="bg-gradient-to-r from-matrix-cyan to-matrix-bright-cyan text-black hover:from-matrix-bright-cyan hover:to-matrix-cyan font-mono font-bold px-8 py-4 text-lg">
                  🧠 GET_AI_ANALYSIS
                  <ArrowRight className="ml-2 w-5 h-5" />
                </Button>
              </Link>
              
              <Link to="/contact">
                <Button variant="outline" className="border-matrix-green text-matrix-green hover:bg-matrix-green/10 font-mono font-bold px-8 py-4 text-lg">
                  📞 CONTACT_EXPERTS
                </Button>
              </Link>
            </div>
          </div>
        </div>
      </section>
    </MobileMatrixOptimizer>
  );
};

export default HomePage;